---
titulo: Customer Success Lead (nodo rol)
capa: rol
tema: customer-success-lead
fuente: conocimiento general (reference-only)
fecha: 2026-07-09
confianza: alta
tags: [customer-success, cs, retention]
english_keywords: [customer-success, cs, retention]
---

# Customer Success Lead (nodo rol)

Sub-wiki **auto-contenido** dentro de `rol/`. Sigue la arquitectura **LLM Wiki** de forma **recursiva**: todo lo relativo a customer-success-lead vive **solo aquí**.

## Superstructura de este nodo
- `raw/` — fuentes crudas / citas de customer-success-lead (inmutables; Hermes solo lee).
- `index.md` — catálogo de páginas de customer-success-lead.
- `log.md` — registro de ingests / queries / lint de customer-success-lead.
- `customer-success-lead.md` — página principal del rol (responsabilidades, skills, herramientas, operación con LLM).
- páginas `*.md` — entidades/conceptos/resúmenes del rol, con YAML frontmatter.
- cross-references a otras entidades vía rutas relativas.

## Convenciones locales
- Frontmatter: `capa: rol`, `tema: customer-success-lead`.
- Una página por concepto/entidad (atómica, reutilizable).
- Al ingerir, la fuente va a `raw/` y las páginas se escriben aquí.
