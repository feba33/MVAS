# Registro de seguros (log.md)

Registro cronológico **append-only** de la entidad `seguros`.
Prefijo: `## [YYYY-MM-DD] <tipo> | <título>` (parseable: `grep "^## \[" log.md`).

## [2026-07-11] setup | Nodo wiki de seguros
- Creada la superstructura recursiva de la entidad `seguros` dentro de `dominio/`:
  `raw/`, `index.md`, `log.md` y `README.md`.
- Principio: toda la info de seguros vive solo en esta carpeta.

## [2026-07-11] ingest | Seguros (industria aseguradora)
- Fuente: Wikipedia (Insurance), EIOPA (Solvency II).
- Página: `seguros.md`.
- Reference-only (URL en frontmatter; sin raw/).
