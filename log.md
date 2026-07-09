# Registro de actividad (log.md)

Registro cronológico **append-only**: ingests, queries, lint passes.
Prefijo de entrada: `## [YYYY-MM-DD] <tipo> | <título>`
(parseable: `grep "^## \[" log.md | tail -5` → últimas 5 entradas).

## [2026-07-09] setup | Estructura inicial MVAS + patrón LLM Wiki
- Creado repo MVAS con 4 capas: sustrato / dominio / organización / rol.
- Integrado patrón LLM Wiki: capa `raw/` (fuentes inmutables), `index.md`,
  `log.md`, y `GUIA-HERMES.md` como esquema.
- Subcarpetas ejemplo sembradas en las 4 capas.
- Fuente del método guardada en `raw/llm-wiki.md`.

## [2026-07-09] ingest | El Financiero — 8 artículos (opinión)
- 3 → `dominio/finanzas/`: incertidumbre (T-MEC), t-mec-revision-anual-inversionistas, rentas-stock-desafios-vivienda.
- 5 → `sustrato/mexico/`: cdmx-nuevos-partidos, roxana-guzman-fracaso-primeras-horas, donde-esta-rocha-moya, crisis-climatica-salud-infantil, amlo-rocha-ismael-n.
- Autónomo (cronjob). Dedupe: sin duplicados previos. Cross-refs y frontmatter YAML aplicados.
