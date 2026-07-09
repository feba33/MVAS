# Registro de finanzas (log.md)

Registro cronológico **append-only** de la entidad `finanzas`.
Prefijo de entrada: `## [YYYY-MM-DD] <tipo> | <título>`
(parseable: `grep "^## \[" log.md | tail -5` → últimas 5 entradas).

## [2026-07-09] setup | Nodo wiki de finanzas
- Creada la superstructura recursiva de la entidad `finanzas` dentro de `dominio/`:
  `raw/`, `index.md`, `log.md` y `README.md`.
- Demuestra el principio: toda la info de finanzas vive solo en esta carpeta.
