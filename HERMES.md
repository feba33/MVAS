# HERMES.md — Guía de operación para Hermes (MVAS)

Este repo es el *super wiki en capas* (patrón LLM Wiki recursivo) mantenido por
Hermes. La fuente de verdad es el repo; esta guía es un atajo rápido.

## Capas
- `sustrato/` — países (legislación, normas, mercados)
- `dominio/` — disciplinas (finanzas, computación, marketing, leyes, contabilidad, diseño, ventas, producto, RRHH, operaciones)
- `organización/` — empresas (operaciones, decisiones, artefactos)
- `rol/` — responsabilidades y capacidades por cargo

## Cómo navegar (QMD — búsqueda híbrida)
MVAS está indexado con **QMD** (BM25 + embeddings on-device + reranker).
Esto deja saltar directo a la página correcta sin recorrer el árbol.

```bash
# Indexar todo el repo (carga modelos una vez; salta .git/, raw/, .qmd/):
env -u PYTHONPATH /opt/data/.venvs/qmd/bin/python scripts/qmd.py index

# Buscar (semántico + lexical + rerank):
env -u PYTHONPATH /opt/data/.venvs/qmd/bin/python scripts/qmd.py \
  search "regulación fintech México" --top-k 5 --rerank

# Acotar a una capa/nodo:
... qmd.py search "cómo opera un growth lead" --node rol
```
> **Pitfall:** la sesión exporta `PYTHONPATH=/opt/data/stt_lib` (STT) que
> sombrea `tokenizers` y rompe `transformers`. SIEMPRE correr qmd con
> `env -u PYTHONPATH`. Detalle en `GUIA-HERMES.md` y skill `qmd`.

## Documentos clave
- `GUIA-HERMES.md` — procedimiento completo (ingest / query / lint / reabastecimiento).
- `esquema.md` — taxonomía y plantilla de nodo recursivo.
- `protocolo-discriminamiento.md` — a qué nodo va cada tema (discernimiento).
- `working.md` — cola de enriquecimiento + reanudación del bucle.
- `scripts/` — `lint.py`, `gap_analysis.py`, `qmd.py`, `web_research.py`, `scrape_elfinanciero.py`.

## Reglas
- `raw/` = solo referencias que aporta el usuario; la fuente web va en `fuente:`
  del frontmatter (nunca copiar el contenido).
- Cada nodo es un wiki **auto-contenido**: `raw/`, `index.md`, `log.md`,
  `README.md` y páginas, con cross-referencias relativas.
