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

1. **Raw sources → `raw/`** — colección curada de documentos fuente (artículos,
   papers, imágenes, datos, transcripciones). **Inmutables**: Hermes los LEE
   pero NUNCA los modifica. Es la fuente de verdad.
2. **The wiki → `sustrato/` `dominio/` `organización/` `rol/`** — directorios de
   markdown generados por Hermes (resúmenes, páginas de entidad, páginas de
   concepto, comparaciones, síntesis). Hermes es dueño de esta capa: la crea,
   la actualiza y mantiene las cross-references. El usuario la lee; Hermes la escribe.
3. **The schema → `GUIA-HERMES.md` + `esquema.md`** — este documento + la
   taxonomía. Dicen a Hermes cómo está estructurado el wiki, las convenciones y
   los workflows. Es el archivo de configuración clave.

## Las 4 capas de contenido (general → específico)

| Capa | Carpeta | Contenido |
|------|---------|-----------|
| Sustrato | `sustrato/` | Fundamento por **país**: legislación, cultura, reglas, normatividad, noticias, mercados. Subcarpetas por país. |
| Dominio | `dominio/` | Referencia y conocimiento puntual por **dominio**: finanzas, computación, marketing, leyes, contabilidad, diseño. |
| Organización | `organización/` | Lo específico de **empresas**: operaciones, decisiones, responsabilidades, artefactos, bases de conocimiento internas. |
| Rol | `rol/` | **Responsabilidades** y sets de capacidades por rol: ingeniero de software, ingeniero UI/UX, road lead. |

## Convenciones de página (wiki)

- Cada página es markdown con **YAML frontmatter**:
  ```yaml
  ---
  titulo: Nombre de la página
  capa: dominio          # sustrato | dominio | organización | rol
  tema: finanzas         # subcarpeta
  fuente: raw/articulo-x.md
  fecha: 2026-07-09
  confianza: alta        # alta | media | baja
  tags: [finanzas, inflación]
  ---
  ```
- Usar **cross-references**: enlazar páginas relacionadas con `[texto](ruta)`.
- Escribir en español; términos técnicos en inglés cuando aplique.
- Mantener páginas atómicas y reutilizables (una entidad/concepto por página).

## PROCESO DE INGEST (insertar información) — pasos exactos

Cada vez que el usuario diga *"actualiza MVAS"* / *"ingiere esto"* / adjunte una
fuente:

1. **Recibir fuente**: el usuario la deposita en `raw/` (o la adjunta en el
   chat → Hermes la guarda en `raw/` con nombre estable). NUNCA modificar `raw/`.
2. **Leer y discutir**: Hermes lee la fuente y **comenta los puntos clave con el
   usuario** (takeaways) antes de escribir.
3. **Clasificar**: ubicar la info por capa (sustrato/dominio/organización/rol) y
   subcarpeta según `esquema.md`.
4. **Escribir/actualizar páginas** en la capa correspondiente:
   - Página de resumen de la fuente (en su subcarpeta).
   - Páginas de entidad/concepto afectadas (¡una fuente puede tocar 10-15 páginas!).
   - Si la nueva info **contradice o amplía** páginas existentes, actualizarlas y
     marcar la contradicción.
5. **Cross-references**: enlazar las páginas nuevas con las existentes.
6. **Actualizar `index.md`**: añadir/actualizar la entrada catalogada de cada
   página nueva (link + resumen de 1 línea + metadata).
7. **Registrar en `log.md`**: añadir entrada
   `## [YYYY-MM-DD] ingest | Título de la fuente`.
8. **Persistir**: dentro de `/opt/data/MVAS`:
   `git add -A && git commit -m "ingest: <título>" && git push`.

> Preferencia sugerida: ingerir fuentes de una en una, manteniéndose involucrado
> (leer resúmenes, guiar énfasis). También se puede batch-ingerir con menos
> supervisión. Lo decide el usuario y se documenta en `esquema.md`.

## PROCESO DE QUERY (retrieval)

1. Leer **`index.md`** primero para localizar páginas relevantes.
2. Taladrar hacia las páginas específicas (de `sustrato/` hacia `rol/`/`organización/`).
3. Sintetizar respuesta **con citas** (links a las páginas).
4. Si la respuesta es valiosa (comparación, análisis, conexión descubierta),
   **archivarla como nueva página del wiki** → así las exploraciones acumulan
   conocimiento igual que las fuentes ingeridas.

## PROCESO DE LINT (cuidado / optimización)

Periódicamente (o cuando el usuario lo pida), hacer health-check del wiki:
- Contradicciones entre páginas.
- Claims obsoletos que fuentes más nuevas superaron.
- Páginas huérfanas (sin inbound links).
- Conceptos importantes mencionados pero sin página propia.
- Cross-references faltantes.
- Huecos de datos que se puedan llenar con web search.
Reportar hallazgos y sugerir nuevas preguntas/fuentes. Aplicar correcciones
con commit+push.

## index.md y log.md (convenciones)

- `index.md`: catálogo por categoría; cada página con link + resumen + metadata.
  Se actualiza en cada ingest. El LLM lo lee primero al responder.
- `log.md`: append-only cronológico; prefijo `## [YYYY-MM-DD] <tipo> | <título>`
  (parseable con `grep "^## \[" log.md`).

## Referencia técnica

- Repo (privado): https://github.com/feba33/MVAS
- Clone local: `/opt/data/MVAS`
- `gh` como `feba33`. Al usar gh en terminal:
  `export PATH=/opt/data/bin:$PATH HOME=/opt/data GH_CONFIG_DIR=/opt/data/.config/gh`
- Patrón base: `raw/llm-wiki.md` (fuente inmutable del método).
