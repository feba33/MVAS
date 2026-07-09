# MVAS — Working Log del Bucle de Enriquecimiento (investigación web)

> **ARCHIVO DE REANUDACIÓN.** Cualquier LLM puede leer este archivo y continuar el
> bucle sin contexto previo. Contiene el **prompt maestro**, el **plan**, la **cola
> de temas** y el **estado**.

## PROCEDIMIENTO DE REABASTECIMIENTO (gap analysis → plan → loop)
Cuando esta cola se vacía, **no parar**: correr `python3 scripts/gap_analysis.py`,
volcar los huecos en temas `pending` aquí, actualizar estado + LOG, commit, y seguir.
Ver sección "REABASTECIMIENTO AUTOMÁTICO" en `GUIA-HERMES.md`.

## GESTIÓN DEL BUCLE
- **Sin cron jobs.** El usuario pidió correr el bucle **en esta conversación**, en
  continuo, usando subagentes (`delegate_task`) para paralelizar. Mínimo 3 bucles más.
- Cronjob de investigación `e273fdbbba14`: **PAUSADO** (lo pausó el usuario). No reanudar.
- Cron de El Financiero `d472fa235ca3`: **PAUSADO**.
- **CLI fallback de investigación:** `curl -sG "https://en.wikipedia.org/w/api.php"
  --data-urlencode "action=query" --data-urlencode "prop=extracts" --data-urlencode
  "exintro" --data-urlencode "explaintext" --data-urlencode "format=json"
  --data-urlencode "titles=<Título>" -o /tmp/x.json` + `read_file`.
  (`web_search` y `web_research.py` no disponibles / bloqueados.)
- **Health-check:** `python3 scripts/lint.py`. **Gap analysis:** `python3 scripts/gap_analysis.py`.

## PROMPT MAESTRO
Enriquecer MVAS con conocimiento real (hasta `/stop`). Sustrato (países/legal),
Dominio (disciplinas), Rol (tech), Organización (empresas). **Raw = cita.**
Si el nodo no existe, créalo con su superstructura (`raw/`, `index.md`, `log.md`, README).

### Pasos de UNA iteración
1. `export PATH=/opt/data/bin:$PATH HOME=/opt/data GH_CONFIG_DIR=/opt/data/.config/gh`; `cd /opt/data/MVAS`; `git pull --ff-only`.
2. Lee este archivo; elige el **primer tema `[ ]`**.
3. Investiga (curl Wikipedia). 4. Escribe página(s). 5. Actualiza índices/logs del nodo + este archivo.
6. `git add -A && git commit -m "mv: ingest <tema> en <entidad>" && git push`.
7. Siguiente tema sin parar. Al vaciarse la cola → gap_analysis → nuevo plan.

## ESTADO
- **Plan generado por:** `scripts/gap_analysis.py` (36 huecos + 5 nodos nuevos = 41 temas)
- **Iteración base:** 34 (corrida anterior completa) · **esta fase inicia en iter 35**
- **Temas completados (fase previa):** 34 · **pendientes en este plan:** 41
- **Cronjob investigación:** `e273fdbbba14` (PAUSADO; bucle corre aquí)

## COLA DE TEMAS ([ ] pending / [x] done) — Plan gap-analysis
### Sustrato
- [ ] sustrato/mexico — LFT (laboral, outsourcing, reparto utilidades)
- [ ] sustrato/mexico — PROFECO / CONDUSEF (protección al consumidor)
- [ ] sustrato/mexico — PLD / UIF (prevención de lavado, AML)
- [ ] sustrato/estados-unidos — SEC y regulación de valores
- [ ] sustrato/estados-unidos — Antitrust (Sherman / Clayton)
- [ ] sustrato/estados-unidos — Bankruptcy / derecho concursal
- [ ] sustrato/canada — Privacidad (PIPEDA)
- [ ] sustrato/canada — Impuestos federales (CRA)
- [ ] sustrato/brasil — LGPD (protección de datos)
- [ ] sustrato/brasil — Impuestos (Receita Federal)
### Dominio (nodos existentes — ampliar)
- [ ] dominio/finanzas — Private Equity / Venture Capital / fundraising
- [ ] dominio/finanzas — Criptoactivos / activos digitales
- [ ] dominio/finanzas — Finanzas conductuales
- [ ] dominio/computacion — Ciberseguridad
- [ ] dominio/computacion — Ingeniería de datos (data engineering)
- [ ] dominio/computacion — ML / AI engineering
- [ ] dominio/computacion — Testing / QA
- [ ] dominio/marketing — Content marketing
- [ ] dominio/marketing — Conversion Rate Optimization (CRO)
- [ ] dominio/marketing — Branding / marca
- [ ] dominio/leyes — Derecho de contratos
- [ ] dominio/leyes — Propiedad intelectual (profundización)
- [ ] dominio/contabilidad — Contabilidad de costos
- [ ] dominio/contabilidad — Auditoría
- [ ] dominio/contabilidad — Contabilidad fiscal
- [ ] dominio/diseno — UX research (métodos)
- [ ] dominio/diseno — Accesibilidad (WCAG)
- [ ] dominio/diseno — Service design
### Dominio (nuevos nodos)
- [ ] dominio/ventas — metodología, funnel, CRM (nuevo nodo)
- [ ] dominio/producto — discovery, métricas AARRR, PMF (nuevo nodo)
- [ ] dominio/recursos-humanos — People / HR (nuevo nodo)
- [ ] dominio/operaciones — supply chain, lean (nuevo nodo)
### Rol (nuevos nodos)
- [ ] rol/sales-lead
- [ ] rol/customer-success-lead
- [ ] rol/people-lead
- [ ] rol/legal-counsel
- [ ] rol/founder-ceo
- [ ] rol/cto
- [ ] rol/data-engineer
- [ ] rol/qa-engineer
### Organización (nuevo nodo)
- [ ] organización/ejemplo-empresa — empresa ejemplo (nuevo nodo)

## LOG DE ITERACIONES
### [2026-07-09] fase previa | iter 1-34 completas (Sustrato + Dominio + 9 roles)
- 34 temas ingestados; wiki usable; lint OK. Ver commits anteriores.

### [2026-07-09] setup | Procedimiento de reabastecimiento + gap_analysis
- Creado `scripts/gap_analysis.py` (taxonomía vs páginas existentes → huecos).
- Documentado el procedimiento en `GUIA-HERMES.md` (sección REABASTECIMIENTO AUTOMÁTICO).
- `gap_analysis.py` reportó 36 huecos + 5 nodos nuevos → este plan de 41 temas.
- Working.md reescrito con el nuevo plan.

### [2026-07-09] LOOP 1 (Sustrato) | iter 35+
### [2026-07-09] LOOP 2 (Dominio existentes) | iter …
### [2026-07-09] LOOP 3 (Nuevos nodos + roles) | iter …
