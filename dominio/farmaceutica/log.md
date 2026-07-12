# Registro de farmaceutica (log.md)

Registro cronológico **append-only** de la entidad `farmaceutica`.
Prefijo: `## [YYYY-MM-DD] <tipo> | <título>` (parseable: `grep "^## \[" log.md`).

## [2026-07-12] setup | Nodo wiki de farmaceutica
- Creada la superstructura recursiva de la entidad `farmaceutica` dentro de `dominio/`:
  `raw/`, `index.md`, `log.md` y `README.md`.
- Principio: toda la info de farmaceutica vive solo en esta carpeta.

## [2026-07-12] ingest | Industria farmacéutica
- Fuente: FDA (Development & Approval Process), EMA, Wikipedia (Pharmaceutical industry).
- Página: `farmaceutica.md`.
- Reference-only (URL en frontmatter; sin raw/).
