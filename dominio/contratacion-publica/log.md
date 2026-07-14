# Registro de contratacion-publica (log.md)

Registro cronológico **append-only** de la entidad `contratacion-publica`.
Prefijo: `## [YYYY-MM-DD] <tipo> | <título>` (parseable: `grep "^## \[" log.md`).

## [2026-07-14] setup | Nodo wiki de contratacion-publica
- Creada la superstructura recursiva de la entidad `contratacion-publica` dentro de `dominio/`:
  `raw/`, `index.md`, `log.md` y `README.md`.
- Principio: toda la info de contratacion-publica vive solo en esta carpeta.

## [2026-07-14] ingest | Contratación pública (public procurement)
- Fuente: Wikipedia EN (Public procurement) + WTO GPA + OCDE.
- Página: `contratacion-publica.md`.
- Reference-only (URL en frontmatter; sin raw/).
