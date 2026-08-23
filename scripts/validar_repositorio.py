from __future__ import annotations

import json
import re
import sys
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

    if errors:
        print("Falhas de validação:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Validação concluída: estrutura, links, JSON, privacidade básica e arquivos temporários OK.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
