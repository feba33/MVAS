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
- **Iteración actual:** 44 (loop 1 = iter 35-44, 10 temas sustrato)
- **Temas completados:** 44 / 75 (34 previos + 41 de este plan; 10 hechos en loop 1)
- **Cronjob investigación:** `e273fdbbba14` (PAUSADO; bucle corre aquí)

## COLA DE TEMAS ([x] done / [ ] pending)
### Sustrato
- [x] sustrato/mexico — LFT (laboral, outsourcing, reparto utilidades)
- [x] sustrato/mexico — PROFECO / CONDUSEF (protección al consumidor)
- [x] sustrato/mexico — PLD / UIF (prevención de lavado, AML)
- [x] sustrato/estados-unidos — SEC y regulación de valores
- [x] sustrato/estados-unidos — Antitrust (Sherman / Clayton)
- [x] sustrato/estados-unidos — Bankruptcy / derecho concursal
- [x] sustrato/canada — Privacidad (PIPEDA)
- [x] sustrato/canada — Impuestos federales (CRA)
- [x] sustrato/brasil — LGPD (protección de datos)
- [x] sustrato/brasil — Impuestos (Receita Federal)
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
### [2026-07-09] fase previa | iter 1-34 completas (34 temas; lint OK)
### [2026-07-09] setup | Procedimiento reabastecimiento + gap_analysis + plan 41 temas
### [2026-07-09] LOOP 1 (Sustrato) | iter 35-44 — 10 páginas vía 4 subagentes
- mexico: lft, profeco-condusef, pld-uif · EE.UU.: sec-valores, antitrust, bankruptcy
- canada: privacidad (PIPEDA), impuestos (CRA) · brasil: lgpd, impuestos (Receita)
- Nota: se borró `sustrato/canada/raw/pipeda-cita.txt` (raw = cita only, no raw files).
### [2026-07-09] LOOP 2 (Dominio existentes) | iter 45+
### [2026-07-09] LOOP 3 (Nuevos nodos + roles) | iter …
