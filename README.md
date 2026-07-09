# MVAS

**Super wiki en capas de conocimiento**, de lo más general a lo más específico y
granular, mantenido con el patrón [LLM Wiki](raw/llm-wiki.md): Hermes construye
y mantiene un wiki persistente de markdown interconectado, en vez de solo recuperar
de documentos crudos en cada consulta.

El usuario aporta fuentes y preguntas; Hermes cuida, mantiene, optimiza y da retrieval.

## Arquitectura

**Capas del patrón LLM Wiki**
- `raw/` — fuentes crudas **inmutables** (el usuario escribe, Hermes solo lee).
- `sustrato/` `dominio/` `organización/` `rol/` — **el wiki** (Hermes lo escribe).
- `GUIA-HERMES.md` + `esquema.md` — **el esquema** (configuración del método).

**Capas de contenido (general → específico)**
| Capa | Carpeta | Contenido |
|------|---------|-----------|
| Sustrato | `sustrato/` | Países: legislación, cultura, normas, noticias, mercados. |
| Dominio | `dominio/` | Referencia por dominio: finanzas, computación, marketing, leyes, contabilidad, diseño. |
| Organización | `organización/` | Empresas: operaciones, decisiones, responsabilidades, artefactos. |
| Rol | `rol/` | Responsabilidades y sets de capacidades: ing. software, ing. UI/UX, road lead. |

**⚠️ Recursivo:** cada entidad (p.ej. `dominio/finanzas/`) es a su vez un wiki
auto-contenido con su propia `raw/`, `index.md` y `log.md`. La info de cada
entidad vive **solo en su carpeta**. Ver `esquema.md` (plantilla de nodo).

**🔎 Capa de discernimiento:** antes de escribir, Hermes **infiere a qué entidad
va cada input** (sin que tú lo especifiques); solo pregunta si hay baja certeza.
Ver `protocolo-discriminamiento.md`.

**Navegación**
- `index.md` — catálogo de nodos (lo lee Hermes primero al responder).
- `log.md` — registro cronológico de actividad.

## Operaciones
- **Ingest**: depositas una fuente en el `raw/` correspondiente → Hermes la lee,
  **infiere la entidad** (discernimiento), la discute, ubica/crea el nodo,
  escribe/actualiza páginas DENTRO del nodo, enlaza, actualiza `index.md`/`log.md`
  del nodo, y hace push.
- **Query**: preguntas → Hermes busca en `index.md`, taladra nodos y páginas,
  sintetiza con citas; las respuestas valiosas se archivan como páginas.
- **Lint**: Hermes hace health-check (contradicciones, huérfanas, gaps, integridad
  recursiva) y optimiza.

## Para Hermes
Ver `GUIA-HERMES.md` (esquema completo y procesos de ingest/query/lint) y
`protocolo-discriminamiento.md` (capa de inferencia de entidad).
