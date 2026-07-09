# MVAS — Working Log del Bucle de Enriquecimiento (investigación web)

> **ARCHIVO DE REANUDACIÓN.** Cualquier LLM puede leer este archivo y continuar el
> bucle sin contexto previo. Contiene el **prompt maestro**, el **plan**, la **cola
> de temas** y el **estado**.

## PROCEDIMIENTO DE REABASTECIMIENTO (gap analysis → plan → loop)
Cuando esta cola se vacía, **no parar**: correr `python3 scripts/gap_analysis.py`,
volcar los huecos en temas `pending` aquí, actualizar estado + LOG, commit, y seguir.
Ver sección "REABASTECIMIENTO AUTOMÁTICO" en `GUIA-HERMES.md`.

## GESTIÓN DEL BUCLE
- **Sin cron jobs.** Bucle en esta conversación, en continuo, con subagentes.
- Cronjob investigación `e273fdbbba14`: **PAUSADO**. Cron El Financiero `d472fa235ca3`: **PAUSADO**.
- **Fallback investigación:** `curl` Wikipedia API (es/en/pt) → /tmp JSON → read_file.
- **Health-check:** `python3 scripts/lint.py`. **Gap analysis:** `python3 scripts/gap_analysis.py`.

## PROMPT MAESTRO
Enriquecer MVAS con conocimiento real (hasta `/stop`). Sustrato, Dominio, Rol, Organización.
**Raw = cita** (URL en `fuente`, sin `raw/`). Si el nodo no existe, créalo con superstructura.

## ESTADO
- **Plan:** generado por `scripts/gap_analysis.py` (36 huecos + 5 nodos nuevos = 41 temas)
- **Iteración actual:** 75 (loop 1 = 35-44; loop 2 = 45-54; loop 3 = 55-75)
- **Temas completados:** 75 / 75 (34 previos + 41 de este plan — PLAN COMPLETO)
- **Cronjob investigación:** `e273fdbbba14` (PAUSADO; bucle corrió aquí)
- **Siguiente paso (procedimiento):** al vaciarse la cola, correr `gap_analysis.py`
  de nuevo para detectar nuevos huecos (p. ej. nuevos países, noticias recientes,
  más dominios) y generar un nuevo plan. El procedimiento está documentado y listo.

## COLA DE TEMAS ([x] done / [ ] pending)
### Sustrato
- [x] sustrato/mexico — LFT
- [x] sustrato/mexico — PROFECO / CONDUSEF
- [x] sustrato/mexico — PLD / UIF
- [x] sustrato/estados-unidos — SEC y regulación de valores
- [x] sustrato/estados-unidos — Antitrust
- [x] sustrato/estados-unidos — Bankruptcy
- [x] sustrato/canada — Privacidad (PIPEDA)
- [x] sustrato/canada — Impuestos (CRA)
- [x] sustrato/brasil — LGPD
- [x] sustrato/brasil — Impuestos (Receita Federal)
### Dominio (nodos existentes — ampliar)
- [x] dominio/finanzas — Private Equity / VC
- [x] dominio/finanzas — Criptoactivos
- [x] dominio/finanzas — Finanzas conductuales
- [x] dominio/computacion — Ciberseguridad
- [x] dominio/computacion — Ingeniería de datos
- [x] dominio/computacion — ML / AI engineering
- [x] dominio/computacion — Testing / QA
- [x] dominio/marketing — Content marketing
- [x] dominio/marketing — CRO
- [x] dominio/marketing — Branding
- [x] dominio/leyes — Derecho de contratos
- [x] dominio/leyes — Propiedad intelectual
- [x] dominio/contabilidad — Contabilidad de costos
- [x] dominio/contabilidad — Auditoría
- [x] dominio/contabilidad — Contabilidad fiscal
- [x] dominio/diseno — UX research
- [x] dominio/diseno — Accesibilidad (WCAG)
- [x] dominio/diseno — Service design
### Dominio (nuevos nodos)
- [x] dominio/ventas
- [x] dominio/producto
- [x] dominio/recursos-humanos
- [x] dominio/operaciones
### Rol (nuevos nodos)
- [x] rol/sales-lead
- [x] rol/customer-success-lead
- [x] rol/people-lead
- [x] rol/legal-counsel
- [x] rol/founder-ceo
- [x] rol/cto
- [x] rol/data-engineer
- [x] rol/qa-engineer
### Organización (nuevo nodo)
- [x] organización/ejemplo-empresa

## LOG DE ITERACIONES
### [2026-07-09] fase previa | iter 1-34 completas (34 temas; lint OK)
### [2026-07-09] setup | Procedimiento reabastecimiento + gap_analysis + plan 41 temas
### [2026-07-09] LOOP 1 (Sustrato) | iter 35-44 — 10 páginas vía 4 subagentes
### [2026-07-09] LOOP 2 (Dominio existentes) | iter 45-54 — 10 páginas vía 3 subagentes
### [2026-07-09] LOOP 3 (Leyes/Contabilidad/Diseño + 4 nodos dominio + organización + 8 roles) | iter 55-75
- dominio/leyes: derecho-contratos, propiedad-intelectual
- dominio/contabilidad: costos, auditoria, impuestos
- dominio/diseno: ux-research, accesibilidad, service-design
- nuevos nodos: dominio/ventas, dominio/producto, dominio/recursos-humanos, dominio/operaciones
- organización/ejemplo-empresa (NovaTech)
- roles: sales-lead, customer-success-lead, people-lead, legal-counsel, founder-ceo, cto, data-engineer, qa-engineer
- **PLAN COMPLETO (75/75).** Procedimiento de reabastecimiento listo en GUIA-HERMES.md + scripts/gap_analysis.py.
### [2026-07-09] ESTADO FINAL DEL PLAN
- Los 41 temas del plan gap-analysis están ingestados. Wiki con 4 capas pobladas.
- Para extender: correr `python3 scripts/gap_analysis.py` (la taxonomía puede ampliarse)
  y volcar nuevos huecos en esta cola, o añadir temas manualmente.
