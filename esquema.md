# Esquema de taxonomía — MVAS

Documento de configuración de la taxonomía y la estructura del wiki.
**Fuente de verdad de la estructura.** El usuario y Hermes lo co-evolucionan.

## 0. Principios de diseño (fuente de verdad)
1. El markdown es la **fuente de verdad**; QMD (BM25+vector, 100% local) es **solo el
   índice de orientación**, no el contenido.
2. **UN entry point + UN raw central:** hay UN SOLO `index.md` raíz (punto de entrada
   de conocimiento) y UN SOLO `raw/` raíz (depósito de fuentes crudas). Las capas
   (`sustrato/` · `dominio/` · `organización/` · `rol/`) son **CONTENIDO de la Wiki**
   (páginas `.md`), NO wikis independientes con su propio raw/estructura.
3. **No duplicar: enlazar** (cross-refs). Las fuentes crudas viven en `raw/` raíz
   (local) o como cita `fuente:` en frontmatter (web) — nunca se copia el cuerpo.
4. El agente (Hermes) **escribe** páginas en las capas + actualiza `index.md` raíz y
   `log.md` raíz; el **usuario es autoridad final** de las guías.
5. **Schema-as-source-of-truth + auto-mejora:** tras cada ciclo Hermes reflexiona y puede
   proponer ediciones a este archivo (ver §Meta-instrucciones).

## Estructura del repo (entry point + raw central + contenido)
```
/MVAS
├── index.md          # ÚNICO entry point / hub de conocimiento (léelo PRIMERO)
├── raw/              # ÚNICO depósito de fuentes crudas (INMUTABLE; solo el usuario añade)
│   └── llm-wiki.md  # patrón base (Karpathy)
├── esquema.md        # este archivo (taxonomía + reglas)
├── GUIA-HERMES.md    # procedimiento ingest/query/lint
├── log.md            # registro cronológico GLOBAL
├── working.md        # bucle de enriquecimiento
├── protocolo-discriminamiento.md  # enrutamiento multi-dimensional
└── <capa>/          # CONTENIDO de la Wiki (páginas .md)
    ├── <entidad>/
    │   ├── <pagina>.md     # contenido con YAML frontmatter
    │   └── (sub-carpetas de contenido si el tema crece)
    └── index.md       # catálogo LIGERO de la capa (opcional; el entry point sigue siendo el raíz)
```
- **No hay `raw/` ni `log.md` por nodo.** Todo raw vive en `raw/` raíz; el `log.md`
  raíz es el único registro cronológico.
- Las capas pueden tener un `index.md` de **catálogo** (solo listado de páginas) para
  conveniencia de navegación, pero NO son wikis aparte: el entry point canónico es
  `index.md` raíz.

## Taxonomía inicial (ejemplo, sujeta a refinamiento del usuario)

- **sustrato/**
  - `mexico/`  `estados-unidos/`  *(cada uno = carpeta de contenido con sus páginas)*
- **dominio/**
  - `finanzas/`  `computacion/`  `marketing/`  `leyes/`  `contabilidad/`  `diseno/`
- **organización/**
  - (por definir: empresas — cada una = carpeta de contenido; mecanismo lo define el usuario)
- **rol/**
  - `ingeniero-software/`  `ingeniero-uiux/`  `road-lead/`

## Convenciones transversales
- **`raw/` raíz (único):** fuentes crudas inmutables que el **usuario deposita localmente**
  (PDF, texto, imágenes); Hermes NO las toca. Para fuentes **web (URL)** se guarda SOLO la
  cita en el frontmatter `fuente` (no se copia a `raw/`).
- **`index.md` raíz (único entry point):** catálogo maestro — lista las capas y nodos con
  una línea + 🏷️ tags + 📅 fecha. El agente lo lee PRIMERO para orientarse.
- **`log.md` raíz (único):** registro cronológico (`## [fecha] tipo | título`).
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

## Principio rector: UN ENTRY POINT + UN RAW CENTRAL; EL RESTO ES CONTENIDO
El repositorio tiene **un solo punto de entrada** (`index.md` raíz) y **un solo
depósito de fuentes** (`raw/` raíz). Las carpetas de capa (`sustrato/`, `dominio/`,
`organización/`, `rol/`) son el **contenido de la Wiki**: páginas `.md` organizadas por
tema, NO wikis autónomas con su propio `raw/`/`log.md`/estructura. Para moverse
entre organizaciones/empresas/tareas/roles se navega por las capas y se recupera con
QMD; el conocimiento es UNO y centralizado, no fragmentado en wikis aislados.

## Profundidad (anti-superficialidad)
Toda página nueva cumple un **mínimo por nivel** (el lint marca como 'superficial'
las que no):
- `profundidad: 1` (resumen/N1): definición + 3–5 bullets + ≥1 fuente. ≥40 líneas.
  **Nunca estado final**: es un punto de partida, no un entregable.
- `profundidad: 2` (estándar/N2, **mínimo aceptable**): secciones completas +
  **≥3 fuentes** + citas + cross-refs + registro en `log.md` raíz. ≥120 líneas.
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

## Crecimiento del contenido (en vez de "promoción a sub-wiki")
Cuando una página crece más allá de `profundidad: 3` (o aparecen 2+ sub-temas
claros), se **expande o se parte** en páginas relacionadas dentro de la MISMA capa
(sub-carpeta de contenido), manteniendo `raw/` raíz central y `index.md` raíz como
únicos puntos de referencia. **NO** se crea un "sub-wiki" aislado con su propio raw.
Regla de no-duplicación: al partir, usa cross-refs, no copies.

## Context management (cómo opera Hermes sobre el wiki)
- **Index-first / single entry point:** leer `index.md` raíz PRIMERO (es el único
  entry point). Solo desciende a la capa/nodo cuando el tema lo exija.
- **Retrieval-aware:** usar QMD (lex para nombres propios/leyes/roles exactos; vec para
  concepto) para traer SOLO la sección/página relevante.
- **Token budget:** priorizar `log.md` raíz > `index.md` raíz > páginas. Nunca leer
  >N líneas por nodo sin necesidad.
- **Compaction:** al llenarse la ventana, escribir resumen de sesión en `working.md` y
  descartar detalle (memoria activa vs archivada).
- **Caching:** `esquema.md` + guías son estables → candidatos a context cache.

## Meta-instrucciones (auto-mejora controlada)
- Tras cada ciclo, Hermes ejecuta **Reflexion**: "¿seguí esquema.md y GUIA-HERMES.md?
  ¿qué faltó? ¿hay patrón repetible?".
- Si surge regla nueva útil → **proponer** edición a `esquema.md`/`GUIA-HERMES.md`,
  aplicar y registrar en `log.md` raíz con versión. `working.md` lleva CHANGELOG de guías.
- El **usuario es autoridad final**: cambios estructurales (nuevas capas, organización)
  requieren aprobación; cambios de estilo/no-nodo se auto-aplican.
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
y crear las subcarpetas (de contenido) que correspondan.
