# chairman (entidad de rol)

Sub-wiki auto-contenido dentro de `rol/`. Arquitectura LLM Wiki recursiva (MVAS).

## Superstructura
- `raw/` — fuentes (inmutables, solo reference-only para web).
- `index.md` — catálogo de páginas.
- `log.md` — registro cronológico.
- páginas con YAML frontmatter (`capa: rol`, `tema: chairman`).

## Convenciones
- `capa: rol`, `tema: chairman`.
- Fuentes web → reference-only (citar URL en `fuente`). No copiar a `raw/`.
