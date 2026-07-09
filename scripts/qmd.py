#!/usr/bin/env python3
"""qmd.py — helper para navegar MVAS con el CLI oficial de QMD (Node.js, @tobilu/qmd).

QMD indexa markdown localmente (BM25 + vectores + rerank, modelos GGUF on-device)
y expone un CLI: `qmd collection add` / `qmd context add` / `qmd embed` /
`qmd status` / `qmd search|vsearch|query`. Este script es un wrapper fino que
siempre apunta a la colección `mvas` (repo MVAS).

Uso:
  python3 scripts/qmd.py index                       # registra MVAS + contexto + embed
  python3 scripts/qmd.py status
  python3 scripts/qmd.py search "consulta" [--mode query|vsearch|search] [--limit N] [--json]
  python3 scripts/qmd.py get "ruta/al/archivo.md"

Requisitos: Node >= 22 y `qmd` en PATH (npm install -g @tobilu/qmd).
Los modelos (~2GB GGUF) se descargan solos en el primer `embed`.
NO confundir con el paquete PyPI `qmd` (Python) — es otro proyecto distinto.
"""
import argparse
import os
import shutil
import subprocess

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COLLECTION = "mvas"
CONTEXT = (
    "Wiki de conocimiento en capas MVAS (sustrato/dominio/organización/rol): "
    "finanzas, computación, marketing, leyes, contabilidad, diseño, ventas, "
    "producto, RRHH, operaciones; países México/EE.UU./Canadá/Brasil; roles."
)


def qmd_bin():
    p = shutil.which("qmd")
    if p:
        return p
    cand = "/opt/data/.npm-global/bin/qmd"
    return cand if os.path.exists(cand) else "qmd"


def run(cmd):
    print("+ " + " ".join(cmd), flush=True)
    subprocess.run(cmd, check=True)


def index():
    run([qmd_bin(), "collection", "add", REPO, "--name", COLLECTION])
    run([qmd_bin(), "context", "add", f"qmd://{COLLECTION}", CONTEXT])
    run([qmd_bin(), "embed"])


def status():
    run([qmd_bin(), "status"])


def search(query, mode, limit, as_json, collection):
    cmd = [qmd_bin(), mode, query]
    if collection:
        cmd += ["--collection", collection]
    if limit:
        cmd += ["--limit", str(limit)]
    if as_json:
        cmd += ["--json"]
    run(cmd)


def get(docid, lines):
    cmd = [qmd_bin(), "get", docid]
    if lines:
        cmd += ["-l", lines]
    run(cmd)


def main():
    ap = argparse.ArgumentParser(description="QMD helper para MVAS")
    sub = ap.add_subparsers(dest="cmd")
    sub.add_parser("index")
    sub.add_parser("status")
    sp = sub.add_parser("search")
    sp.add_argument("query")
    sp.add_argument("--mode", default="query")
    sp.add_argument("--limit", type=int, default=None)
    sp.add_argument("--json", action="store_true")
    sp.add_argument("--collection", default=COLLECTION)
    gp = sub.add_parser("get")
    gp.add_argument("docid")
    gp.add_argument("--lines", default=None)
    args = ap.parse_args()
    if args.cmd == "index":
        index()
    elif args.cmd == "status":
        status()
    elif args.cmd == "search":
        search(args.query, args.mode, args.limit, args.json, args.collection)
    elif args.cmd == "get":
        get(args.docid, args.lines)
    else:
        ap.print_help()


if __name__ == "__main__":
    main()
