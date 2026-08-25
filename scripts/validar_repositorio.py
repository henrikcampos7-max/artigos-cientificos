from __future__ import annotations

import json
import re
import sys
import unicodedata
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
REQUIRED = {
    "README.md",
    "ORIENTACOES.md",
    "GOVERNANCA_CIENTIFICA.md",
    "SQUAD.md",
    "CONTRIBUTING.md",
    "AGENTS.md",
    "docs/AUDITORIA_ACERVO_2026-08-23.md",
    "docs/DILIGENCIA_IJAERS_2026-08-23.md",
    "templates/metadata-artigo.example.json",
    "schemas/article-metadata.schema.json",
    "journal_profiles/README.md",
    "journal_profiles/GUIA_VOZ_AUTORAL.md",
    "journal_profiles/CATALOGO.json",
    "schemas/journal-catalog.schema.json",
    "skills/preparar-artigo-para-revista/SKILL.md",
    "skills/preparar-artigo-para-revista/agents/openai.yaml",
    "scripts/resolver_revista.py",
    "templates/PERFIL_REVISTA.md",
}
TEXT_EXTENSIONS = {".md", ".py", ".json", ".yml", ".yaml", ".csv", ".txt"}
STATUS_VALUES = {
    "ideia",
    "protocolo",
    "rascunho_nao_validado",
    "revisao_humana",
    "pronto_para_submissao",
    "submetido",
    "aceito",
    "publicado",
    "retirado",
}
MARKDOWN_LINK = re.compile(r"!?(?:\[[^]]*\])\(([^)]+)\)")
EMAIL = re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.I)
WINDOWS_USER_PATH = re.compile(r"\b[A-Z]:\\Users\\[^\\\s]+", re.I)
DOI = re.compile(r"^10\.\d{4,9}/\S+$", re.I)
SLUG = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def check_markdown_links(path: Path, text: str, errors: list[str]) -> None:
    for raw_target in MARKDOWN_LINK.findall(text):
        target = raw_target.strip().split(maxsplit=1)[0].strip("<>")
        if not target or target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        file_part = unquote(target.split("#", 1)[0])
        if not file_part:
            continue
        resolved = (path.parent / file_part).resolve()
        if not resolved.exists():
            fail(errors, f"link local inexistente em {path.relative_to(ROOT)}: {target}")


def check_metadata(path: Path, data: object, errors: list[str]) -> None:
    if path.name != "metadata.json" or "articles" not in path.parts:
        return
    if not isinstance(data, dict):
        fail(errors, f"metadados não são objeto JSON: {path.relative_to(ROOT)}")
        return
    required = {
        "schema_version",
        "slug",
        "title",
        "status",
        "study_type",
        "authors_confirmed",
        "human_review",
        "ai_use_logged",
        "contains_patient_data",
        "repository_visibility_approved",
        "last_verified",
    }
    missing = sorted(required - data.keys())
    if missing:
        fail(errors, f"campos ausentes em {path.relative_to(ROOT)}: {', '.join(missing)}")
    if data.get("status") not in STATUS_VALUES:
        fail(errors, f"status inválido em {path.relative_to(ROOT)}: {data.get('status')!r}")
    if data.get("contains_patient_data") is True:
        fail(errors, f"artigo público marcado com dados de pacientes: {path.relative_to(ROOT)}")
    if data.get("repository_visibility_approved") is not True:
        fail(errors, f"visibilidade pública não aprovada: {path.relative_to(ROOT)}")
    doi = data.get("doi")
    if doi and not DOI.match(str(doi)):
        fail(errors, f"DOI inválido em {path.relative_to(ROOT)}: {doi!r}")


def normalize_alias(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    return re.sub(r"[^a-z0-9]+", " ", normalized.lower()).strip()


def check_journal_catalog(data: object, errors: list[str]) -> None:
    if not isinstance(data, dict):
        fail(errors, "journal_profiles/CATALOGO.json deve conter um objeto JSON")
        return
    journals = data.get("journals")
    if not isinstance(journals, list) or not journals:
        fail(errors, "journal_profiles/CATALOGO.json não contém periódicos")
        return

    seen_slugs: set[str] = set()
    seen_aliases: dict[str, str] = {}
    allowed_regions = {"nacional", "internacional", "avaliada"}
    for index, journal in enumerate(journals, start=1):
        if not isinstance(journal, dict):
            fail(errors, f"periódico {index} do catálogo não é objeto")
            continue
        slug = journal.get("slug")
        name = journal.get("name")
        region = journal.get("region")
        profile = journal.get("profile")
        aliases = journal.get("aliases")
        if not isinstance(slug, str) or not SLUG.fullmatch(slug):
            fail(errors, f"slug inválido no catálogo: {slug!r}")
            continue
        if slug in seen_slugs:
            fail(errors, f"slug duplicado no catálogo: {slug}")
        seen_slugs.add(slug)
        if not isinstance(name, str) or not name.strip():
            fail(errors, f"nome ausente no catálogo: {slug}")
        if region not in allowed_regions:
            fail(errors, f"região inválida no catálogo para {slug}: {region!r}")
        if not isinstance(profile, str):
            fail(errors, f"perfil ausente no catálogo: {slug}")
        else:
            profile_path = (ROOT / "journal_profiles" / profile).resolve()
            profiles_root = (ROOT / "journal_profiles").resolve()
            if profiles_root not in profile_path.parents or not profile_path.is_file():
                fail(errors, f"perfil inexistente ou fora da biblioteca para {slug}: {profile}")
        if not isinstance(aliases, list) or not aliases:
            fail(errors, f"aliases ausentes no catálogo: {slug}")
            continue
        for alias in [name, *aliases]:
            if not isinstance(alias, str) or not alias.strip():
                fail(errors, f"alias inválido no catálogo: {slug}")
                continue
            key = normalize_alias(alias)
            owner = seen_aliases.get(key)
            if owner and owner != slug:
                fail(errors, f"alias ambíguo no catálogo: {alias!r} ({owner} e {slug})")
            else:
                seen_aliases[key] = slug


def main() -> int:
    errors: list[str] = []
    for relative in sorted(REQUIRED):
        if not (ROOT / relative).exists():
            fail(errors, f"arquivo obrigatório ausente: {relative}")

    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or ".git" in path.parts:
            continue
        relative = path.relative_to(ROOT)
        name = path.name.lower()
        if name.startswith("~$") or name in {".env", "desktop.ini", "thumbs.db"}:
            fail(errors, f"arquivo local/temporário rastreável: {relative}")
        if path.stat().st_size > 25 * 1024 * 1024:
            fail(errors, f"arquivo acima de 25 MiB requer revisão de licença/LFS: {relative}")
        if path.suffix.lower() not in TEXT_EXTENSIONS:
            continue
        try:
            text = path.read_text(encoding="utf-8-sig")
        except UnicodeDecodeError:
            fail(errors, f"arquivo textual fora de UTF-8: {relative}")
            continue
        if "\x00" in text:
            fail(errors, f"NUL em arquivo textual: {relative}")
        if WINDOWS_USER_PATH.search(text):
            fail(errors, f"caminho pessoal do Windows exposto: {relative}")
        if EMAIL.search(text):
            fail(errors, f"e-mail exposto em arquivo público: {relative}")
        if path.suffix.lower() == ".md":
            check_markdown_links(path, text, errors)
        if path.suffix.lower() == ".json":
            try:
                data = json.loads(text)
            except json.JSONDecodeError as exc:
                fail(errors, f"JSON inválido em {relative}: {exc}")
            else:
                check_metadata(path, data, errors)
                if relative.as_posix() == "journal_profiles/CATALOGO.json":
                    check_journal_catalog(data, errors)

    if errors:
        print("Falhas de validação:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Validação concluída: estrutura, perfis editoriais, links, JSON, privacidade básica e arquivos temporários OK.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
