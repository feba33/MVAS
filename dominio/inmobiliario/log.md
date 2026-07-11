# Registro de inmobiliario (log.md)

Registro cronológico **append-only** de la entidad `inmobiliario`.
Prefijo: `## [YYYY-MM-DD] <tipo> | <título>` (parseable: `grep "^## \[" log.md`).

## [2026-07-11] setup | Nodo wiki de inmobiliario
- Creada la superstructura recursiva de la entidad `inmobiliario` dentro de `dominio/`:
  `raw/`, `index.md`, `log.md` y `README.md`.
- Principio: toda la info de bienes raíces vive solo en esta carpeta.

## [2026-07-11] ingest | Bienes raíces (real estate)
- Fuente: Wikipedia (Real estate), REIT.com.
- Página: `bienes-raices.md`.
- Reference-only (URL en frontmatter; sin raw/).
