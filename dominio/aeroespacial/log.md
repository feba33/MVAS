# Registro de aeroespacial (log.md)

Registro cronológico **append-only** de la entidad `aeroespacial`.
Prefijo: `## [YYYY-MM-DD] <tipo> | <título>` (parseable: `grep "^## \[" log.md`).

## [2026-07-11] setup | Nodo wiki de aeroespacial
- Creada la superstructura recursiva de la entidad `aeroespacial` dentro de `dominio/`:
  `raw/`, `index.md`, `log.md` y `README.md`.
- Principio: toda la info de aeroespacial vive solo en esta carpeta.

## [2026-07-11] ingest | Aeroespacial (aeronáutica y espacio)
- Fuente: Wikipedia (Aerospace) + síntesis.
- Página: `aeroespacial.md`.
- Reference-only (URL en frontmatter; sin raw/).
