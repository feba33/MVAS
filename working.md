# MVAS · Working — Investigación continua (loop autónomo)

> **Archivo de estado y reanudación.** Cualquier LLM puede leer este archivo y
> continuar el trabajo exactamente donde se quedó. **Última actualización: 2026-07-09.**

## 🎯 Prompt maestro (la tarea)
Buscar en la web contenido valioso para las tres capas de MVAS e ingerirlo en el
wiki siguiendo `protocolo-discriminamiento.md` y la regla **reference-only**
(fuentes web = solo citar la URL en el frontmatter `fuente`; NO guardar el
contenido en `raw/`).

Enfoques por capa:
- **Sustrato** (países / contexto): legalidad, normas, marcos legales, derecho
  corporativo, noticias. Foco: **México**, **EE.UU.** y otros países del
  hemisferio (o los que consideres relevantes). Ej.: LGSM, Código de Comercio,
  Delaware GCL, contratos, regulación de IA, protección de datos, noticias
  jurídicas recientes.
- **Dominio** (disciplinas): libros, material académico, estrategias,
  herramientas, insights, conocimiento valioso. Ej.: finanzas corporativas,
  contabilidad (NIF/IFRS), marketing/growth, computación, diseño, operaciones,
  estrategia.
- **Rol** (cargos): roles y capacidades comunes en tecnología, útiles en
  consultoras / startups / producto. Generalizar a partir de descripciones de
  trabajo (web scraping de job posts), Reddit, Google. Ej.: growth lead,
  product lead/manager, engineering manager, data lead, design lead, founder.
  **Objetivo:** que un LLM pueda entrar a la entidad y operar efectivamente
  (responsabilidades, skills, frameworks, KPIs, artefactos típicos).

## 🔁 Protocolo de iteración (1 iteración = 1 a 3 entradas)
1. `export PATH=/opt/data/bin:$PATH HOME=/opt/data GH_CONFIG_DIR=/opt/data/.config/gh`
   `cd /opt/data/MVAS`
   `TOKEN=$(gh auth token)`; `git remote set-url origin https://x-access-token:${TOKEN}@github.com/feba33/MVAS.git`
   `git pull --ff-only`
2. Leer este `working.md`; ubicar **Próxima tarea** / primer item sin tachar del checklist.
3. Elegir 1-3 temas (cubrir las 3 capas a lo largo del tiempo).
4. Investigar en la web:
   - `python3 scripts/web_research.py "query" 5` (terminal) → digest de resultados.
   - O `browser_navigate` a Google/Reddit para descubrir fuentes.
   - Elegir 2-4 fuentes sólidas (autoridad, actualidad).
5. Discernir entidad destino (`protocolo-discriminamiento.md`). Si no existe,
   crearla con su superstructura: `raw/` (vacío, se usa bajo demanda),
   `index.md`, `log.md`, `README.md` (wiki autocontenido de la entidad).
6. Ingestar: crear/actualizar `<capa>/<entidad>/<slug>.md` con:
   - Frontmatter YAML: `capa`, `tema`, `fuente: <url>`, `fecha`, `confianza`
     (`alta|media|baja`), `tags`.
   - Cuerpo: resumen condensado y útil (no copiar texto íntegro; sintetizar).
   - **CITAR la URL** en `fuente`. NO crear archivo en `raw/` para fuentes web.
7. Actualizar `index.md` y `log.md` de la entidad y los globales (raíz).
8. Actualizar este `working.md` (checklist tachado, índice de progreso,
   log de iteración, **Próxima tarea** clara).
9. `git add -A && git commit -m "MVAS: ingest <tema>" && git push`.
10. Si error crítico: escribirlo en **Bloqueos**, dejar **Estado actual**
    claro y terminar la iteración. La siguiente retoma. **Nunca borrar el
    progreso ni este archivo.**

## 📌 Reglas
- Solo citar URL (reference-only) para web. `raw/` queda para docs que el
  usuario deposita localmente.
- No usar `clarify`. Si baja certeza → inferir y marcar `confianza: media/baja`.
- Commits pequeños y frecuentes. `working.md` SIEMPRE actualizado y commiteado.
- Respetar límites del modelo: máximo ~3 entradas por iteración.

## 🗺️ Plan de cobertura (checklist)
### Sustrato
- [x] México: Ley General de Sociedades Mercantiles (LGSM) — tipos de sociedad
- [x] México: Código de Comercio — contratos mercantiles
- [x] México: LFPDPPP (protección de datos) y regulación de IA
- [ ] México: noticias legales recientes (suprema corte, DOF)
- [ ] EE.UU.: Delaware General Corporation Law / tipos de entity
- [ ] EE.UU.: SEC, FTC, regulación de IA (federal/estatal)
- [ ] Canadá / Brasil: marcos societarios clave (según relevancia)
### Dominio
- [ ] finanzas: valoración (DCF, múltiplos), estructura de capital, WACC
- [ ] contabilidad: NIF/IFRS, consolidación, estados financieros
- [ ] marketing: growth, SEO, performance, embudo
- [ ] computación: arquitectura de software, cloud, DevOps, CI/CD
- [ ] diseño: UX, design systems, accesibilidad
- [ ] estrategia: Porter, OKR, frameworks de decisión
- [ ] operaciones: supply chain, procesos, lean
### Rol
- [ ] growth lead
- [ ] product lead / product manager
- [ ] engineering manager
- [ ] data lead / analytics lead
- [ ] design lead / UX lead
- [ ] founder / CEO (startup)
- [ ] consultant (consultora)

## 📊 Índice de progreso
| Entidad | Capa | Entradas | Última |
|---------|------|----------|--------|
| sustrato/mexico (LGSM, CCom, LFPDPPP, IA) | sustrato | 4 | 2026-07-09 |
| dominio/finanzas (T-MEC, vivienda, valoración) | dominio | 4 | 2026-07-09 |

## 🧾 Log de iteraciones
### 2026-07-09 — iter 0 (setup)
- Creado `scripts/web_research.py` (CLI de investigación, stdlib).
- Creado `working.md` (este archivo) con prompt maestro, protocolo y checklist.
- Loop arrancado vía cronjob recurrente (lee este archivo y continúa).

### 2026-07-09 — iter 1 (sustrato/mexico)
- 2 entradas en `sustrato/mexico/`:
  - `lgsm.md` — Ley General de Sociedades Mercantiles: 7 tipos de sociedad, reforma DOF 20-10-2023, SAS (art. 260, montos DOF 26-12-2025).
  - `codigo-de-comercio.md` — Código de Comercio: actos de comercio, contratos mercantiles, títulos de crédito, quiebras; reforma DOF 14-11-2025.
- Fuentes: Cámara de Diputados (oficial, ambas) + CICDE y Gobierno.com.mx (digest). Reference-only.
- Índices/logs de entidad y globales actualizados; checklist tachado (2 items).
- Próxima tarea: `sustrato/mexico` → LFPDPPP y regulación de IA.

### 2026-07-09 — iter 2 (sustrato/mexico + dominio/finanzas)
- 3 entradas en total (cubiertas 2 de 3 capas; rol pendiente):
  - `sustrato/mexico/lfpdpdp.md` — LFPDPPP 2025: nueva ley publicada DOF 20-03-2025, vigencia 21-03-2025, abroga la de 2010; INAI disuelto → Secretaría Anticorrupción y Buen Gobierno; refuerza derechos ARCO+ y eleva obligaciones. Confianza alta.
  - `sustrato/mexico/regulacion-ia.md` — Regulación de IA en México: iniciativas 2023-2025 (cuadro CeCo), enfoque por riesgo (estilo UE), propuesta de marco de 3 niveles del Senado (03-10-2025). Confianza media (sin ley vigente).
  - `dominio/finanzas/valoracion.md` — Valoración de empresas: 3 enfoques (DCF, comps, activos), EV vs Equity, WACC, múltiplos EV/EBITDA-SDE-revenue y rangos por sector.
- Fuentes: Hogan Lovells + Cámara de Diputados (LFPDPPP); CeCo + Mobile Time (IA); Finance Interview Prep + CT Acquisitions (valoración). Reference-only (URL en frontmatter; sin archivos en raw/).
- Índices/logs de entidad y globales actualizados; checklist tachado (1 item), índice de progreso ampliado.
- Próxima tarea: siguiente item sin tachar → `Sustrato › México › noticias legales recientes (suprema corte, DOF)`. Sugerido tras ello iniciar capa `rol` (p.ej. growth lead) para cubrir las 3 capas.

## ▶️ Estado actual / Próxima tarea
- **Próxima tarea:** siguiente item sin tachar del checklist →
  **Sustrato › México › noticias legales recientes (suprema corte, DOF)**.
  (Luego iniciar capa `rol` — p.ej. growth lead / product manager — para cubrir las 3 capas.)
- Notas: el cronjob itera cada 2h; cada corrida hace 1-3 entradas y actualiza
  este archivo. Para detener: decir `/stop` o eliminar el cronjob.

## 🚧 Bloqueos
- (ninguno)
