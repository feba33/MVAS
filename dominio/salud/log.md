# Registro de salud (log.md)

Registro cronológico **append-only** de la entidad `salud`.
Prefijo: `## [YYYY-MM-DD] <tipo> | <título>` (parseable: `grep "^## \[" log.md`).

## [2026-07-11] setup | Nodo wiki de salud
- Creada la superstructura recursiva de la entidad `salud` dentro de `dominio/`:
  `raw/`, `index.md`, `log.md` y `README.md`.
- Principio: toda la info de salud vive solo en esta carpeta.

## [2026-07-11] ingest | Salud / healthcare
- Fuente: Wikipedia (Health care), WHO (health systems).
- Página: `salud.md`.
- Reference-only (URL en frontmatter; sin raw/).
