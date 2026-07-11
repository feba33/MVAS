# Registro de manufactura (log.md)

Registro cronológico **append-only** de la entidad `manufactura`.
Prefijo: `## [YYYY-MM-DD] <tipo> | <título>` (parseable: `grep "^## \[" log.md`).

## [2026-07-11] setup | Nodo wiki de manufactura
- Creada la superstructura recursiva de la entidad `manufactura` dentro de `dominio/`:
  `raw/`, `index.md`, `log.md` y `README.md`.
- Principio: toda la info de manufactura vive solo en esta carpeta.

## [2026-07-11] ingest | Manufactura
- Fuente: Wikipedia (Manufacturing), SixSigma.us (Lean Six Sigma).
- Página: `manufactura.md`.
- Reference-only (URL en frontmatter; sin raw/).
