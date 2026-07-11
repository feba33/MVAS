# Registro de auditor-interno (log.md)

Registro cronológico **append-only** de la entidad `auditor-interno`.
Prefijo: `## [YYYY-MM-DD] <tipo> | <título>` (parseable: `grep "^## \[" log.md`).

## [2026-07-11] setup | Nodo wiki de auditor-interno
- Creada la superstructura recursiva de la entidad `auditor-interno` dentro de `rol/`:
  `raw/`, `index.md`, `log.md` y `README.md`.
- Principio: toda la info de auditor-interno vive solo en esta carpeta.

## [2026-07-11] ingest | Auditor Interno (Internal Auditor)
- Fuente: Wikipedia (Internal audit) — reference-only.
- Página: `auditor-interno.md`. Función de aseguramiento independiente que agrega valor;
  independencia organizativa (reporta a comité de auditoría); rol en control interno, riesgo y
  gobierno; plan anual; modelo tres líneas; normas IIA; COSO. Distinto de auditor externo.
  Cross-ref gobierno-corporativo, controller, chief-risk-officer, board-member, cfo.
- Reference-only (URL en frontmatter; sin raw/).
