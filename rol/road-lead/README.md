# road-lead (entidad de rol)

Sub-wiki **auto-contenido** dentro de `rol/`. Sigue la arquitectura **LLM Wiki**
de forma **recursiva**: todo lo relativo a road-lead vive **solo aquí**.

## Superstructura de esta entidad
- `raw/` — fuentes crudas de road-lead (inmutables; Hermes solo lee).
- `index.md` — catálogo de páginas de road-lead.
- `log.md` — registro de ingests / queries / lint de road-lead.
- páginas `*.md` — entidades/conceptos/resúmenes de road-lead, con YAML frontmatter.
- cross-references a otras entidades vía rutas relativas.

## Convenciones locales
- Frontmatter: `capa: rol`, `tema: road-lead`.
- Una página por concepto/entidad (atómica, reutilizable).
- Al ingerir, la fuente va a `raw/` y las páginas se escriben aquí.
