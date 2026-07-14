# Registro de pymes (log.md)

Registro cronológico **append-only** de la entidad `pymes`.
Prefijo: `## [YYYY-MM-DD] <tipo> | <título>` (parseable: `grep "^## \[" log.md`).

## [2026-07-14] setup | Nodo wiki de pymes
- Creada la superstructura recursiva de la entidad `pymes` dentro de `dominio/`:
  `raw/`, `index.md`, `log.md` y `README.md`.
- Principio: toda la info de pymes vive solo en esta carpeta.

## [2026-07-14] ingest | PyMEs / SMEs
- Fuente: Wikipedia (SME), OCDE.
- Página: `pymes.md`.
- Reference-only (URL en frontmatter; sin raw/).
