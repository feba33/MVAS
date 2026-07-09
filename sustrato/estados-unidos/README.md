# estados-unidos (entidad de sustrato)

Sub-wiki **auto-contenido** dentro de `sustrato/`. Sigue la arquitectura **LLM Wiki**
de forma **recursiva**: todo lo relativo a estados-unidos vive **solo aquí**.

## Superstructura de esta entidad
- `raw/` — fuentes crudas de estados-unidos (inmutables; Hermes solo lee).
- `index.md` — catálogo de páginas de estados-unidos.
- `log.md` — registro de ingests / queries / lint de estados-unidos.
- páginas `*.md` — entidades/conceptos/resúmenes de estados-unidos, con YAML frontmatter.
- cross-references a otras entidades vía rutas relativas.

## Convenciones locales
- Frontmatter: `capa: sustrato`, `tema: estados-unidos`.
- Una página por concepto/entidad (atómica, reutilizable).
- Al ingerir, la fuente va a `raw/` y las páginas se escriben aquí.
