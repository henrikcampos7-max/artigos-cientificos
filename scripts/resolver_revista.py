from __future__ import annotations

import argparse
import json
import sys
import unicodedata
from difflib import get_close_matches
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "journal_profiles" / "CATALOGO.json"


def normalize(value: str) -> str:
    ascii_value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    return " ".join("".join(character if character.isalnum() else " " for character in ascii_value.lower()).split())


def load_catalog() -> list[dict[str, object]]:
    data = json.loads(CATALOG.read_text(encoding="utf-8"))
    journals = data.get("journals")
    if not isinstance(journals, list):
        raise ValueError("catálogo sem lista de periódicos")
    return journals


def build_index(journals: list[dict[str, object]]) -> dict[str, dict[str, object]]:
    index: dict[str, dict[str, object]] = {}
    for journal in journals:
        values = [journal.get("name"), journal.get("slug"), *(journal.get("aliases") or [])]
        for value in values:
            if isinstance(value, str):
                index[normalize(value)] = journal
    return index


def resolve(query: str, journals: list[dict[str, object]]) -> tuple[dict[str, object] | None, list[str]]:
    index = build_index(journals)
    key = normalize(query)
    if key in index:
        return index[key], []
    suggestions = get_close_matches(key, index.keys(), n=5, cutoff=0.55)
    names: list[str] = []
    for suggestion in suggestions:
        name = index[suggestion].get("name")
        if isinstance(name, str) and name not in names:
            names.append(name)
    return None, names


def main() -> int:
    parser = argparse.ArgumentParser(description="Resolve nome, sigla ou alias para um perfil editorial.")
    parser.add_argument("query", help="Nome, sigla ou alias da revista")
    parser.add_argument("--json", action="store_true", dest="as_json", help="Exibe o registro do catálogo em JSON")
    args = parser.parse_args()

    try:
        journal, suggestions = resolve(args.query, load_catalog())
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"Erro ao ler catálogo: {exc}", file=sys.stderr)
        return 2

    if journal is None:
        print(f"Revista não encontrada: {args.query}", file=sys.stderr)
        if suggestions:
            print("Sugestões:", file=sys.stderr)
            for suggestion in suggestions:
                print(f"- {suggestion}", file=sys.stderr)
        return 1

    if args.as_json:
        print(json.dumps(journal, ensure_ascii=False, indent=2))
        return 0

    profile = ROOT / "journal_profiles" / str(journal["profile"])
    print(f"Revista: {journal['name']}")
    print(f"Classificação: {journal['classification']}")
    print(f"Perfil: {profile}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
