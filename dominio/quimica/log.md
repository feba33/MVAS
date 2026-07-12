# Registro de quimica (log.md)

Registro cronológico **append-only** de la entidad `quimica`.
Prefijo: `## [YYYY-MM-DD] <tipo> | <título>` (parseable: `grep "^## \[" log.md`).

## [2026-07-12] setup | Nodo wiki de quimica
- Creada la superstructura recursiva de la entidad `quimica` dentro de `dominio/`:
  `raw/`, `index.md`, `log.md` y `README.md`.
- Principio: toda la info de quimica vive solo en esta carpeta.

## [2026-07-12] ingest | Industria química
- Fuente: ECHA (REACH), EPA (TSCA), Wikipedia (Chemical industry).
- Página: `quimica.md`.
- Reference-only (URL en frontmatter; sin raw/).
