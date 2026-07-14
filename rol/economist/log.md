# Registro de economist (log.md)

Registro cronológico **append-only** de la entidad `economist`.
Prefijo: `## [YYYY-MM-DD] <tipo> | <título>` (parseable: `grep "^## \[" log.md`).

## [2026-07-14] setup | Nodo wiki de economist
- Creada la superstructura recursiva de la entidad `economist` dentro de `rol/`:
  `raw/`, `index.md`, `log.md` y `README.md`.
- Principio: toda la info de economist vive solo en esta carpeta.

## [2026-07-14] ingest | Economist
- Fuente: Wikipedia EN (Economist) + AEA (reference-only).
- Página: `economist.md`.
- Reference-only (URL en frontmatter; sin raw/).
