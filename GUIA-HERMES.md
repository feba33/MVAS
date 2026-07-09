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
   markdown generados por Hermes. Hermes es dueño de esta capa.
3. **The schema → `GUIA-HERMES.md` + `esquema.md`** — este documento + la
   taxonomía. Dicen a Hermes cómo está estructurado el wiki y los workflows.

## Las 4 capas de contenido (general → específico)

| Capa | Carpeta | Contenido |
|------|---------|-----------|
| Sustrato | `sustrato/` | Fundamento por **país**: legislación, cultura, reglas, normatividad, noticias, mercados. |
| Dominio | `dominio/` | Referencia y conocimiento puntual por **dominio**: finanzas, computación, marketing, leyes, contabilidad, diseño. |
| Organización | `organización/` | Lo específico de **empresas**: operaciones, decisiones, responsabilidades, artefactos. |
| Rol | `rol/` | **Responsabilidades** y sets de capacidades por rol: ingeniero de software, ingeniero UI/UX, road lead. |

## ⚠️ ARQUITECTURA RECURSIVA (fractal) — CLAVE

La arquitectura LLM Wiki **se aplica a CADA instancia** del repo, no solo al raíz.
**Cada entidad es, en sí misma, un wiki auto-contenido** con su propia
superstructura anidada:

- `raw/` — fuentes crudas de **ESTA** entidad (inmutables).
- `index.md` — catálogo de páginas de **ESTA** entidad.
- `log.md` — registro cronológico de **ESTA** entidad.
- páginas `*.md` — contenido, con YAML frontmatter.
- cross-references a otras entidades (rutas relativas).

**Principio de aislamiento:** la información relevante a una entidad vive
**solo dentro de su carpeta**. Ej.: TODO lo de `finanzas` está en
`dominio/finanzas/`, nunca esparcido. El raíz es el nodo wiki superior;
`sustrato/ dominio/ organización/ rol/` son nodos; y `dominio/finanzas/`
es un nodo hijo — y así recursivamente (`dominio/finanzas/derivados/`
podría ser un nodo más). Ver plantilla en `esquema.md`.

## Convenciones de página (wiki)

- Cada página es markdown con **YAML frontmatter**:
  ```yaml
  ---
  titulo: Nombre de la página
  capa: dominio          # sustrato | dominio | organización | rol
  tema: finanzas         # entidad/subcarpeta a la que pertenece
  fuente: raw/articulo-x.md   # puede ser raw/ de la entidad
  fecha: 2026-07-09
  confianza: alta        # alta | media | baja
  tags: [finanzas, inflación]
  ---
  ```
- Usar **cross-references**: enlazar páginas relacionadas con `[texto](ruta-relativa)`.
- Escribir en español; términos técnicos en inglés cuando aplique.
- Mantener páginas atómicas y reutilizables (una entidad/concepto por página).

## PROCESO DE INGEST (insertar información) — pasos exactos

Cada vez que el usuario diga *"actualiza MVAS"* / *"ingerie esto"* / adjunte una fuente:

1. **Recibir fuente**: el usuario la deposita en el `raw/` correspondiente
   (raíz `raw/` para general, o `dominio/finanzas/raw/` para esa entidad) →
   o la adjunta en el chat → Hermes la guarda en el `raw/` adecuado con nombre
   estable. NUNCA modificar ningún `raw/`.
2. **Leer y discutir**: Hermes lee la fuente y **comenta los puntos clave con el
   usuario** (takeaways) antes de escribir.
3. **Clasificar y ubicar el NODO**: la info va en la carpeta de su entidad
   (`dominio/finanzas/`, `sustrato/mexico/`, etc.).
   - Si el nodo **no existe**, **créalo con su superstructura** (raw/, index.md,
     log.md, README) siguiendo la plantilla recursiva de `esquema.md`.
   - Si ya existe, usa su superstructura **interna**.
4. **Escribir DENTRO del nodo**: páginas en la carpeta del nodo; fuentes en su
   `raw/`; actualizar su `index.md` y `log.md` (no los del raíz, salvo que la
   entrada también merezca aparecer en el índice global del raíz).
   - Página de resumen de la fuente + páginas de entidad/concepto afectadas
     (¡una fuente puede tocar 10-15 páginas!).
   - Si la nueva info **contradice o amplía** páginas existentes, actualizarlas y
     marcar la contradicción.
5. **Cross-references**: enlazar las páginas nuevas con las existentes (dentro
   del nodo y hacia otros nodos vía rutas relativas).
6. **Actualizar índices**: `index.md` del nodo + (opcionalmente) `index.md` del
   raíz si es una entrada de navegación de alto nivel.
7. **Registrar en `log.md`** del nodo: `## [YYYY-MM-DD] ingest | Título`.
8. **Persistir** dentro de `/opt/data/MVAS`:
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
  completa (raw/, index.md, log.md) y que su info esté aislada en su carpeta.
Reportar hallazgos y aplicar correcciones con commit+push.

## index.md y log.md (convenciones)

- `index.md`: catálogo por categoría; cada página con link + resumen + metadata.
  El raíz lista **nodos**; cada nodo lista **sus páginas**.
- `log.md`: append-only cronológico; prefijo `## [YYYY-MM-DD] <tipo> | <título>`
  (parseable con `grep "^## \[" log.md`).

## Referencia técnica

- Repo (privado): https://github.com/feba33/MVAS — clone: `/opt/data/MVAS`
- `gh` como `feba33`. Al usar gh en terminal:
  `export PATH=/opt/data/bin:$PATH HOME=/opt/data GH_CONFIG_DIR=/opt/data/.config/gh`
- Patrón base: `raw/llm-wiki.md` (fuente inmutable del método).
