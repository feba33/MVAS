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
- **Iteración actual:** 137 — Round 13 COMPLETA (8/8). ITER 137 ingestó 5 nodos nuevos (dominio/gestion-riesgos + 4 roles: chief-revenue-officer, chief-communications-officer, chief-analytics-officer, head-of-innovation).
- **Temas completados:** 229 (Round 12 COMPLETA 13/13 + Round 13 COMPLETA 8/8).
- **Cronjob investigación:** `e273fdbbba14` (PAUSADO)
- **Iteración actual:** 145 — Round 15 COMPLETA (13/13: sustrato x3 + dominio x5 + rol x5). ITER 143 ingestó sustrato NA (medio-ambiente MX, política monetaria US/CA); ITER 144 ingestó 5 dominios nuevos; ITER 145 ingestó 5 roles nuevos.
- **Iteración actual:** 149 — Round 17 COMPLETA (13/13: sustrato NA x3 + dominio x5 + rol x5).
- **Temas completados (acumulado):** 367 (Rounds 15-23 COMPLETAS; 13 temas cada una).
- **Iteración actual:** 154 — Round 21 COMPLETA (13/13: sustrato NA x3 + dominio x5 + rol x5).
- **Round 20 COMPLETA** (iter 153, 13/13): gap_analysis.py = 0 huecos → extendida taxonomía con 3 deepenings sustrato NA (mexico→mineria, estados-unidos→seguridad-social, canada→medio-ambiente) + 10 nodos nuevos (dominio: aviacion, maritimo, seguridad-nacional, ciberdefensa, auditoria-gubernamental; rol: vp-product, chief-commercial-officer, chief-medical-officer, vp-operations, head-of-engineering). ALCANCE respetado (sustrato = solo Norteamérica).
- **Round 21 COMPLETA** (iter 154, 13/13): gap_analysis.py = 0 huecos → extendida taxonomía con 3 deepenings sustrato NA (mexico→finanzas-publicas, estados-unidos→finanzas-publicas, canada→finanzas-publicas) + 10 nodos nuevos (dominio: seguridad-alimentaria, derecho-penal, energia-nuclear, ciencias-materiales, derecho-ambiental; rol: ml-engineer, security-engineer, fp-and-a-manager, product-designer, account-manager). ALCANCE respetado (sustrato = solo Norteamérica).
- **Iteración actual:** 156 — Round 22 COMPLETA (13/13: sustrato NA x3 + dominio x5 + rol x5). ITER 155 ejecutó gap_analysis.py (=0 huecos) y extendió la taxonomía con 3 deepenings sustrato NA (mexico/estados-unidos/canada → propiedad-intelectual) + 10 nodos nuevos (dominio: arbitraje, tributacion-internacional, derecho-internacional, ingenieria, contabilidad-forense; rol: chairman, partner, staff-engineer, delivery-manager, engagement-manager). ITER 156 ingestó los 13 nodos.
- **Round 22 COMPLETA** (iter 156, 13/13): gap_analysis.py = 0 huecos → extendida taxonomía con 3 deepenings sustrato NA (mexico/estados-unidos/canada → propiedad-intelectual) + 10 nodos nuevos (dominio: arbitraje, tributacion-internacional, derecho-internacional, ingenieria, contabilidad-forense; rol: chairman, partner, staff-engineer, delivery-manager, engagement-manager). ALCANCE respetado (sustrato = solo Norteamérica).
- **Round 23 (iter 157):** COMPLETA (13/13) — gap_analysis extendido (3 deepenings NA + 10 nodos nuevos); cola Round 23 cerrada. ALCANCE respetado (sustrato = solo Norteamérica).
- **Round 18 COMPLETA** (iter 150, 13/13). **Round 19 COMPLETA** (iter 152, 13/13): gap_analysis.py = 0 huecos en taxonomía previa → extendida con 3 deepenings sustrato NA (mexico→turismo, estados-unidos→infraestructura, canada→energia) + 10 nodos nuevos (dominio: ciudades-inteligentes, healthtech, publicidad, franquicias, eventos; rol: legal-ops, head-of-facilities, head-of-public-affairs, sales-engineer, business-analyst). ALCANCE respetado (sustrato = solo Norteamérica).
- **Siguiente paso:** ejecutar Round 19 (13 ingests en 3 bucles: LOOP 1 sustrato NA, LOOP 2 dominio x5, LOOP 3 rol x5). Cron de investigación `e273fdbbba14` sigue PAUSADO.

## COLA DE TEMAS ([x] done / [ ] pending)
# COLA ROUND 12 (13 temas — reabastecimiento gap_analysis.py, Round 11 completa)
- [x] sustrato/mexico/sat — SAT / sistema tributario (ISR, IVA)
- [x] sustrato/estados-unidos/inmigracion — USCIS, H-1B, H-2A, green card
- [x] sustrato/canada/transporte — Transport Canada, ferrocarriles, aviación, puertos
- [x] dominio/alimentos-bebidas — F&B (industria, regulación, cadena, marca)
- [x] dominio/moda — Moda / apparel & retail fashion
- [x] dominio/espacio — Space economy (satélites, lanzamiento, downstream)
- [x] dominio/agua — Agua y saneamiento (infra, regulación, escasez)
- [x] dominio/semiconductores — Semiconductores / chips (fabs, diseño, CHIPS Act)
- [x] rol/chief-strategy-officer — CSO (estrategia corporativa)
- [x] rol/chief-privacy-officer — DPO (privacidad, GDPR, CPRA)
- [x] rol/chief-people-officer — CHRO (talento, cultura, RRHH)
- [x] rol/chief-client-officer — Chief Client Officer (CX, retención)
- [x] rol/head-of-operations — Head of Operations

# COLA ROUND 13 (8 temas — reabastecimiento gap_analysis.py, taxonomía ampliada)
### dominio/
- [x] dominio/farmaceutica — Industria farmacéutica (I+D, FDA/EMA, patentes, cadena frío)
- [x] dominio/quimica — Industria química (petroquímica, especialidades, REACH/TSCA)
- [x] dominio/calidad — Gestión de la calidad (ISO 9001, TQM, Six Sigma)
- [x] dominio/gestion-riesgos — ERM (ISO 31000, riesgo operativo, continuidad)
### rol/
- [x] rol/chief-revenue-officer — CRO (dueño del top-line, ventas+marketing+CS)
- [x] rol/chief-communications-officer — CCO (comms, reputación, PR)
- [x] rol/chief-analytics-officer — CAO (analítica y ciencia de datos)
- [x] rol/head-of-innovation — Head of Innovation (labs, corporate venturing)
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
- [x] sustrato/mexico — Telecomunicaciones (IFT, sector telecom, banda ancha)
- [x] sustrato/estados-unidos — Energía (DOE, FERC, grid, oil & gas, renovables)
- [x] sustrato/canada — Comercio exterior (Global Affairs Canada, export, USMCA)
### Dominio (nuevos nodos)
- [x] dominio/analitica-negocio — Analítica de negocio / Business Analytics / BI
- [x] dominio/gobierno-corporativo — Gobierno corporativo (consejo, accionistas, fiduciario)
- [x] dominio/ia-generativa — IA generativa (LLMs, adopción, gobernanza)
- [x] dominio/cultura-organizacional — Cultura organizacional
- [x] dominio/gestion-cambio — Gestión del cambio (ADKAR, Kotter)
### Rol (nuevos nodos)
- [x] rol/controller — Controller (controlador financiero)
- [x] rol/project-manager — Project Manager
- [x] rol/data-analyst — Data Analyst
- [x] rol/board-member — Board Member (consejero)
- [x] rol/auditor-interno — Auditor Interno

### [2026-07-11] Round 10 — ITER 125 | gap_analysis extendido (taxonomía Round 10) + apertura de cola
- gap_analysis.py (post-Round 9) = 0 huecos reales, 0 nodos nuevos → se **EXTENDIÓ** `scripts/gap_analysis.py`
  (Round 10) con 3 deepenings sustrato NA (mexico→telecomunicaciones, estados-unidos→energia,
  canada→comercio-exterior) + 10 nodos nuevos (dominio: analitica-negocio, gobierno-corporativo,
  ia-generativa, cultura-organizacional, gestion-cambio; rol: controller, project-manager,
  data-analyst, board-member, auditor-interno). ALCANCE respetado: sustrato = solo Norteamérica.
- Abierta cola Round 10 (13 temas: sustrato x3, dominio x5, rol x5).
- **Próxima tarea (iter 128):** LOOP 3 (rol) COMPLETO → Round 10 cola 13/13. Siguiente: ejecutar `scripts/gap_analysis.py`; si 0 huecos → extender taxonomía para Round 11 (iter 129).
  canada/comercio-exterior.

### [2026-07-11] Round 10 — ITER 128 | LOOP 3 (rol) — 5 ingests (nuevos nodos)
- 5 nodos `rol/` creados con superstructura completa (README, index, log, raw/):
  - `rol/controller/` — Controlador financiero: reporting, cierre mensual, GAAP, controles, SOX, CPA/CMA.
  - `rol/project-manager/` — Gestor de proyectos: alcance, equipo, riesgos, stakeholders; ciclo de vida; PMP/PMBOK; agile/scrum.
  - `rol/data-analyst/` — Analista de datos: SQL, dashboards, data storytelling; diferenciación de data scientist/engineer.
  - `rol/board-member/` — Miembro de la Junta: órgano rector, elegido por accionistas, deberes fiduciarios, comités.
  - `rol/auditor-interno/` — Auditor interno: aseguramiento independiente, tres líneas, COSO, normas IIA.
- Reference-only (URL en frontmatter; sin raw/). Cross-refs a contabilidad, gobierno-corporativo, cfo, ceo, chief-risk-officer, analitica-negocio, gestion-cambio.
- **Próxima tarea (iter 129):** Ejecutar `scripts/gap_analysis.py`. Si 0 huecos → extender taxonomía (deepenings sustrato NA + nuevos nodos dominio/rol) para Round 11 y abrir cola.
  canada/comercio-exterior.

### [2026-07-11] Round 11 — ITER 129 | gap_analysis extendido (taxonomía Round 11) + apertura de cola
- gap_analysis.py (post-Round 10) = 0 huecos, 0 nodos nuevos → se **EXTENDIÓ** `scripts/gap_analysis.py` con 14 temas para Round 11:
  - sustrato NA deepening (4): mexico/inversion-extranjera, mexico/sector-manufacturero, estados-unidos/agricultura, canada/inmigracion.
  - dominio nuevos (5): banca, capital-riesgo, cadena-suministro, consultoria, servicios-profesionales.
  - rol nuevos (5): chief-compliance-officer, treasurer, chief-investment-officer, head-of-research, chief-digital-officer.
- ALCANCE respetado: sustrato = solo Norteamérica (sin nuevos países).
- Abierta cola Round 11 (14 temas: sustrato x4, dominio x5, rol x5).
- **Próxima tarea (iter 130):** LOOP 1 (sustrato NA deepening) — inversion-extranjera, sector-manufacturero, agricultura, inmigracion (iter 130).
### [2026-07-11] Round 11 — ITER 130 | LOOP 1 (sustrato NA) — 3 ingests (iter 130)
- 3 temas sustrato (deepening de nodos NA existentes), cubriendo sustrato México (x2) + EE.UU. (x1):
  - `sustrato/mexico/inversion-extranjera.md` — IED en México: LIE (sectores reservados, RNIE), IMMEX (importación temporal sin IGI/IVA), >USD$40B IED 3T2025, maquila, Shelter.
  - `sustrato/mexico/sector-manufacturero.md` — Manufactura MX: maquiladora/IMMEX, >USD$300B exportados 2024, clústeres (auto/aero/electrónica/médica), nearshoring, USMCA.
  - `sustrato/estados-unidos/agricultura.md` — USDA, Farm Bill, subsidios/price supports/loan programs, 2.04M granjas, exportador neto.
- Reference-only (URL en frontmatter; sin raw/). Alcance respetado: sustrato = solo Norteamérica (los 3 temas son NA).
- **Próxima tarea (iter 131):** sustrato/canada/inmigracion (IRCC, permisos de trabajo) — cierra LOOP 1 sustrato (4/4); luego LOOP 2 dominio (banca, capital-riesgo, cadena-suministro, consultoria, servicios-profesionales). Restan 11 temas Round 11.

### [2026-07-11] Round 11 — ITER 131 | LOOP 1 (sustrato NA) cierra + LOOP 2 (dominio) + LOOP 3 (rol) — 11 ingests
- 11 temas ingestados cubriendo las 3 capas (**Round 11 COMPLETA, 14/14**):
  - [sustrato] `sustrato/canada/inmigracion.md` (deepening nodo NA existente): IRCC/IRPA, Express Entry (CRS), PNP, TFWP (LMIA/ESDC), IMP, study permits, PGWP, doble ciudadanía. Cierra LOOP 1 sustrato (4/4).
  - [dominio] `dominio/banca/`, `dominio/capital-riesgo/`, `dominio/cadena-suministro/`, `dominio/consultoria/`, `dominio/servicios-profesionales/` (5 nodos nuevos, superstructura completa).
  - [rol] `rol/chief-compliance-officer/`, `rol/treasurer/`, `rol/chief-investment-officer/`, `rol/head-of-research/`, `rol/chief-digital-officer/` (5 nodos nuevos, superstructura completa).
- Reference-only (URL en frontmatter; sin raw/). Alcance respetado: sustrato = solo Norteamérica (los 11 temas son NA o generales).
- **Round 11 COMPLETA (14/14 temas en 3 bucles: LOOP 1 sustrato NA, LOOP 2 dominio x5, LOOP 3 rol x5).** Cola Round 11 VACÍA → reabastecimiento: ejecutar `python3 scripts/gap_analysis.py` para abrir Round 12.

### [2026-07-11] Reabastecimiento — Round 12 ABIERTA (gap_analysis.py extendida)
- gap_analysis.py post-Round 11 = 0 (taxonomía agotada) → extendida la taxonomía para Round 12:
  - TAXONOMY: +`sustrato/mexico/sat`, +`sustrato/estados-unidos/inmigracion`, +`sustrato/canada/transporte` (3 deepenings NA). Nota: `sustrato/canada/impuestos` ya existía (creada en run `inga`), así que no genera gap nuevo (no se duplicó).
  - NEW_NODES (Round 12): +5 `dominio/` (alimentos-bebidas, moda, espacio, agua, semiconductores) +5 `rol/` (chief-strategy-officer, chief-privacy-officer, chief-people-officer, chief-client-officer, head-of-operations).
- Verificado: gap_analysis.py ahora reporta 3 sustrato + 10 nodos nuevos = **13 huecos**. Cola Round 12 ABIERTA (13 temas). ALCANCE sustrato = solo Norteamérica.
- Próxima tarea (iter 132): sustrato/mexico/sat (Sistema tributario mexicano) — abre LOOP 1 sustrato NA de Round 12.

### [2026-07-12] Round 12 — ITER 132 | sustrato/mexico SAT (LOOP 1) — 1 ingest
- 1 tema sustrato (deepening de nodo NA existente): `sustrato/mexico/sat.md` — SAT (Servicio de Administración Tributaria): órgano desconcentrado de la SHCP (Ley del SAT, 1997), máxima autoridad fiscal; administra RFC, CFF, CFDI 4.0 (e.firma, CIEC, Buzón Tributario, Mi Contabilidad); recauda ISR/IVA/IEPS/aranceles y cuotas IMSS-ISSSTE; carga tributaria baja (~13-14% PIB). Complementa `regimen-fiscal.md`. Reference-only (URL en frontmatter; sin raw/).
- **Round 12 LOOP 1 sustrato NA (1/3):** mexico/sat hecho; restan estados-unidos/inmigracion y canada/transporte. Próxima tarea (iter 133): sustrato/estados-unidos/inmigracion.
- **Próxima tarea (iter 133):** sustrato/estados-unidos/inmigracion (USCIS, H-1B, H-2A, green card).

### [2026-07-12] Round 12 — ITER 133 | sustrato/estados-unidos inmigración (LOOP 1) — 1 ingest
- 1 tema sustrato (deepening de nodo NA existente): `sustrato/estados-unidos/inmigracion.md` — USCIS (DHS, sucesora del INS 2002; ICE/CBP), green card/LPR (~12.8M 2024, ~9M a ciudadanía; vías familia/empleo/diversity/refugiado; ajuste de estatus o consular; ciudadanía 1-5 años); H-1B (specialty occupation, cap 85k, patrocinio, dual intent, lottery); H-2A (agrícola temporal, sin cap, empleador paga vivienda/comida/transporte, DOL audita); VWP (42 países, ESTA). Reference-only (URL en frontmatter; sin raw/).
- **Round 12 LOOP 1 sustrato NA (2/3):** estados-unidos/inmigracion hecho; resta canada/transporte. Próxima tarea (iter 134): sustrato/canada/transporte.

### [2026-07-12] Round 12 — ITER 134 | sustrato/canada transporte (LOOP 1) — 1 ingest
- 1 tema sustrato (deepening de nodo NA existente): `sustrato/canada/transporte.md` — Transport Canada (depto federal carretera/ferrocarril/marítimo/aéreo; reorg 1994 privatizó CN y descentralizó puertos/aeropuertos); ferrocarril 49,422 km (129 km eléctricos), dos Class I (CN, CPKC — única CA-US-MX), Via Rail (corona) pasajeros; Port of Vancouver (mayor de Canadá, 4º NA, 170+ economías); aviación civil por TC, ATC por NAV CANADA. Reference-only (URL en frontmatter; sin raw/).
- **Round 12 LOOP 1 sustrato NA COMPLETO (3/3).** Restan 10 temas Round 12 (dominio x5, rol x5). Próxima tarea (iter 135): dominio/alimentos-bebidas (LOOP 2 dominio).

### [2026-07-12] Round 12 — ITER 135 | LOOP 2 (dominio x5) + LOOP 3 (rol x5) — 10 ingests
- 10 temas ingestados cubriendo dominio (x5) + rol (x5). **Round 12 COMPLETA (13/13)**. Cola Round 12 VACÍA.
  - [dominio] `dominio/alimentos-bebidas/` (F&B: cadena, FSMA/HACCP, mercado), `dominio/moda/` (apparel, ~USD 1.44T 2026), `dominio/espacio/` (space economy: upstream/downstream), `dominio/agua/` (utilities, escasez), `dominio/semiconductores/` (chips: fabless/foundry/CHIPS Act).
  - [rol] `rol/chief-strategy-officer/` (CSO), `rol/chief-privacy-officer/` (CPO privacidad, vs DPO), `rol/chief-people-officer/` (CPO/CHRO), `rol/chief-client-officer/` (CCO, CX/retención), `rol/head-of-operations/` (Ops).
- Reference-only (URL en frontmatter; sin raw/). Superstructura completa en cada nodo nuevo. Alcance sustrato respetado (Round 12 no agregó países; LOOP 1 fueron deepenings NA).
- **Siguiente paso (iter 136 / Round 13):** reabastecimiento — ejecutar `python3 scripts/gap_analysis.py`; si 0 huecos, extender taxonomía y abrir cola Round 13.

### [2026-07-12] Round 12 — ITER 135b | Reabastecimiento → Round 13 (plan)
- Cola Round 12 VACÍA. `gap_analysis.py` devolvió 0 huecos en nodos existentes → se amplió la taxonomía (NEW_NODES Round 13) con 8 nodos nuevos: 4 dominio (farmaceutica, quimica, calidad, gestion-riesgos) + 4 rol (chief-revenue-officer, chief-communications-officer, chief-analytics-officer, head-of-innovation). Alcance respetado (sustrato = solo NA; los deepenings sustrato/educacion se filtran por ALLOWED_SUSTRATO y ya cubren vía TAXONOMY).
- Se abrió **COLA ROUND 13 (8 temas)** en working.md (pendientes). Próxima tarea (iter 136): dominio/farmaceutica.

### [2026-07-12] Round 13 — ITER 136 | dominio x3 (farmaceutica, quimica, calidad) — 3 nodos nuevos
- gap_analysis.py (post-Round 12) = 0 → taxonomía Round 13 ya abierta en iter 135b. Ejecutada la ingest de 3 nodos `dominio/` nuevos:
  - `dominio/farmaceutica/` — Industria farmacéutica: I+D/desarrollo (FDA/EMA; 10-15 años, USD 1.3-2.6B, 7-12% aprobación), patentes/Hatch-Waxman, genéricos/biosimilares, cadena de frío, CDMO.
  - `dominio/quimica/` — Industria química: petroquímica/commodities, especialidades, fine chemicals/API; REACH (UE, precautorio) vs TSCA (EE.UU., Lautenberg 2016); ESG/química verde.
  - `dominio/calidad/` — Gestión de la calidad: ISO 9001:2015, TQM, Six Sigma (DMAIC), Lean; herramientas (PDCA, FMEA, SPC, Pareto); GMP en industrias reguladas.
- Reference-only (URL en frontmatter; sin raw/). Superstructura completa en cada nodo. Alcance sustrato respetado (solo NA; los 3 temas son dominio).
- **Round 13 (3/8).** Cola restante: dominio/gestion-riesgos + rol x4. Próxima tarea (iter 137): dominio/gestion-riesgos.

### [2026-07-12] Round 13 — ITER 137 | 5 nodos nuevos (1 dominio + 4 rol) — CIERRA ROUND 13
- gap_analysis.py (post-Round 12) = 0 → taxonomía Round 13 ya abierta en iter 135b. Ejecutada la ingest de 5 nodos nuevos cubriendo dominio + rol:
  - `dominio/gestion-riesgos/` — ERM: ISO 31000, COSO 2017, categorías de riesgo, riesgo operativo, continuidad/resiliencia.
  - `rol/chief-revenue-officer/` — CRO: dueño de todos los ingresos (ventas+marketing+CS), RevOps; reporta a CEO; vs CFO/CMO.
  - `rol/chief-communications-officer/` — CCO: comunicaciones, PR, reputación, asesor del CEO (Arthur Page Society).
  - `rol/chief-analytics-officer/` — CAO: analítica y aporte a decisiones operativas; vs CIO/CDO.
  - `rol/head-of-innovation/` — Head of Innovation: gestión de innovación, labs, corporate venturing, ISO 56000.
- Reference-only (URL en frontmatter; sin raw/). Superstructura completa en cada nodo. Alcance sustrato respetado (Round 13 no agregó países; los 5 temas son dominio/rol generales).
- **Round 13 COMPLETA (8/8 temas: dominio x4 + rol x4).** Cola Round 13 VACÍA → reabastecimiento (gap_analysis.py) para Round 14.

### [2026-07-12] Round 14 — ITER 138 | gap_analysis extendido (taxonomía Round 14) + apertura de cola
- gap_analysis.py (post-Round 13) = 0 huecos, 0 nodos nuevos → se **EXTENDIÓ** `scripts/gap_analysis.py`
  (Round 14) con 3 deepenings sustrato NA (mexico/estados-unidos/canada → educacion) + 10 nodos nuevos
  (dominio: blockchain, etica-ia, pricing, geopolitica, inteligencia-competitiva; rol: program-manager,
  solutions-architect, investor-relations, regulatory-affairs, actuario). ALCANCE respetado: sustrato = solo Norteamérica.
- Abierta cola Round 14 (13 temas: sustrato x3, dominio x5, rol x5).
- **Próxima tarea (iter 139+):** LOOP 1 (sustrato NA educación) — sustrato/mexico/educacion.md, sustrato/estados-unidos/educacion.md, sustrato/canada/educacion.md.

### [2026-07-12] Round 14 — ITER 139 | LOOP 1 (sustrato NA) — 3 ingests (educación mx/us/ca)
- 3 temas sustrato (deepening de nodos NA existentes): `sustrato/mexico/educacion.md`, `sustrato/estados-unidos/educacion.md`, `sustrato/canada/educacion.md` (sistemas educativos de Norteamérica: SEP / Dept of Ed federal + estados / competencia provincial; K-12, superior, bilingüe FR/EN). Cola Round 14: 3/13.
- **Próxima tarea (iter 140):** LOOP 2 (dominio x5 nuevos): blockchain, etica-ia, pricing, geopolitica, inteligencia-competitiva.

### [2026-07-12] Round 14 — ITER 140 | LOOP 2 (dominio x5) — 5 ingests (blockchain, etica-ia, pricing, geopolitica, inteligencia-competitiva)
- 5 temas dominio (nuevos nodos): `dominio/blockchain/`, `dominio/etica-ia/`, `dominio/pricing/`, `dominio/geopolitica/`, `dominio/inteligencia-competitiva/` (cada uno con superstructura: raw/, index.md, log.md, README.md, <slug>.md). Cola Round 14: 8/13.
- **Próxima tarea (iter 141):** LOOP 3 (rol x5 nuevos): program-manager, solutions-architect, investor-relations, regulatory-affairs, actuario.

### [2026-07-12] Round 14 — ITER 141 | LOOP 3 (rol x5) — 5 ingests (program-manager, solutions-architect, investor-relations, regulatory-affairs, actuario)
- 5 temas rol (nuevos nodos): `rol/program-manager/`, `rol/solutions-architect/`, `rol/investor-relations/`, `rol/regulatory-affairs/`, `rol/actuario/` (cada uno con superstructura: raw/, index.md, log.md, README.md, <slug>.md).
- **ROUND 14 COMPLETA (13/13):** sustrato x3 (educación NA) + dominio x5 + rol x5. Cola Round 14 vacía.
- **Próximo paso:** ejecutar `python3 scripts/gap_analysis.py` → se esperan 0 gaps; si hay nuevos, abrir Round 15. El cron de investigación `e273fdbbba14` sigue PAUSADO.

### [2026-07-12] Round 15 — ITER 142 | gap_analysis extendido (taxonomía Round 15) + apertura de cola
- gap_analysis.py (post-Round 14) = 0 huecos, 0 nodos nuevos → se **EXTENDIÓ** `scripts/gap_analysis.py`
  (Round 15) con 3 deepenings sustrato NA (mexico→medio-ambiente, estados-unidos→politica-monetaria,
  canada→politica-monetaria) + 10 nodos nuevos (dominio: automatizacion, insurtech, legaltech, crowdfunding,
  iot; rol: enterprise-architect, head-of-corporate-development, chief-procurement-officer, head-of-tax,
  chief-diversity-officer). ALCANCE respetado: sustrato = solo Norteamérica.
- Re-ejecutado → 13 sugerencias (3 sustrato + 10 nuevos). Abierta cola Round 15 (13 temas).
- **Próxima tarea (iter 143+):** LOOP 1 (sustrato NA) — medio-ambiente MX, política monetaria US, política monetaria CA.

### [2026-07-12] Round 15 — ITER 143-145 | 13 ingests (3 loops: sustrato + dominio + rol)
- ITER 143 (LOOP 1, sustrato NA): 3 deepenings en nodos existentes:
  - `sustrato/mexico/medio-ambiente.md` — SEMARNAT, LGEEPA, cambio climático, ESG, economía circular.
  - `sustrato/estados-unidos/politica-monetaria.md` — Federal Reserve, FOMC, tasa de fondos federales, dual mandate.
  - `sustrato/canada/politica-monetaria.md` — Bank of Canada, tasa de política, inflation targeting 2%.
- ITER 144 (LOOP 2, dominio): 5 nodos nuevos con superstructura completa: `automatizacion`, `insurtech`, `legaltech`, `crowdfunding`, `iot`.
- ITER 145 (LOOP 3, rol): 5 nodos nuevos con superstructura completa: `enterprise-architect`, `head-of-corporate-development`, `chief-procurement-officer`, `head-of-tax`, `chief-diversity-officer`.
- **Round 15 COMPLETA (13/13: sustrato x3 + dominio x5 + rol x5).** Reference-only (Wikipedia EN + fuentes oficiales gob/SAT/BoC/Fed; sin raw/).
- Próxima tarea (iter 146+): ejecutar `python3 scripts/gap_analysis.py` → 0 gaps esperados; si hay huecos, abrir Round 16.

### [2026-07-12] Round 16 — ITER 146 | gap_analysis extendido (taxonomía Round 16) + apertura de cola
- gap_analysis.py (post-Round 15) = 0 huecos, 0 nodos nuevos → se **EXTENDIÓ** `scripts/gap_analysis.py`
  (Round 16) con 3 deepenings sustrato NA (mexico→seguridad-social, estados-unidos→labor, canada→labor)
  + 10 nodos nuevos (dominio: cloud-computing, robotica, realidad-extendida, infraestructura, seguridad-corporativa;
  rol: chief-security-officer, chief-learning-officer, chief-quality-officer, head-of-partnerships, chief-experience-officer).
  ALCANCE respetado: sustrato = solo Norteamérica.
- Re-ejecutado → 13 sugerencias (3 sustrato + 10 nuevos). Abierta cola Round 16 (13 temas).
- **Próxima tarea (iter 147+):** LOOP 1 (sustrato NA deepening) — sustrato/mexico/seguridad-social.md, sustrato/estados-unidos/labor.md, sustrato/canada/labor.md.

### [2026-07-12] Round 16 — ITER 147 | COMPLETA (13/13: sustrato NA x3 + dominio x5 + rol x5)
- LOOP 1 (sustrato NA): `sustrato/mexico/seguridad-social.md` (IMSS/ISSSTE), `sustrato/estados-unidos/labor.md` (DOL/FLSA/OSHA/NLRB), `sustrato/canada/labor.md` (Labour Code/ESDC) — 3 páginas en nodos existentes + index/log nodos + raíz.
- LOOP 2 (dominio): 5 nodos nuevos (superstructura completa: README/index/log/raw/.gitkeep + página) — `cloud-computing`, `robotica`, `realidad-extendida`, `infraestructura`, `seguridad-corporativa`.
- LOOP 3 (rol): 5 nodos nuevos — `chief-security-officer` (CSO), `chief-learning-officer` (CLO), `chief-quality-officer` (CQO), `head-of-partnerships`, `chief-experience-officer` (CXO).
- Reference-only (Wikipedia EN + fuentes oficiales gob/SAT/BoC/Fed/ASIS/ATD/ASQ; sin raw/). Total ingest Round 16 = 13 (3 págs sustrato + 10 nodos nuevos).
- **Próxima tarea (iter 148+):** re-ejecutar `python3 scripts/gap_analysis.py` → 0 gaps; si 0, Round 16 cierra el reabastecimiento → ampliar taxonomía (Round 17) o pausar. Alcance sustrato sigue = solo Norteamérica.

### [2026-07-12] Round 17 — ITER 148 | gap_analysis extendido (taxonomía Round 17) + apertura de cola
- gap_analysis.py (post-Round 16) = 0 huecos, 0 nodos nuevos → se **EXTENDIÓ** `scripts/gap_analysis.py`
  (Round 17) con 3 deepenings sustrato NA (mexico→transporte, estados-unidos→defensa, canada→seguridad-social)
  + 10 nodos nuevos (dominio: redes-sociales, deportes, entretenimiento, juegos-videojuegos, economia-circular;
  rol: chief-ai-officer, chief-design-officer, chief-transformation-officer, chief-ethics-officer,
  chief-knowledge-officer). ALCANCE respetado: sustrato = solo Norteamérica.
- Re-ejecutado → 13 sugerencias (3 sustrato + 10 nuevos). Abierta cola Round 17 (13 temas).
- **Próxima tarea (iter 149+):** LOOP 1 (sustrato NA) — mexico/transporte, estados-unidos/defensa, canada/seguridad-social.

## COLA ROUND 14 (CERRADA — 13/13 COMPLETA)
- Todos los temas [x]. Reabastecimiento post-Round 13 finalizado.

## COLA ROUND 15 (gap_analysis.py iter 142 → taxonomía extendida; sustrato solo NA) — COMPLETA 13/13
### Sustrato (deepening nodos NA existentes)
- [x] sustrato/mexico — Medio ambiente (SEMARNAT, LGEEPA, cambio climático, ESG México) — done iter 143
- [x] sustrato/estados-unidos — Política monetaria (Federal Reserve, FOMC, tasa de fondos federales) — done iter 143
- [x] sustrato/canada — Política monetaria (Bank of Canada, tasa de política, inflation targeting) — done iter 143
### Dominio (nuevos nodos)
- [x] dominio/automatizacion — Automatización / RPA / hyperautomation / IA agentes — done iter 144
- [x] dominio/insurtech — Insurtech (modelos, telematics, IA en seguros) — done iter 144
- [x] dominio/legaltech — Legaltech (CLM, e-discovery, IA legal) — done iter 144
- [x] dominio/crowdfunding — Crowdfunding (reward/equity/debt, regulación) — done iter 144
- [x] dominio/iot — Internet de las Cosas (IIoT, edge, seguridad) — done iter 144
### Rol (nuevos nodos)
- [x] rol/enterprise-architect — Enterprise Architect (TOGAF, arquitectura empresarial) — done iter 145
- [x] rol/head-of-corporate-development — Corp Dev (M&A, asignación de capital) — done iter 145
- [x] rol/chief-procurement-officer — CPO (sourcing, supplier management) — done iter 145
- [x] rol/head-of-tax — Head of Tax / Tax Director (estrategia fiscal, transfer pricing) — done iter 145
- [x] rol/chief-diversity-officer — CDO Diversity (DEI, equidad, inclusión) — done iter 145

## COLA ROUND 16 (gap_analysis.py iter 146 → taxonomía extendida; sustrato solo NA)
### Sustrato (deepening nodos NA existentes)
- [x] sustrato/mexico — Seguridad social (IMSS, ISSSTE, seguro social, salud/pensiones laborales)
- [x] sustrato/estados-unidos — Trabajo / laboral (DOL, FLSA, OSHA, NLRB, sindicatos)
- [x] sustrato/canada — Trabajo / laboral (Labour Code federal, ESDC, estándares provinciales)
### Dominio (nuevos nodos)
- [x] dominio/cloud-computing — Cloud computing (IaaS/PaaS/SaaS, hyperscalers, IaC, FinOps)
- [x] dominio/robotica — Robótica (industrial, colaborativa, logística, móvil)
- [x] dominio/realidad-extendida — XR (VR/AR/MR, metaverso, casos industriales)
- [x] dominio/infraestructura — Infraestructura (concesiones, APP/PPP, transporte, energética)
- [x] dominio/seguridad-corporativa — Seguridad corporativa (física, crisis, resiliencia, continuidad)
### Rol (nuevos nodos)
- [x] rol/chief-security-officer — CSO (seguridad corporativa/física, crisis, resiliencia)
- [x] rol/chief-learning-officer — CLO (L&D, desarrollo de talento, upskilling)
- [x] rol/chief-quality-officer — CQO (calidad, excelencia operativa, mejora continua)
- [x] rol/head-of-partnerships — Head of Partnerships (alianzas estratégicas, canales, co-ventures)
- [x] rol/chief-experience-officer — CXO (experiencia de cliente + empleado + marca)

## COLA ROUND 17 (gap_analysis.py iter 148 → taxonomía extendida; sustrato solo NA) — COMPLETA 13/13
### Sustrato (deepening nodos NA existentes)
- [x] sustrato/mexico — Transporte e infraestructura (SICT, carreteras, puertos, aeropuertos, fronteras) — done iter 149
- [x] sustrato/estados-unidos — Defensa / Department of Defense (Pentagon, presupuesto FY2025, industria de defensa) — done iter 149
- [x] sustrato/canada — Seguridad social (CPP, OAS, EI, Canada Health Transfer) — done iter 149
### Dominio (nuevos nodos)
- [x] dominio/redes-sociales — Redes sociales (plataformas, algoritmos, monetización, regulación, marketing) — done iter 149
- [x] dominio/deportes — Industria del deporte (derechos de medios, patrocinios, ligas, mercado global, eSports) — done iter 149
- [x] dominio/entretenimiento — Entretenimiento (filmed entertainment, streaming, música, industrias creativas) — done iter 149
- [x] dominio/juegos-videojuegos — Videojuegos / eSports (consolas, mobile, PC, modelos de monetización) — done iter 149
- [x] dominio/economia-circular — Economía circular (modelos de negocio circulares, reciclaje, diseño para circularidad, residuos) — done iter 149
### Rol (nuevos nodos)
- [x] rol/chief-ai-officer — CAIO (Chief AI Officer) — done iter 149
- [x] rol/chief-design-officer — Chief Design Officer — done iter 149
- [x] rol/chief-transformation-officer — Chief Transformation Officer — done iter 149
- [x] rol/chief-ethics-officer — Chief Ethics Officer / Chief Integrity Officer — done iter 149
- [x] rol/chief-knowledge-officer — CKO (Chief Knowledge Officer) — done iter 149

### [2026-07-12] Round 17 — ITER 149 | COMPLETA (13/13: sustrato NA x3 + dominio x5 + rol x5)
- LOOP 1 (sustrato NA): 3 páginas en nodos existentes (index/log nodos + raíz actualizados):
  - `sustrato/mexico/transporte.md` — SICT (antes SCT); carreteras ~377k km; APIs (Manzanillo/Lázaro Cárdenas/Veracruz); CPKC (única CA-US-MX); AICM/AIFA; ~28 cruces fronterizos.
  - `sustrato/estados-unidos/defensa.md` — DoD (1947/Pentágono), presupuesto FY2025 ~USD 849.8B, primes (Lockheed/RTX/Boeing/Northrop/GD/L3Harris), DARPA, FMS, Goldwater-Nichols.
  - `sustrato/canada/seguridad-social.md` — CPP (contributivo ~5.95%), OAS (residencial ~$727-800/mes + GIS), EI (~55% hasta 45 sem), Canada Health Transfer.
- LOOP 2 (dominio): 5 nodos nuevos con superstructura completa (README/index/log/raw/README + página): `redes-sociales`, `deportes`, `entretenimiento`, `juegos-videojuegos`, `economia-circular`.
- LOOP 3 (rol): 5 nodos nuevos con superstructura completa: `chief-ai-officer` (CAIO), `chief-design-officer` (CDO design), `chief-transformation-officer`, `chief-ethics-officer`, `chief-knowledge-officer` (CKO).
- Reference-only (Wikipedia EN + fuentes oficiales gob/SICT/DoD Comptroller/Canada.ca/Statista; sin raw/). Alcance sustrato = solo Norteamérica (respetado).
- **Round 17 COMPLETA (13/13).** Cola Round 17 VACÍA.

## COLA ROUND 18 (gap_analysis.py iter 150 → taxonomía extendida; sustrato solo NA) — COMPLETA 13/13
### Sustrato (deepening nodos NA existentes)
- [x] sustrato/mexico — Agricultura (SADER, producción agroalimentaria, seguridad alimentaria, T-MEC, riego, exportaciones) — done iter 150
- [x] sustrato/estados-unidos — Comercio exterior (USTR, Sección 301, aranceles, acuerdos comerciales, nearshoring) — done iter 150
- [x] sustrato/canada — Telecomunicaciones (CRTC, espectro, banda ancha, Bell/Rogers/Telus, 5G) — done iter 150
### Dominio (nuevos nodos)
- [x] dominio/energias-renovables — Energías renovables (solar, eólica, almacenamiento, hidrógeno verde, descarbonización)
- [x] dominio/finanzas-publicas — Finanzas públicas (presupuesto, deuda soberana, política fiscal, multilaterales)
- [x] dominio/economia-digital — Economía digital (plataformas, mercados de dos lados, gig economy, CBDC)
- [x] dominio/gobierno-de-datos — Gobierno de datos (DAMA/DCAM, calidad, linaje, privacidad by design)
- [x] dominio/propiedad-intelectual — Propiedad intelectual (patentes, marcas, derechos de autor, licencias)
### Rol (nuevos nodos)
- [x] rol/head-of-revops — Head of RevOps (RevOps, alinear ventas+marketing+CS)
- [x] rol/chief-content-officer — Chief Content Officer (contenido, editorial, narrativa)
- [x] rol/head-of-sales-enablement — Head of Sales Enablement (capacitación, playbooks)
- [x] rol/head-of-people-analytics — Head of People Analytics (attrition, engagement, DEI)
- [x] rol/chief-pricing-officer — Chief Pricing Officer (estrategia de precios, elasticidad)

### [2026-07-12] Round 18 — ITER 150 | COMPLETA (13/13: sustrato NA x3 + dominio x5 + rol x5)
- LOOP 1 (sustrato NA): 3 páginas en nodos existentes (index/log nodos + raíz actualizados):
  - `sustrato/mexico/agricultura.md` — SADER; potencia agroalimentaria (maíz, aguacate, tomate, berries, tequila, cerveza); USMCA/T-MEC, 14+ TLC; riego/sequía; autosuficiencia alimentaria.
  - `sustrato/estados-unidos/comercio-exterior.md` — USTR; USMCA, Sección 301 (China), Sección 232 (acero/aluminio), aranceles, OMC.
  - `sustrato/canada/telecomunicaciones.md` — CRTC; Big 3 (Bell/Rogers/Telus); espectro, 5G, ISED.
- LOOP 2 (dominio): 5 nodos nuevos con superstructura completa: `energias-renovables`, `finanzas-publicas`, `economia-digital`, `gobierno-de-datos`, `propiedad-intelectual`.
- LOOP 3 (rol): 5 nodos nuevos con superstructura completa: `head-of-revops`, `chief-content-officer`, `head-of-sales-enablement`, `head-of-people-analytics`, `chief-pricing-officer`.
- Reference-only (Wikipedia EN + fuentes oficiales gob/SADER/USTR/CRTC; sin raw/). Alcance sustrato = solo Norteamérica (respetado).
- **Round 18 COMPLETA (13/13).** Cola Round 18 VACÍA.
- **Próxima tarea (iter 151+):** reabastecimiento → ejecutar `python3 scripts/gap_analysis.py`; se esperan 0 gaps (Round 18 ya cubrió la taxonomía extendida). Si 0, el bucle de enriquecimiento llega a estado estable (taxonomía agotada para el alcance actual de Norteamérica). Opciones: (a) PAUSAR hasta nueva dirección del usuario o (b) ampliar taxonomía para Round 19 (nuevos dominios/roles/países NA). Cron de investigación `e273fdbbba14` sigue PAUSADO salvo que el usuario lo reanude.

## COLA ROUND 14 (gap_analysis.py iter 138 → taxonomía extendida; sustrato solo NA)
### Sustrato (deepening nodos NA existentes)
- [x] sustrato/mexico — Educación (SEP, sistema educativo, educación superior) — done iter 139
- [x] sustrato/estados-unidos — Educación (Dept of Education, K-12, higher ed, FAFSA) — done iter 139
- [x] sustrato/canada — Educación (provincias, PSE, student aid, bilingüe) — done iter 139
### Dominio (nuevos nodos)
- [x] dominio/blockchain — Blockchain & web3 (consenso, smart contracts, DAOs, tokens) — done iter 140
- [x] dominio/etica-ia — Ética de la IA / IA responsable (fairness, sesgo, EU AI Act) — done iter 140
- [x] dominio/pricing — Pricing (estrategias, elasticidad, dynamic pricing) — done iter 140
- [x] dominio/geopolitica — Geopolítica/geoeconomía (sanciones, bloques, supply chain) — done iter 140
- [x] dominio/inteligencia-competitiva — Inteligencia competitiva (CI process, fuentes, ética) — done iter 140
### Rol (nuevos nodos)
- [x] rol/program-manager — Program Manager (PMO, portafolio) — done iter 141
- [x] rol/solutions-architect — Solutions Architect — done iter 141
- [x] rol/investor-relations — Investor Relations (IR, relación con mercados) — done iter 141
- [x] rol/regulatory-affairs — Regulatory Affairs (cumplimiento regulatorio) — done iter 141
- [x] rol/actuario — Actuario (riesgo, seguros, pensiones) — done iter 141

## COLA ROUND 11 (14 temas — gap_analysis extendido, Round 10 completa)
- [x] sustrato/mexico/inversion-extranjera — IED (IMMEX, maquiladora, regulación)
- [x] sustrato/mexico/sector-manufacturero — Manufactura MX (industria, exportación)
- [x] sustrato/estados-unidos/agricultura — USDA, Farm Bill, subsidios
- [x] sustrato/canada/inmigracion — IRCC, permisos de trabajo
- [x] dominio/banca — Banca (comercial, múltiple, digital, Basilea)
- [x] dominio/capital-riesgo — VC / Private Equity (fundraising, ciclo)
- [x] dominio/cadena-suministro — Supply Chain (procurement, logística)
- [x] dominio/consultoria — Consultoría de gestión (estrategia, big four)
- [x] dominio/servicios-profesionales — Servicios profesionales (firmas, utilización)
- [x] rol/chief-compliance-officer — CCO (Chief Compliance Officer)
- [x] rol/treasurer — Treasurer (liquidez, financiamiento, riesgo tasa/divisa)
- [x] rol/chief-investment-officer — CIO inversiones (portafolio, activos)
- [x] rol/head-of-research — Head of Research / R&D (I+D, pipeline)
- [x] rol/chief-digital-officer — CDO digital (transformación digital)

### [2026-07-11] Round 10 — ITER 127 | LOOP 2 (dominio) — 5 ingests (nuevos nodos)
- 5 nodos `dominio/` creados con superstructura completa (README, index, log, raw/):
  - `dominio/analitica-negocio/` — Business Analytics/BI: dashboards, KPIs, descriptiva→prescriptiva, brecha insight→acción.
  - `dominio/gobierno-corporativo/` — Junta de directores, deberes fiduciarios, shareholder vs stakeholder (Business Roundtable 2019), ESG, SOX.
  - `dominio/ia-generativa/` — GenAI: LLMs, adopción empresarial 2025, riesgos (Deloitte 4 categorías), agentes.
  - `dominio/cultura-organizacional/` — Modelo de Schein (artefactos/valores/supuestos); cultura difícil de cambiar.
  - `dominio/gestion-cambio/` — Lewin, Kotter 8 pasos, ADKAR (Prosci), McKinsey 7S; ~70% de transformaciones fallan.
- Reference-only (URL en frontmatter; sin raw/). Cross-refs a finanzas, estrategia, sostenibilidad, rol/board-member, ciso, head-of-people, data-analyst.
- **Próxima tarea (iter 128):** LOOP 3 (rol) — controller, project-manager, data-analyst, board-member, auditor-interno.

## COLA ROUND 19 (13 temas — COMPLETA ✅)
### Sustrato (deepening nodos NA existentes)
- [x] sustrato/mexico — Turismo (SECTUR, destinos, turismo de sol y playa, turismo médico)
- [x] sustrato/estados-unidos — Infraestructura (IIJA, DOT, carreteras, puentes, banda ancha)
- [x] sustrato/canada — Energía (hidro, oil sands, gas, red eléctrica, NRCan)
### Dominio (nuevos nodos)
- [x] dominio/ciudades-inteligentes — Smart cities (IoT urbano, movilidad, datos, sostenibilidad)
- [x] dominio/healthtech — Salud digital (telemedicina, wearables, IA en salud, startups)
- [x] dominio/publicidad — Publicidad / advertising (medios, programática, agencias, medición)
- [x] dominio/franquicias — Franquicias / franchising (modelo, royalties, FDD, regulación)
- [x] dominio/eventos — Industria de eventos / MICE (meetings, incentives, conferences, exhibitions)
### Rol (nuevos nodos)
- [x] rol/legal-ops — Legal Operations (eBilling, proveedores, tecnología legal, contratos)
- [x] rol/head-of-facilities — Head of Facilities / Facilities Management (workplace, FM, ISO 41001)
- [x] rol/head-of-public-affairs — Head of Public Affairs / Government Relations (lobbying, políticas públicas)
- [x] rol/sales-engineer — Sales Engineer (pre-venta técnica, demos, POCs)
- [x] rol/business-analyst — Business Analyst (requisitos, procesos, BPM, puente negocio-TI)

### [2026-07-12] Round 19 — ITER 151 | gap_analysis extendido (taxonomía Round 19) + apertura de cola
- gap_analysis.py (post-Round 18) = 0 huecos, 0 nodos nuevos → se **EXTENDIÓ** `scripts/gap_analysis.py`
  (Round 19) con 3 deepenings sustrato NA (mexico→turismo, estados-unidos→infraestructura, canada→energia)
  + 10 nodos nuevos (dominio: ciudades-inteligentes, healthtech, publicidad, franquicias, eventos; rol:
  legal-ops, head-of-facilities, head-of-public-affairs, sales-engineer, business-analyst). ALCANCE respetado: sustrato = solo Norteamérica.
- Re-ejecutado → 13 sugerencias (3 sustrato + 10 nuevos). Abierta cola Round 19 (13 temas).
- **LOOPs 1-3 ejecutados (iter 152):** sustrato NA (turismo/infraestructura/energía) + 5 dominio + 5 rol = 13 ingests. **Round 19 COMPLETA (13/13).** Temas acumulados: 315. ALCANCE sustrato = solo Norteamérica (respetado).

### [2026-07-12] Round 19 — ITER 152 | LOOPs 1-3 (sustrato + dominio + rol) — 13 ingests COMPLETOS
- LOOP 1 (sustrato NA): `mexico/turismo.md`, `estados-unidos/infraestructura.md`, `canada/energia.md` (deepenings; append a index/log de nodos existentes).
- LOOP 2 (dominio, 5 nuevos): `ciudades-inteligentes`, `healthtech`, `publicidad`, `franquicias`, `eventos` (superstructura completa: raw/, README, index, log).
- LOOP 3 (rol, 5 nuevos): `legal-ops`, `head-of-facilities`, `head-of-public-affairs`, `sales-engineer`, `business-analyst` (superstructura completa).
- Índices/logs de nodos + globales (root index.md/log.md) actualizados. Reference-only (Wikipedia EN + fuentes oficiales gob/SECTUR/DOT/NRCAN; sin raw/).
- **Próxima tarea (iter 153):** COLA VACÍA → `python3 scripts/gap_analysis.py`; si 0 → reabastecer taxonomía (Round 20: nuevos dominio/rol + deepenings NA) o pausar hasta próximo cron.

## COLA ROUND 20 (13 temas — COMPLETA ✅)
### Sustrato (deepening nodos NA existentes)
- [x] sustrato/mexico — Minería (SGM, CAMIMEX, plata/oro/cobre, Ley Minera, PIB ~2.4%)
- [x] sustrato/estados-unidos — Seguridad social (SSA/OASDI, Medicare, Medicaid, SSI, SNAP)
- [x] sustrato/canada — Medio ambiente (ECCC, net-zero, cambio climático, precio al carbono)
### Dominio (nuevos nodos)
- [x] dominio/aviacion — Aviación comercial (FAA, EASA, ICAO, aerolíneas, MRO)
- [x] dominio/maritimo — Sector marítimo y puertos (OMI, navieras, logística portuaria)
- [x] dominio/seguridad-nacional — Seguridad nacional (inteligencia, defensa, infraestructura crítica)
- [x] dominio/ciberdefensa — Ciberdefensa estatal (CISA, US Cyber Command, SOC/CSIRT)
- [x] dominio/auditoria-gubernamental — Auditoría pública (GAO, ASF, OAG, ISSAI)
### Rol (nuevos nodos)
- [x] rol/vp-product — VP of Product (estrategia de portafolio, org de producto)
- [x] rol/chief-commercial-officer — Chief Commercial Officer (estrategia comercial e ingresos)
- [x] rol/chief-medical-officer — Chief Medical Officer (liderazgo clínico; no es CMO marketing)
- [x] rol/vp-operations — VP of Operations (operaciones a escala, eficiencia)
- [x] rol/head-of-engineering — Head of Engineering (managers de ingeniería, entrega)

## COLA ROUND 21 (13 temas — COMPLETA ✅)
### Sustrato (deepening nodos NA existentes)
- [x] sustrato/mexico — Finanzas públicas (SHCP, PEF, deuda pública ~50% PIB)
- [x] sustrato/estados-unidos — Finanzas públicas (Treasury, deuda nacional >USD$36B, debt ceiling)
- [x] sustrato/canada — Finanzas públicas (Dept of Finance, PBO, deuda/PIB ~30-45%)
### Dominio (nuevos nodos)
- [x] dominio/seguridad-alimentaria — Seguridad alimentaria (HACCP, FSMA, Codex, COFEPRIS/SENASICA)
- [x] dominio/derecho-penal — Derecho penal (delitos, white-collar crime, responsabilidad corporativa)
- [x] dominio/energia-nuclear — Energía nuclear (fisión, SMR, NRC/CNSC/IAEA, residuos)
- [x] dominio/ciencias-materiales — Ciencias de materiales (metales, polímeros, compuestos, semiconductores)
- [x] dominio/derecho-ambiental — Derecho ambiental (NEPA, LGEEPA, CEPA, ESG)
### Rol (nuevos nodos)
- [x] rol/ml-engineer — ML Engineer (entrena/despliega modelos en producción, MLOps)
- [x] rol/security-engineer — Security Engineer (AppSec, cloud security, threat modeling)
- [x] rol/fp-and-a-manager — FP&A Manager (planificación, presupuesto, forecast, variaciones)
- [x] rol/product-designer — Product Designer / UX (diseña experiencias de producto)
- [x] rol/account-manager — Account Manager (relación post-venta, retención, crecimiento)

## COLA ROUND 22 (13 temas — COMPLETA ✅)
### Sustrato (deepening nodos NA existentes)
- [x] sustrato/mexico/propiedad-intelectual — IMPI, LPI (Ley 27/2020), derechos de autor
- [x] sustrato/estados-unidos/propiedad-intelectual — USPTO, AIA 2011, Copyright Office, Lanham Act
- [x] sustrato/canada/propiedad-intelectual — CIPO/ISED, Patent Act, Trade-marks Act
### Dominio (nuevos nodos)
- [x] dominio/arbitraje — Arbitraje comercial e inversión (CIADI/UNCITRAL, ISDS)
- [x] dominio/tributacion-internacional — Fiscalidad internacional (BEPS/OCDE, precios de transferencia)
- [x] dominio/derecho-internacional — Derecho internacional público
- [x] dominio/ingenieria — Disciplinas, colegiación, ingeniería de sistemas
- [x] dominio/contabilidad-forense — Fraude, litigios, auditoría forense
### Rol (nuevos nodos)
- [x] rol/chairman — Chairman / Presidente del Consejo (gobernanza)
- [x] rol/partner — Equity partner (firmas de servicios)
- [x] rol/staff-engineer — Staff/Principal Engineer (ladder IC)
- [x] rol/delivery-manager — Delivery Manager (entrega de servicios)
- [x] rol/engagement-manager — Engagement Manager (consultoría)

## COLA ROUND 23 (13 temas — EN CURSO)
### Sustrato (deepening nodos NA existentes)
- [x] sustrato/mexico — Salud / sistema de salud (Secretaría de Salud, IMSS/INSABI, Cofepris)
- [x] sustrato/estados-unidos — Telecomunicaciones (FCC, banda ancha, 5G, espectro)
- [x] sustrato/canada — Agricultura (AAFC, supply management, granos)
### Dominio (nuevos nodos)
- [x] dominio/dispositivos-medicos — Dispositivos médicos (FDA 510(k)/PMA, COFEPRIS, Health Canada, MDR)
- [x] dominio/computacion-cuantica — Computación cuántica (qubits, algoritmos, casos)
- [x] dominio/investigacion-operaciones — Investigación de operaciones (optimización, colas, simulación)
- [x] dominio/teoria-de-juegos — Teoría de juegos (Nash, subastas, negocio)
- [x] dominio/gobierno-de-ti — Gobierno de TI (COBIT, alineación TI-negocio)
### Rol (nuevos nodos)
- [x] rol/platform-engineer — Platform Engineer (plataformas internas, golden paths)
- [x] rol/cloud-architect — Cloud Architect (arquitecturas cloud, multi-cloud)
- [x] rol/research-scientist — Research Scientist (R&D, publicación)
- [x] rol/technical-program-manager — Technical Program Manager (TPM)
- [x] rol/community-manager — Community Manager (comunidad, redes sociales)

### [2026-07-13] Round 21 — ITER 154 | gap_analysis extendido (taxonomía Round 21) + 13 ingests COMPLETOS
- gap_analysis.py (post-Round 20) = 0 huecos → se **EXTENDIÓ** `scripts/gap_analysis.py` (Round 21) con 3 deepenings sustrato NA (mexico→finanzas-publicas, estados-unidos→finanzas-publicas, canada→finanzas-publicas) + 10 nodos nuevos (dominio: seguridad-alimentaria, derecho-penal, energia-nuclear, ciencias-materiales, derecho-ambiental; rol: ml-engineer, security-engineer, fp-and-a-manager, product-designer, account-manager). ALCANCE respetado: sustrato = solo Norteamérica.
- LOOP 1 (sustrato NA): `mexico/finanzas-publicas.md`, `estados-unidos/finanzas-publicas.md`, `canada/finanzas-publicas.md` (deepenings; append a index/log de nodos existentes).
- LOOP 2 (dominio, 5 nuevos): `seguridad-alimentaria`, `derecho-penal`, `energia-nuclear`, `ciencias-materiales`, `derecho-ambiental` (superstructura completa: raw/, README, index, log).
- LOOP 3 (rol, 5 nuevos): `ml-engineer`, `security-engineer`, `fp-and-a-manager`, `product-designer`, `account-manager` (superstructura completa).
- Índices/logs de nodos + globales (root index.md/log.md) actualizados. Reference-only (Wikipedia EN + fuentes oficiales gob/hacienda/Treasury/NRC/FDA/EPA/MRS/OWASP/NNGroup/Salesforce; sin raw/).
- **Round 21 COMPLETA (13/13).** Temas acumulados: 341. ALCANCE sustrato = solo Norteamérica (respetado).

### [2026-07-13] Round 20 — ITER 153 | gap_analysis extendido (taxonomía Round 20) + apertura de cola
- gap_analysis.py (post-Round 19) = 0 huecos → se **EXTENDIÓ** `scripts/gap_analysis.py` (Round 20) con 3 deepenings sustrato NA (mexico→mineria, estados-unidos→seguridad-social, canada→medio-ambiente) + 10 nodos nuevos (dominio: aviacion, maritimo, seguridad-nacional, ciberdefensa, auditoria-gubernamental; rol: vp-product, chief-commercial-officer, chief-medical-officer, vp-operations, head-of-engineering). ALCANCE respetado: sustrato = solo Norteamérica.
- Re-ejecutado → 13 sugerencias. Abierta cola Round 20 (13 temas).
- **LOOPs 1-3 ejecutados (iter 153):** sustrato NA (mineria/seguridad-social/medio-ambiente) + 5 dominio + 5 rol = 13 ingests. **Round 20 COMPLETA (13/13).** Temas acumulados: 328. ALCANCE sustrato = solo Norteamérica (respetado).

### [2026-07-13] Round 20 — ITER 153 | LOOPs 1-3 (sustrato + dominio + rol) — 13 ingests COMPLETOS
- LOOP 1 (sustrato NA): `mexico/mineria.md`, `estados-unidos/seguridad-social.md`, `canada/medio-ambiente.md` (deepenings; append a index/log de nodos existentes).
- LOOP 2 (dominio, 5 nuevos): `aviacion`, `maritimo`, `seguridad-nacional`, `ciberdefensa`, `auditoria-gubernamental` (superstructura completa: raw/, README, index, log).
- LOOP 3 (rol, 5 nuevos): `vp-product`, `chief-commercial-officer`, `chief-medical-officer`, `vp-operations`, `head-of-engineering` (superstructura completa).
- Índices/logs de nodos + globales (root index.md/log.md) actualizados. Reference-only (Wikipedia EN + fuentes oficiales gob/SSA/Canada.ca/CAMIMEX/IMO/CISA/GAO/ASF; sin raw/).

### [2026-07-13] Round 22 — ITER 156 | gap_analysis extendido (taxonomía Round 22) + 13 ingests COMPLETOS
- ITER 155: gap_analysis.py (post-Round 21) = 0 huecos → se **EXTENDIÓ** `scripts/gap_analysis.py` (Round 22) con 3 deepenings sustrato NA (mexico/estados-unidos/canada → propiedad-intelectual) + 10 nodos nuevos (dominio: arbitraje, tributacion-internacional, derecho-internacional, ingenieria, contabilidad-forense; rol: chairman, partner, staff-engineer, delivery-manager, engagement-manager). ALCANCE respetado: sustrato = solo Norteamérica.
- LOOP 1 (sustrato NA): `mexico/propiedad-intelectual.md`, `estados-unidos/propiedad-intelectual.md`, `canada/propiedad-intelectual.md` (deepenings; append a index/log de nodos existentes).
- LOOP 2 (dominio, 5 nuevos): `arbitraje`, `tributacion-internacional`, `derecho-internacional`, `ingenieria`, `contabilidad-forense` (superstructura completa: raw/, README, index, log).
- LOOP 3 (rol, 5 nuevos): `chairman`, `partner`, `staff-engineer`, `delivery-manager`, `engagement-manager` (superstructura completa).
- Índices/logs de nodos + globales (root index.md/log.md) actualizados. Reference-only (Wikipedia EN + fuentes oficiales gob/IMPI/USPTO/CIPO/OCDE/INCOSE/ACFE/staffeng; sin raw/).
- **Round 22 COMPLETA (13/13).** Temas acumulados: 354. ALCANCE sustrato = solo Norteamérica (respetado).

### [2026-07-13] Round 23 — ITER 157 | gap_analysis extendido (taxonomía Round 23) + apertura de cola
- gap_analysis.py (post-Round 22) = 0 huecos → se **EXTENDIÓ** `scripts/gap_analysis.py` (Round 23) con 3 deepenings sustrato NA (mexico→salud, estados-unidos→telecomunicaciones, canada→agricultura) + 10 nodos nuevos (dominio: dispositivos-medicos, computacion-cuantica, investigacion-operaciones, teoria-de-juegos, gobierno-de-ti; rol: platform-engineer, cloud-architect, research-scientist, technical-program-manager, community-manager). ALCANCE respetado: sustrato = solo Norteamérica.
- Re-ejecutado → 13 sugerencias (3 sustrato + 10 nuevos). Abierta cola Round 23 (13 temas).
- **LOOP 1 (sustrato NA) COMPLETO:** sustrato/mexico/salud, sustrato/estados-unidos/telecomunicaciones, sustrato/canada/agricultura (deepenings; +index/log nodos + root).
- **LOOP 2 (dominio x5) COMPLETO:** dispositivos-medicos, computacion-cuantica, investigacion-operaciones, teoria-de-juegos, gobierno-de-ti (5 nodos nuevos; +raw/README/README/index/log + root).
- **LOOP 3 (rol x5) COMPLETO:** platform-engineer, cloud-architect, research-scientist, technical-program-manager, community-manager (5 nodos nuevos; +raw/README/README/index/log + root).
- **Round 23 COMPLETA (13/13).** Temas acumulados: 367. ALCANCE sustrato = solo Norteamérica (respetado).
- **Próxima tarea (iter 158):** COLA VACÍA → `python3 scripts/gap_analysis.py`; si 0 → reabastecer taxonomía (Round 24: nuevos dominio/rol + deepenings NA) o pausar hasta próximo cron.

## LOG DE RONDAS
### [2026-07-13] Ronda 20: +13 (3 sustrato NA + 5 dominio + 5 rol); COMPLETA.
### [2026-07-13] Ronda 21: +13 (3 sustrato NA + 5 dominio + 5 rol); COMPLETA.
### [2026-07-13] Ronda 22: +13 (3 sustrato NA + 5 dominio + 5 rol); COMPLETA.
### [2026-07-13] Ronda 23: +13 (3 sustrato NA + 5 dominio + 5 rol); COMPLETA.
### [2026-07-13] Ronda 26: +13 (3 sustrato NA + 10 nodos) — COMPLETA (iter 162)
### [2026-07-14] Ronda 31: +13 (3 sustrato NA + 10 nodos) — COMPLETA (iter 166)

### [2026-07-13] Round 24 — ITER 158 | gap_analysis extendido (taxonomía Round 24) + apertura de cola
- gap_analysis.py (post-Round 23) = 0 huecos → se **EXTENDIÓ** `scripts/gap_analysis.py` (Round 24) con 3 deepenings sustrato NA + 10 nodos nuevos. ALCANCE respetado: sustrato = solo Norteamérica.
- Re-ejecutado → 13 sugerencias (3 sustrato + 10 nuevos). Abierta cola Round 24 (13 temas).

### [2026-07-13] Round 24 — ITER 159 | 13 ingests COMPLETOS (LOOP 1 sustrato x3 + LOOP 2 dominio x5 + LOOP 3 rol x5)
- 3 → sustrato (deepenings NA): `sustrato/mexico/politica-monetaria.md` (Banxico), `sustrato/estados-unidos/medio-ambiente.md` (EPA), `sustrato/canada/defensa.md` (DND/CAF/NORAD).
- 5 → dominio (nuevos): `derecho-administrativo`, `control-interno`, `seguridad-y-salud-ocupacional`, `proteccion-de-datos`, `gestion-de-activos`.
- 5 → rol (nuevos): `vp-finance`, `devops-engineer`, `supply-chain-manager`, `hr-business-partner`, `channel-manager`.
- Superstructura recursiva completa en los 10 nodos nuevos (raw/, README, index, log). Reference-only (Wikipedia EN + fuentes oficiales gob/banxico.org.mx/epa.gov/canada.ca/COSO/ISO/OSHA/GDPR; sin raw/).
- **Temas completados: 380** (367 Round 23 + 13 Round 24).
- **Próxima tarea (iter 159):** COLA Round 24 COMPLETA (13/13). Siguiente: `python3 scripts/gap_analysis.py`; si 0 → reabastecer taxonomía (Round 25) o pausar hasta próximo cron.

## COLA ROUND 24 (gap_analysis.py iter 158 → taxonomía extendida; sustrato solo NA)
### Sustrato (deepening nodos NA existentes)
- [x] sustrato/mexico — Política monetaria (Banxico, tasa de referencia, inflation targeting, Junta de Gobierno)
- [x] sustrato/estados-unidos — Medio ambiente (EPA, Clean Air/Water Act, NEPA, climate policy)
- [x] sustrato/canada — Defensa (DND/CAF, NORAD, procurement, política industrial de defensa)
### Dominio (nuevos nodos)
- [x] dominio/derecho-administrativo — Derecho administrativo / regulatory law (permisos, licencias, sanciones, revisión judicial)
- [x] dominio/control-interno — Control interno (COSO 2013, ICFR, SOX 404, monitoreo)
- [x] dominio/seguridad-y-salud-ocupacional — Seguridad y salud ocupacional (ISO 45001, OSHA/CSST, bienestar)
- [x] dominio/proteccion-de-datos — Protección de datos / privacidad transversal (GDPR/CCPA/CPRA/LGPD/PIPL)
- [x] dominio/gestion-de-activos — Gestión de activos / asset & wealth management
### Rol (nuevos nodos)
- [x] rol/vp-finance — VP of Finance (reporta a CFO, lidera FP&A/controller/treasury)
- [x] rol/devops-engineer — DevOps Engineer (CI/CD, IaC, pipelines, observabilidad)
- [x] rol/supply-chain-manager — Supply Chain Manager (planificación, sourcing, logística, resiliencia)
- [x] rol/hr-business-partner — HR Business Partner (HRBP, people analytics, talento)
- [x] rol/channel-manager — Channel Manager (canales partner/reseller/distributor)

## COLA ROUND 25 (13 temas — COMPLETA ✅)
### Sustrato (deepening nodos NA existentes)
- [x] sustrato/mexico — Seguridad pública (Guardia Nacional, SSP, FGR)
- [x] sustrato/estados-unidos — Sistema financiero (Fed, OCC, FDIC, Dodd-Frank)
- [x] sustrato/canada — Infraestructura (Infrastructure Canada, vivienda, banda ancha)
### Dominio (nuevos nodos)
- [x] dominio/proptech — PropTech (tecnología inmobiliaria)
- [x] dominio/regtech — RegTech (tecnología regulatoria)
- [x] dominio/nanotecnologia — Nanotecnología (materiales a nanoescala)
- [x] dominio/derecho-de-la-competencia — Derecho de la competencia / antitrust
- [x] dominio/microfinanzas — Microfinanzas (inclusión financiera)
### Rol (nuevos nodos)
- [x] rol/engineering-manager — Engineering Manager (EM)
- [x] rol/creative-director — Creative Director
- [x] rol/site-reliability-engineer — Site Reliability Engineer (SRE)
- [x] rol/vp-human-resources — VP of Human Resources (VP HR)
- [x] rol/managing-director — Managing Director (MD)

## LOG DE RONDAS (continuación)
### [2026-07-13] Ronda 25: +13 (3 sustrato NA + 5 dominio + 5 rol); COMPLETA.

### [2026-07-13] Round 25 — ITER 160 | gap_analysis extendido (taxonomía Round 25) + 13 ingests COMPLETOS
- gap_analysis.py (post-Round 24) = 0 huecos → se **EXTENDIÓ** `scripts/gap_analysis.py` (Round 25) con 3 deepenings sustrato NA (mexico→seguridad-publica, estados-unidos→sistema-financiero, canada→infraestructura) + 10 nodos nuevos (dominio: proptech, regtech, nanotecnologia, derecho-de-la-competencia, microfinanzas; rol: engineering-manager, creative-director, site-reliability-engineer, vp-human-resources, managing-director). ALCANCE respetado: sustrato = solo Norteamérica.
- LOOP 1 (sustrato NA): `mexico/seguridad-publica.md`, `estados-unidos/sistema-financiero.md`, `canada/infraestructura.md` (deepenings; append a index/log de nodos existentes).
- LOOP 2 (dominio, 5 nuevos): `proptech`, `regtech`, `nanotecnologia`, `derecho-de-la-competencia`, `microfinanzas` (superstructura completa: raw/, README, index, log).
- LOOP 3 (rol, 5 nuevos): `engineering-manager`, `creative-director`, `site-reliability-engineer`, `vp-human-resources`, `managing-director` (superstructura completa).
- Índices/logs de nodos + globales (root index.md/log.md) actualizados. Reference-only (Wikipedia EN + fuentes oficiales gob/guardianacional/gob.mx/fgr/infrastructure.gc.ca/federalreserve.gov; sin raw/).
- **Round 25 COMPLETA (13/13).** Temas acumulados: 393. ALCANCE sustrato = solo Norteamérica (respetado).
- **Próxima tarea (iter 161):** COLA VACÍA → `python3 scripts/gap_analysis.py`; si 0 → reabastecer taxonomía (Round 26: nuevos dominio/rol + deepenings NA) o pausar hasta próximo cron.

## COLA ROUND 26 (13 temas — COMPLETA ✅)
### Sustrato (deepening nodos NA existentes)
- [x] sustrato/mexico — Poder Judicial (PJF, SCJN, reforma judicial 2024-2025)
- [x] sustrato/estados-unidos — Poder Judicial (federal judiciary, SCOTUS, Art. III, DOJ)
- [x] sustrato/canada — Poder Judicial (Supreme Court of Canada, Carta, cortes provinciales)
### Dominio (nuevos nodos)
- [x] dominio/etica-empresarial — Ética empresarial / corporate ethics
- [x] dominio/compensacion-beneficios — Compensación y beneficios / total rewards
- [x] dominio/transformacion-digital — Transformación digital
- [x] dominio/finanzas-cuantitativas — Finanzas cuantitativas / quantitative finance
- [x] dominio/relaciones-laborales — Relaciones laborales / industrial relations
### Rol (nuevos nodos)
- [x] rol/head-of-talent — Head of Talent
- [x] rol/head-of-sales-ops — Head of Sales Operations
- [x] rol/head-of-marketing-ops — Head of Marketing Operations
- [x] rol/head-of-it — Head of IT / IT Director
- [x] rol/chief-brand-officer — Chief Brand Officer (CBO)

## LOG DE RONDAS
### [2026-07-13] Ronda 26: +13 (3 sustrato NA + 5 dominio + 5 rol); COMPLETA.

### [2026-07-13] Round 26 — ITER 161 | gap_analysis extendido (taxonomía Round 26) + 13 ingests COMPLETOS
- gap_analysis.py (post-Round 25) = 0 huecos → se **EXTENDIÓ** `scripts/gap_analysis.py` (Round 26) con 3 deepenings sustrato NA (mexico→poder-judicial, estados-unidos→poder-judicial, canada→poder-judicial) + 10 nodos nuevos (dominio: etica-empresarial, compensacion-beneficios, transformacion-digital, finanzas-cuantitativas, relaciones-laborales; rol: head-of-talent, head-of-sales-ops, head-of-marketing-ops, head-of-it, chief-brand-officer). ALCANCE respetado: sustrato = solo Norteamérica.
- LOOP 1 (sustrato NA): `mexico/poder-judicial.md`, `estados-unidos/poder-judicial.md`, `canada/poder-judicial.md` (deepenings; append a index/log de nodos existentes).
- LOOP 2 (dominio, 5 nuevos): `etica-empresarial`, `compensacion-beneficios`, `transformacion-digital`, `finanzas-cuantitativas`, `relaciones-laborales` (superstructura completa: raw/, README, index, log).
- LOOP 3 (rol, 5 nuevos): `head-of-talent`, `head-of-sales-ops`, `head-of-marketing-ops`, `head-of-it`, `chief-brand-officer` (superstructura completa).
- Índices/logs de nodos + globales (root index.md/log.md) actualizados. Reference-only (Wikipedia EN + fuentes oficiales gob/oaj.gob.mx/justiciaabierta/uscourts.gov/scc-csc.ca; sin raw/). México poder-judicial usa fuentes vivas de la reforma 2024-2025.
- **Round 26 COMPLETA (13/13).** Temas acumulados: 406. ALCANCE sustrato = solo Norteamérica (respetado).

## COLA ROUND 27 (gap_analysis.py iter 162 → taxonomía extendida; sustrato solo NA) — COMPLETA ✅
### Sustrato (deepening nodos NA existentes)
- [x] sustrato/mexico — Relaciones exteriores (SRE, política exterior, diplomacia, tratados)
- [x] sustrato/estados-unidos — Seguridad nacional (DHS, FBI, inteligencia, homeland security)
- [x] sustrato/canada — Ciencia e innovación (NRC, ISED, políticas de CTI)
### Dominio (nuevos nodos)
- [x] dominio/electromovilidad — Electromovilidad (EV, baterías, carga, V2G)
- [x] dominio/comercio-electronico — Comercio electrónico / e-commerce
- [x] dominio/outsourcing — Outsourcing / offshoring (BPO, nearshoring)
- [x] dominio/gobierno-abierto — Gobierno abierto (transparencia, datos abiertos)
- [x] dominio/economia-comportamental — Economía conductual / behavioral economics
### Rol (nuevos nodos)
- [x] rol/technical-writer — Technical Writer (documentación)
- [x] rol/portfolio-manager — Portfolio Manager (carteras de inversión)
- [x] rol/change-manager — Change Manager (gestión del cambio)
- [x] rol/benefits-manager — Benefits Manager (beneficios/compensación)
- [x] rol/consultor — Consultor / Management Consultant

### [2026-07-13] Round 27 — ITER 162 | gap_analysis extendido (taxonomía Round 27) + apertura de cola
- gap_analysis.py (post-Round 26) = 0 huecos → se **EXTENDIÓ** `scripts/gap_analysis.py` (Round 27) con 3 deepenings sustrato NA (mexico→relaciones-exteriores, estados-unidos→seguridad-nacional, canada→ciencia-e-innovacion) + 10 nodos nuevos (dominio: electromovilidad, comercio-electronico, outsourcing, gobierno-abierto, economia-comportamental; rol: technical-writer, portfolio-manager, change-manager, benefits-manager, consultor). ALCANCE respetado: sustrato = solo Norteamérica.
- Re-ejecutado → 13 sugerencias (3 sustrato + 10 nuevos). Abierta cola Round 27 (13 temas).
### [2026-07-13] Round 27 — ITER 162 | 13 ingests COMPLETOS (3 sustrato NA + 5 dominio + 5 rol)
- 3 → sustrato (deepenings NA): `relaciones-exteriores` (MX/SRE), `seguridad-nacional` (US/DHS-FBI-IC), `ciencia-e-innovacion` (CA/NRC-ISED).
- 5 → dominio (nuevos): `electromovilidad`, `comercio-electronico`, `outsourcing`, `gobierno-abierto`, `economia-comportamental`.
- 5 → rol (nuevos): `technical-writer`, `portfolio-manager`, `change-manager`, `benefits-manager`, `consultor`.
- Superstructura recursiva completa (raw/, README, index, log) en los 10 nodos nuevos + 3 páginas sustrato. Reference-only (Wikipedia EN + fuentes oficiales; sin raw/).
- **Round 27 COMPLETA (13/13).** ALCANCE sustrato = solo Norteamérica (respetado).

## COLA ROUND 28 (13 temas — gap_analysis.py iter 163 → taxonomía extendida; sustrato solo NA) — COMPLETA ✅

### [2026-07-13] Round 28 — ITER 163 | gap_analysis extendido (taxonomía Round 28) + 13 ingests COMPLETOS
- gap_analysis.py (post-Round 27) = 0 huecos → se **EXTENDIÓ** `scripts/gap_analysis.py` (Round 28) con 3 deepenings sustrato NA (mexico→economia, estados-unidos→ciencia-e-innovacion, canada→demografia-poblacion) + 10 nodos nuevos (dominio: aduanas, finanzas-sostenibles, cadena-de-valor, inteligencia-de-mercado, clima-organizacional; rol: software-engineer, prompt-engineer, fractional-executive, head-of-customer-experience, category-manager). ALCANCE respetado: sustrato = solo Norteamérica.
- LOOP 1 (sustrato NA): `mexico/economia.md`, `estados-unidos/ciencia-e-innovacion.md`, `canada/demografia-poblacion.md` (deepenings; append a index/log de nodos existentes).
- LOOP 2 (dominio, 5 nuevos): `aduanas`, `finanzas-sostenibles`, `cadena-de-valor`, `inteligencia-de-mercado`, `clima-organizacional` (superstructura completa: raw/, README, index, log).
- LOOP 3 (rol, 5 nuevos): `software-engineer`, `prompt-engineer`, `fractional-executive`, `head-of-customer-experience`, `category-manager` (superstructura completa).
- Índices/logs de nodos + globales (root index.md/log.md) actualizados. Reference-only (Wikipedia EN + fuentes oficiales inegi.org.mx, banxico.org.mx, nsf.gov, statcan.gc.ca, wcoomd.org, icmagroup.org; sin raw/).
- **Round 28 COMPLETA (13/13).** Temas acumulados: 432. ALCANCE sustrato = solo Norteamérica (respetado).
### Sustrato (deepening nodos NA existentes)
- [x] sustrato/mexico — Economía (PIB, INEGI, Banxico, sectores, informalidad, comercio exterior)
- [x] sustrato/estados-unidos — Ciencia e innovación (NSF, DOE national labs, NIH, CHIPS Act)
- [x] sustrato/canada — Demografía y población (Statistics Canada, censo, crecimiento por inmigración)
### Dominio (nuevos nodos)
- [x] dominio/aduanas — Aduanas / despacho aduanero (aranceles, valoración, OMA, SIAVI)
- [x] dominio/finanzas-sostenibles — Finanzas sostenibles / green & sustainable finance
- [x] dominio/cadena-de-valor — Cadena de valor (Porter)
- [x] dominio/inteligencia-de-mercado — Inteligencia de mercado (TAM/SAM/SOM, VoC)
- [x] dominio/clima-organizacional — Clima organizacional (engagement, vs cultura)
### Rol (nuevos nodos)
- [x] rol/software-engineer — Software Engineer
- [x] rol/prompt-engineer — Prompt Engineer (LLMs)
- [x] rol/fractional-executive — Ejecutivo fraccionario / Fractional CXO
- [x] rol/head-of-customer-experience — Head of Customer Experience (CX)
- [x] rol/category-manager — Category Manager (retail/compras)

## 2026-07-13 — Iter 164 · Round 29 (13/13) · COMPLETA
- gap_analysis.py → 0 gaps en Round 28. Extendí taxonomía (3 deepenings NA + 10 nodos nuevos) en scripts/gap_analysis.py.
- Deepenings NA: sustrato/mexico/demografia-poblacion, sustrato/estados-unidos/demografia-poblacion, sustrato/canada/seguridad-publica.
- 10 nodos nuevos: dominio/i-d, dominio/compras, dominio/juego-azar, dominio/tercer-sector, dominio/servicios-ambientales, rol/country-manager, rol/regional-director, rol/data-architect, rol/network-engineer, rol/dba.
- Index/log raíz + nodos actualizados. Reference-only (Wikipedia EN + oficiales de gobierno; sin raw/).
- Próxima: gap_analysis.py; si 0 gaps → extender taxonomía Round 30; si hay gaps → reabrir Round 29.

## COLA ROUND 30 (13 temas — COMPLETA ✅)
### Sustrato (deepening nodos NA existentes)
- [x] sustrato/mexico — Infraestructura (SICT transporte, CFE/PEMEX energía, CONAGUA agua, vivienda, inversión) — done iter 165
- [x] sustrato/estados-unidos — Sector manufacturero (2º mayor del mundo, USD$2.9T 2024, CHIPS/IRA, reshoring) — done iter 165
- [x] sustrato/canada — Relaciones exteriores (Global Affairs Canada, multilateralismo, paz, comercio) — done iter 165
### Dominio (nuevos nodos)
- [x] dominio/salud-publica — Salud pública (prevención, epidemiología, sistemas poblacionales)
- [x] dominio/derecho-tributario — Derecho tributario (potestad, impuestos, procedimiento, controversias)
- [x] dominio/agrotech — AgTech (agricultura de precisión, IoT, biotec)
- [x] dominio/movilidad-urbana — Movilidad urbana sostenible (modos, última milla, MaaS)
- [x] dominio/gestion-del-conocimiento — Gestión del conocimiento (KM)
### Rol (nuevos nodos)
- [x] rol/paralegal — Paralegal / asistente legal
- [x] rol/wealth-manager — Wealth Manager (asesoría patrimonial HNW/UHNW)
- [x] rol/procurement-manager — Procurement Manager (abastecimiento, sourcing)
- [x] rol/executive-assistant — Executive Assistant (soporte a ejecutivo senior)
- [x] rol/learning-manager — Learning & Development Manager (L&D)

## 2026-07-14 — Iter 165 · Round 30 (13/13) · COMPLETA
- gap_analysis.py → 0 gaps en Round 29. Extendí taxonomía (3 deepenings NA + 10 nodos nuevos) en scripts/gap_analysis.py.
- Deepenings NA: sustrato/mexico/infraestructura, sustrato/estados-unidos/sector-manufacturero, sustrato/canada/relaciones-exteriores.
- 10 nodos nuevos: dominio/salud-publica, dominio/derecho-tributario, dominio/agrotech, dominio/movilidad-urbana, dominio/gestion-del-conocimiento, rol/paralegal, rol/wealth-manager, rol/procurement-manager, rol/executive-assistant, rol/learning-manager.
- Index/log raíz + nodos actualizados. Reference-only (Wikipedia EN + oficiales de gobierno; sin raw/).
- Próxima: gap_analysis.py; si 0 gaps → extender taxonomía Round 31; si hay gaps → reabrir Round 30.

## COLA ROUND 31 (13 temas — gap_analysis.py iter 166 → taxonomía extendida; sustrato solo NA) — COMPLETA (13/13)
### Sustrato (deepening nodos NA existentes)
- [x] sustrato/mexico — Ciencia e innovación (CONAHCYT, SNCTI, I+D, nearshoring de conocimiento)
- [x] sustrato/estados-unidos — Relaciones exteriores (Department of State, diplomacia, tratados, USAID)
- [x] sustrato/canada — Economía (PIB, sectores, recursos, comercio, Bank of Canada)
### Dominio (nuevos nodos)
- [x] dominio/derechos-humanos — Derechos humanos (marco internacional, constitucional, empresariales)
- [x] dominio/comportamiento-del-consumidor — Comportamiento del consumidor (psicología, journey, nudge)
- [x] dominio/trabajo-remoto — Trabajo remoto / teletrabajo (políticas, herramientas, legal)
- [x] dominio/desarrollo-organizacional — Desarrollo organizacional (OD, diagnóstico, intervenciones)
- [x] dominio/inteligencia-emocional — Inteligencia emocional (EQ, liderazgo, equipos)
### Rol (nuevos nodos)
- [x] rol/agile-coach — Agile Coach (transformación ágil, coaching a líderes)
- [x] rol/devsecops-engineer — DevSecOps Engineer (security as code, shift-left)
- [x] rol/account-director — Account Director (cuentas estratégicas, retención/expansión)
- [x] rol/social-media-manager — Social Media Manager (canales, comunidad, métricas)
- [x] rol/plant-manager — Plant Manager (operaciones de planta, P&L)

## COLA ROUND 32 (13 temas — gap_analysis.py iter 167 → taxonomía extendida; sustrato solo NA) — COMPLETA (13/13)
### Sustrato (deepening nodos NA existentes)
- [x] sustrato/mexico — Competitividad (IMCO, WEF, Doing Business, clústeres, facilitación de negocios)
- [x] sustrato/estados-unidos — Transporte (DOT, FAA, FHWA, FRA, USCG; modos carretero/ferroviario/aéreo/marítimo)
- [x] sustrato/canada — Sector manufacturero (Ontario auto, Quebec aeroespacial, Alberta petroquímica)
### Dominio (nuevos nodos)
- [x] dominio/metodologias-agiles — Metodologías ágiles (Scrum, Kanban, SAFe, Lean, XP)
- [x] dominio/gobierno-de-ia — Gobierno de IA (EU AI Act, NIST AI RMF, ISO 42001)
- [x] dominio/ciencia-de-datos — Ciencia de datos (CRISP-DM, modelado, ML aplicado)
- [x] dominio/derecho-concursal — Derecho concursal / insolvencia (Chapter 11/15 US, LCM MX, BIA/CCAA CA)
- [x] dominio/mercados-de-carbono — Mercados de carbono (ETS/cap-and-trade, bonos, precios)
### Rol (nuevos nodos)
- [x] rol/ai-engineer — AI Engineer (productos/agentes de IA, RAG, evals; vs ml-engineer)
- [x] rol/customer-success-manager — Customer Success Manager (salud de cuenta, retención/expansión)
- [x] rol/compliance-manager — Compliance Manager (AML/KYC, controles, monitorización)
- [x] rol/sales-manager — Sales Manager (equipo IC, cuotas, coaching, pipeline)
- [x] rol/field-marketing-manager

### Round 33 (13 temas) — COMPLETA ✅
- [x] sustrato/mexico/gobierno-federal
- [x] sustrato/estados-unidos/impuestos
- [x] sustrato/canada/elecciones
- [x] dominio/inteligencia-artificial
- [x] dominio/derecho-civil
- [x] dominio/cosmetica
- [x] dominio/empaque
- [x] dominio/textil
- [x] rol/accountant
- [x] rol/team-lead
- [x] rol/content-manager
- [x] rol/it-manager
- [x] rol/head-of-design

## LOG DE ITERACIONES (Round 32)
### [2026-07-14] ingest | Round 32 — Reabastecimiento continuo (3 deepenings NA + 10 nodos nuevos)
- gap_analysis.py → 0 gaps en Round 31. Extendida taxonomía para Round 32 (3 deepenings NA + 10 nodos nuevos).
- Alcance sustrato: solo Norteamérica (respetado). Deepenings: sustrato/mexico/competitividad, sustrato/estados-unidos/transporte, sustrato/canada/sector-manufacturero.
- 10 nodos nuevos: dominio/metodologias-agiles, dominio/gobierno-de-ia, dominio/ciencia-de-datos, dominio/derecho-concursal, dominio/mercados-de-carbono, rol/ai-engineer, rol/customer-success-manager, rol/compliance-manager, rol/sales-manager, rol/field-marketing-manager.
- Total Round 32: 13 temas ingestados (3 sustrato + 10 nodos). Fuentes: Wikipedia EN + oficiales de gobierno (reference-only; sin raw/).
- Índice de progreso: 484 tópicos en 167 iteraciones.

## [2026-07-14] ingest | Round 33 — Reabastecimiento continuo (3 deepenings NA + 10 nodos nuevos)
- gap_analysis.py → 0 gaps en Round 32. Extendida taxonomía para Round 33 (3 deepenings NA + 10 nodos nuevos).
- Alcance sustrato: solo Norteamérica (respetado). Deepenings: sustrato/mexico/gobierno-federal, sustrato/estados-unidos/impuestos, sustrato/canada/elecciones.
- 10 nodos nuevos: dominio/inteligencia-artificial, dominio/derecho-civil, dominio/cosmetica, dominio/empaque, dominio/textil, rol/accountant, rol/team-lead, rol/content-manager, rol/it-manager, rol/head-of-design.
- Total Round 33: 13 temas ingestados (3 sustrato + 10 nodos). Fuentes: Wikipedia EN + oficiales de gobierno (reference-only; sin raw/).
- Reparado index.md raíz: agregadas entradas faltantes (mexico/competitividad, estados-unidos/transporte, canada/sector-manufacturero) y eliminados duplicados en canada.
- Índice de progreso: 497 tópicos en 168 iteraciones.

## [2026-07-14] ingest | Round 34 — Reabastecimiento continuo (3 deepenings NA + 10 nodos nuevos)
- gap_analysis.py → 0 gaps en Round 33. Extendida taxonomía para Round 34 (3 deepenings NA + 10 nodos nuevos).
- Alcance sustrato: solo Norteamérica (respetado). Deepenings: sustrato/mexico/trabajo, sustrato/estados-unidos/elecciones, sustrato/canada/cultura.
- 10 nodos nuevos: dominio/salud-mental, dominio/gamificacion, dominio/urbanismo, dominio/arquitectura, dominio/biometria, rol/chief-administrative-officer, rol/head-of-data-science, rol/head-of-employer-branding, rol/director-of-operations, rol/head-of-communications.
- Total Round 34: 13 temas ingestados (3 sustrato + 10 nodos). Fuentes: Wikipedia EN + oficiales de gobierno (reference-only; sin raw/).
- Índice de progreso: 510 tópicos en 169 iteraciones.

## ✅ COLA ROUND 34 — COMPLETA (13/13)
- [x] sustrato/mexico/trabajo
- [x] sustrato/estados-unidos/elecciones
- [x] sustrato/canada/cultura
- [x] dominio/salud-mental
- [x] dominio/gamificacion
- [x] dominio/urbanismo
- [x] dominio/arquitectura
- [x] dominio/biometria
- [x] rol/chief-administrative-officer
- [x] rol/head-of-data-science
- [x] rol/head-of-employer-branding
- [x] rol/director-of-operations
- [x] rol/head-of-communications

## [2026-07-14] ingest | Round 35 — Reabastecimiento continuo (3 deepenings NA + 10 nodos nuevos)
- gap_analysis.py → 0 gaps en Round 34. Extendida taxonomía para Round 35 (3 deepenings NA + 10 nodos nuevos).
- Alcance sustrato: solo Norteamérica (respetado). Deepenings: sustrato/mexico/vivienda, sustrato/estados-unidos/seguridad-publica, sustrato/canada/vivienda.
- 10 nodos nuevos: dominio/edtech, dominio/foodtech, dominio/deep-tech, dominio/pymes, dominio/impresion-3d, rol/chief-innovation-officer, rol/system-administrator, rol/risk-manager, rol/sales-development-representative, rol/bookkeeper.
- Total Round 35: 13 temas ingestados (3 sustrato + 10 nodos). Fuentes: Wikipedia EN + oficiales de gobierno (reference-only; sin raw/).
- Índice de progreso: 523 tópicos en 170 iteraciones.

## ✅ COLA ROUND 35 — COMPLETA (13/13)
- [x] sustrato/mexico/vivienda
- [x] sustrato/estados-unidos/seguridad-publica
- [x] sustrato/canada/vivienda
- [x] dominio/edtech
- [x] dominio/foodtech
- [x] dominio/deep-tech
- [x] dominio/pymes
- [x] dominio/impresion-3d
- [x] rol/chief-innovation-officer
- [x] rol/system-administrator
- [x] rol/risk-manager
- [x] rol/sales-development-representative
- [x] rol/bookkeeper

## [2026-07-14] ingest | Round 36 — Reabastecimiento continuo (3 deepenings NA + 10 nodos nuevos)
- gap_analysis.py → 0 gaps en Round 35. Extendida taxonomía para Round 36 (3 deepenings NA + 10 nodos nuevos).
- Alcance sustrato: solo Norteamérica (respetado). Deepenings: sustrato/mexico/banca-desarrollo, sustrato/estados-unidos/banca-desarrollo, sustrato/canada/banca-desarrollo.
- 10 nodos nuevos: dominio/banca-de-inversion, dominio/mercados-emergentes, dominio/contratacion-publica, dominio/it-service-management, dominio/modelos-de-negocio, rol/developer-advocate, rol/security-architect, rol/analytics-engineer, rol/ux-researcher, rol/economist.
- Total Round 36: 13 temas ingestados (3 sustrato + 10 nodos). Fuentes: Wikipedia EN + oficiales de gobierno (reference-only; sin raw/).
- Índice de progreso: 536 tópicos en 171 iteraciones.

## ✅ COLA ROUND 36 — COMPLETA (13/13)
- [x] sustrato/mexico/banca-desarrollo
- [x] sustrato/estados-unidos/banca-desarrollo
- [x] sustrato/canada/banca-desarrollo
- [x] dominio/banca-de-inversion
- [x] dominio/mercados-emergentes
- [x] dominio/contratacion-publica
- [x] dominio/it-service-management
- [x] dominio/modelos-de-negocio
- [x] rol/developer-advocate
- [x] rol/security-architect
- [x] rol/analytics-engineer
- [x] rol/ux-researcher
- [x] rol/economist

## COLA ROUND 37 (13 temas — gap_analysis.py iter 172 → taxonomía extendida; sustrato solo NA) — COMPLETA ✅
### Sustrato (deepening nodos NA existentes)
- [x] sustrato/mexico — Entidades federativas / estados (coordinación fiscal, gobiernos estatales)
- [x] sustrato/estados-unidos — Estados / federalismo (gobiernos estatales, state law)
- [x] sustrato/canada — Pueblos indígenas (First Nations, Inuit, Métis, duty to consult)
### Dominio (nuevos nodos)
- [x] dominio/centros-de-datos — Data centers (Tier, colocation, sostenibilidad)
- [x] dominio/economia-social — Economía social y solidaria
- [x] dominio/finanzas-descentralizadas — DeFi
- [x] dominio/investigacion-clinica — Ensayos clínicos
- [x] dominio/derecho-del-consumidor — Derecho del consumidor
### Rol (nuevos nodos)
- [x] rol/copywriter — Copywriter / Redactor
- [x] rol/underwriter — Underwriter / Suscriptor
- [x] rol/credit-analyst — Credit Analyst
- [x] rol/mlops-engineer — MLOps Engineer
- [x] rol/deal-desk — Deal Desk

## ✅ COLA — Round 38 (COMPLETA 13/13 ✅)
Alcance sustrato: solo Norteamérica. 13 temas = 3 deepenings NA + 10 nodos nuevos.
- [x] sustrato/mexico/sector-servicios — Sector servicios México (~60% PIB)
- [x] sustrato/estados-unidos/proteccion-consumidor — Protección al consumidor EE.UU. (FTC/CFPB/CPSC)
- [x] sustrato/canada/sector-servicios — Sector servicios Canadá (~70% PIB)
- [x] dominio/marketing-digital — NODO NUEVO: SEO/SEM, performance, atribución
- [x] dominio/diversidad-equidad-inclusion — NODO NUEVO: DEI
- [x] rol/head-of-customer-success — NODO NUEVO: lidera org CS
- [x] dominio/bienestar-laboral — NODO NUEVO: employee wellbeing
- [x] dominio/gestion-del-talento — NODO NUEVO: talent management
- [x] dominio/customer-success — NODO NUEVO: disciplina CS
- [x] rol/payroll-manager — NODO NUEVO: nómina
- [x] rol/data-governance-lead — NODO NUEVO: gobernanza de datos
- [x] rol/investment-banker — NODO NUEVO: M&A/underwriting
- [x] rol/quality-manager — NODO NUEVO: calidad ISO 9001

### [2026-07-15] Round 38 — ITER 175 | 7 nodos nuevos (CIERRA Round 38)
- gap_analysis.py → 0 gaps previos. Ingestados los 7 nodos nuevos pendientes de la cola Round 38 (3 dominio + 4 rol), completando la ronda 13/13. (Los 6 previos ya ingestados en iter 173-174.)
- 3 nodos dominio nuevos: `dominio/bienestar-laboral/`, `dominio/gestion-del-talento/`, `dominio/customer-success/` (superstructura completa + página cada uno).
- 4 nodos rol nuevos: `rol/payroll-manager/`, `rol/data-governance-lead/`, `rol/investment-banker/`, `rol/quality-manager/` (superstructura completa + página cada uno).
- Alcance sustrato respetado (solo Norteamérica; Round 38 no agregó países). Reference-only (Wikipedia EN + BLS/OMS/ISO/DAMA/SHRM/Gainsight/CFA; sin raw/).
- **Round 38 COMPLETA (13/13).** Tópicos acumulados: 562 en 175 iteraciones.

## ✅ COLA ROUND 39 — COMPLETA (13/13)
### Sustrato (deepening nodos NA existentes)
- [x] sustrato/mexico — Pobreza y desigualdad (CONEVAL, medición multidimensional, programas sociales)
- [x] sustrato/estados-unidos — Pobreza y desigualdad (Census poverty line, desigualdad, safety net)
- [x] sustrato/canada — Pobreza y desigualdad (MBM, Canada Poverty Reduction Strategy)
### Dominio (nuevos nodos)
- [x] dominio/fidelizacion — Fidelización de clientes (loyalty, retención, programas de recompensas)
- [x] dominio/logistica-inversa — Logística inversa (devoluciones, economía circular)
- [x] dominio/comercio-mayorista — Comercio mayorista / distribución (B2B)
- [x] dominio/pesca-acuicultura — Pesca y acuicultura (industria, sostenibilidad)
- [x] dominio/salud-animal — Salud animal / veterinary (zoonosis, industria)
### Rol (nuevos nodos)
- [x] rol/hr-generalist — HR Generalist (operaciones de RRHH)
- [x] rol/penetration-tester — Penetration Tester / Red Team (seguridad ofensiva)
- [x] rol/credit-manager — Credit Manager (crédito, cobranza)
- [x] rol/process-engineer — Process Engineer (ingeniería de procesos)
- [x] rol/event-manager — Event Manager (MICE, producción de eventos)

## [2026-07-15] Round 39 — ITER 176 | gap_analysis extendido (taxonomía Round 39) + 13 ingests COMPLETOS
- gap_analysis.py (post-Round 38) = 0 huecos → se **EXTENDIÓ** `scripts/gap_analysis.py` (Round 39) con 3 deepenings sustrato NA (mexico→pobreza-desigualdad, estados-unidos→pobreza-desigualdad, canada→pobreza-desigualdad) + 10 nodos nuevos (dominio: fidelizacion, logistica-inversa, comercio-mayorista, pesca-acuicultura, salud-animal; rol: hr-generalist, penetration-tester, credit-manager, process-engineer, event-manager). ALCANCE respetado: sustrato = solo Norteamérica.
- LOOP 1 (sustrato NA): `mexico/pobreza-desigualdad.md`, `estados-unidos/pobreza-desigualdad.md`, `canada/pobreza-desigualdad.md` (deepenings; append a index/log de nodos existentes).
- LOOP 2 (dominio, 5 nuevos): `fidelizacion`, `logistica-inversa`, `comercio-mayorista`, `pesca-acuicultura`, `salud-animal` (superstructura completa: raw/, README, index, log).
- LOOP 3 (rol, 5 nuevos): `hr-generalist`, `penetration-tester`, `credit-manager`, `process-engineer`, `event-manager` (superstructura completa).
- Índices/logs de nodos + globales (root index.md/log.md) actualizados. Reference-only (Wikipedia EN + CONEVAL/Census/ESDC/StatCan/SHRM/OWASP; sin raw/).
- **Round 39 COMPLETA (13/13).** Tópicos acumulados: 575. ALCANCE sustrato = solo Norteamérica (respetado).

## ✅ COLA ROUND 40 — COMPLETA (13/13)
### Sustrato (deepening nodos NA existentes)
- [x] sustrato/mexico — Fronteras (frontera norte con EE.UU., T-MEC/USMCA, maquiladoras, Plan Frontera Sur, aduanas)
- [x] sustrato/estados-unidos — Fronteras (frontera sur CBP/USBP, frontera norte Canadá, USMCA, aduanas)
- [x] sustrato/canada — Fronteras (frontera terrestre más larga del mundo con EE.UU., CBSA, Windsor-Detroit/Peace Bridge)
### Dominio (nuevos nodos)
- [x] dominio/liderazgo — Liderazgo (teorías, estilos, desarrollo de líderes)
- [x] dominio/mercados-financieros — Mercados financieros (exchanges, microestructura, regulación SEC/ESMA/IOSCO)
- [x] dominio/finanzas-personales — Finanzas personales (presupuesto, inversión, retiro, planificación)
- [x] dominio/comunicacion-corporativa — Comunicación corporativa (medios, interna, crisis, reputación)
- [x] dominio/empresa-familiar — Empresa familiar (gobierno familiar, sucesión, protocolo)
### Rol (nuevos nodos)
- [x] rol/principal-engineer — Principal Engineer (ladder IC senior, arquitectura org)
- [x] rol/talent-acquisition-manager — Talent Acquisition Manager (lidera TA, sourcing, employer brand)
- [x] rol/compensation-manager — Compensation Manager (bandas salariales, job grading, equity)
- [x] rol/financial-planner — Financial Planner (CFP, retiro, inversiones, seguros)
- [x] rol/general-manager — General Manager (P&L de unidad de negocio/país)

## [2026-07-15] Round 40 — ITER 177 | gap_analysis extendido (taxonomía Round 40) + 13 ingests COMPLETOS
- gap_analysis.py (post-Round 39) = 0 huecos → se **EXTENDIÓ** `scripts/gap_analysis.py` (Round 40) con 3 deepenings sustrato NA (mexico→fronteras, estados-unidos→fronteras, canada→fronteras) + 10 nodos nuevos (dominio: liderazgo, mercados-financieros, finanzas-personales, comunicacion-corporativa, empresa-familiar; rol: principal-engineer, talent-acquisition-manager, compensation-manager, financial-planner, general-manager). ALCANCE respetado: sustrato = solo Norteamérica.
- LOOP 1 (sustrato NA): `mexico/fronteras.md`, `estados-unidos/fronteras.md`, `canada/fronteras.md` (deepenings; append a index/log de nodos existentes).
- LOOP 2 (dominio, 5 nuevos): `liderazgo`, `mercados-financieros`, `finanzas-personales`, `comunicacion-corporativa`, `empresa-familiar` (superstructura completa: raw/, README, index, log).
- LOOP 3 (rol, 5 nuevos): `principal-engineer`, `talent-acquisition-manager`, `compensation-manager`, `financial-planner`, `general-manager` (superstructura completa).
- Índices/logs de nodos + globales (root index.md/log.md) actualizados. Reference-only (Wikipedia EN + SRE/CBP/CBSA/SEC/CFP/SHRM/WorldatWork/McKinsey/HBR; sin raw/).
- **Round 40 COMPLETA (13/13).** Tópicos acumulados: 588. ALCANCE sustrato = solo Norteamérica (respetado).

## 📊 ÍNDICE DE PROGRESO (acumulado)
- **Tópicos ingeridos (acumulado): 588** (Round 40: +13 = 3 deepenings NA + 10 nodos nuevos).
- **Rondas:** 40 completas (Round 1..40).
- **Nodos sustrato (NA):** México 61 (+fronteras), EE.UU. 49 (+fronteras), Canadá 43 (+fronteras).
- **Nodos dominio:** ~145 (Round 40 +5 nuevos: liderazgo, mercados-financieros, finanzas-personales, comunicacion-corporativa, empresa-familiar).
- **Nodos rol:** ~135 (Round 40 +5 nuevos: principal-engineer, talent-acquisition-manager, compensation-manager, financial-planner, general-manager).
- **Organización:** 1 (ejemplo-empresa / NovaTech).
- **Alcance sustrato:** solo Norteamérica (MX/US/CA) en profundizaciones; otros países ya no se amplían salvo indicación.
- **Iteraciones totales:** 177.

## 🚦 ESTADO
- **Iteración actual:** 177 (Round 40 COMPLETA — 13/13 ingestados).
- **Última acción:** Round 40 iter 177 — 3 deepenings sustrato NA (fronteras MX/US/CA) + 10 nodos nuevos (5 dominio + 5 rol) ingestados; Round 40 COMPLETA (13/13). Tópicos acumulados: 588.
- **Bloqueos:** ninguno.
- **Cola:** Round 40 CERRADA (13/13). Próxima: `python3 scripts/gap_analysis.py`; si 0 → extender taxonomía (Round 41), o pausar hasta el próximo cron.

## ▶️ PRÓXIMA TAREA
- Round 40 COMPLETA (13/13). Siguiente paso de reabastecimiento: ejecutar `python3 scripts/gap_analysis.py`; si reporta 0 gaps → extender taxonomía (3 deepenings NA + 10 nodos nuevos) para Round 41, o pausar hasta el próximo cron. Mantener alcance sustrato = solo Norteamérica.
- Tras vaciar, re-correr `python3 scripts/gap_analysis.py`; si 0 → extender taxonomía para Round 41.
