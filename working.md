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
- **Reanudar (solo si el usuario lo pida):** `cronjob action=resume job_id=e273fdbbba14`.
- **Pausar / detener (cuando el usuario digite `/stop`):** `cronjob action=pause job_id=e273fdbbba14`
  (o `remove`). El cron de El Financiero (`d472fa235ca3`) es **independiente**; pausar/remover
  también ese si se quiere parar todo.
- **CLI de investigación:** `python3 scripts/web_research.py "<query>"` (DuckDuckGo + extracción;
  **actualmente devuelve "sin resultados"** — DuckDuckGo lo bloquea). **Fallback fiable:**
  `curl -sG "https://en.wikipedia.org/w/api.php" --data-urlencode ... -o /tmp/x.json` y luego
  `read_file` del JSON (evita el gate curl|python3).
- **Health-check:** `python3 scripts/lint.py`.

## PROMPT MAESTRO (qué hacer)
Enriquecer MVAS con conocimiento real extraído de la web, **hasta que el usuario
digite `/stop`**. Cubrir tres capas siguiendo estas guías:

### Guías por capa
- **Sustrato:** legalidad, normas, marcos legales, derecho corporativo, noticias.
- **Dominio:** libros y material académico, estrategias, herramientas, conocimiento.
- **Rol:** roles y capacidades comunes en el **sector tecnología**, en todos los
  departamentos. Web scraping de descripciones de trabajo + Reddit + generalización.
  IE: *growth lead, product lead*. Que un LLM pueda entrar y **operar efectivamente**.

### Reglas de ingest (MVAS)
- `protocolo-discriminamiento.md`: infiere la entidad destino SIN que el usuario la diga.
- **Raw = cita:** NO guardes documento en `raw/`; cita la **URL en `fuente`** (reference-only).
- Crea página en `<capa>/<entidad>/<slug>.md` con YAML frontmatter; resume 3-6 bullets.
- Actualiza `index.md`/`log.md` del nodo (+ raíz si es nodo nuevo). Si el nodo no existe,
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
- **Iteración actual:** 23 (18 dominio/sustrato previos + 5 sustrato EE.UU. esta corrida)
- **Última ejecución:** 2026-07-09 (corrida continua en conversación, sin cron)
- **Temas completados:** 22 / 41 (restan: Canadá/Brasil, libros marketing, 9 roles)
- **Cronjob investigación:** `e273fdbbba14` (PAUSADO por el usuario; bucle corre aquí)

## COLA DE TEMAS ([ ] pending / [x] done)
### Sustrato
- [x] Marco societario México — LGSM → `sustrato/mexico/lgsm.md`
- [x] Código de Comercio México → `sustrato/mexico/codigo-de-comercio.md`
- [x] Régimen fiscal México — ISR, IVA, RESICO → `sustrato/mexico/regimen-fiscal.md`
- [x] Protección de datos México — LFPDPPP 2025 → `sustrato/mexico/lfpdpdp.md`
- [x] Regulación de IA México → `sustrato/mexico/regulacion-ia.md`
- [x] Competencia económica México — COFECE → `sustrato/mexico/cofece.md`
- [x] Delaware General Corporation Law → `sustrato/estados-unidos/delaware-gcl.md`
- [x] LLC / estructuras EE.UU. → `sustrato/estados-unidos/llc.md`
- [x] Impuestos federales EE.UU. — IRS → `sustrato/estados-unidos/irs.md`
- [x] Employment law EE.UU. — at-will → `sustrato/estados-unidos/empleo-at-will.md`
- [x] IP / Copyright / Patent EE.UU. → `sustrato/estados-unidos/copyright.md`, `patente.md`
- [x] Noticias recientes regulación fintech → `sustrato/estados-unidos/fintech-regulacion.md`
- [ ] Derecho corporativo Canadá / Brasil (hemisferio) — crear nodos `sustrato/canada`, `sustrato/brasil`
### Dominio
- [x] Finanzas — valoración → `dominio/finanzas/valoracion.md`
- [x] Finanzas — instrumentos financieros → `dominio/finanzas/instrumentos-financieros.md`
- [x] Finanzas — libros clave → `dominio/finanzas/libros-clave.md`
- [x] Computación — paradigmas → `dominio/computacion/paradigmas.md`
- [x] Computación — arquitectura → `dominio/computacion/arquitectura.md`
- [x] Computación — DevOps → `dominio/computacion/devops.md`
- [x] Marketing — 4Ps, growth hacking, SEO/SEM → `dominio/marketing/marketing-mix.md`
- [x] Leyes — ramas del derecho → `dominio/leyes/ramas-derecho.md`
- [x] Contabilidad — NIIF / US GAAP → `dominio/contabilidad/niif-us-gaap.md`
- [x] Diseño — Design Thinking / UX research → `dominio/diseno/design-thinking.md`
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
### [2026-07-09] sesión previa (loop) | estado al reanudar
- Ingestados previos: sustrato/mexico (lgsm, codigo, lfpdpdp, regulacion-ia); dominio/finanzas (valoracion).
- `raw = cita/URL` ya aplicado.

### [2026-07-09] iter 5 | Optimización raw=cita + working.md
### [2026-07-09] iter 6-9 | Sustrato (regimen-fiscal, cofece, delaware-gcl, llc)
### [2026-07-09] iter 10-13 | Dominio (instrumentos, paradigmas, marketing-mix, niif-us-gaap)
### [2026-07-09] iter 14-18 | Dominio (libros finanzas, arquitectura, devops, ramas-derecho, design-thinking)
### [2026-07-09] iter 19-23 | Sustrato EE.UU. (irs, empleo-at-will, copyright, patente, fintech-regulacion)
- Todas vía `curl` a Wikipedia API (en) → /tmp JSON → read_file.
- **Pendiente sustrato:** crear nodos `canada` y `brasil` (derecho corporativo hemisferio).
