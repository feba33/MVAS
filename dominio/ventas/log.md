# Registro de ventas (log.md)

Registro cronológico **append-only** de la entidad `ventas`.
Prefijo: `## [YYYY-MM-DD] <tipo> | <título>` (parseable: `grep "^## \[" log.md`).

## [2026-07-09] setup | Nodo wiki de ventas
- Creada la superstructura recursiva de la entidad `ventas` dentro de `dominio/`:
  `raw/`, `index.md`, `log.md` y `README.md`.
- Demuestra el principio: toda la info de ventas vive solo en esta carpeta.

## [2026-07-09] ingest | Metodología y operación de ventas
- Fuente: conocimiento general — reference-only.
- Página: `ventas.md`. Metodologías (SPIN, Challenger, MEDDIC), funnel (TOFU/MOFU/BOFU),
  CRM (Salesforce/HubSpot) y métricas clave (pipeline, CAC, win rate).
