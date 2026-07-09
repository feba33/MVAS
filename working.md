# MVAS — Working Log del Bucle de Enriquecimiento (investigación web)

> **ARCHIVO DE REANUDACIÓN.** Cualquier LLM puede leer este archivo y continuar el
> bucle sin contexto previo. Contiene el **prompt maestro**, el **plan**, la **cola
> de temas** y el **estado**. Para reanudar: lee TODO este archivo, busca el primer
> tema `pending` (`[ ]`) en la cola, ejecuta **UNA iteración** (investigar → ingerir →
> actualizar este archivo → commit), y deja el archivo actualizado para la siguiente.

## GESTIÓN DEL BUCLE
- **Cronjob de investigación `e273fdbbba14`:** el usuario lo **PAUSÓ** expresamente para
  que Hermes corra el bucle **en esta conversación, en continuo, hasta `/stop`**. No
  reanudar ese cronjob mientras el usuario no lo pida.
- **Reanudar (solo si el usuario lo pide):** `cronjob action=resume job_id=e273fdbbba14`.
- **Pausar / detener (cuando el usuario digite `/stop`):** `cronjob action=pause job_id=e273fdbbba14`
  (o `remove`). El cron de El Financiero (`d472fa235ca3`) es **independiente**.
- **CLI de investigación:** `python3 scripts/web_research.py "<query>"` (DuckDuckGo;
  **devuelve "sin resultados"** — bloqueado). **Fallback:** `curl -sG
  "https://en.wikipedia.org/w/api.php" --data-urlencode ... -o /tmp/x.json` + `read_file`.
- **Health-check:** `python3 scripts/lint.py`.

## PROMPT MAESTRO
Enriquecer MVAS con conocimiento real extraído de la web, **hasta `/stop`**.
- **Sustrato:** legalidad, normas, marcos, derecho corporativo (México, EE.UU., Canadá, Brasil, hemisferio).
- **Dominio:** libros/académico, estrategias, herramientas, conocimiento.
- **Rol:** roles del sector tecnología en todos los departamentos; scraping de job descriptions + Reddit; que un LLM pueda **operar efectivamente**.

### Reglas de ingest
- `protocolo-discriminamiento.md`: infiere entidad destino sin que el usuario la diga.
- **Raw = cita:** NO guardes documento en `raw/`; cita **URL en `fuente`** (reference-only).
- Página en `<capa>/<entidad>/<slug>.md` con YAML frontmatter; resume 3-6 bullets.
- Actualiza `index.md`/`log.md` del nodo (+ raíz si nodo nuevo). Si el nodo no existe,
  **créalo con su superstructura** (`raw/`, `index.md`, `log.md`, `README`) y añade al `index.md` raíz.
- **DEDUPE**; aplica **filtro de relevancia**. Sigue `GUIA-HERMES.md` y el skill.

### Pasos de UNA iteración
1. Entorno: `export PATH=/opt/data/bin:$PATH HOME=/opt/data GH_CONFIG_DIR=/opt/data/.config/gh`;
   config git; `cd /opt/data/MVAS` (o clona); `git pull --ff-only`.
2. Lee este `working.md`; elige el **primer tema `[ ]`** de la cola.
3. Investiga (curl Wikipedia API, browser). 4. Escribe página(s). 5. Actualiza índices/logs + este archivo.
6. `git add -A && git commit -m "mv: ingest <tema> en <entidad>" && git push`.
7. Siguiente tema sin parar hasta `/stop`.

## ESTADO
- **Iteración actual:** 25
- **Última ejecución:** 2026-07-09 (corrida continua en conversación, sin cron)
- **Temas completados:** 24 / 41 (restan: libros marketing, 9 roles)
- **Cronjob investigación:** `e273fdbbba14` (PAUSADO; bucle corre aquí)

## COLA DE TEMAS ([ ] pending / [x] done)
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
- [x] Leyes — ramas → `dominio/leyes/ramas-derecho.md`
- [x] Contabilidad — NIIF/GAAP → `dominio/contabilidad/niif-us-gaap.md`
- [x] Diseño — Design Thinking → `dominio/diseno/design-thinking.md`
- [ ] Marketing — libros clave (Traction, Hooked)
### Rol
- [ ] growth lead
- [ ] product lead / product manager
- [ ] engineering manager
- [ ] data lead / data scientist
- [ ] UX/UI lead
- [ ] marketing lead
- [ ] finance lead / controller
- [ ] operations lead
- [ ] agile coach / scrum master

## LOG DE ITERACIONES
### [2026-07-09] previas | lgsm, codigo, lfpdpdp, regulacion-ia, valoracion (loop)
### [2026-07-09] iter 5 | Optimización raw=cita + working.md
### [2026-07-09] iter 6-9 | Sustrato MX (regimen-fiscal, cofece) + EE.UU. (delaware-gcl, llc)
### [2026-07-09] iter 10-13 | Dominio (instrumentos, paradigmas, marketing-mix, niif-us-gaap)
### [2026-07-09] iter 14-18 | Dominio (libros finanzas, arquitectura, devops, ramas-derecho, design-thinking)
### [2026-07-09] iter 19-23 | Sustrato EE.UU. (irs, at-will, copyright, patente, fintech)
### [2026-07-09] iter 24-25 | Nodos sustrato/canada (CBCA) y sustrato/brasil (Lei das S.A.) + index.md raíz rehecho
