# Registro de automotriz (log.md)

Registro cronológico **append-only** de la entidad `automotriz`.
Prefijo: `## [YYYY-MM-DD] <tipo> | <título>` (parseable: `grep "^## \[" log.md`).

## [2026-07-11] setup | Nodo wiki de automotriz
- Creada la superstructura recursiva de la entidad `automotriz` dentro de `dominio/`:
  `raw/`, `index.md`, `log.md` y `README.md`.
- Principio: toda la info de automotriz vive solo en esta carpeta.

## [2026-07-11] ingest | Industria automotriz
- Fuente: Wikipedia (Automotive industry).
- Página: `automotriz.md`.
- Reference-only (URL en frontmatter; sin raw/).
