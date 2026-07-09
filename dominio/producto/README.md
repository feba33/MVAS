# producto (entidad de dominio)

Sub-wiki **auto-contenido** dentro de `dominio/`. Sigue la arquitectura **LLM Wiki** de forma **recursiva**: todo lo relativo a producto vive **solo aquí**.

## Superstructura de esta entidad
- `raw/` — fuentes crudas de producto (inmutables; Hermes solo lee).
- `index.md` — catálogo de páginas de producto.
- `log.md` — registro de ingests / queries / lint de producto.
- `producto.md` — página principal de la entidad (discovery, AARRR, PMF, roadmap).
- páginas `*.md` — entidades/conceptos/resúmenes de producto, con YAML frontmatter.
- cross-references a otras entidades vía rutas relativas.

## Convenciones locales
- Frontmatter: `capa: dominio`, `tema: producto`.
- Una página por concepto/entidad (atómica, reutilizable).
- Al ingerir, la fuente va a `raw/` y las páginas se escriben aquí.
