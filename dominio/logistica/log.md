# Registro de logistica (log.md)

Registro cronológico **append-only** de la entidad `logistica`.
Prefijo: `## [YYYY-MM-DD] <tipo> | <título>` (parseable: `grep "^## \[" log.md`).

## [2026-07-10] setup | Nodo wiki de logistica
- Creada la superstructura recursiva de la entidad `logistica` dentro de `dominio/`:
  `raw/`, `index.md`, `log.md` y `README.md`.
- Principio: toda la info de logística vive solo en esta carpeta.

## [2026-07-10] ingest | Cadena de suministro, última milla e Incoterms
- Fuente: IBM Think / CSCMP (SCM), Kaizen / Delpa (última milla), ICC / Trade Finance Global (Incoterms 2020).
- Páginas: `gestion-cadena-suministro.md`, `ultima-milla.md`, `incoterms.md`.
- Reference-only (URL en frontmatter; sin raw/).
