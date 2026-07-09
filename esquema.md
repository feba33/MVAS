# Esquema de taxonomía — MVAS

Documento de configuración de la taxonomía de subcarpetas por capa. **Fuente de
verdad de la estructura.** El usuario y Hermes lo co-evolucionan.

> El usuario proveerá / refinará la taxonomía completa. Mientras tanto, estas son
> las subcarpetas iniciales sembradas como ejemplo:

- **sustrato/**
  - `mexico/`  `estados-unidos/`
- **dominio/**
  - `finanzas/`  `computacion/`  `marketing/`  `leyes/`  `contabilidad/`  `diseno/`
- **organización/**
  - (por definir: empresas)
- **rol/**
  - `ingeniero-software/`  `ingeniero-uiux/`  `road-lead/`

## Convenciones transversales
- `raw/` — fuentes crudas inmutables (el usuario las pone; Hermes no las toca).
- `index.md` — catálogo de páginas, se actualiza en cada ingest.
- `log.md` — registro cronológico (`## [fecha] tipo | título`).
- Cada página del wiki lleva YAML frontmatter (capa, tema, fuente, fecha,
  confianza, tags). Ver `GUIA-HERMES.md`.

Cuando el usuario pase el esquema definitivo, reemplazar este archivo y crear las
subcarpetas que correspondan.
