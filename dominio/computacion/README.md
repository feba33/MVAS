# computacion (entidad de dominio)

Sub-wiki **auto-contenido** dentro de `dominio/`. Sigue la arquitectura **LLM Wiki**
de forma **recursiva**: todo lo relativo a computacion vive **solo aquí**.

## Superstructura de esta entidad
- `raw/` — fuentes crudas de computacion (inmutables; Hermes solo lee).
- `index.md` — catálogo de páginas de computacion.
- `log.md` — registro de ingests / queries / lint de computacion.
- páginas `*.md` — entidades/conceptos/resúmenes de computacion, con YAML frontmatter.
- cross-references a otras entidades vía rutas relativas.

## Convenciones locales
- Frontmatter: `capa: dominio`, `tema: computacion`.
- Una página por concepto/entidad (atómica, reutilizable).
- Al ingerir, la fuente va a `raw/` y las páginas se escriben aquí.
