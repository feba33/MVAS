# Registro de calidad (log.md)

Registro cronológico **append-only** de la entidad `calidad`.
Prefijo: `## [YYYY-MM-DD] <tipo> | <título>` (parseable: `grep "^## \[" log.md`).

## [2026-07-12] setup | Nodo wiki de calidad
- Creada la superstructura recursiva de la entidad `calidad` dentro de `dominio/`:
  `raw/`, `index.md`, `log.md` y `README.md`.
- Principio: toda la info de calidad vive solo en esta carpeta.

## [2026-07-12] ingest | Gestión de la calidad
- Fuente: ISO (ISO 9001), Wikipedia (Quality management).
- Página: `calidad.md`.
- Reference-only (URL en frontmatter; sin raw/).
