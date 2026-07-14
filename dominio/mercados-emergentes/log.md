# Registro de mercados-emergentes (log.md)

Registro cronológico **append-only** de la entidad `mercados-emergentes`.
Prefijo: `## [YYYY-MM-DD] <tipo> | <título>` (parseable: `grep "^## \[" log.md`).

## [2026-07-14] setup | Nodo wiki de mercados-emergentes
- Creada la superstructura recursiva de la entidad `mercados-emergentes` dentro de `dominio/`:
  `raw/`, `index.md`, `log.md` y `README.md`.
- Principio: toda la info de mercados-emergentes vive solo en esta carpeta.

## [2026-07-14] ingest | Mercados emergentes (emerging markets)
- Fuente: Wikipedia EN (Emerging market) + IMF/World Bank (contexto).
- Página: `mercados-emergentes.md`.
- Reference-only (URL en frontmatter; sin raw/).
