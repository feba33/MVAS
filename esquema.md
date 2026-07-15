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
- **Frontmatter obligatorio por página** (YAML):
  - Base: `titulo, capa, tema, fuente, fecha, confianza, tags, english_keywords`.
  - **Transversal (filtrable por dimensión cruzada, indexado por QMD):** `rol: [..]`, `actividades: [..]`, `organizaciones: [..]`, `responsabilidades: [..]`, `tareas: [..]`, `profundidad: 1|2|3`, `estado: borrador|profundo`.
    Son **multivalor**: una página puede aplicar a varios roles / organizaciones / actividades. Al indexarse en QMD permiten recuperar por esas dimensiones con `qmd query` (lex/vec) sin herramientas externas.
- **Bilingüe (obligatorio):** además de `tags` (español), TODA página nueva debe
  incluir `english_keywords:` (k-words en inglés) para retrieval cross-lingual
  (BM25 + embedding). Se derivan traduciendo las `tags` con
  `scripts/add_en_keywords.py` (lo corre Hermes en lote).
- Ver `GUIA-HERMES.md` para el procedimiento completo de ingest/query/lint.

Cuando el usuario pase la taxonomía definitiva, reemplazar este archivo y crear las
subcarpetas (con su superstructura recursiva) que correspondan.

## Principio rector: CADA ELEMENTO ES SU PROPIA WIKI
El repositorio es **fractal**. El raíz `/MVAS` es un wiki; cada nodo
(`sustrato/<país>`, `dominio/<dominio>`, `rol/<rol>`, `organización/<empresa>`)
es **su propia wiki auto-contenida** con `raw/`, `index.md`, `log.md`, `README.md`
y sus páginas. Una página (`<nodo>/<tema>.md`) es la unidad atómica; cuando crece
más allá de `profundidad: 3` se **PROMUEVE a sub-nodo** (sub-wiki) con su propia
superstructura. Regla de aislamiento: la información de un elemento vive SOLO en su
carpeta; para moverse entre organizaciones/empresas/tareas se navega de nodo a nodo.

## Profundidad (anti-superficialidad)
Toda página nueva cumple un **mínimo por nivel** (el lint marca como 'superficial'
las que no):
- `profundidad: 1` (visor/índice): ≥40 líneas, 3+ secciones.
- `profundidad: 2` (sustantiva): ≥120 líneas, secciones completas.
- `profundidad: 3` (referencia): ≥200 líneas, caso(s) trabajado(s), métricas, contradicciones.
Secciones obligatorias por defecto: Definición · Marco normativo (si aplica) · Actores
· Proceso/Ciclo · Riesgos · Métricas/KPIs · Herramientas · Casos · Referencias.
Ingest mínimo: **≥3 fuentes** y una pasada de *deepen* (borrador → autocrítica →
expandir) antes de commit. Nunca se commitea una página `estado: borrador` como si
fuera definitiva.

## Filtrado (solo herramientas probadas: QMD)
El filtrado multidimensional por rol/actividad/org/se responsabilidad se hace con
**QMD** (instalado, híbrido BM25+vector, 100% local). Los campos transversales del
frontmatter se indexan, así que `qmd query` con `lex:`/`vec:`/`intent:` recupera por
esas dimensiones y `--collection` acota a un corpus. **No se usan scripts de
filtrado propios** — QMD es la única herramienta de búsqueda/filtrado.
