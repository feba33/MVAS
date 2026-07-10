# Registro de negociacion (log.md)

Registro cronológico **append-only** de la entidad `negociacion`.
Prefijo: `## [YYYY-MM-DD] <tipo> | <título>` (parseable: `grep "^## \[" log.md`).

## [2026-07-10] setup | Nodo wiki de negociacion
- Creada la superstructura recursiva de la entidad `negociacion` dentro de `dominio/`:
  `raw/`, `index.md`, `log.md` y `README.md`.

## [2026-07-10] ingest | Negociación
- Fuentes web (reference-only): Wikipedia (es), Program on Negotiation (Harvard).
- Página: `negociacion.md` (método Harvard, BATNA, ZOPA, valor creado/repartido).
- Reference-only (URL en frontmatter; sin raw/).
