# MVAS — Working Log del Bucle de Enriquecimiento (investigación web)

> **ARCHIVO DE REANUDACIÓN.** Cualquier LLM puede leer este archivo y continuar el
> bucle sin contexto previo. Contiene el **prompt maestro**, el **plan**, la **cola
> de temas** y el **estado**.

## GESTIÓN DEL BUCLE
- **Cronjob de investigación `e273fdbbba14`:** el usuario lo **PAUSÓ** expresamente para
  que Hermes corriera el bucle **en esta conversación, en continuo, hasta `/stop`**.
  El bucle de esta corrida **ya completó** todos los temas de la cola. El cronjob
  sigue pausado; no reanudar salvo petición del usuario.
- **Reanudar (si el usuario lo pide):** `cronjob action=resume job_id=e273fdbbba14`.
- **CLI de investigación:** `python3 scripts/web_research.py "<query>"` (DuckDuckGo;
  **devuelve "sin resultados"** — bloqueado). **Fallback usado:** `curl -sG
  "https://en.wikipedia.org/w/api.php" ... -o /tmp/x.json` + `read_file`.
- **Health-check:** `python3 scripts/lint.py`.

## PROMPT MAESTRO
Enriquecer MVAS con conocimiento real extraído de la web (hasta `/stop`).
- **Sustrato:** legalidad, normas, marcos, derecho corporativo (México, EE.UU., Canadá, Brasil).
- **Dominio:** libros/académico, estrategias, herramientas, conocimiento.
- **Rol:** roles del sector tecnología en todos los departamentos; que un LLM pueda **operar efectivamente**.

### Reglas de ingest
- `protocolo-discriminamiento.md`: infiere entidad destino sin que el usuario la diga.
- **Raw = cita:** NO guardes documento en `raw/`; cita **URL en `fuente`** (reference-only).
- Página en `<capa>/<entidad>/<slug>.md` con YAML frontmatter; resume 3-6 bullets.
- Si el nodo no existe, **créalo con su superstructura** (`raw/`, `index.md`, `log.md`, `README`).
- **DEDUPE**; aplica **filtro de relevancia**. Sigue `GUIA-HERMES.md` y el skill.

## ESTADO
- **Iteración actual:** 34 (corrida continua completa)
- **Última ejecución:** 2026-07-09
- **Temas completados:** 34 / ~41 (todos los temas de la cola ingestados)
- **Cronjob investigación:** `e273fdbbba14` (PAUSADO; bucle corrió aquí y terminó la cola)

## COLA DE TEMAS ([x] done)
### Sustrato
- [x] LGSM → `sustrato/mexico/lgsm.md`
- [x] Código de Comercio → `sustrato/mexico/codigo-de-comercio.md`
- [x] Régimen fiscal (ISR/IVA/RESICO) → `sustrato/mexico/regimen-fiscal.md`
- [x] LFPDPPP 2025 → `sustrato/mexico/lfpdpdp.md`
- [x] Regulación IA → `sustrato/mexico/regulacion-ia.md`
- [x] COFECE → `sustrato/mexico/cofece.md`
- [x] Delaware GCL → `sustrato/estados-unidos/delaware-gcl.md`
- [x] LLC → `sustrato/estados-unidos/llc.md`
- [x] IRS → `sustrato/estados-unidos/irs.md`
- [x] At-will → `sustrato/estados-unidos/empleo-at-will.md`
- [x] Copyright / Patente → `sustrato/estados-unidos/copyright.md`, `patente.md`
- [x] Fintech → `sustrato/estados-unidos/fintech-regulacion.md`
- [x] Canadá (CBCA) → `sustrato/canada/corporativo.md`
- [x] Brasil (Lei das S.A.) → `sustrato/brasil/corporativo.md`
### Dominio
- [x] Finanzas — valoración → `dominio/finanzas/valoracion.md`
- [x] Finanzas — instrumentos → `dominio/finanzas/instrumentos-financieros.md`
- [x] Finanzas — libros clave → `dominio/finanzas/libros-clave.md`
- [x] Computación — paradigmas → `dominio/computacion/paradigmas.md`
- [x] Computación — arquitectura → `dominio/computacion/arquitectura.md`
- [x] Computación — DevOps → `dominio/computacion/devops.md`
- [x] Marketing — mix 4Ps → `dominio/marketing/marketing-mix.md`
- [x] Marketing — libros clave → `dominio/marketing/libros-clave.md`
- [x] Leyes — ramas → `dominio/leyes/ramas-derecho.md`
- [x] Contabilidad — NIIF/GAAP → `dominio/contabilidad/niif-us-gaap.md`
- [x] Diseño — Design Thinking → `dominio/diseno/design-thinking.md`
### Rol
- [x] growth lead → `rol/growth-lead/growth-lead.md`
- [x] product lead / PM → `rol/product-lead/product-lead.md`
- [x] engineering manager → `rol/engineering-manager/engineering-manager.md`
- [x] data lead → `rol/data-lead/data-lead.md`
- [x] UX/UI lead → `rol/ux-ui-lead/ux-ui-lead.md`
- [x] marketing lead → `rol/marketing-lead/marketing-lead.md`
- [x] finance lead / controller → `rol/finance-lead/finance-lead.md`
- [x] operations lead → `rol/operations-lead/operations-lead.md`
- [x] agile coach / scrum master → `rol/agile-coach/agile-coach.md`

## LOG DE ITERACIONES
### [2026-07-09] iter 1-23 | Sustrato + Dominio (corrida continua en conversación)
- Mexico (lgsm, codigo, lfpdpdp, regulacion-ia, regimen-fiscal, cofece), EE.UU.
  (delaware-gcl, llc, irs, at-will, copyright, patente, fintech), Canada (CBCA),
  Brasil (Lei das S.A.); Dominio (valoracion, instrumentos, libros finanzas,
  paradigmas, arquitectura, devops, marketing-mix, libros marketing, ramas-derecho,
  niif-us-gaap, design-thinking).
- Fuentes: `web_research.py` (ES, parcial) + `curl` Wikipedia API (en/pt/es) → /tmp JSON → read_file.
- **Raw = cita/URL** aplicado en todos.

### [2026-07-09] iter 24-25 | Nodos sustrato/canada y sustrato/brasil + index.md raíz rehecho

### [2026-07-09] iter 26-34 | 9 nodos de rol (growth-lead, product-lead, engineering-manager,
data-lead, ux-ui-lead, marketing-lead, finance-lead, operations-lead, agile-coach)
- Creados vía subagentes (delegate_task) con superstructura completa + página de conocimiento.

### [2026-07-09] ESTADO FINAL
- **Cola vacía:** todos los temas ingestados. Wiki en estado usable.
- Cronjob `e273fdbbba14` permanece PAUSADO (el usuario lo pausó para correr aquí).
- Para extender MVAS: añadir temas a la cola de este archivo y reanudar el bucle, o
  reanudar el cronjob.
