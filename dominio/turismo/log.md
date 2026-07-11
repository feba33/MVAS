# Registro de turismo (log.md)

Registro cronológico **append-only** de la entidad `turismo`.
Prefijo: `## [YYYY-MM-DD] <tipo> | <título>` (parseable: `grep "^## \[" log.md`).

## [2026-07-11] setup | Nodo wiki de turismo
- Creada la superstructura recursiva de la entidad `turismo` dentro de `dominio/`:
  `raw/`, `index.md`, `log.md` y `README.md`.
- Principio: toda la info de turismo vive solo en esta carpeta.

## [2026-07-11] ingest | Turismo / hospitalidad
- Fuente: Wikipedia (Tourism, Hospitality industry, Hotel).
- Página: `turismo.md`.
- Reference-only (URL en frontmatter; sin raw/).
