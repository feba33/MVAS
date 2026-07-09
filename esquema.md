# Esquema de taxonomía — MVAS

Documento de configuración de la taxonomía y la **estructura recursiva** del wiki.
**Fuente de verdad de la estructura.** El usuario y Hermes lo co-evolucionan.

## Plantilla de NODO (recursiva) — ⚠️ clave

Cada entidad (un dominio, un país, una empresa, un rol) es un **wiki auto-contenido**
con esta superstructura anidada. La arquitectura LLM Wiki se repite en cada instancia:

```
<capa>/<entidad>/
├── README.md      # identidad de la entidad + convenciones locales
├── index.md       # catálogo de páginas de ESTA entidad
├── log.md         # registro cronológico de ESTA entidad
├── raw/           # fuentes crudas de la entidad (INMUTABLES)
│   └── README.md
└── <paginas>.md   # contenido (entidad/concepto/resumen) con YAML frontmatter
```

- **Aislamiento:** la info de la entidad vive SOLO en su carpeta.
- **Cross-references:** entre páginas del nodo y hacia otros nodos (rutas relativas).
- El raíz `/MVAS` es el nodo superior (tiene su `raw/`, `index.md`, `log.md` y los
  4 nodos de capa `sustrato/ dominio/ organización/ rol/`). Y cada uno de esos
  nodos contiene entidades que son nodos hijos. Fractal.

## Taxonomía inicial (ejemplo, sujeta a refinamiento del usuario)

- **sustrato/**
  - `mexico/`  `estados-unidos/`  *(cada uno = nodo con su superstructura)*
- **dominio/**
  - `finanzas/`  `computacion/`  `marketing/`  `leyes/`  `contabilidad/`  `diseno/`
- **organización/**
  - (por definir: empresas — cada una = nodo)
- **rol/**
  - `ingeniero-software/`  `ingeniero-uiux/`  `road-lead/`

## Convenciones transversales
- `raw/` (en cualquier nivel) — fuentes crudas inmutables que el **usuario deposita localmente** (PDF, texto, imágenes); Hermes no las toca. Para fuentes **web (URL)** se guarda SOLO la cita en el frontmatter `fuente` (no se copia a `raw/`).
- `index.md` — catálogo (el raíz lista nodos; el nodo lista sus páginas).
- `log.md` — registro cronológico (`## [fecha] tipo | título`).
- Cada página lleva YAML frontmatter (capa, tema, fuente, fecha, confianza, tags).
- **Bilingüe (obligatorio):** además de `tags` (español), TODA página nueva debe
  incluir `english_keywords:` (k-words en inglés) para retrieval cross-lingual
  (BM25 + embedding). Se derivan traduciendo las `tags` con
  `scripts/add_en_keywords.py` (lo corre Hermes en lote).
- Ver `GUIA-HERMES.md` para el procedimiento completo de ingest/query/lint.

Cuando el usuario pase la taxonomía definitiva, reemplazar este archivo y crear las
subcarpetas (con su superstructura recursiva) que correspondan.
