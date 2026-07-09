# MVAS

**Super wiki en capas de conocimiento**, de lo más general a lo más específico y
granular, mantenido con el patrón [LLM Wiki](raw/llm-wiki.md): Hermes construye
y mantiene un wiki persistente de markdown interconectado, en vez de solo recuperar
de documentos crudos en cada consulta.

El usuario aporta fuentes y preguntas; Hermes cuida, mantiene, optimiza y da retrieval.

## Arquitectura (3 capas del patrón + 4 capas de contenido)

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

**Navegación**
- `index.md` — catálogo de páginas (lo lee Hermes primero al responder).
- `log.md` — registro cronológico de actividad.

## Operaciones
- **Ingest**: el usuario deposita una fuente en `raw/` → Hermes la lee, la discute,
  clasifica, escribe/actualiza páginas en la capa correcta, enlaza, actualiza
  `index.md` y `log.md`, y hace push.
- **Query**: el usuario pregunta → Hermes busca en `index.md`, taladra páginas,
  sintetiza con citas; las respuestas valiosas se archivan como páginas nuevas.
- **Lint**: Hermes hace health-check (contradicciones, huérfanas, gaps) y optimiza.

## Para Hermes
Ver `GUIA-HERMES.md` (esquema completo y procesos de ingest/query/lint).
