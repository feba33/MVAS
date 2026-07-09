# diseno (entidad de dominio)

Sub-wiki **auto-contenido** dentro de `dominio/`. Sigue la arquitectura **LLM Wiki**
de forma **recursiva**: todo lo relativo a diseno vive **solo aquí**.

## Superstructura de esta entidad
- `raw/` — fuentes crudas de diseno (inmutables; Hermes solo lee).
- `index.md` — catálogo de páginas de diseno.
- `log.md` — registro de ingests / queries / lint de diseno.
- páginas `*.md` — entidades/conceptos/resúmenes de diseno, con YAML frontmatter.
- cross-references a otras entidades vía rutas relativas.

## Convenciones locales
- Frontmatter: `capa: dominio`, `tema: diseno`.
- Una página por concepto/entidad (atómica, reutilizable).
- Al ingerir, la fuente va a `raw/` y las páginas se escriben aquí.
