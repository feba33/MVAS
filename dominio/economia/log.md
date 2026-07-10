# Registro de economia (log.md)

Registro cronológico **append-only** de la entidad `economia`.
Prefijo: `## [YYYY-MM-DD] <tipo> | <título>` (parseable: `grep "^## \[" log.md`).

## [2026-07-10] setup | Nodo wiki de economia
- Creada la superstructura recursiva de la entidad `economia` dentro de `dominio/`:
  `raw/`, `index.md`, `log.md` y `README.md`.

## [2026-07-10] ingest | Economía — macroeconomía + política fiscal/ciclo
- Fuentes web (reference-only): Wikipedia (es).
- Páginas: `macroeconomia.md` (PIB, inflación, desempleo, política monetaria, bancos
  centrales) e `indicadores-ciclo-fiscal.md` (política fiscal, déficit/deuda, indicadores,
  ciclo económico).
- Reference-only (URL en frontmatter; sin raw/).
