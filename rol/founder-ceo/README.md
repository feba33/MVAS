---
titulo: Founder / CEO (nodo rol)
capa: rol
tema: founder-ceo
fuente: conocimiento general (reference-only)
fecha: 2026-07-09
confianza: alta
tags: [founder, ceo, strategy]
english_keywords: [founder, ceo, strategy]
---

# Founder / CEO (nodo rol)

Sub-wiki **auto-contenido** dentro de `rol/`. Sigue la arquitectura **LLM Wiki** de forma **recursiva**: todo lo relativo a founder-ceo vive **solo aquí**.

## Superstructura de este nodo
- `raw/` — fuentes crudas / citas de founder-ceo (inmutables; Hermes solo lee).
- `index.md` — catálogo de páginas de founder-ceo.
- `log.md` — registro de ingests / queries / lint de founder-ceo.
- `founder-ceo.md` — página principal del rol (responsabilidades, skills, herramientas, operación con LLM).
- páginas `*.md` — entidades/conceptos/resúmenes del rol, con YAML frontmatter.
- cross-references a otras entidades vía rutas relativas.

## Convenciones locales
- Frontmatter: `capa: rol`, `tema: founder-ceo`.
- Una página por concepto/entidad (atómica, reutilizable).
- Al ingerir, la fuente va a `raw/` y las páginas se escriben aquí.
