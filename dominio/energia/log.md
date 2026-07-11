# Registro de energia (log.md)

Registro cronológico **append-only** de la entidad `energia`.
Prefijo: `## [YYYY-MM-DD] <tipo> | <título>` (parseable: `grep "^## \[" log.md`).

## [2026-07-11] setup | Nodo wiki de energia
- Creada la superstructura recursiva de la entidad `energia` dentro de `dominio/`:
  `raw/`, `index.md`, `log.md` y `README.md`.
- Principio: toda la info de energía vive solo en esta carpeta.

## [2026-07-11] ingest | Sector energético
- Fuente: Wikipedia (Energy industry), FERC, Global Legal Insights (Energy Laws USA).
- Página: `energia.md`.
- Reference-only (URL en frontmatter; sin raw/).
