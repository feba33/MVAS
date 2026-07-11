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
**ALCANCE SUSTRATO: solo Norteamérica — México, Estados Unidos, Canadá.** NO agregar ningún
otro país (LatAm/Europa). Las capas Dominio/Rol son generales (agnósticas de país) y sí se
enriquecen. Si `gap_analysis.py` sugiere un país fuera de Norteamérica, ignorarlo.
**Raw = cita** (URL en `fuente`, sin `raw/`). Si el nodo no existe, créalo con superstructura.

## ESTADO
- **✅ ALCANCE: solo Norteamérica (México, EE.UU., Canadá) para sustrato.** Los países fuera de
  alcance ya creados (ecuador, portugal, argentina, brasil, chile, colombia, peru, uruguay, españa
  — 48 páginas) SE MANTENEN en el repo (decisión usuario 2026-07-10, opción 3: no borrar ni
  archivar; solo detener la búsqueda de nuevos países). El bucle NO agrega más países no-NA.
  `gap_analysis.py` filtra países no-NA.
- **2026-07-10 (iter 115) — PROFUNDIZACIÓN NORteamérica:** añadidas 4 páginas de mercado NA:
  `sustrato/canada/competition-bureau.md` + `provincial-federal.md`, `sustrato/mexico/comercio-exterior.md`
  (T-MEC/USMCA, IMMEX) y `sustrato/estados-unidos/controles-exportacion.md` (EAR/ITAR). CBCA ya cubierto
  en `corporativo.md` (no se duplicó). Siguiente paso sugerido: dominio/seguros, dominio/energia, etc. (Round 5 pendiente).
- **Plan:** Round 5 — tras Round 4 COMPLETO, `scripts/gap_analysis.py` (iter 114) agotó la taxonomía; se extendió la taxonomía con 10 nodos nuevos sugeridos (sustrato/ecuador, sustrato/portugal, dominio/seguros, dominio/energia, dominio/inmobiliario, dominio/retail, dominio/manufactura, rol/cio, rol/coo, rol/cmo). Cola Round 5 = 10 temas (sustrato x2, dominio x5, rol x3).
- **Iteración actual:** 125 — Round 10 en curso (cola de 13 temas; ver LOG ITER 125 abajo).
- **Temas completados:** 181 (168 previos + Round 9: 13/13 ingestados en iter 124).
- **Cronjob investigación:** `e273fdbbba14` (PAUSADO)
- **Siguiente paso:** Round 10 en curso (13 temas: 3 sustrato NA + 5 dominio + 5 rol). `gap_analysis.py` (post-Round 9) = 0 → extendida taxonomía para Round 10 (3 deepenings NA + 10 nodos nuevos). ALCANCE sustrato = solo Norteamérica (sin nuevos países no-NA). NO agregar países fuera de Norteamérica.

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

### Sustrato (nuevos países — LatAm + España)
- [x] sustrato/argentina — Protección de datos personales (Ley 25.326 / AAIP)
- [x] sustrato/argentina — Impuestos y Aduanas (AFIP)
- [x] sustrato/colombia — Protección de datos (Ley 1581) + impuestos (DIAN)
- [x] sustrato/españa — RGPD europeo / AEPD / CNMV
### Dominio (nuevos nodos)
- [x] dominio/sostenibilidad — ESG (CSRD, GRI, SASB, TCFD, ISSB)
- [x] dominio/logistica — Supply chain / última milla / incoterms
- [x] dominio/ciberseguridad-gobierno — Framework NIST / ISO 27001 (gobernanza)
### Rol (nuevos nodos)
- [x] rol/compliance-officer — Oficial de cumplimiento (PLD/anticorrupción)
- [x] rol/cfo — Director financiero
- [x] rol/head-of-people — (ampliación de people-lead)

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

### [2026-07-09] Round 2 — ITER 76-78 | 3 nodos nuevos (sustrato + dominio + rol)
- gap_analysis.py reportó 0 huecos (taxonomía del plan 1 agotada) → se abrió cola Round 2
  con 11 temas nuevos (LatAm/España + ESG + compliance officer).
- ingestados 3 temas cubriendo las 3 capas:
  - `sustrato/argentina` (nuevo): proteccion-datos-personales.md — Ley 25.326, DNPDP/AAIP, adecuación UE 2003.
  - `dominio/sostenibilidad` (nuevo): esg-marco.md — ESG + CSRD/GRI/SASB/TCFD/ISSB.
  - `rol/compliance-officer` (nuevo): compliance-officer.md — GRC, AML, anticorrupción, ISO 37301.
- Reference-only (URL en frontmatter; sin raw/). Superstructura completa en cada nodo.
### [2026-07-09] Round 2 — ITER 79 | sustrato/argentina impuestos-aduanas
- gap_analysis.py agotó taxonomía plan 1 → cola Round 2 sigue abierta (6 temas pendientes).
- ingestado 1 tema [sustrato]: `sustrato/argentina/impuestos-aduanas.md` — AFIP/ARCA, IVA 21%,
  Ganancias, Bienes Personales, Monotributo, seguridad social, tributos aduaneros
  (DI/TE/IVA/IVA Adicional/Ganancias/IIBB), NCM, CUIT, RG 5617/2024; transición AFIP→ARCA (2024).
- Reference-only (URL en frontmatter; sin raw/). Superstructura completa en el nodo argentina.
- **Próxima tarea (iter 80):** sustrato/colombia — Protección de datos (Ley 1581) + impuestos (DIAN) [sustrato].
  Cola Round 2 restante: 6 temas (sustrato x2, dominio x2, rol x2).

### [2026-07-09] Round 2 — ITER 80 | sustrato/colombia (nuevo nodo)
- gap_analysis.py agotó taxonomía plan 1 → cola Round 2 sigue abierta (5 temas pendientes).
- Creado nodo `sustrato/colombia` con superstructura completa (README, index, log, raw/).
- 2 páginas [sustrato]:
  - `sustrato/colombia/proteccion-datos.md` — Ley Estatutaria 1581/2012: habeas data (art.15-20),
    SIC/Delegatura/RNBD, datos sensibles, autorización, transferencia internacional (art.26),
    reglamentación D.1377/2013·886/2014·1081/2015.
  - `sustrato/colombia/impuestos.md` — DIAN; UVT 2026 $52.374; renta 35% PJ / escala 39% PN;
    IVA 19%; retención en la fuente (tarifas 2026); GMF 4x1000; RST (Ley 1943/2018 + 2010/2019);
    Monotributo; NIT/RUT; facturación electrónica.
- Reference-only (URL en frontmatter; sin raw/).
- **Próxima tarea (iter 81):** sustrato/españa — RGPD europeo / AEPD / CNMV [sustrato].
  Cola Round 2 restante: 5 temas (sustrato x1, dominio x2, rol x2).

### [2026-07-10] Round 2 — ITER 81 | sustrato/españa (nuevo nodo)
- gap_analysis.py agotó taxonomía plan 1 → cola Round 2 sigue abierta (4 temas pendientes).
- Creado nodo `sustrato/españa` con superstructura completa (README, index, log, raw/).
- 2 páginas [sustrato]:
  - `sustrato/españa/rgpd-aepd.md` — RGPD (UE 2016/679, aplicable 25-05-2018) + LOPDGDD
    (LO 3/2018) + AEPD: principios (art.5), base legal (art.6), derechos (arts.12-22),
    DPD, transferencias internacionales (cap.V), sanciones (art.83 hasta 20M€/4%), derechos digitales.
  - `sustrato/españa/cnmv.md` — CNMV (Ley 6/2002): autoridad administrativa independiente,
    funciones (art.18: transparencia, precios, protección inversor), supervisión de entidades/
    instrumentos, abuso de mercado (MAR), criptoactivos/MiCA, potestad sancionadora.
- Reference-only (URL en frontmatter; sin raw/).
- **Próxima tarea (iter 82):** dominio/logistica — Supply chain / última milla / incoterms [dominio].
  Cola Round 2 restante: 4 temas (dominio x2, rol x2).

### [2026-07-10] Round 2 — ITER 82 | dominio/logistica (nuevo nodo)
- gap_analysis.py agotó taxonomía plan 1 → cola Round 2 sigue abierta (3 temas pendientes).
- Creado nodo `dominio/logistica` con superstructura completa (README, index, log, raw/).
- 3 páginas [dominio]:
  - `dominio/logistica/gestion-cadena-suministro.md` — SCM: flujo Plan-Source-Make-Deliver-Return,
    inventario, KPIs (OTIF, turns), tendencias (nearshoring, gemelos digitales, ESG).
  - `dominio/logistica/ultima-milla.md` — Last mile: tramo final CD→cliente, ~50% del costo,
    lockers/microfulfillment, route optimization, KPIs (costo/entrega, fallidas).
  - `dominio/logistica/incoterms.md` — Incoterms 2020 (ICC): 11 reglas, grupos E/F/C/D,
    cambios 2020 vs 2010, división riesgo-costo entre comprador/vendedor.
- Reference-only (URL en frontmatter; sin raw/).
- **Próxima tarea (iter 83):** dominio/ciberseguridad-gobierno — NIST CSF 2.0 / ISO 27001 [dominio].
  Cola Round 2 restante: 3 temas (dominio x1, rol x2).

### [2026-07-10] Round 2 — ITER 83 | dominio/ciberseguridad-gobierno (nuevo nodo)
- gap_analysis.py agotó taxonomía plan 1 → cola Round 2 sigue abierta (2 temas pendientes).
- Creado nodo `dominio/ciberseguridad-gobierno` con superstructura completa (README, index, log, raw/).
- 2 páginas [dominio]:
  - `dominio/ciberseguridad-gobierno/nist-csf.md` — NIST CSF 2.0: 6 funciones (GOV, ID, PR, DE, RS, RC),
    voluntario/flexible, gobernanza de ciber alineada al negocio, tiers y perfiles.
  - `dominio/ciberseguridad-gobierno/iso-27001.md` — ISO 27001:2022 ISMS certificable, 93 controles
    Anexo A, vs NIST CSF 2.0 (complementarios).
- Reference-only (URL en frontmatter; sin raw/).
### [2026-07-10] Round 2 — ITER 84 | rol/cfo (nuevo nodo)
- gap_analysis.py agotó taxonomía plan 1 → cola Round 2 sigue abierta (1 tema pendiente).
- Creado nodo `rol/cfo` con superstructura completa (README, index, log, raw/).
- 1 página [rol]:
  - `rol/cfo/cfo.md` — Chief Financial Officer: estrategia financiera, FP&A, tesorería,
    reporting, estructura de capital; reporting al CEO/junta; CRO/CIO/Treasurer reportan;
    evolución a socio estratégico (CEO-en-espera); cualificaciones CPA/CA/CMA/CIMA + MBA/CFA;
    mandato legal (India Sec.203, US CFO Act 1990).
- Reference-only (URL en frontmatter; sin raw/).
- **Próxima tarea (iter 85):** rol/head-of-people — ampliación de people-lead [rol].
  Cola Round 2 restante: 1 tema (rol x1) — último de la cola Round 2.

### [2026-07-10] Round 2 — ITER 85 | rol/head-of-people (nuevo nodo — cierra cola Round 2)
- gap_analysis.py agotó taxonomía plan 1 → cola Round 2 se vacía (0 temas pendientes).
- Creado nodo `rol/head-of-people` con superstructura completa (README, index, log, raw/).
- 1 página [rol]:
  - `rol/head-of-people/head-of-people.md` — Head of People / VP People / CPO / CHRO:
    liderazgo estratégico de talento, cultura, total rewards y people operations; reporta
    al CEO; diferenciado de `rol/people-lead` (táctico-operativo).
- Reference-only (URL en frontmatter; sin raw/). Cross-ref a people-lead, recursos-humanos,
  founder-ceo, cfo, compliance-officer.
- **COLA ROUND 2 CERRADA.** Se ejecutó `python3 scripts/gap_analysis.py` → 25 huecos en
  nodos existentes + 2 nodos nuevos sugeridos (`dominio/juridico`, `dominio/estrategia`).
  Abierta cola Round 3 (29 temas) abajo.

### [2026-07-10] Round 3 — ITER 86 | sustrato/chile (nuevo nodo — LOOP 1)
- gap_analysis.py no sugirió sustrato; se añade Chile para cubrir la capa sustrato en Round 3.
- Creado nodo `sustrato/chile` con superstructura completa (README, index, log, raw/).
- 2 páginas [sustrato]:
  - `sustrato/chile/proteccion-datos.md` — Ley 19.628 (1999) + reforma Ley 21.719 (2023);
    CPLT como autoridad; transferencias internacionales; proyecto de nueva ley en trámite.
  - `sustrato/chile/impuestos.md` — SII: IVA 19%, Renta 1ª cat./global complementario,
    F29 mensual, F22 anual, PPM, retención BHE 15,25%, factura electrónica, aduana/TLC.
- Reference-only (URL en frontmatter; sin raw/).
- **Próxima tarea (iter 87):** dominio/finanzas — Derivados + Mercados de capitales [dominio] (LOOP 2).
  Cola Round 3 restante: 27 temas.

### [2026-07-10] Round 3 — ITER 87 | dominio/finanzas derivados + mercados-capitales (LOOP 2)
- 2 páginas añadidas al nodo existente `dominio/finanzas`:
  - `dominio/finanzas/derivados.md` — futuros/opciones/forwards/swaps; cobertura vs
    especulación; apalancamiento (margen 5-10%); mercados MEFF/CME/Eurex y OTC; riesgo
    de contraparte.
  - `dominio/finanzas/mercados-capitales.md` — ECM/IPO (salida a bolsa), DCM/bonos,
    underwriting (aseguramiento de emisión), actores del mercado.
- Reference-only (URL en frontmatter; sin raw/).
- **Próxima tarea (iter 88):** rol/product-owner + rol/scrum-master [rol] (LOOP 3).
  Cola Round 3 restante: 25 temas.

### [2026-07-10] Round 3 — ITER 88 | rol/product-owner + rol/scrum-master (nuevos nodos — LOOP 3)
- 2 nodos nuevos creados con superstructura completa:
  - `rol/product-owner/product-owner.md` — maximiza valor del producto, dueño del
    Product Backlog/PBIs, voz del cliente, stakeholders; vs PM/Product Lead.
  - `rol/scrum-master/scrum-master.md` — líder servicial, facilita eventos Scrum,
    remueve impedimentos, protege al equipo; vs Agile Coach/Engineering Manager.
- Reference-only (URL en frontmatter; sin raw/).
- **Cierra 3 bucles de ingest de esta corrida (sustrato + dominio + rol).** Cola Round 3
  restante: 23 temas (incl. dominio/computacion x4, marketing x3, leyes x3, contabilidad
  x2, diseño x2, juridico, estrategia, y roles design-lead/marketing-manager/ops-lead/
  support-lead/reclutador). Próxima corrida retoma desde iter 89.

### [2026-07-10] Round 3 — ITER 89 | dominio/computacion — Estilos arquitectura + Bases de datos (LOOP 4)
- 2 páginas añadidas al nodo existente `dominio/computacion`:
  - `dominio/computacion/estilos-arquitectura.md` — monolito modular, SOA, microservicios
    (servicios poco acoplados, protocolos ligeros, despliegue/escala independiente),
    event-driven (EDA: producción/detección de eventos, tolerancia a fallos), serverless;
    tabla de trade-offs.
  - `dominio/computacion/bases-datos.md` — SQL relacional (RDBMS, ACID); NoSQL (documental/
    clave-valor/columnar/grafo, sin esquema, polyglot); distribuidas (sharding, replicación,
    consenso); teorema CAP (CP vs AP); NewSQL.
- Reference-only (URL en frontmatter; sin raw/). Cross-ref a arquitectura, devops, data-engineering.
- **Próxima tarea (iter 90):** dominio/finanzas — Finanzas corporativas (M&A, valoración, tesorería).
  Cola Round 3 restante: 21 temas.

### [2026-07-10] Round 3 — ITER 90 | dominio/finanzas — Finanzas corporativas (M&A, valoración, tesorería) (LOOP 5)
- gap_analysis.py no sugirió sustrato; Round 3 sigue ampliando dominio/finanzas.
- 1 página añadida al nodo existente `dominio/finanzas`:
  - `dominio/finanzas/finanzas-corporativas.md` — finanzas corporativas como 3 pilares
    (M&A: merger/acquisition/tender offer/hostile takeover, sinergias, LBO; valoración:
    valor económico de la participación, cross-ref a valoracion.md; tesorería: liquidez,
    cobranza/pagos/concentración/inversión/fondeo, mitigación de riesgo) sobre el objetivo
    de maximizar valor de accionista.
- Reference-only (URL en frontmatter; sin raw/). Cross-ref a valoracion, mercados-capitales,
  private-equity-vc, derivados y rol/cfo (sin duplicar valoracion.md).
- **Próxima tarea (iter 91):** dominio/finanzas — Riesgo financiero (mercado, crédito,
  liquidez, operativo) — COMPLETADA en esta corrida. Cola Round 3 restante: 19 temas.

### [2026-07-10] Round 3 — ITER 91 | dominio/finanzas — Riesgo financiero (LOOP 6)
- 1 página añadida al nodo existente `dominio/finanzas`:
  - `dominio/finanzas/riesgo-financiero.md` — riesgo financiero: los 4 tipos
    principales (mercado: FX/tasa/equidad/commodities/inflación; crédito/contraparte;
    liquidez: financiamiento y mercado; operativo: procesos/personas/sistemas/externos
    + legal, tecnológico, PLD) con sub-riesgos y mitigación; marcos de gobernanza COSO
    ERM, ISO 31000, Basilea III (LCR/NSFR), CNBV; ciclo identificar-medir-mitigar-monitorear.
- Reference-only (URL en frontmatter; sin raw/). Cross-ref a derivados (coberturas),
  finanzas-corporativas (tesorería/liquidez), valoracion, rol/cfo y rol/compliance-officer.
- **Próxima tarea (iter 92):** dominio/computacion — Plataforma / DevOps / SRE.
  Cola Round 3 restante: 19 temas.

### [2026-07-10] Round 3 — ITER 92-93 | dominio/computacion — Plataforma/SRE + Frontend (LOOP 7)
- 2 páginas añadidas al nodo existente `dominio/computacion`:
  - `dominio/computacion/plataforma-sre.md` — Ingeniería de Plataforma + SRE: IDP/golden
    paths, SLI/SLO/error budget, tabla DevOps vs SRE vs Platform Eng; cross-ref devops,
    estilos-arquitectura, bases-datos.
  - `dominio/computacion/frontend.md` — Frontend 2026: React/Vue/Svelte/Angular/Astro/
    Next.js, meta-frameworks, Core Web Vitals, tabla de decisión; cross-ref arquitectura,
    estilos-arquitectura, testing-qa, plataforma-sre.
- Reference-only (URL en frontmatter; sin raw/).
- **Cumple ≥3 bucles de ingest por corrida (Round 3 lleva 7 bucles).** Cola Round 3
  restante: 17 temas (marketing x3, leyes x3, contabilidad x2, diseño x2, juridico,
  estrategia, roles design-lead/marketing-manager/ops-lead/support-lead/reclutador).
  Próxima corrida retoma desde iter 94.

### [2026-07-10] Round 3 — ITER 94 | dominio/marketing — Demand generation / paid media (LOOP 1)
- 1 página añadida al nodo existente `dominio/marketing`:
  - `dominio/marketing/demand-generation.md` — demand gen full-funnel vs lead gen;
    paid media (Google/LinkedIn/Meta); ABM + intent data; métricas (CPL, CAC, pipeline).
- Reference-only (URL en frontmatter; sin raw/). Cross-ref a content-marketing, cro,
  rol/marketing-lead, rol/growth-lead.
- **Próxima tarea (iter 95):** dominio/marketing — Analítica de marketing + Lifecycle/email.

### [2026-07-10] Round 3 — ITER 95 | dominio/marketing — Analítica + Lifecycle/email (LOOP 2)
- 2 páginas añadidas al nodo existente `dominio/marketing`:
  - `dominio/marketing/analitica-marketing.md` — atribución: first/last/lineal/U-shaped/
    data-driven, multitouch, MMM, method stacking B2B 2026.
  - `dominio/marketing/lifecycle-email.md` — email disparado por comportamiento, etapas/
    triggers, retención y LTV; cierra ciclo post-conversión.
- Reference-only (URL en frontmatter; sin raw/). Cross-ref a demand-generation, cro,
  rol/customer-success-lead, dominio/finanzas (unit economics).
- Cola Round 3 restante: 14 temas (leyes x3, contabilidad x2, diseño x2, juridico,
  estrategia, roles design-lead/marketing-manager/ops-lead/support-lead/reclutador).
  Próxima tarea (iter 96): dominio/leyes — Derecho societario / corporativo.

### [2026-07-10] Round 3 — ITER 96 | dominio/leyes — Derecho societario / corporativo (LOOP 3)
- 1 página añadida al nodo existente `dominio/leyes`:
  - `dominio/leyes/derecho-societario.md` — contrato de sociedad, civil vs mercantil,
    persona jurídica/responsabilidad limitada, levantamiento del velo; tipos LGSM
    (SA/SAPI/SAS/SRL); órganos (asamblea/consejo/comisario); gobierno corporativo.
- Reference-only (URL en frontmatter; sin raw/). Cross-ref a sustrato/mexico/lgsm,
  codigo-de-comercio, dominio/juridico, rol/legal-counsel, founder-ceo, cfo,
  dominio/finanzas (M&A, mercados-capitales).
- **Próxima tarea (iter 97):** dominio/leyes — Derecho laboral (profundización).

### [2026-07-10] Round 3 — ITER 97 | dominio/leyes — Derecho laboral LFT (LOOP 4)
- 1 página añadida al nodo existente `dominio/leyes`:
  - `dominio/leyes/derecho-laboral.md` — relación laboral, jornada/salario/PTU,
    IMSS/INFONAVIT, rescisión, reforma outsourcing 2021 + REPSE, justicia laboral,
    reforma reducción de jornada 2026 (DOF 01-05-2026).
- Reference-only (URL en frontmatter; sin raw/). Cross-ref a sustrato/mexico/lft,
  dominio/juridico, rol/compliance-officer, people-lead/head-of-people,
  recursos-humanos, contabilidad/impuestos.
- Cola Round 3 restante: 12 temas (leyes x1, contabilidad x2, diseño x2, juridico,
  estrategia, roles design-lead/marketing-manager/ops-lead/support-lead/reclutador).
  Próxima tarea (iter 98): dominio/leyes — Cumplimiento / regulación.

### [2026-07-10] Round 3 — ITER 98 | dominio/leyes — Cumplimiento / regulación (LOOP 5)
- 1 página añadida al nodo existente `dominio/leyes`:
  - `dominio/leyes/cumplimiento-regulacion.md` — compliance transversal; ISO 37301
    (CMS certificable, PDCA); enfoque basado en riesgo; DOJ/UK Bribery Act; vs ISO 37001.
- Reference-only (URL en frontmatter; sin raw/). Cross-ref a dominio/juridico,
  rol/compliance-officer, ciberseguridad-gobierno (ISO 27001), sostenibilidad (ESG),
  finanzas/riesgo-financiero.

### [2026-07-10] Round 3 — ITER 99 | dominio/contabilidad — Consolidación + Tesorería (LOOP 6)
- 2 páginas añadidas al nodo existente `dominio/contabilidad`:
  - `dominio/contabilidad/consolidacion.md` — grupo como una entidad; control=obligación;
    métodos (integración/equivalencia/costo); eliminaciones intercompañía; NIIF 10/3.
  - `dominio/contabilidad/tesoreria.md` — treasury (liquidez, working capital, cash
    forecasting, TMS/ERP); conexión con finanzas corporativas y CFO.
- Reference-only (URL en frontmatter; sin raw/). Cross-ref a niif-us-gaap, auditoria,
  rol/cfo, finanzas-corporativas, riesgo-financiero.

### [2026-07-10] Round 3 — ITER 100 | dominio/diseno — Design systems + UX writing (LOOP 7)
- 2 páginas añadidas al nodo existente `dominio/diseno`:
  - `dominio/diseno/design-systems.md` — single source of truth, Atomic Design, design
    tokens, component/pattern library; conecta con frontend.
  - `dominio/diseno/ux-writing.md` — microcopy, voz/tono, claridad/brevedad/acción;
    impacto en conversión; vive dentro de design-systems.
- Reference-only (URL en frontmatter; sin raw/). Cross-ref a accesibilidad, ux-research,
  service-design, frontend, rol/design-lead, ux-ui-lead, cro, lifecycle-email.
- Cola Round 3 restante: 7 temas (juridico, estrategia, roles design-lead/marketing-manager/
  ops-lead/support-lead/reclutador). Próxima tarea (iter 101): dominio/juridico (nuevo nodo).

### [2026-07-10] Round 3 — ITER 101 | NODO NUEVO dominio/juridico — Jurídico interno (LOOP 8)
- Creado nodo `dominio/juridico` con superstructura completa (README, index, log, raw/).
- 1 página: `juridico-interno.md` — función in-house; jerarquía GC/CLO → counsel →
  legal ops; contratos, M&A, gobernanza corporativa, litigios, investigaciones, externos.
- Reference-only (URL en frontmatter; sin raw/). Cross-ref a leyes/derecho-societario,
  derecho-contratos, cumplimiento-regulacion, finanzas-corporativas, rol/legal-counsel,
  rol/compliance-officer, founder-ceo, cfo.

### [2026-07-10] Round 3 — ITER 102 | NODO NUEVO dominio/estrategia — Estrategia/OKRs (LOOP 9)
- Creado nodo `dominio/estrategia` con superstructura completa (README, index, log, raw/).
- 1 página: `estrategia-okr.md` — OKRs + Hoshin Kanri (despliegue/catchball/PDCA); OGSM,
  Balanced Scorecard, KPIs lag; brecha de ejecución entre estrategia y operación.
- Reference-only (URL en frontmatter; sin raw/). Cross-ref a founder-ceo, product-lead,
  head-of-people, marketing-lead, producto, finanzas-corporativas, operaciones.
- Cola Round 3 restante: 5 temas (roles design-lead/marketing-manager/ops-lead/
  support-lead/reclutador). Próxima tarea (iter 103): rol/design-lead.

### [2026-07-10] Round 3 — ITER 103-107 | NODOS NUEVOS rol/* (design-lead, marketing-manager, ops-lead, support-lead, reclutador) (LOOP 10-14)
- 5 nodos `rol/` creados con superstructura completa (README, index, log, raw/), 1 página c/u:
  - `rol/design-lead/design-lead.md` — visión/estrategia de diseño, mentoría, research, abogacía UX (LinkedIn).
  - `rol/marketing-manager/marketing-manager.md` — estrategia/ejecución/optimización de marketing; brand, campañas, AI fluency (LHH, Interview Guys).
  - `rol/ops-lead/ops-lead.md` — diseña/controla producción; eficiencia, procesos, cadena, mejora continua (Wikipedia Operations mgmt).
  - `rol/support-lead/support-lead.md` — servicio al cliente; calidad por retención; CSAT/NPS; vs customer-success (Wikipedia Customer service).
  - `rol/reclutador/reclutador.md` — proceso reclutamiento; sourcing+IA; in-house vs agency (Wikipedia Recruitment).
- Reference-only (URL en frontmatter; sin raw/). Cross-refs a dominio/marketing, dominio/diseno,
  dominio/operaciones, dominio/recursos-humanos, head-of-people, customer-success-lead, operations-lead, founder-ceo.
- Cola Round 3 restante: 3 temas (sustrato/chile x2, organización/caso x1).
  Próxima tarea (iter 108): sustrato/chile — Marco general Chile (nuevo país).

### [2026-07-10] Round 3 — ITER 108-109 | sustrato/chile — Marco general + Emprendimiento (LOOP 15-16)
- Nodo existente `sustrato/chile` (ya tenía proteccion-datos + impuestos). 2 páginas añadidas:
  - `sustrato/chile/chile-general.md` — economía ingresos altos, miembro OCDE, competitividad,
    libertad económica, TLC (Wikipedia Economy of Chile en/es).
  - `sustrato/chile/chile-emprendimiento.md` — Start-Up Chile/CORFO, PyMEs, Régimen SIMPLE
    2025 (Wikipedia + SII, reference-only; confianza media en detalles del SIMPLE).
- `organización/caso` (NovaTech) ya existe con métricas desde iteraciones previas → se marca
  [x] sin nueva ingest.
- **Round 3 COMPLETO (114/114).** Reabastecimiento: re-ejecutar `python3 scripts/gap_analysis.py`\
  para abrir Round 4. Próxima tarea (iter 110): gap analysis → nuevo plan.

### [2026-07-10] Round 4 — ITER 110 | gap analysis + plan Round 4 (reabastecimiento)
- gap_analysis.py (Round 3) reportó 5 falsos positivos: slugs obsoletos que ya estaban
  ingestados en Round 3 (estilos-arquitectura, plataforma-sre, demand-generation,
  lifecycle-email, cumplimiento-regulacion). Corregida la taxonomía de `scripts/gap_analysis.py`
  (slugs reales + 6 nodos nuevos + 6 roles nuevos). Re-ejecutado → 2 huecos reales en `rol`
  (product-marketing-manager, data-scientist) + 6 nodos nuevos sugeridos.
- Abierta cola Round 4 (11 temas: sustrato x4, dominio x5, rol x2). Próxima tarea (iter 111):
  sustrato/peru + sustrato/uruguay (LOOP 1, capa sustrato).

### [2026-07-10] Round 4 — ITER 111 | LOOP 1 (sustrato) — peru + uruguay
- Creados nodos `sustrato/peru` y `sustrato/uruguay` (superstructura completa).
- `sustrato/peru`: `proteccion-datos.md` (Ley 29733 + Reglamento DS 003-2013-JUS; MINJUS/ANPD)
  e `impuestos.md` (SUNAT: IGV 18%, Renta 29,5%, RUC).
- `sustrato/uruguay`: `proteccion-datos.md` (Ley 18.331 + URCDP) e `impuestos.md`
  (DGI: IVA 22%, IRAE 25%, IRPF, Patrimonio).
- Reference-only (URL en frontmatter; sin raw/). Próxima tarea (iter 112): dominio/economia,
  estadistica, project-management, negociacion (LOOP 2).

### [2026-07-10] Round 4 — ITER 112 | LOOP 2 (dominio) — economia, estadistica, project-management, negociacion
- Creados 4 nodos `dominio/` (superstructura completa).
- `economia`: macroeconomia.md + indicadores-ciclo-fiscal.md.
- `estadistica`: estadistica-ciencia-datos.md. `project-management`: gestion-proyectos.md.
- `negociacion`: negociacion.md (método Harvard, BATNA, ZOPA).
- Reference-only (URL en frontmatter; sin raw/). Próxima tarea (iter 113): rol/product-marketing-manager
  + rol/data-scientist (LOOP 3).

### [2026-07-10] Round 4 — ITER 113 | LOOP 3 (rol) — product-marketing-manager + data-scientist
- Creados 2 nodos `rol/` (superstructura completa).
- `product-marketing-manager`: product-marketing-manager.md (PMM: GTM, posicionamiento, mensaje).
- `data-scientist`: data-scientist.md (estadística + ML + programación; modelado predictivo).
- Reference-only (URL en frontmatter; sin raw/).
- **Round 4 COMPLETO (11/11 temas en 3 bucles).** Siguiente paso de reabastecimiento:
  re-ejecutar `python3 scripts/gap_analysis.py` para abrir Round 5.

### [2026-07-10] Round 5 — ITER 114 | gap_analysis (plan) + LOOP 1 (sustrato) — ecuador + portugal
- Reabastecimiento: extendida la taxonomía de `scripts/gap_analysis.py` (10 nodos nuevos:
  sustrato/ecuador, sustrato/portugal, dominio/seguros, dominio/energia, dominio/inmobiliario,
  dominio/retail, dominio/manufactura, rol/cio, rol/coo, rol/cmo). Re-ejecutado → 10 sugerencias.
  Abierta cola Round 5 (10 temas).
- Creados nodos `sustrato/ecuador` y `sustrato/portugal` (superstructura completa).
- `sustrato/ecuador`: proteccion-datos.md (LOPDP, R.O. Sup. 459/2021, vigencia 2023; SPDP) +
  impuestos.md (SRI: IVA 15%/5%/0%, Renta ~25%, RUC).
- `sustrato/portugal`: proteccion-datos.md (RGPD + Lei 58/2019; CNPD) + impuestos.md
  (AT: IRS hasta 48%, IRC 21%, IVA 23%/13%/6%).
- Reference-only (URL en frontmatter; sin raw/). **LOOP 1 de Round 5 (capa sustrato) COMPLETO.**
  - **Próxima tarea (iter 115):** LOOP 2 (dominio) — seguros, energia, inmobiliario, retail, manufactura.

  ### [2026-07-11] Round 5 — ITER 115 | LOOP 2 (dominio) — seguros, energia, inmobiliario, retail, manufactura
  - Creados 5 nodos `dominio/` con superstructura completa (README, index, log, raw/).
  - `dominio/seguros`: `seguros.md` — vida, P&C, reaseguro, ciencia actuarial, Solvency II.
  - `dominio/energia`: `energia.md` — renovables, oil&gas, redes, regulación (FERC/CRE/SENER).
  - `dominio/inmobiliario`: `bienes-raices.md` — residencial/comercial, REITs, cap rate, ciclos.
  - `dominio/retail`: `retail.md` — omnicanal, merchandising, e-commerce, última milla.
  - `dominio/manufactura`: `manufactura.md` — lean, Six Sigma/DMAIC, Industry 4.0, cadena de producción.
  - Reference-only (URL en frontmatter; sin raw/). **LOOP 2 de Round 5 (capa dominio) COMPLETO.**
  - **Próxima tarea (iter 116):** LOOP 3 (rol) — cio, coo, cmo.

  ### [2026-07-11] Round 5 — ITER 116 | LOOP 3 (rol) — cio, coo, cmo
  - Creados 3 nodos `rol/` con superstructura completa (README, index, log, raw/).
  - `rol/cio`: `cio.md` — estrategia de TI, transformación digital, datos/ciberseguridad; reporta a CEO; vs CTO.
  - `rol/coo`: `coo.md` — ejecuta estrategia, opera día a día, excelencia operativa; tipologías integrator/heir apparent.
  - `rol/cmo`: `cmo.md` — marca, demanda, GTM, customer insight, martech; ROI del marketing.
  - Reference-only (URL en frontmatter; sin raw/). **LOOP 3 de Round 5 (capa rol) COMPLETO.**
  - **Round 5 COMPLETO (10/10 temas en 3 bucles).** Siguiente paso: ejecutar `python3 scripts/gap_analysis.py` para abrir Round 6.

### [2026-07-11] Round 6 — ITER 117 | gap_analysis (plan) + 7 nodos nuevos sugeridos
- Reabastecimiento: agotada la taxonomía de Round 5 (0 huecos, 0 nodos nuevos). Extendida
  `scripts/gap_analysis.py` con 7 nodos nuevos en capas generales (dominio/rol, dentro del alcance):
  `dominio/salud`, `dominio/educacion`, `dominio/transporte`, `dominio/telecomunicaciones`,
  `rol/chief-data-officer`, `rol/chief-sustainability-officer`, `rol/chief-risk-officer`.
- Re-ejecutado → 7 sugerencias. Abierta cola Round 6 (7 temas: dominio x4, rol x3).
- **Próxima tarea (iter 118):** LOOP 1 (dominio): salud, educacion, transporte, telecomunicaciones.

### [2026-07-11] Round 6 — ITER 118 | LOOP 1 (dominio) — salud, educacion, transporte, telecomunicaciones
- Creados 4 nodos `dominio/` con superstructura completa (README, index, log, raw/).
- `dominio/salud`: `salud.md` — sistemas de salud, seguros médicos, farmacia, telemedicina.
- `dominio/educacion`: `educacion.md` — modelos, niveles, edtech, política educativa.
- `dominio/transporte`: `transporte.md` — modos, logística urbana, aviación, regulación.
- `dominio/telecomunicaciones`: `telecomunicaciones.md` — redes fijas/móviles, 5G, espectro, regulación.
- Reference-only (URL en frontmatter; sin raw/). **LOOP 1 de Round 6 (capa dominio) COMPLETO.**
- **Próxima tarea (iter 119):** LOOP 2 (rol): chief-data-officer, chief-sustainability-officer, chief-risk-officer.

### [2026-07-11] Round 6 — ITER 119 | LOOP 2 (rol) — CDO, CSO, CRO
- Creados 3 nodos `rol/` con superstructura completa (README, index, log, raw/).
- `rol/chief-data-officer`: `chief-data-officer.md` — gobierno de datos, analítica, democratización, habilitación de IA.
- `rol/chief-sustainability-officer`: `chief-sustainability-officer.md` — ESG, descarbonización, reporting climático, responsabilidad social.
- `rol/chief-risk-officer`: `chief-risk-officer.md` — riesgo enterprise, ERM, crédito/mercado/operativo, continuidad.
- Reference-only (URL en frontmatter; sin raw/). **LOOP 2 de Round 6 (capa rol) COMPLETO.**
- **Round 6 COMPLETO (7/7 temas en 2 bucles).** Siguiente paso: ejecutar gap_analysis para Round 7.

### [2026-07-11] Round 7 — ITER 120 | gap_analysis extendido + 5 ingests (3 capas)
- gap_analysis.py agotó taxonomía (0 huecos) → extendida (3 huecos sustrato NA + 10 nodos nuevos).
- 5 temas ingestados cubriendo las 3 capas:
  - [sustrato] `sustrato/mexico/energia.md` (nodo existente): CFE, PEMEX, SENER/CRE/CNH/ASEA, reforma 2013, renovables.
  - [dominio] `dominio/agronegocios/` (nuevo nodo): cadena agroalimentaria, agtech, commodities.
  - [dominio] `dominio/construccion/` (nuevo nodo): ciclo AEC, contratación, costos, tendencias.
  - [rol] `rol/ciso/` (nuevo nodo): CISO, dueño del riesgo de seguridad/ciberseguridad.
  - [rol] `rol/general-counsel/` (nuevo nodo): GC/CLO, asesor legal máximo, gobierno corporativo.
- Reference-only (URL en frontmatter; sin raw/). Superstructura completa en cada nodo nuevo.
- **Cola Round 7 restante: 8 temas** (sustrato x3, dominio x4, rol x2). → **COMPLETADO en iter 121** (ver bloque ITER 121 abajo): sustrato/estados-unidos→salud, sustrato/canada→salud, dominio/turismo.

### [2026-07-11] Round 7 — ITER 121 | 3 ingests (sustrato + sustrato + dominio)
- 3 temas ingestados cubriendo sustrato (x2) + dominio (x1). Cola Round 7 restante: 5 temas (sustrato x1, dominio x3, rol x2).
  - [sustrato] `sustrato/estados-unidos/salud.md` (nodo existente): healthcare EE.UU. — FDA (FD&C), CMS (Medicare/Medicaid/CHIP), HIPAA (Título II PHI), Medicare Part A/B/C/D, Medicaid; ~17.8% PIB; sin cobertura universal.
  - [sustrato] `sustrato/canada/salud.md` (nodo existente): medicare single-payer universal (Canada Health Act 1984, 5 principios), provincias administran, Health Canada regula fármacos, CADTH→Canada's Drug Agency (CDA).
  - [dominio] `dominio/turismo/` (nuevo nodo): turismo y hospitalidad — industria, segmentos, cadena de valor, OTAs, sostenibilidad; superstructura completa (README/index/log/raw).
- Reference-only (URL en frontmatter; sin raw/).
- **Próxima tarea (iter 122):** dominio/medios-comunicacion — Medios de comunicación / publishing [dominio].

### [2026-07-11] Round 7 — ITER 122 | 5 ingests (dominio x3 + rol x2) — CIERRA COLA ROUND 7
- 5 temas ingestados cubriendo dominio (x3) + rol (x2). Cola Round 7 VACÍA (13/13 en iter 120+121+122).
  - [dominio] `dominio/medios-comunicacion/` (nuevo): mass media, publishing, news, modelos de negocio, media capture.
  - [dominio] `dominio/automotriz/` (nuevo): industria automotriz/movilidad — OEM, Tier 1/2/3, VEs, autonomía, MaaS.
  - [dominio] `dominio/gobierno-publico/` (nuevo): sector público, SOEs, administración pública, procurement.
  - [rol] `rol/brand-manager/` (nuevo): Brand Manager — percepción de marca, brand equity, cadena de suministro.
  - [rol] `rol/business-development/` (nuevo): Business Development — crecimiento vía relaciones/mercados/partnerships.
- Reference-only (URL en frontmatter; sin raw/). Superstructura completa en cada nodo nuevo.
- **Próxima tarea / estado:** Reabastecimiento ejecutado — gap_analysis.py = 0 huecos reales, 0 nodos nuevos (post-corrección de falsos positivos `healthcare`→`salud`). Bucle puede pausar (DETENER) hasta nueva dirección de taxonomía/alcance del usuario.


## COLA ROUND 4 (gap_analysis.py iter 110 — taxonomía corregida)
### Sustrato (nuevos países)
- [x] sustrato/peru — Protección de datos (Ley 29733 / ANPD)
- [x] sustrato/peru — Impuestos y aduanas (SUNAT: IGV, IR, RUC)
- [x] sustrato/uruguay — Protección de datos (URCDP Ley 18.331)
- [x] sustrato/uruguay — Impuestos (DGI: IRPF, IRAE, IVA)
### Dominio (nuevos nodos)
- [x] dominio/economia — Macroeconomía (PIB, inflación, política monetaria, bancos centrales)
- [x] dominio/economia — Indicadores y ciclo económico / política fiscal
- [x] dominio/estadistica — Estadística y ciencia de datos (inferencia, probabilidad, visualización)
- [x] dominio/project-management — Gestión de proyectos (PMP, agile/waterfall, triple restricción)
- [x] dominio/negociacion — Negociación (método Harvard, BATNA, ZOPA)
### Rol (ampliar nodo existente)
- [x] rol/product-marketing-manager — Product Marketing Manager (PMM)
- [x] rol/data-scientist — Data Scientist

## ✅ CIERRE ROUND 4
Todos los temas de la cola ingestados (11/11 en 3 bucles: LOOP 1 sustrato, LOOP 2 dominio, LOOP 3 rol).
Siguiente paso de reabastecimiento: re-ejecutar `python3 scripts/gap_analysis.py` para abrir Round 5 (nuevos países/disciplinas/roles).

## COLA ROUND 5 (gap_analysis.py iter 114 — taxonomía extendida)
### Sustrato (nuevos países)
- [x] sustrato/ecuador — Protección de datos (LOPDP, R.O. Sup. 459/2021; SPDP)
- [x] sustrato/ecuador — Impuestos y aduanas (SRI: IVA 15%/5%/0%, Renta ~25%, RUC)
- [x] sustrato/portugal — Protección de datos (RGPD + Lei 58/2019; CNPD)
- [x] sustrato/portugal — Impuestos (AT: IRS hasta 48%, IRC 21%, IVA 23%/13%/6%)
### Dominio (nuevos nodos)
- [x] dominio/seguros — Seguros (vida, P&C, actuarial, reaseguro, Solvency II)
- [x] dominio/energia — Energía (renovables, oil&gas, redes, regulación)
- [x] dominio/inmobiliario — Bienes raíces / real estate (mercado, financiamiento, REITs)
- [x] dominio/retail — Retail / comercio (omnicanal, merchandising, e-commerce)
- [x] dominio/manufactura — Manufactura (lean, Six Sigma, cadena de producción)
### Rol (nuevos nodos)
- [x] rol/cio — CIO (Chief Information Officer)
- [x] rol/coo — COO (Chief Operating Officer)
- [x] rol/cmo — CMO (Chief Marketing Officer)

## ✅ CIERRE ROUND 5
COMPLETO — Round 5 finalizado (10/10 temas en 3 bucles: LOOP 1 sustrato ecuador+portugal, LOOP 2 dominio x5, LOOP 3 rol x3). Siguiente paso: ejecutar `python3 scripts/gap_analysis.py` para abrir Round 6.

## COLA ROUND 6 (gap_analysis.py iter 117 — taxonomía extendida)
### Dominio (nuevos nodos)
- [x] dominio/salud — Salud / healthcare (sistemas de salud, seguros médicos, farmacia, telemedicina)
- [x] dominio/educacion — Educación (modelos, edtech, política educativa)
- [x] dominio/transporte — Transporte / movilidad (logística urbana, aviación, regulación)
- [x] dominio/telecomunicaciones — Telecomunicaciones (redes, 5G, regulación)
### Rol (nuevos nodos)
- [x] rol/chief-data-officer — CDO (Chief Data Officer)
- [x] rol/chief-sustainability-officer — CSO (Chief Sustainability Officer)
- [x] rol/chief-risk-officer — CRO (Chief Risk Officer)

## ✅ CIERRE ROUND 6
COMPLETO — Round 6 finalizado (7/7 temas en 2 bucles: LOOP 1 dominio x4, LOOP 2 rol x3). Siguiente paso: ejecutar `python3 scripts/gap_analysis.py`; si devuelve 0 (taxonomía agotada), ampliar NEW_NODES/TAXONOMY para Round 7 o detener.


## COLA ROUND 7 (gap_analysis.py iter 120 — taxonomía extendida; sustrato solo NA)
### Sustrato (extender nodos NA existentes)
- [x] sustrato/mexico — Sector energía (CRE/SENER, PEMEX/CFE, renovables)
- [x] sustrato/estados-unidos — Salud / healthcare (FDA, CMS, HIPAA, Medicare-Medicaid)
- [x] sustrato/canada — Salud / healthcare (Health Canada, provincias, CADTH)
### Dominio (nuevos nodos)
- [x] dominio/agronegocios — Agroindustria / agronegocios
- [x] dominio/construccion — Construcción / ingeniería AEC
- [x] dominio/turismo — Turismo / hospitalidad
- [x] dominio/medios-comunicacion — Medios de comunicación / publishing
- [x] dominio/automotriz — Industria automotriz / movilidad
- [x] dominio/gobierno-publico — Sector público / gobierno
### Rol (nuevos nodos)
- [x] rol/ciso — CISO — Chief Information Security Officer
- [x] rol/general-counsel — General Counsel
- [x] rol/brand-manager — Brand Manager
- [x] rol/business-development — Business Development
## COLA ROUND 3 (gap_analysis.py iter 85 + nuevos países)
### Sustrato (nuevo país)
- [x] sustrato/chile — Protección de datos (Ley 19.628 / Consejo Transparencia)
- [x] sustrato/chile — Impuestos y Aduanas (SII: IVA 19%, Renta, F29/F22)
### Dominio (nodos existentes — ampliar)
- [x] dominio/finanzas — Derivados (futuros, opciones, swaps)
- [x] dominio/finanzas — Mercados de capitales (IPO, emisión deuda)
- [x] dominio/finanzas — Finanzas corporativas (M&A, valoración, tesorería)
- [x] dominio/finanzas — Riesgo financiero
- [x] dominio/computacion — Arquitectura de software (microservicios, event-driven)
- [x] dominio/computacion — Plataforma / DevOps / SRE
- [x] dominio/computacion — Frontend (frameworks, performance)
- [x] dominio/computacion — Bases de datos (SQL, NoSQL, distribuidas)
- [x] dominio/marketing — Demand generation / paid media
- [x] dominio/marketing — Analítica de marketing (atribución)
- [x] dominio/marketing — Lifecycle / email marketing
- [x] dominio/leyes — Derecho societario / corporativo
- [x] dominio/leyes — Derecho laboral (profundización)
- [x] dominio/leyes — Cumplimiento / regulación
- [x] dominio/contabilidad — Consolidación / reportes financieros
- [x] dominio/contabilidad — Tesorería / flujo de efectivo
- [x] dominio/diseno — Design systems / componentes
- [x] dominio/diseno — UX writing / microcopy
### Dominio (nuevos nodos)
- [x] dominio/juridico — Jurídico / legal interno de empresa (nuevo nodo)
- [x] dominio/estrategia — Estrategia / OKRs / planeación (nuevo nodo)
### Rol (nuevos nodos)
- [x] rol/product-owner — Product Owner / PO
- [x] rol/scrum-master — Scrum Master
- [x] rol/design-lead — Design Lead / UX Lead
- [x] rol/marketing-manager — Marketing Manager
- [x] rol/ops-lead — Operations Lead
- [x] rol/support-lead — Support / CX Lead
- [x] rol/reclutador — Recruiter / Talent Acquisition

## COLA ROUND 8 (gap_analysis.py iter 122 → taxonomía extendida en iter 123; sustrato solo NA)
### Sustrato (deepening nodos NA existentes)
- [x] sustrato/mexico — Sistema financiero / banca (Banxico, CNBV, banca múltiple, Sofipos)
- [x] sustrato/estados-unidos — Sector tecnológico (Big Tech, antitrust, IA, CHIPS Act)
- [x] sustrato/canada — Sector bancario (Big Six, OSFI)
### Dominio (nuevos nodos)
- [x] dominio/biotecnologia — Biotecnología (biofármacos, agtech, genómica)
- [x] dominio/mineria — Minería (commodities, minerales críticos, ESG)
- [x] dominio/defensa-seguridad — Defensa y seguridad (armamento, dual-use)
- [x] dominio/aeroespacial — Aeroespacial (aeronáutica, espacio/NewSpace)
- [x] dominio/fintech — Fintech (pagos, banca digital, lending, regtech)
### Rol (nuevos nodos)
- [x] rol/chief-product-officer — CPO
- [x] rol/vp-engineering — VP Engineering
- [x] rol/vp-sales — VP Sales
- [x] rol/chief-of-staff — Chief of Staff
- [x] rol/account-executive — Account Executive

### [2026-07-11] Round 8 — ITER 123 | gap_analysis extendido + 13 ingests (3 capas) — REANUDA bucle
- `gap_analysis.py` (iter 122) = 0 huecos reales, 0 nodos nuevos → se **EXTENDIÓ** `scripts/gap_analysis.py`
  (Round 8) con 3 huecos sustrato NA (mexico→banca, estados-unidos→sector-tecnologia, canada→sector-bancario)
  + 10 nodos nuevos (dominio: biotecnologia, mineria, defensa-seguridad, aeroespacial, fintech; rol:
  chief-product-officer, vp-engineering, vp-sales, chief-of-staff, account-executive). ALCANCE respetado:
  sustrato = solo Norteamérica; NO se agregan países fuera de NA.
- 13 temas ingestados cubriendo las 3 capas:
  - [sustrato] `sustrato/mexico/banca-sistema-financiero.md`, `sustrato/estados-unidos/sector-tecnologia.md`, `sustrato/canada/sector-bancario.md` (deepening de nodos NA existentes).
  - [dominio] `dominio/biotecnologia/`, `dominio/mineria/`, `dominio/defensa-seguridad/`, `dominio/aeroespacial/`, `dominio/fintech/` (5 nodos nuevos).
  - [rol] `rol/chief-product-officer/`, `rol/vp-engineering/`, `rol/vp-sales/`, `rol/chief-of-staff/`, `rol/account-executive/` (5 nodos nuevos).
- Reference-only (URL en frontmatter; sin raw/). Superstructura completa en cada nodo nuevo.
- **Round 8 COMPLETO (13/13 temas en 3 bucles: LOOP 1 sustrato, LOOP 2 dominio, LOOP 3 rol).** Cola Round 8 VACÍA.
  Siguiente paso: re-ejecutar `python3 scripts/gap_analysis.py`; si devuelve 0, ampliar taxonomía para Round 9 o pausar.


## COLA ROUND 9 (gap_analysis.py iter 123 → taxonomía extendida en iter 124; sustrato solo NA)
### Sustrato (deepening nodos NA existentes)
- [x] sustrato/mexico — Sistema de pensiones (AFORE / CONSAR / SAR)
- [x] sustrato/estados-unidos — Vivienda y mercado inmobiliario (Fannie/Freddie Mac, FHA/HUD)
- [x] sustrato/canada — Recursos naturales (NRCan, energía, minerales, bosques)
### Dominio (nuevos nodos)
- [x] dominio/emprendimiento — Emprendimiento
- [x] dominio/relaciones-publicas — Relaciones públicas (PR)
- [x] dominio/innovacion — Gestión de la innovación (ISO 56000)
- [x] dominio/experiencia-cliente — Customer experience (CX)
- [x] dominio/comercio-internacional — Comercio internacional
### Rol (nuevos nodos)
- [x] rol/product-manager — Product Manager (PM)
- [x] rol/financial-analyst — Financial Analyst
- [x] rol/head-of-growth — Head of Growth
- [x] rol/vp-marketing — VP of Marketing
- [x] rol/tech-lead — Tech Lead

### [2026-07-11] Round 9 — ITER 124 | gap_analysis extendido + 13 ingests (3 capas)
- gap_analysis.py (iter 123) = 0 huecos reales, 0 nodos nuevos → se **EXTENDIÓ** `scripts/gap_analysis.py`
  (Round 9) con 3 deepenings sustrato NA (mexico→pensiones-afore, estados-unidos→vivienda-real-estate,
  canada→recursos-naturales) + 10 nodos nuevos (dominio: emprendimiento, relaciones-publicas, innovacion,
  experiencia-cliente, comercio-internacional; rol: product-manager, financial-analyst, head-of-growth,
  vp-marketing, tech-lead). ALCANCE respetado: sustrato = solo Norteamérica; NO se agregan países fuera de NA.
- 13 temas ingestados cubriendo las 3 capas:
  - [sustrato] `sustrato/mexico/pensiones-afore.md`, `sustrato/estados-unidos/vivienda-real-estate.md`, `sustrato/canada/recursos-naturales.md` (deepening de nodos NA existentes).
  - [dominio] `dominio/emprendimiento/`, `dominio/relaciones-publicas/`, `dominio/innovacion/`, `dominio/experiencia-cliente/`, `dominio/comercio-internacional/` (5 nodos nuevos).
  - [rol] `rol/product-manager/`, `rol/financial-analyst/`, `rol/head-of-growth/`, `rol/vp-marketing/`, `rol/tech-lead/` (5 nodos nuevos).
- Reference-only (URL en frontmatter; sin raw/). Superstructura completa en cada nodo nuevo.
- **Round 9 COMPLETO (13/13 temas en 3 bucles: LOOP 1 sustrato, LOOP 2 dominio, LOOP 3 rol).** Cola Round 9 VACÍA.
  Siguiente paso: re-ejecutar `python3 scripts/gap_analysis.py`; devuelve 0 (taxonomía agotada) → ampliar
  taxonomía para Round 10 o PAUSAR el bucle hasta nueva dirección del usuario (alcance sustrato = solo Norteamérica).

## COLA ROUND 10 (gap_analysis.py iter 124 → taxonomía extendida en iter 125; sustrato solo NA)
### Sustrato (deepening nodos NA existentes)
- [ ] sustrato/mexico — Telecomunicaciones (IFT, sector telecom, banda ancha)
- [ ] sustrato/estados-unidos — Energía (DOE, FERC, grid, oil & gas, renovables)
- [ ] sustrato/canada — Comercio exterior (Global Affairs Canada, export, USMCA)
### Dominio (nuevos nodos)
- [ ] dominio/analitica-negocio — Analítica de negocio / Business Analytics / BI
- [ ] dominio/gobierno-corporativo — Gobierno corporativo (consejo, accionistas, fiduciario)
- [ ] dominio/ia-generativa — IA generativa (LLMs, adopción, gobernanza)
- [ ] dominio/cultura-organizacional — Cultura organizacional
- [ ] dominio/gestion-cambio — Gestión del cambio (ADKAR, Kotter)
### Rol (nuevos nodos)
- [ ] rol/controller — Controller (controlador financiero)
- [ ] rol/project-manager — Project Manager
- [ ] rol/data-analyst — Data Analyst
- [ ] rol/board-member — Board Member / Consejero
- [ ] rol/auditor-interno — Auditor Interno

### [2026-07-11] Round 10 — ITER 125 | gap_analysis extendido (taxonomía Round 10) + apertura de cola
- gap_analysis.py (post-Round 9) = 0 huecos reales, 0 nodos nuevos → se **EXTENDIÓ** `scripts/gap_analysis.py`
  (Round 10) con 3 deepenings sustrato NA (mexico→telecomunicaciones, estados-unidos→energia,
  canada→comercio-exterior) + 10 nodos nuevos (dominio: analitica-negocio, gobierno-corporativo,
  ia-generativa, cultura-organizacional, gestion-cambio; rol: controller, project-manager,
  data-analyst, board-member, auditor-interno). ALCANCE respetado: sustrato = solo Norteamérica.
- Abierta cola Round 10 (13 temas: sustrato x3, dominio x5, rol x5).
- **Próxima tarea (iter 126):** LOOP 1 (sustrato) — mexico/telecomunicaciones, estados-unidos/energia,
  canada/comercio-exterior.
