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

1. **Raw sources → `raw/`** — colección curada de documentos fuente. **Inmutables**:
   Hermes los LEE pero NUNCA los modifica. Es la fuente de verdad.
2. **The wiki → `sustrato/` `dominio/` `organización/` `rol/`** — markdown
   generado por Hermes. Hermes es dueño de esta capa.
3. **The schema → `GUIA-HERMES.md` + `esquema.md`** — configuración del método.

## Las 4 capas de contenido (general → específico)

| Capa | Carpeta | Contenido |
|------|---------|-----------|
| Sustrato | `sustrato/` | Fundamento por **país**: legislación, cultura, reglas, normatividad, noticias, mercados. |
| Dominio | `dominio/` | Referencia y conocimiento puntual por **dominio**: finanzas, computación, marketing, leyes, contabilidad, diseño. |
| Organización | `organización/` | Lo específico de **empresas**: operaciones, decisiones, responsabilidades, artefactos. |
| Rol | `rol/` | **Responsabilidades** y sets de capacidades por rol: ingeniero de software, ingeniero UI/UX, road lead. |

## ⚠️ ARQUITECTURA RECURSIVA (fractal) — CLAVE

La arquitectura LLM Wiki **se aplica a CADA instancia**. **Cada entidad es, en sí
misma, un wiki auto-contenido** con su propia superstructura anidada:
`raw/`, `index.md`, `log.md`, páginas, cross-refs.

**Principio de aislamiento:** la información relevante a una entidad vive **solo
dentro de su carpeta**. Ej.: TODO lo de `finanzas` está en `dominio/finanzas/`.
El raíz es el nodo wiki superior; `sustrato/ dominio/ organización/ rol/` son
nodos; y `dominio/finanzas/` es un nodo hijo — y así recursivamente.

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
  ---
  ```
- **Cross-references:** enlazar con `[texto](ruta-relativa)`.
- Páginas atómicas y reutilizables (una entidad/concepto por página).

## PROCESO DE INGEST (insertar información) — pasos exactos

1. **Recibir fuente**: el usuario la deposita en el `raw/` correspondiente
   (raíz `raw/` para general, o `dominio/finanzas/raw/` para esa entidad) →
   o la adjunta en el chat → Hermes la guarda en el `raw/` adecuado con nombre
   estable. NUNCA modificar ningún `raw/`.
   **Optimización (raw = cita):** si la fuente es **web/scraping**, no es necesario
   guardar el documento en `raw/`; basta citar la **URL en el frontmatter `fuente`**
   de la página (ver `esquema.md`). Aplica a ingesta automática (El Financiero, bucle
   de investigación web).
2. **🔎 DISCERNIMIENTO (inferir entidad):** analizar el input, buscar en la
   taxonomía (`esquema.md` / `index.md` / nodos) las entidades mencionadas, e
   **inferir el nodo destino**.
   - Certeza **ALTA** → proceder (mencionar el destino inferido al usuario).
   - Certeza **BAJA** / ambiguo → **PEDIR CONFIRMACIÓN** con `clarify` ANTES
     de escribir. No escribir a ciegas.
3. **Leer y discutir**: Hermes lee la fuente y **comenta los puntos clave con el
   usuario** (takeaways) antes de escribir.
4. **Ubicar/crear el NODO**: la info va en la carpeta de su entidad
   (`dominio/finanzas/`, `sustrato/mexico/`, etc.).
   - Si el nodo **no existe**, **créalo con su superstructura** (raw/, index.md,
     log.md, README) siguiendo la plantilla recursiva de `esquema.md`.
   - Si ya existe, usa su superstructura **interna**.
5. **Escribir DENTRO del nodo**: páginas en la carpeta del nodo; fuentes en su
   `raw/`; actualizar su `index.md` y `log.md`.
   - Página de resumen de la fuente + páginas de entidad/concepto afectadas
     (¡una fuente puede tocar 10-15 páginas!).
   - Si la nueva info **contradice o amplía** páginas existentes, actualizarlas y
     marcar la contradicción.
6. **Cross-references**: enlazar las páginas nuevas con las existentes (dentro
   del nodo y hacia otros nodos vía rutas relativas).
7. **Actualizar índices**: `index.md` del nodo + (opcional) `index.md` del raíz
   si es navegación de alto nivel.
8. **Registrar en `log.md`** del nodo: `## [YYYY-MM-DD] ingest | Título`.
9. **Persistir** dentro de `/opt/data/MVAS`:
   `git add -A && git commit -m "ingest: <título>" && git push`.

> Preferencia sugerida: ingerir fuentes de una en una, manteniéndose involucrado.
> También se puede batch-ingerir con menos supervisión.

## PROCESO DE QUERY (retrieval)

1. Leer **`index.md`** (raíz y/o del nodo) para localizar páginas.
2. Taladrar hacia las páginas específicas (de `sustrato/` hacia `rol/`/`organización/`,
   y dentro de cada nodo hacia sus páginas).
3. Sintetizar respuesta **con citas** (links a las páginas).
4. Si la respuesta es valiosa (comparación, análisis, conexión), **archívala como
   nueva página del wiki** dentro del nodo correspondiente.

## PROCESO DE LINT (cuidado / optimización)

Periódicamente (o cuando el usuario lo pida), health-check del wiki:
- Contradicciones entre páginas (y entre nodos).
- Claims obsoletos que fuentes más nuevas superaron.
- Páginas huérfanas (sin inbound links).
- Conceptos importantes mencionados pero sin página propia.
- Cross-references faltantes (internas y entre nodos).
- Huecos de datos que se puedan llenar con web search.
- **Integridad recursiva**: verificar que cada entidad tenga su superstructura
  completa y que su info esté aislada en su carpeta.
Reportar hallazgos y aplicar correcciones con commit+push.

## index.md y log.md (convenciones)

- `index.md`: catálogo por categoría. El raíz lista **nodos**; cada nodo lista
  **sus páginas**. Se actualiza en cada ingest.
- `log.md`: append-only cronológico; prefijo `## [YYYY-MM-DD] <tipo> | <título>`
  (parseable con `grep "^##" log.md`).

## REABASTECIMIENTO AUTOMÁTICO DEL BUCLE (análisis de huecos)

Cuando la cola de `working.md` se queda sin temas `pending` (el bucle "completa"),
Hermes **no se detiene**: analiza la base, genera un nuevo plan y sigue. Procedimiento:

1. **Analizar huecos:** correr `python3 scripts/gap_analysis.py`. Reporta temas
   faltantes en nodos existentes y nodos sugeridos (nuevos).
2. **Generar plan:** convertir la lista de huecos en temas `pending` en `working.md`
   (agrupados por capa). Añadir también temas que el usuario o el análisis sugieran
   (noticias, nuevos países, nuevos dominios).
3. **Actualizar `working.md`:** reescribir la cola con los nuevos temas, subir
   `Iteración actual` y `Temas completados`, y registrar en el LOG. Commit + push.
4. **Continuar el bucle:** ejecutar ingest por cada tema `pending` (investigar →
   escribir → actualizar índices/logs → commit), sin pausas, hasta que la cola
   se vacíe otra vez. Al vaciarse, volver al paso 1.

El bucle puede correr **en la conversación** (sin cron) iterando directamente, o vía
el cronjob `e273fdbbba14` (investigación continua). En conversación se usa
`delegate_task` para paralelizar la creación de nodos/páginas. **Raw = cita**
(URL en `fuente`, sin `raw/`).

## NAVEGACIÓN (QMD — búsqueda híbrida)
MVAS se indexa en una colección QMD (`mvas`, DB en `.qmd/`, gitignored) para
búsqueda semántica + BM25 + rerank sobre el repo completo de Markdown.
- **Helper:** `scripts/qmd.py` (librería `qmd`, venv aislado `/opt/data/.venvs/qmd`).
- **Indexar tras edits:** `env -u PYTHONPATH /opt/data/.venvs/qmd/bin/python scripts/qmd.py index`
  (salta `.git/`, `raw/`, `.qmd/`; carga los modelos Qwen3-0.6B una sola vez).
- **Buscar:** `env -u PYTHONPATH /opt/data/.venvs/qmd/bin/python scripts/qmd.py search "consulta" --top-k 5 --rerank [--node dominio]`
- **Skill `qmd`:** instalación, fix de `tokenizers`, pitfall de `PYTHONPATH=/opt/data/stt_lib`, y API baja.
- Así Hermes salta directo a la página correcta sin recorrer todo el árbol.

## Referencia técnica

- Repo (privado): https://github.com/feba33/MVAS — clone: `/opt/data/MVAS`
- `gh` como `feba33`. Al usar gh en terminal:
  `export PATH=/opt/data/bin:$PATH HOME=/opt/data GH_CONFIG_DIR=/opt/data/.config/gh`
- Patrón base: `raw/llm-wiki.md`. Discernimiento: `protocolo-discriminamiento.md`.
