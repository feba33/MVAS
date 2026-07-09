# HERMES.md — Guía de operación para Hermes (MVAS)

Este repo es el *super wiki en capas* (patrón LLM Wiki recursivo) mantenido por
Hermes. La fuente de verdad es el repo; esta guía es un atajo rápido.

## Capas
- `sustrato/` — países (legislación, normas, mercados)
- `dominio/` — disciplinas (finanzas, computación, marketing, leyes, contabilidad, diseño, ventas, producto, RRHH, operaciones)
- `organización/` — empresas (operaciones, decisiones, artefactos)
- `rol/` — responsabilidades y capacidades por cargo

## Cómo navegar (QMD — búsqueda híbrida on-device)
MVAS está indexado con **QMD**, el CLI oficial de Node.js (`@tobilu/qmd`, por
Tobi Lütke): BM25 + vectores + reranker, todo local con modelos GGUF (~2GB, en
`~/.cache/qmd`). Esto deja saltar directo a la página correcta.

```bash
# Setup una vez (descarga modelos + indexa 249 .md):
qmd collection add /opt/data/MVAS --name mvas
qmd context add qmd://mvas "Wiki MVAS en capas (sustrato/dominio/organización/rol)"
qmd embed

# Buscar:
qmd query "regulación fintech México" --collection mvas        # híbrido + rerank (mejor)
qmd search "handleError async" --collection mvas                # BM25, instant
qmd vsearch "cómo opera un growth lead" --collection mvas       # vector
# Helper:
python3 scripts/qmd.py search "consulta" [--mode query|vsearch|search] [--limit N] [--json]
```
> **No confundir** con el paquete PyPI `qmd` (Python, chengzhag/qmd-py): es otro
> proyecto distinto. El correcto es `@tobilu/qmd` (npm). MVAS es en español; el
> modelo de embedding por defecto es inglés-leaning — para mejorar ES, ver
> `QMD_EMBED_MODEL` en la skill `qmd`.

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
