# mexico (entidad de sustrato)

Sub-wiki **auto-contenido** dentro de `sustrato/`. Sigue la arquitectura **LLM Wiki**
de forma **recursiva**: todo lo relativo a mexico vive **solo aquí**.

## Superstructura de esta entidad
- `raw/` — fuentes crudas de mexico (inmutables; Hermes solo lee).
- `index.md` — catálogo de páginas de mexico.
- `log.md` — registro de ingests / queries / lint de mexico.
- páginas `*.md` — entidades/conceptos/resúmenes de mexico, con YAML frontmatter.
- cross-references a otras entidades vía rutas relativas.

## Convenciones locales
- Frontmatter: `capa: sustrato`, `tema: mexico`.
- Una página por concepto/entidad (atómica, reutilizable).
- Al ingerir, la fuente va a `raw/` y las páginas se escriben aquí.
