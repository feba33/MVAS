#!/usr/bin/env python3
"""qmd.py — helper para navegar MVAS (o cualquier repo .md) con QMD (Query Markdown).

QMD = motor de búsqueda híbrida (BM25 + embeddings on-device + reranker) sobre
documentos Markdown. Este script indexa el repo en UNA sola carga de modelo y
expone búsqueda desde la línea de comandos.

Uso (¡IMPORTANTE: correr SIN el PYTHONPATH de stt_lib!):
  env -u PYTHONPATH /opt/data/.venvs/qmd/bin/python scripts/qmd.py index
  env -u PYTHONPATH /opt/data/.venvs/qmd/bin/python scripts/qmd.py search "regulación fintech México" --top-k 5 --rerank
  env -u PYTHONPATH /opt/data/.venvs/qmd/bin/python scripts/qmd.py collections

Por qué `env -u PYTHONPATH`: la sesión exporta PYTHONPATH=/opt/data/stt_lib
(STT), que sombrea el `tokenizers` del venv de qmd y rompe transformers.
Al correr sin ese PYTHONPATH, se usa el tokenizers 0.22.2 del venv.
"""
import argparse
import os
import sys

# Al ejecutar `python scripts/qmd.py`, este directorio (scripts/) sombrea el
# paquete `qmd` instalado en el venv. Lo quitamos de sys.path para
# que `from qmd import ...` resuelva al paquete, no a este archivo.
_THIS_DIR = os.path.dirname(os.path.abspath(__file__))
if _THIS_DIR in sys.path:
    sys.path.remove(_THIS_DIR)

ROOT_DEFAULT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_DEFAULT = os.path.join(ROOT_DEFAULT, ".qmd")
COLLECTION = "mvas"
SKIP_DIRS = {".git", "raw", "__pycache__", ".qmd"}
SKIP_FILES = {"README.md", "log.md"}


def iter_md(root):
    for dirpath, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for f in files:
            if f.endswith(".md") and f not in SKIP_FILES:
                yield os.path.join(dirpath, f)


def build(root, db):
    from qmd import connect
    c = connect(db_path=db)
    col = c.collection(COLLECTION)
    docs = []
    for path in iter_md(root):
        rel = os.path.relpath(path, root)
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        node = rel.split(os.sep)[0] if os.sep in rel else ""
        docs.append({
            "document_id": rel,
            "markdown": text,
            "metadata": {"path": rel, "node": node},
        })
    for d in docs:
        col.add_document(d["document_id"], d["markdown"], d["metadata"])
    c.close()
    print(f"Indexed {len(docs)} markdown docs -> collection '{COLLECTION}' @ {db}")


def search(query, db, top_k, rerank, node):
    from qmd import connect
    c = connect(db_path=db)
    col = c.collection(COLLECTION)
    filters = {"node": node} if node else None
    res = col.hybrid_search(query, top_k=top_k, rerank=rerank, filters=filters)
    c.close()
    print(f"Q: {query!r}  top_k={top_k} rerank={rerank}" + (f" node={node}" if node else ""))
    if not res:
        print("  (sin resultados)")
        return
    for i, r in enumerate(res, 1):
        print(f"\n[{i}] {r.chunk_ref.document_id}  score={r.score:.4f}  {r.metadata}")
        print("    " + r.text.replace("\n", " ")[:300])


def collections(db):
    from qmd import connect
    c = connect(db_path=db)
    infos = c.list_collections()
    c.close()
    if not infos:
        print("(ninguna colección)")
        return
    for ci in infos:
        print(f"- {ci.name}  docs={getattr(ci, 'num_documents', '?')}")


def main():
    ap = argparse.ArgumentParser(description="QMD helper para MVAS")
    sub = ap.add_subparsers(dest="cmd")
    bi = sub.add_parser("index")
    bi.add_argument("--db", default=DB_DEFAULT)
    bi.add_argument("--root", default=ROOT_DEFAULT)
    sp = sub.add_parser("search")
    sp.add_argument("query")
    sp.add_argument("--db", default=DB_DEFAULT)
    sp.add_argument("--top-k", type=int, default=5)
    sp.add_argument("--rerank", action="store_true")
    sp.add_argument("--node", default=None, help="filtrar por nodo (p.ej. dominio, sustrato, rol)")
    cp = sub.add_parser("collections")
    cp.add_argument("--db", default=DB_DEFAULT)
    args = ap.parse_args()
    if args.cmd == "index":
        build(args.root, args.db)
    elif args.cmd == "search":
        search(args.query, args.db, args.top_k, args.rerank, args.node)
    elif args.cmd == "collections":
        collections(args.db)
    else:
        ap.print_help()


if __name__ == "__main__":
    main()
