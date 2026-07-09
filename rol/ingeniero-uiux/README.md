# ingeniero-uiux (entidad de rol)

Sub-wiki **auto-contenido** dentro de `rol/`. Sigue la arquitectura **LLM Wiki**
de forma **recursiva**: todo lo relativo a ingeniero-uiux vive **solo aquí**.

## Superstructura de esta entidad
- `raw/` — fuentes crudas de ingeniero-uiux (inmutables; Hermes solo lee).
- `index.md` — catálogo de páginas de ingeniero-uiux.
- `log.md` — registro de ingests / queries / lint de ingeniero-uiux.
- páginas `*.md` — entidades/conceptos/resúmenes de ingeniero-uiux, con YAML frontmatter.
- cross-references a otras entidades vía rutas relativas.

## Convenciones locales
- Frontmatter: `capa: rol`, `tema: ingeniero-uiux`.
- Una página por concepto/entidad (atómica, reutilizable).
- Al ingerir, la fuente va a `raw/` y las páginas se escriben aquí.
