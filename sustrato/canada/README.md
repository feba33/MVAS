# canada (entidad de sustrato)

Sub-wiki **auto-contenido** dentro de `sustrato/`. Sigue la arquitectura **LLM Wiki**
de forma **recursiva**: todo lo relativo a canada vive **solo aquí**.

## Superstructura de esta entidad
- `raw/` — fuentes crudas de canada (inmutables; Hermes solo lee).
- `index.md` — catálogo de páginas de canada.
- `log.md` — registro de ingests / queries / lint de canada.
- páginas `*.md` — entidades/conceptos/resúmenes de canada, con YAML frontmatter.
- cross-references a otras entidades vía rutas relativas.

## Convenciones locales
- Frontmatter: `capa: sustrato`, `tema: canada`.
- Una página por concepto/entidad (atómica, reutilizable).
- Al ingerir, la fuente va a `raw/` y las páginas se escriben aquí.
