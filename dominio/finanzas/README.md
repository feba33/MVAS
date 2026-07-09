# finanzas (entidad de dominio)

Sub-wiki **auto-contenido** dentro de `dominio/`. Sigue la arquitectura **LLM Wiki**
de forma **recursiva**: todo lo relativo a finanzas vive **solo aquí**.

## Superstructura de esta entidad
- `raw/` — fuentes crudas de finanzas (inmutables; Hermes solo lee).
- `index.md` — catálogo de páginas de finanzas.
- `log.md` — registro de ingests / queries / lint de finanzas.
- páginas `*.md` — entidades/conceptos/resúmenes de finanzas, con YAML frontmatter.
- cross-references a otras entidades vía rutas relativas (p.ej. a `organización/empresa-x/`).

## Convenciones locales
- Frontmatter: `capa: dominio`, `tema: finanzas`.
- Una página por concepto/entidad (atómica, reutilizable).
- Al ingerir, la fuente va a `raw/` y las páginas se escriben aquí; se actualizan
  `index.md` y `log.md` de este nodo (no los del raíz, salvo navegación global).
