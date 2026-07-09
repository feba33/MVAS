# brasil (entidad de sustrato)

Sub-wiki **auto-contenido** dentro de `sustrato/`. Sigue la arquitectura **LLM Wiki**
de forma **recursiva**: todo lo relativo a brasil vive **solo aquí**.

## Superstructura de esta entidad
- `raw/` — fuentes crudas de brasil (inmutables; Hermes solo lee).
- `index.md` — catálogo de páginas de brasil.
- `log.md` — registro de ingests / queries / lint de brasil.
- páginas `*.md` — entidades/conceptos/resúmenes de brasil, con YAML frontmatter.
- cross-references a otras entidades vía rutas relativas.

## Convenciones locales
- Frontmatter: `capa: sustrato`, `tema: brasil`.
- Una página por concepto/entidad (atómica, reutilizable).
- Al ingerir, la fuente va a `raw/` y las páginas se escriben aquí.
