#!/usr/bin/env python3
"""MVAS wiki linter (stdlib only, no external deps).

Uso:
    python3 scripts/lint.py

Health-check mecánico del wiki. Reporta y sale con código != 0 si hay errores
(usable en el cronjob). Chequea:
  1. Frontmatter YAML con los campos obligatorios en cada página de contenido.
  2. Links markdown relativos internos rotos (apuntan a archivos inexistentes).
  3. Páginas huérfanas: contenido no listado en el index.md de su nodo.
  4. Carpetas duplicadas por normalización de encoding (NFC vs NFD).
  5. Superstructura incompleta: todo nodo con index.md debe tener README.md,
     log.md y raw/README.md.

No detecta contradicciones semánticas (eso queda para el lint asistido por LLM).
"""
import os
import re
import sys
import unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REQUIRED = ("titulo", "capa", "tema", "fuente", "fecha", "confianza", "tags")
SPECIAL = {"README.md", "index.md", "log.md"}
LAYERS = ("sustrato", "dominio", "organización", "rol")
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
CODE_RE = re.compile(r"`[^`]*`")


def links_of(text):
    # ignorar links dentro de code-spans (ej. ejemplos de formato en index.md)
    return LINK_RE.findall(CODE_RE.sub("", text))

errors = []


def rel(p):
    return os.path.relpath(p, ROOT)


def content_pages():
    """Páginas de contenido: *.md bajo una capa, que no son README/index/log ni raw/."""
    for dirpath, dirs, files in os.walk(ROOT):
        parts = rel(dirpath).split(os.sep)
        if ".git" in parts or "raw" in parts or parts[0] not in LAYERS:
            continue
        for f in files:
            if f.endswith(".md") and f not in SPECIAL:
                yield os.path.join(dirpath, f)


def parse_frontmatter(text):
    # ponytail: parser mínimo key: value (el frontmatter aquí es plano, no YAML anidado).
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    keys = set()
    for line in text[3:end].splitlines():
        m = re.match(r"^([A-Za-z0-9_]+)\s*:", line)
        if m:
            keys.add(m.group(1))
    return keys


def check_frontmatter():
    for p in content_pages():
        text = open(p, encoding="utf-8").read()
        keys = parse_frontmatter(text)
        if keys is None:
            errors.append(f"[frontmatter] {rel(p)}: sin bloque YAML válido (---)")
            continue
        missing = [k for k in REQUIRED if k not in keys]
        if missing:
            errors.append(f"[frontmatter] {rel(p)}: faltan campos {missing}")


def check_links():
    for dirpath, dirs, files in os.walk(ROOT):
        if ".git" in dirpath.split(os.sep):
            continue
        for f in files:
            if not f.endswith(".md"):
                continue
            path = os.path.join(dirpath, f)
            for target in links_of(open(path, encoding="utf-8").read()):
                target = target.split("#")[0].strip()
                if not target or "://" in target or target.startswith("mailto:"):
                    continue
                dest = os.path.normpath(os.path.join(dirpath, target))
                if not os.path.exists(dest):
                    errors.append(f"[link roto] {rel(path)} -> {target}")


def check_orphans():
    for p in content_pages():
        node = os.path.dirname(p)
        index = os.path.join(node, "index.md")
        name = os.path.basename(p)
        if not os.path.exists(index):
            errors.append(f"[huérfana] {rel(p)}: su nodo no tiene index.md")
            continue
        idx = open(index, encoding="utf-8").read()
        # aceptar link con o sin extensión .md
        if name not in idx and name[:-3] not in idx:
            errors.append(f"[huérfana] {rel(p)}: no listada en {rel(index)}")


def check_encoding_dups():
    for dirpath, dirs, files in os.walk(ROOT):
        if ".git" in dirpath.split(os.sep):
            continue
        seen = {}
        for d in dirs:
            key = unicodedata.normalize("NFC", d)
            if key in seen and seen[key] != d:
                errors.append(
                    f"[encoding] {rel(dirpath)}: carpetas duplicadas "
                    f"'{seen[key]}' y '{d}' (NFC/NFD)")
            seen[key] = d


def check_superstructure():
    for dirpath, dirs, files in os.walk(ROOT):
        if ".git" in dirpath.split(os.sep) or dirpath.endswith("raw"):
            continue
        if "index.md" in files:
            for need in ("README.md", "log.md", os.path.join("raw", "README.md")):
                if not os.path.exists(os.path.join(dirpath, need)):
                    errors.append(f"[superstructura] {rel(dirpath)}: falta {need}")


def main():
    for check in (check_frontmatter, check_links, check_orphans,
                  check_encoding_dups, check_superstructure):
        check()
    if errors:
        print(f"❌ {len(errors)} hallazgo(s):")
        for e in sorted(errors):
            print("  " + e)
        sys.exit(1)
    print("✅ wiki OK — sin hallazgos.")


if __name__ == "__main__":
    main()
