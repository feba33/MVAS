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
- **Plan:** Round 3 — gap_analysis.py (iter 85) reportó 25 huecos en nodos existentes
  + 2 nodos nuevos sugeridos (`dominio/juridico`, `dominio/estrategia`). Cola Round 3
  abierta con 29 temas (cubre las 3 capas; sustrato vía nuevo país Chile).
- **Iteración actual:** 89 (Round 3 — 4 bucles de ingest completados en esta corrida:
  sustrato/chile, dominio/finanzas derivados+mercados, rol PO+Scrum Master)
- **Temas completados:** 90 / 114 (85 previos + 5 de Round 3 ingestados en 4 bucles; restan 21 en cola)
- **Cronjob investigación:** `e273fdbbba14` (PAUSADO; bucle corrió aquí)
- **Siguiente paso (procedimiento):** ejecutar cola Round 3 (≥3 bucles por corrida).
  Próxima tarea (iter 90): dominio/finanzas — Finanzas corporativas (M&A, valoración, tesorería).

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

## COLA ROUND 3 (gap_analysis.py iter 85 + nuevos países)
### Sustrato (nuevo país)
- [x] sustrato/chile — Protección de datos (Ley 19.628 / Consejo Transparencia)
- [x] sustrato/chile — Impuestos y Aduanas (SII: IVA 19%, Renta, F29/F22)
### Dominio (nodos existentes — ampliar)
- [x] dominio/finanzas — Derivados (futuros, opciones, swaps)
- [x] dominio/finanzas — Mercados de capitales (IPO, emisión deuda)
- [ ] dominio/finanzas — Finanzas corporativas (M&A, valoración, tesorería)
- [ ] dominio/finanzas — Riesgo financiero
- [x] dominio/computacion — Arquitectura de software (microservicios, event-driven)
- [ ] dominio/computacion — Plataforma / DevOps / SRE
- [ ] dominio/computacion — Frontend (frameworks, performance)
- [x] dominio/computacion — Bases de datos (SQL, NoSQL, distribuidas)
- [ ] dominio/marketing — Demand generation / paid media
- [ ] dominio/marketing — Analítica de marketing (atribución)
- [ ] dominio/marketing — Lifecycle / email marketing
- [ ] dominio/leyes — Derecho societario / corporativo
- [ ] dominio/leyes — Derecho laboral (profundización)
- [ ] dominio/leyes — Cumplimiento / regulación
- [ ] dominio/contabilidad — Consolidación / reportes financieros
- [ ] dominio/contabilidad — Tesorería / flujo de efectivo
- [ ] dominio/diseno — Design systems / componentes
- [ ] dominio/diseno — UX writing / microcopy
### Dominio (nuevos nodos)
- [ ] dominio/juridico — Jurídico / legal interno de empresa (nuevo nodo)
- [ ] dominio/estrategia — Estrategia / OKRs / planeación (nuevo nodo)
### Rol (nuevos nodos)
- [x] rol/product-owner — Product Owner / PO
- [x] rol/scrum-master — Scrum Master
- [ ] rol/design-lead — Design Lead / UX Lead
- [ ] rol/marketing-manager — Marketing Manager
- [ ] rol/ops-lead — Operations Lead
- [ ] rol/support-lead — Support / CX Lead
- [ ] rol/reclutador — Recruiter / Talent Acquisition

