# GUÍA PARA HERMES — Repositorio MVAS (esquema del wiki)

MVAS es un **super wiki en capas de conocimiento**, de lo más general a lo más
específico y granular, mantenido con el patrón **LLM Wiki** (ver
`raw/llm-wiki.md`): en vez de solo recuperar de documentos crudos en cada
consulta, Hermes **construye y mantiene incrementalmente un wiki persistente**
de markdown interconectado que vive entre el usuario y las fuentes crudas.

Mi trabajo: **cuidar, mantener, optimizar y dar retrieval** de este wiki.
El usuario aporta las fuentes y las preguntas; yo hago todo el trabajo de
mantenimiento (resumir, cross-referenciar, archivar, llevar consistencia).

## Las 3 capas del patrón LLM Wiki (mapeadas a MVAS)
1. **Raw sources → `raw/` (raíz)** — colección curada de documentos fuente.
   **Inmutables**: Hermes los LEE pero NUNCA los modifica. Es la fuente de verdad.
2. **The wiki → `sustrato/` `dominio/` `organización/` `rol/`** — markdown
   generado por Hermes. Hermes es dueño de esta capa. **Es el CONTENIDO del wiki.**
3. **The schema → `GUIA-HERMES.md` + `esquema.md`** — configuración del método.

## Las 4 capas de contenido (general → específico)

| Capa | Carpeta | Contenido |
|------|---------|-----------|
| Sustrato | `sustrato/` | Fundamento por **país**: legislación, cultura, reglas, normatividad, noticias, mercados. |
| Dominio | `dominio/` | Referencia y conocimiento puntual por **dominio**: finanzas, computación, marketing, leyes, contabilidad, diseño. |
| Organización | `organización/` | Lo específico de **empresas**: operaciones, decisiones, responsabilidades, artefactos. |
| Rol | `rol/` | **Responsabilidades** y sets de capacidades por rol: ingeniero de software, ingeniero UI/UX, road lead. |

## ⚠️ ARQUITECTURA: UN ENTRY POINT + UN RAW CENTRAL (NO fractal por nodo)
El repositorio tiene **UN SOLO punto de entrada** (`index.md` raíz) y **UN SOLO
depósito de fuentes** (`raw/` raíz). Las carpetas de capa (`sustrato/` `dominio/`
`organización/` `rol/`) son **CONTENIDO de la Wiki**: páginas `.md` organizadas
por tema. **NO son wikis autónomos con su propio `raw/`/`log.md`/estructura.**
- `index.md` raíz = único entry point / hub (léelo PRIMERO).
- `raw/` raíz = único depósito de fuentes crudas (solo el usuario añade).
- Las capas pueden tener un `index.md` de **catálogo** ligero (solo listado) para
  conveniencia de navegación, pero el entry point canónico es siempre el raíz.
- El conocimiento es UNO y centralizado; para moverse entre organizaciones/empresas/
  tareas/roles se navega por las capas y se recupera con QMD.

## ⚠️ CAPA DE DISCERNIMIENTO / ENRUTAMIENTO (inferencia)
Antes de escribir, Hermes **infiere a qué entidad va cada input** SIN que el
usuario lo especifique. Ver `protocolo-discriminamiento.md`. Regla: inferir; si
la certeza es baja, **pedir confirmación** (`clarify`). El usuario no debe
señalar la entidad manualmente.

## 💡 OPTIMIZACIÓN: fuentes web = solo referencia (no raw)
Cuando la fuente es **web (URL, scrape, RSS)**, NO se copia el contenido a `raw/`.
Se guarda **solo una cita/referencia** en el frontmatter de la página del wiki:
`fuente: <url>` (+ título, autor, fecha si aplica). El contenido vivo queda en el
origen; el wiki guarda el resumen condensado y el puntero. Esto evita duplicación,
mantiene el repo ligero y preserva la trazabilidad.

`raw/` se reserva para **documentos que el usuario deposita localmente** (PDF,
texto, imágenes, notas) — esas sí se guardan completas como fuente inmutable.
Al ingerir desde web, **omite el paso de crear archivo en `raw/`**.

## Convenciones de página (wiki)
- Cada página es markdown con **YAML frontmatter**:
  ```yaml
  ---
  titulo: Nombre de la página
  capa: dominio          # sustrato | dominio | organización | rol
  tema: finanzas         # entidad/subcarpeta a la que pertenece
  fuente: raw/articulo-x.md
  fecha: 2026-07-09
  confianza: alta        # alta | media | baja
  tags: [finanzas, inflación]
  english_keywords: [finance, inflation]   # obligatorio (retrieval cross-lingual)
  # Transversal (filtrable, indexado por QMD):
  rol: [cfo]
  actividades: [tesorería]
  organizaciones: [ejemplo-empresa]
  responsabilidades: [reportar]
  tareas: [cierre-mensual]
  profundidad: 2          # 1|2|3
  estado: profundo         # borrador | profundo
  ---
  ```
- **Cross-references:** enlazar con `[texto](ruta-relativa)`.
- Páginas atómicas y reutilizables (una entidad/concepto por página).

## PROCESO DE INGEST (insertar información) — pasos exactos
1. **Recibir fuente**: el usuario la deposita en `raw/` raíz (único) → o la adjunta
   en el chat → Hermes la guarda en `raw/` raíz con nombre estable.
   NUNCA modificar ningún `raw/`.
   **Optimización (raw = cita):** si la fuente es **web/scraping**, no es necesario
   guardar el documento en `raw/`; basta citar la **URL en el frontmatter `fuente`**
   de la página (ver `esquema.md`). Aplica a ingesta automática.
2. **🔎 DISCERNIMIENTO (inferir entidad):** analizar el input, buscar en la
   taxonomía (`esquema.md` / `index.md` raíz) las entidades mencionadas, e
   **inferir la carpeta de capa destino**.
   - Certeza **ALTA** → proceder (mencionar el destino inferido al usuario).
   - Certeza **BAJA** / ambiguo → **PEDIR CONFIRMACIÓN** con `clarify` ANTES
     de escribir. No escribir a ciegas.
3. **Leer y discutir**: Hermes lee la fuente y **comenta los puntos clave con el
   usuario** (takeaways) antes de escribir.
4. **Ubicar/crear la carpeta de CONTENIDO**: la info va en la carpeta de su capa
   (`dominio/finanzas/`, `sustrato/mexico/`, etc.).
   - Si la carpeta **no existe**, **créala (solo contenido: páginas)**. NO crear
     `raw/` ni `log.md` por nodo — esos son centrales en el raíz.
5. **Escribir DENTRO de la carpeta**: páginas `.md` con frontmatter; fuentes en
   `raw/` raíz.
   - Página de resumen de la fuente + páginas de entidad/concepto afectadas
     (¡una fuente puede tocar 10-15 páginas!).
   - Si la nueva info **contradice o amplía** páginas existentes, actualizarlas y
     marcar la contradicción.
6. **Cross-references**: enlazar las páginas nuevas con las existentes (dentro
   de la capa y hacia otras capas vía rutas relativas).
7. **Actualizar índices**: `index.md` raíz (único entry point) + el `index.md` de
   catálogo de la capa si existe.
8. **Registrar en `log.md` raíz**: `## [YYYY-MM-DD] ingest | Título`.
9. **Persistir** dentro de `/opt/data/MVAS`:
   `git add -A && git commit -m "ingest: <título>" && git push`.

> Preferencia sugerida: ingerir fuentes de una en una, manteniéndose involucrado.
> También se puede batch-ingerir con menos supervisión.

## PROCESO DE QUERY (retrieval)
1. Leer **`index.md` raíz** (único entry point) para localizar páginas.
2. Recuperar las páginas específicas (de `sustrato/` hacia `rol/`/`organización/`,
   y dentro de cada carpeta hacia sus páginas) vía QMD o rutas relativas.
3. Sintetizar respuesta **con citas** (links a las páginas).
4. Si la respuesta es valiosa (comparación, análisis, conexión), **archívala como
   nueva página del wiki** dentro de la capa correspondiente.

## PROCESO DE LINT (cuidado / optimización)
Periódicamente (o cuando el usuario lo pida), health-check del wiki:
- Contradicciones entre páginas.
- Claims obsoletos que fuentes más nuevas superaron.
- Páginas huérfanas (sin inbound links).
- Conceptos importantes mencionados pero sin página propia.
- Cross-references faltantes (internas y entre capas).
- Huecos de datos que se puedan llenar con web search.
- **Integridad centralizada**: verificar que `raw/` y `index.md` raíz sean ÚNICOS
  y que el contenido esté en las capas (NO duplicado en "wikis" aislados por nodo).
Reportar hallazgos y aplicar correcciones con commit+push.

## index.md y log.md (convenciones)
- `index.md` raíz: catálogo maestro — lista las capas y nodos con una línea +
  🏷️ tags + 📅 fecha. **Único entry point.**
- `log.md` raíz: append-only cronológico; prefijo `## [YYYY-MM-DD] <tipo> | <título>`
  (parseable con `grep "^##" log.md`).
- Las capas pueden tener `index.md` de catálogo ligero (opcional).

## REABASTECIMIENTO AUTOMÁTICO DEL BUCLE (análisis de huecos)
Cuando la cola de `working.md` se queda sin temas `pending` (el bucle "completa"),
Hermes **no se detiene**: analiza la base, genera un nuevo plan y sigue. Procedimiento:
1. **Analizar huecos:** correr `python3 scripts/gap_analysis.py`. Reporta temas
   faltantes en capas existentes y nodos sugeridos (nuevos).
2. **Generar plan:** convertir la lista de huecos en temas `pending` en `working.md`
   (agrupados por capa). Añadir también temas que el usuario o el análisis sugieran.
3. **Actualizar `working.md`:** reescribir la cola con los nuevos temas, subir
   `Iteración actual` y `Temas completados`, y registrar en el LOG. Commit + push.
4. **Continuar el bucle:** ejecutar ingest por cada tema `pending` (investigar →
   escribir página(s) en la capa → actualizar `index.md` raíz + `log.md` raíz →
   commit), sin pausas, hasta que la cola se vacíe otra vez. Al vaciarse, volver al paso 1.
El bucle puede correr **en la conversación** (sin cron) iterando directamente, o vía
el cronjob `e273fdbbba14` (investigación continua). En conversación se usa
`delegate_task` para paralelizar la creación de páginas. **Raw = cita**
(URL en `fuente`, sin `raw/`).

## NAVEGACIÓN (QMD — búsqueda híbrida on-device)
MVAS se indexa como colección `mvas` del CLI **QMD** (Node.js, `@tobilu/qmd` por Tobi Lütke; modelos GGUF locales, nada en la nube).
- **Instalado:** `npm install -g @tobilu/qmd` (Node ≥ 22; bin en `/opt/data/.npm-global/bin`).
- **Indexar (una vez):** `qmd collection add /opt/data/MVAS --name mvas` → `qmd context add qmd://mvas "wiki MVAS en capas"` → `qmd embed` (descarga ~2GB GGUF + vectores; re-embed al añadir archivos).
- **Buscar:** `qmd query "consulta" --collection mvas` (híbrido+rerank, mejor) · `qmd search` (BM25, instant) · `qmd vsearch` (vector). Añade `--json --limit N`.
- **Helper:** `scripts/qmd.py index|status|search|get` envuelve ese CLI.
- **MCP (recomendado):** `~/.hermes/config.yaml` → `mcp_servers.qmd: {command: qmd, args: [mcp]}`; o daemon HTTP `qmd mcp --http --daemon`.
- **K-words bilingües:** toda página lleva `tags` (ES) + `english_keywords` (EN); el script `scripts/add_en_keywords.py` las regenera en lote. Así el retrieval funciona en ES y EN.
- **Skill `qmd`:** instalación, MCP, modelo multilingüe, y el pitfall de NO confundirlo con el paquete PyPI `qmd` (Python), que es OTRO proyecto.
- Así Hermes salta directo a la página correcta sin recorrer todo el árbol.

## MODO OPERATIVO: retrieval-first + deepen
En **CADA** pregunta del usuario, antes de responder:
1. **Orientación:** leer `index.md` raíz (ÚNICO entry point).
2. **Retrieval:** `qmd query` (lex/vec/intent) sobre la colección `mvas`; si la
   pregunta es de una dimensión concreta (rol X, actividad Y, org Z), incluir esos
   términos en `lex:`/`intent:` para aprovechar el frontmatter transversal indexado.
3. **Evaluar profundidad:** si las páginas recuperadas son `estado: borrador` o
   `profundidad: 1` en un tema central, HACER research a fondo (≥3 fuentes) y
   **ARCHIVAR** la respuesta como página profunda nueva (el wiki crece y la próxima
   vez ya está compilado → ahorro de tokens).
4. Responder **con citas** a las páginas del wiki.

Esto es la *"conciencia mayor al hacer preguntas"* que busca el usuario: Hermes no
re-deriva desde cero si el wiki ya lo tiene, y si no, lo construye y lo deja guardado.

## CONTEXT MANAGEMENT (operar sobre el wiki grande)
1. **Index-first / single entry point:** ante una tarea, PRIMERO consulta `index.md`
   raíz (único entry point) y `esquema.md` §0–§1. No vuelques el wiki.
2. **Retrieval-aware:** usa QMD híbrido — `lex` para nombres propios/leyes/roles exactos,
   `vec` para concepto. Recupera SOLO la sección relevante, no el documento entero.
3. **Token budget:** lee en orden `log.md` raíz → `index.md` raíz → páginas.
   Nunca leas >N líneas por nodo sin necesidad.
4. **Compaction:** si la ventana se llena, escribe resumen de sesión en `working.md` y
   libera detalle (memoria activa vs archivada).
5. **Caching:** `esquema.md` + guías son estables → candidatos a context cache.

## MEJORA CONTINUA (meta-instrucciones)
1. Al terminar cada ciclo: **Reflexion** — "¿seguí esquema.md y esta guía? ¿qué faltó?
   ¿hay patrón repetible?".
2. Si detectas una regla útil → **propón** edición a `esquema.md`/`GUIA-HERMES.md`,
   aplícala y regístrala en `log.md` raíz + CHANGELOG de `working.md`.
3. El **usuario es autoridad final**: cambios estructurales (nuevas capas, organización)
   quedan pendientes de su aprobación; cambios de estilo/no-nodo se auto-aplican.
4. Riesgo de drift: TODO cambio a guías va con bitácora + versión para revertir.

## Referencia técnica

- Repo (privado): https://github.com/feba33/MVAS — clone: `/opt/data/MVAS`
- `gh` como `feba33`. Al usar gh en terminal:
  `export PATH=/opt/data/bin:$PATH HOME=/opt/data GH_CONFIG_DIR=/opt/data/.config/gh`
- Patrón base: `raw/llm-wiki.md`. Discernimiento: `protocolo-discriminamiento.md`.
