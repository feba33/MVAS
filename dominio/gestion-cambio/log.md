# Registro de gestion-cambio (log.md)

Registro cronológico **append-only** de la entidad `gestion-cambio`.
Prefijo: `## [YYYY-MM-DD] <tipo> | <título>` (parseable: `grep "^## \[" log.md`).

## [2026-07-11] setup | Nodo wiki de gestion-cambio
- Creada la superstructura recursiva de la entidad `gestion-cambio` dentro de `dominio/`:
  `raw/`, `index.md`, `log.md` y `README.md`.
- Principio: toda la info de gestion-cambio vive solo en esta carpeta.

## [2026-07-11] ingest | Gestión del cambio
- Fuentes: Deckary (Kotter/ADKAR case studies), Prosci (ADKAR), Status.net (modelos) — reference-only.
- Página: `gestion-cambio.md`. Modelos Lewin (unfreeze-change-refreeze), Kotter 8 pasos,
  ADKAR (Prosci), McKinsey 7S; ~70% de transformaciones fallan (cultura barrera). Cross-ref
  cultura-organizacional, estrategia, chief-of-staff, head-of-people, innovacion.
- Reference-only (URL en frontmatter; sin raw/).
