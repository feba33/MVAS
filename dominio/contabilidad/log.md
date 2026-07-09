# Registro de contabilidad (log.md)

Registro cronológico **append-only** de la entidad `contabilidad`.
Prefijo: `## [YYYY-MM-DD] <tipo> | <título>` (parseable: `grep "^## \[" log.md`).

## [2026-07-09] setup | Nodo wiki de contabilidad
- Creada la superstructura recursiva de la entidad `contabilidad` dentro de `dominio/`:
  `raw/`, `index.md`, `log.md` y `README.md`.
- Demuestra el principio: toda la info de contabilidad vive solo en esta carpeta.

## [2026-07-09] ingest | NIIF vs US GAAP
- Fuente: Wikipedia (en) + FASB — reference-only.
- Página: `niif-us-gaap.md`. IFRS (IASB, principios) vs US GAAP (FASB, reglas); convergencia ingresos.

## [2026-07-09] ingest | Contabilidad de costos
- Fuente: conocimiento general — reference-only.
- Página: `costos.md`. Costeo directo/absorbente, ABC, fijos/variables, CPV.

## [2026-07-09] ingest | Auditoría
- Fuente: Wikipedia (en) — Audit (https://en.wikipedia.org/wiki/Audit, reference-only).
- Página: `auditoria.md`. Auditoría interna/externa, integrada (PCAOB/SOX), IFRS audit, dictamen.

## [2026-07-09] ingest | Contabilidad fiscal (impuestos)
- Fuente: conocimiento general — reference-only.
- Página: `impuestos.md`. Impuesto corriente/diferido, IAS 12 / ASC 740, NIIF vs GAAP.
