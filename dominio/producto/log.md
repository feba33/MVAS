# Registro de producto (log.md)

Registro cronológico **append-only** de la entidad `producto`.
Prefijo: `## [YYYY-MM-DD] <tipo> | <título>` (parseable: `grep "^## \[" log.md`).

## [2026-07-09] setup | Nodo wiki de producto
- Creada la superstructura recursiva de la entidad `producto` dentro de `dominio/`:
  `raw/`, `index.md`, `log.md`, `README.md` y la página principal `producto.md`.
- Demuestra el principio: toda la info de producto vive solo en esta carpeta.

## [2026-07-09] ingest | Producto (entidad de dominio)
- Fuente: conocimiento general — reference-only.
- Página: `producto.md`. Discovery (oportunidad/problema), métricas AARRR (activation/retention/revenue/referral), PMF (product-market fit) y roadmap.
- Cross-ref: `rol/product-lead/` y `dominio/marketing/`.
