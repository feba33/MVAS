# Registro de educacion (log.md)

Registro cronológico **append-only** de la entidad `educacion`.
Prefijo: `## [YYYY-MM-DD] <tipo> | <título>` (parseable: `grep "^## \[" log.md`).

## [2026-07-11] setup | Nodo wiki de educacion
- Creada la superstructura recursiva de la entidad `educacion` dentro de `dominio/`:
  `raw/`, `index.md`, `log.md` y `README.md`.
- Principio: toda la info de educación vive solo en esta carpeta.

## [2026-07-11] ingest | Educación
- Fuente: Wikipedia (Education), OECD (Education).
- Página: `educacion.md`.
- Reference-only (URL en frontmatter; sin raw/).
