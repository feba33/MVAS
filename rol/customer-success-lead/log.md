# Registro de customer-success-lead (log.md)

Registro cronológico **append-only** del nodo `customer-success-lead`.
Prefijo: `## [YYYY-MM-DD] <tipo> | <título>` (parseable: `grep "^## \[" log.md`).

## [2026-07-09] setup | Nodo wiki de customer-success-lead
- Creada la superstructura recursiva del rol `customer-success-lead` dentro de `rol/`:
  `raw/`, `index.md`, `log.md`, `README.md` y la página principal `customer-success-lead.md`.
- Demuestra el principio: toda la info de customer-success-lead vive solo en esta carpeta.

## [2026-07-09] ingest | Customer Success Lead (rol)
- Fuente: conocimiento general — reference-only.
- Página: `customer-success-lead.md`. Responsabilidades (onboarding, retención, expansión, NPS), skills (empatía, data), herramientas (Gainsight, Intercom) y operación con LLM (playbooks, análisis de churn, QBRs).
- Cross-ref: `rol/sales-lead/` y `dominio/producto/producto.md`.
