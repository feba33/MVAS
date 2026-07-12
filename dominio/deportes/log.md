# Registro de deportes (log.md)

Registro cronológico **append-only** de la entidad `deportes`.
Prefijo: `## [YYYY-MM-DD] <tipo> | <título>` (parseable: `grep "^## \[" log.md`).

## [2026-07-12] setup | Nodo wiki de deportes
- Creada la superstructura recursiva de la entidad `deportes` dentro de `dominio/`:
  `raw/`, `index.md`, `log.md` y `README.md`.

## [2026-07-12] ingest | Industria del deporte (media rights, patrocinios, ligas, eSports)
- Fuente: Wikipedia (Sports, Sports broadcasting, Sports marketing) — reference-only (URL en frontmatter, sin raw/).
- Página: `deportes.md`.
