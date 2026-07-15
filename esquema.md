# Esquema de taxonomía — MVAS

Documento de configuración de la taxonomía y la **estructura recursiva** del wiki.
**Fuente de verdad de la estructura.** El usuario y Hermes lo co-evolucionan.

## 0. Principios de diseño (fuente de verdad)
1. El markdown es la **fuente de verdad**; QMD (BM25+vector, 100% local) es **solo el
   índice de orientación**, no el contenido.
2. Estructura **recursiva / fractal**: CADA elemento del repo es su propia wiki
   auto-contenida (ver §Plantilla de NODO).
3. **No duplicar: enlazar** (cross-refs). Las fuentes crudas viven en `raw/` (local) o
   como cita `fuente:` en frontmatter (web) — nunca se copia el cuerpo del origen.
4. El agente (Hermes) **escribe** en `log.md` / `working.md` / `raw/`; el **usuario es
   autoridad final** de las guías. Los cambios estructurales requieren su aprobación.
5. **Schema-as-source-of-truth + auto-mejora**: tras cada ciclo Hermes reflexiona y puede
   proponer ediciones a este archivo (ver §Meta-instrucciones).

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
  nodos contiene entidades que son nodos hijos. **Fractal.**

## Taxonomía inicial (ejemplo, sujeta a refinamiento del usuario)

- **sustrato/**
  - `mexico/`  `estados-unidos/`  *(cada uno = nodo con su superstructura)*
- **dominio/**
  - `finanzas/`  `computacion/`  `marketing/`  `leyes/`  `contabilidad/`  `diseno/`
- **organización/**
  - (por definir: empresas — cada una = nodo; mecanismo lo define el usuario)
- **rol/**
  - `ingeniero-software/`  `ingeniero-uiux/`  `road-lead/`

## Convenciones transversales
- `raw/` (en cualquier nivel) — fuentes crudas inmutables que el **usuario deposita localmente**
  (PDF, texto, imágenes); Hermes no las toca. Para fuentes **web (URL)** se guarda SOLO la
  cita en el frontmatter `fuente` (no se copia a `raw/`).
- `index.md` — catálogo (el raíz lista nodos; el nodo lista sus páginas).
- `log.md` — registro cronológico (`## [fecha] tipo | título`).
- **Frontmatter obligatorio por página** (YAML):
  - Base: `titulo, capa, tema, fuente, fecha, confianza, tags, english_keywords`.
  - **Transversal (filtrable por dimensión cruzada, indexado por QMD):** `rol: [..]`,
    `actividades: [..]`, `organizaciones: [..]`, `responsabilidades: [..]`, `tareas: [..]`,
    `profundidad: 1|2|3`, `estado: borrador|profundo`.
    Son **multivalor**: una página puede aplicar a varios roles / organizaciones / actividades.
    Al indexarse en QMD permiten recuperar por esas dimensiones con `qmd query` (lex/vec).
- **Bilingüe (obligatorio):** además de `tags` (español), TODA página nueva debe
  incluir `english_keywords:` (k-words en inglés) para retrieval cross-lingual
  (BM25 + embedding). Se derivan traduciendo las `tags` con
  `scripts/add_en_keywords.py` (lo corre Hermes en lote).
- **Citas como ciudadano primordial:** toda afirmación fáctica lleva `fuente:` en
  frontmatter (o inline). Sin fuente → `confianza: baja` o se borra. Nunca se duplica
  el cuerpo del origen (ahorra tokens y preserva trazabilidad).
- Ver `GUIA-HERMES.md` para el procedimiento completo de ingest/query/lint.

## Secciones obligatorias POR TIPO
- **país**: Contexto · Marco legal · Economía · Riesgos · Cross-refs
- **rol**: Definición · Responsabilidades · Habilidades · Cómo un LLM opera aquí · Referencias
- **dominio**: Definición · Componentes · Herramientas · Casos · Cross-refs
- **empresa**: Qué es · Estructura/Org · Producto · Mercado · Riesgos · Referencias
(Toda afirmación fáctica → fuente en frontmatter o inline.)

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
- `profundidad: 1` (resumen/N1): definición + 3–5 bullets + ≥1 fuente. ≥40 líneas.
  **Nunca estado final**: es un punto de partida, no un entregable.
- `profundidad: 2` (estándar/N2, **mínimo aceptable**): secciones completas +
  **≥3 fuentes** + citas + cross-refs + `log.md`. ≥120 líneas.
- `profundidad: 3` (profundo/N3): análisis, contra-argumentos, datos, casos,
  **≥5 fuentes**, mantenido activamente. ≥200 líneas.
- **Regla anti-stub:** ningún nodo permanece en `estado: borrador` / N1 permanente.
  El bucle de enriquecimiento (`working.md` + `scripts/gap_analysis.py` +
  `scripts/lint.py`) debe subirlo a N2 en la próxima pasada. Un stub puro
  (1–2 líneas) es SOLO transitorio.
- Secciones obligatorias por defecto (afinar por tipo en §Secciones): Definición · Marco
  normativo (si aplica) · Actores · Proceso/Ciclo · Riesgos · Métricas/KPIs ·
  Herramientas · Casos · Referencias.
- Ingest mínimo: **≥3 fuentes** y una pasada de *deepen* (borrador → autocrítica →
  expandir) antes de commit. Nunca se commitea una página `estado: borrador` como si
  fuera definitiva.

## Promoción PÁGINA → NODO (sub-wiki)
Umbral (cumple cualquiera): **>60 líneas · >5 secciones · >4 fuentes · aparecen 2+
sub-temas claros**. Al cumplirse: crear carpeta, mover contenido a `README.md`,
generar `index.md`+`log.md`+`raw/`, registrar en `log.md` del padre y en §Taxonomía.
El agente **PROPONE**; aplica si no hay conflicto (cambio estructural → aprobación
del usuario).

## Context management (cómo opera Hermes sobre el wiki grande)
- **Index-first / progressive disclosure:** leer `index.md` (raíz y del nodo) ANTES que
  `README.md`; solo bajar al nodo cuando el tema lo exija.
- **Retrieval-aware:** usar QMD (lex para nombres propios/leyes/roles exactos; vec para
  concepto) DENTRO del nodo para traer SOLO la sección relevante.
- **Token budget:** priorizar `log.md` > `index.md` > `README.md`; nunca leer >N líneas
  por nodo sin necesidad.
- **Compaction:** al llenarse la ventana, escribir resumen de sesión en `working.md` y
  descartar detalle (memoria activa vs archivada).
- **Caching:** `esquema.md` + guías son estables → candidatos a context cache.

## Meta-instrucciones (auto-mejora controlada)
- Tras cada ciclo, Hermes ejecuta **Reflexion**: "¿seguí esquema.md y GUIA-HERMES.md?
  ¿qué faltó? ¿hay patrón repetible?".
- Si surge regla nueva útil → **proponer** edición a `esquema.md`/`GUIA-HERMES.md`,
  aplicar y registrar en `log.md` con versión. `working.md` lleva CHANGELOG de guías.
- El **usuario es autoridad final**: cambios estructurales (nuevas capas, promociones
  grandes) requieren aprobación; cambios de estilo/no-nodo se auto-aplican.
- Riesgo de drift: TODO cambio a guías va con bitácora + versión para poder revertir.

## Filtrado (solo QMD — herramienta probada)
El filtrado multidimensional por rol/actividad/org/responsabilidad se hace con **QMD**
(instalado, híbrido BM25+vector, 100% local). QMD filtra SOLO por **colección**
(nivel de carpeta, `--collection`); NO por campos de frontmatter. El filtrado por
dimensión se logra porque **el frontmatter se indexa como texto**, así `qmd query` con
`lex:`/`vec:`/`intent:` recupera por esas dimensiones y `--collection` acota el corpus.
**No se usan scripts de filtrado propios** — QMD es la única herramienta de
búsqueda/filtrado; el agente hace post-filtrado leyendo el YAML de los candidatos.

---

Cuando el usuario pase la taxonomía definitiva de `organización/`, reemplazar este archivo
y crear las subcarpetas (con su superstructura recursiva) que correspondan.
