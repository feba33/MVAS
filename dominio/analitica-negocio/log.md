# Registro de analitica-negocio (log.md)

Registro cronológico **append-only** de la entidad `analitica-negocio`.
Prefijo: `## [YYYY-MM-DD] <tipo> | <título>` (parseable: `grep "^## \[" log.md`).

## [2026-07-11] setup | Nodo wiki de analitica-negocio
- Creada la superstructura recursiva de la entidad `analitica-negocio` dentro de `dominio/`:
  `raw/`, `index.md`, `log.md` y `README.md`.
- Principio: toda la info de analitica-negocio vive solo en esta carpeta.

## [2026-07-11] ingest | Analítica de negocio / Business Analytics
- Fuentes: Databricks (business analytics), Domo (analytics dashboards) — reference-only.
- Página: `analitica-negocio.md`. Tipos (descriptiva/diagnóstica/predictiva/prescriptiva);
  dashboards/KPIs; brecha insight→acción (90.5% Fortune 1000 prioriza data/IA, <24% cultura
  data-driven, McKinsey: 70% de transformaciones fallan). Cross-ref estadistica, finanzas,
  rol/data-analyst, rol/data-scientist, rol/chief-data-officer.
- Reference-only (URL en frontmatter; sin raw/).
