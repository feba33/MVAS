# Registro de actividad (log.md)

Registro cronológico **append-only**: ingests, queries, lint passes.
Prefijo de entrada: `## [YYYY-MM-DD] <tipo> | <título>`
(parseable: `grep "^## \[" log.md | tail -5` → últimas 5 entradas).

## [2026-07-09] setup | Estructura inicial MVAS + patrón LLM Wiki
- Creado repo MVAS con 4 capas: sustrato / dominio / organización / rol.
- Integrado patrón LLM Wiki: capa `raw/` (fuentes inmutables), `index.md`,
  `log.md`, y `GUIA-HERMES.md` como esquema.
- Subcarpetas ejemplo sembradas en las 4 capas.
- Fuente del método guardada en `raw/llm-wiki.md`.

## [2026-07-09] ingest | El Financiero — 8 artículos (opinión)
- 3 → `dominio/finanzas/`: incertidumbre (T-MEC), t-mec-revision-anual-inversionistas, rentas-stock-desafios-vivienda.
- 5 → `sustrato/mexico/`: cdmx-nuevos-partidos, roxana-guzman-fracaso-primeras-horas, donde-esta-rocha-moya, crisis-climatica-salud-infantil, amlo-rocha-ismael-n.
- Autónomo (cronjob). Dedupe: sin duplicados previos. Cross-refs y frontmatter YAML aplicados.

## [2026-07-09] ingest | LGSM — Ley General de Sociedades Mercantiles (sustrato/mexico)
- 1 → `sustrato/mexico/`: `lgsm.md` (los 7 tipos de sociedad, reforma DOF 20-10-2023, SAS art. 260).
- Fuentes: Cámara de Diputados (oficial) + CICDE. Cross-ref a `dominio/leyes/` y `dominio/finanzas/`.
- Autónomo (cronjob). Reference-only (URL en frontmatter, sin archivos en raw/).

## [2026-07-09] ingest | Código de Comercio (CCom) — sustrato/mexico
- 1 → `sustrato/mexico/`: `codigo-de-comercio.md` (actos de comercio, contratos, títulos de crédito; reforma DOF 14-11-2025).
- Fuentes: Cámara de Diputados (oficial) + Gobierno.com.mx. Cross-ref a `lgsm.md` y `dominio/leyes/`.
- Autónomo (cronjob). Reference-only.

## [2026-07-09] ingest | LFPDPPP 2025 + Regulación de IA — sustrato/mexico
- 2 → `sustrato/mexico/`: `lfpdpdp.md` (nueva ley de protección de datos, DOF 20-03-2025, abroga la de 2010, INAI→Secretaría Anticorrupción) y `regulacion-ia.md` (iniciativas 2023-2025, enfoque por riesgo, marco de 3 niveles; confianza media).
- Fuentes: Hogan Lovells, Cámara de Diputados (LFPDPPP); CeCo y Mobile Time (IA). Reference-only.

## [2026-07-09] ingest | Valoración de empresas — dominio/finanzas
- 1 → `dominio/finanzas/`: `valoracion.md` (DCF, múltiplos EV/EBITDA-SDE-revenue, WACC, EV vs Equity, estructura de capital).
- Fuentes: Finance Interview Prep (2026) + CT Acquisitions (2026). Reference-only.

## [2026-07-09] ingest | Round 2 — 3 nodos nuevos (iter 76-78)
- `sustrato/argentina` (nuevo): `proteccion-datos-personales.md` — Ley 25.326, DNPDP/AAIP, adecuación UE 2003. Fuentes: Wikipedia (es).
- `dominio/sostenibilidad` (nuevo): `esg-marco.md` — ESG + CSRD/GRI/SASB/TCFD/ISSB. Fuentes: Wikipedia (en).
- `rol/compliance-officer` (nuevo): `compliance-officer.md` — GRC, AML, anticorrupción, ISO 37301. Fuentes: Wikipedia (en).
- Autónomo (cronjob). Reference-only (URL en frontmatter, sin raw/). Lint OK por construcción.

## [2026-07-09] ingest | Argentina — Impuestos y Aduanas (AFIP/ARCA) — iter 79
- 1 → `sustrato/argentina`: `impuestos-aduanas.md` — niveles de recaudación, DGI/DGA/DGRSS,
  IVA 21%, Ganancias, Bienes Personales, Monotributo, seguridad social, tributos aduaneros
  (DI/TE/IVA/IVA Adicional/Ganancias/IIBB), NCM, CUIT, RG 5617/2024; transición AFIP→ARCA (2024).
- Fuentes: Wikipedia (es) AFIP, Argentina.gob.ar Sistema Tributario, Arancely, Expat.com.
- Autónomo (cronjob). Reference-only.

## [2026-07-09] ingest | Colombia — protección de datos + impuestos (DIAN) — iter 80
- Nuevo nodo `sustrato/colombia` (superstructura completa: README, index, log, raw/).
- 2 páginas: `proteccion-datos.md` (Ley Estatutaria 1581/2012: habeas data art.15-20,
  SIC/Delegatura/RNBD, datos sensibles, transferencia internacional art.26, D.1377/2013·886/2014·1081/2015)
  y `impuestos.md` (DIAN, UVT $52.374, renta 35% PJ / 39% PN, IVA 19%, retención en la fuente
  2026, GMF 4x1000, RST Ley 1943/2018 + 2010/2019, Monotributo, NIT/RUT, facturación electrónica).
- Fuentes: Gestor Normativo Función Pública (Ley 1581, D.1377), portal DIAN, Gerencie.com.
- Autónomo (cronjob). Reference-only (URL en frontmatter, sin raw/).

## [2026-07-10] ingest | España — RGPD/AEPD + CNMV (nuevo nodo sustrato/españa) — iter 81
- Nuevo nodo `sustrato/españa` (superstructura completa: README, index, log, raw/).
- 2 páginas: `rgpd-aepd.md` (RGPD UE 2016/679 + LOPDGDD LO 3/2018 + AEPD: principios,
  derechos, transferencias internacionales, sanciones hasta 20M€/4%, derechos digitales) y
  `cnmv.md` (CNMV Ley 6/2002: supervisión del mercado de valores, protección del inversor,
  abuso de mercado, criptoactivos/MiCA, potestad sancionadora).
- Fuentes: AEPD (normativa, principios), European Commission (data protection), CNMV (portal), BOE Ley 6/2002.
- Autónomo (cronjob). Reference-only (URL en frontmatter, sin raw/).

## [2026-07-10] ingest | CFO — rol/cfo (nuevo nodo) — iter 84
- Nuevo nodo `rol/cfo` (superstructura completa: README, index, log, raw/).
- 1 → `rol/cfo`: `cfo.md` — Chief Financial Officer: estrategia financiera, FP&A, tesorería,
  reporting, estructura de capital; CRO/CIO/Treasurer reportan; evolución a socio estratégico.
- Fuentes: Wikipedia (en) "Chief financial officer".
- Autónomo (cronjob). Reference-only (URL en frontmatter, sin raw/).

## [2026-07-10] ingest | Head of People — rol/head-of-people (nuevo nodo) — iter 85
- Nuevo nodo `rol/head-of-people` (superstructura completa: README, index, log, raw/).
- 1 → `rol/head-of-people`: `head-of-people.md` — Head of People / VP People / CPO / CHRO:
  liderazgo estratégico de talento, cultura, total rewards y people operations; reporta al CEO;
  diferenciado de `rol/people-lead` (táctico-operativo).
- Fuentes (web, reference-only): FirstHR "Chief People Officer", Torchora "VP People",
  Pebl "VP of People", AIHR "Chief People Officer".
- Autónomo (cronjob). Reference-only (URL en frontmatter, sin raw/).
- **Cierra la cola Round 2** (último tema pendiente). Siguiente: gap analysis → Round 3.

## [2026-07-10] ingest | Chile — protección de datos + impuestos (SII) — iter 86
- Nuevo nodo `sustrato/chile` (superstructura completa: README, index, log, raw/).
- 2 → `sustrato/chile`: `proteccion-datos.md` (Ley 19.628 + reforma Ley 21.719, CPLT)
  y `impuestos.md` (SII: IVA 19%, Renta 1ª cat./global complementario, F29/F22, PPM).
- Fuentes (web, reference-only): leychile.cl 19.628, digital.gob.cl, sii.cl, BaseAPI F29.
- Autónomo (cronjob). Reference-only (URL en frontmatter, sin raw/).
- **LOOP 1 de Round 3 (capa sustrato).**

## [2026-07-10] ingest | Finanzas — Derivados + Mercados de capitales — iter 87
- 2 → `dominio/finanzas`: `derivados.md` (futuros/opciones/swaps/forwards, cobertura,
  apalancamiento, MEFF/CME/Eurex, OTC) y `mercados-capitales.md` (ECM/IPO, DCM/bonos,
  underwriting).
- Fuentes (web, reference-only): StrategyCenter, Estudyando, BBVA, Rankia.
- Autónomo (cronjob). Reference-only (URL en frontmatter, sin raw/).
- **LOOP 2 de Round 3 (capa dominio).**

## [2026-07-10] ingest | Roles — Product Owner + Scrum Master — iter 88

## [2026-07-10] ingest | Finanzas corporativas — M&A, valoración, tesorería — iter 90
- 1 → `dominio/finanzas/finanzas-corporativas.md`. Visión integrada (3 pilares) sobre maximizar valor de accionista; cruza con valoracion/mercados-capitales/PE-VC/derivados y rol/cfo.

## [2026-07-10] ingest | Computación — Estilos arquitectura + Bases de datos — iter 89
- 2 → `dominio/computacion`: `estilos-arquitectura.md` (monolito modular, SOA, microservicios,
  EDA, serverless; tabla de trade-offs) y `bases-datos.md` (SQL relacional, NoSQL, distribuidas,
  CAP, NewSQL).
- Fuentes (web, reference-only): Wikipedia (en) Microservices, Event-driven architecture,
  Database, NoSQL, SQL, CAP theorem, Distributed database.
- Autónomo (cronjob). Reference-only (URL en frontmatter, sin raw/).
- **LOOP 4 de Round 3 (capa dominio — continuación de computación).**
- 2 nodos nuevos `rol/product-owner` y `rol/scrum-master` (superstructura completa cada uno).
- 1 → `rol/product-owner`: `product-owner.md` — maximiza valor del producto, dueño del
  backlog/PBIs, voz del cliente, stakeholder; vs PM/Product Lead.
- 1 → `rol/scrum-master`: `scrum-master.md` — líder servicial, facilita eventos Scrum,
  remueve impedimentos, protege al equipo; vs Agile Coach/EM.
- Fuentes (web, reference-only): GeeksforGeeks, TeachingAgile, LinkedIn, Mr.Torras.
- Autónomo (cronjob). Reference-only (URL en frontmatter, sin raw/).
- **LOOP 3 de Round 3 (capa rol).** Cumple ≥3 bucles de ingest por corrida.


## [2026-07-10] ingest | Computación — Plataforma/SRE + Frontend — iter 92-93
- 2 → `dominio/computacion`: `plataforma-sre.md` (Ingeniería de Plataforma + SRE; IDP/golden
  paths, SLI/SLO/error budget, tabla DevOps vs SRE vs Platform Eng; cross-ref devops,
  estilos-arquitectura, bases-datos) y `frontend.md` (frameworks 2026 React/Vue/Svelte/
  Angular/Astro/Next.js, meta-frameworks, Core Web Vitals, tabla de decisión; cross-ref
  arquitectura, estilos-arquitectura, testing-qa, plataforma-sre).
- Fuentes (web, reference-only): Splunk, Gart Solutions, SwitchtoDevOps, OpenSpace, Urolime
  (plataforma-sre); Midrocket, DEV.to, Coderio, Pharos Production (frontend).
- Autónomo (cronjob). Reference-only (URL en frontmatter, sin raw/).
- **LOOP 7 de Round 3 (capa dominio — continuación de computación).**

## [2026-07-10] ingest | Marketing — Demand generation / paid media — iter 94
- 1 → `dominio/marketing/demand-generation.md`. Demand gen full-funnel vs lead gen; paid media (Google/LinkedIn/Meta); ABM + intent data; métricas (CPL, CAC, pipeline).
- Fuentes (web, reference-only): Geisheker (2026), Digital Scouts.
- Autónomo (cronjob). Reference-only (URL en frontmatter, sin raw/). **LOOP 1 de Round 3 (capa dominio — marketing).**

## [2026-07-10] ingest | Marketing — Analítica + Lifecycle/email — iter 95
- 2 → `dominio/marketing`: `analitica-marketing.md` (atribución: first/last/lineal/U-shaped/data-driven, multitouch, MMM, method stacking B2B 2026) y `lifecycle-email.md` (email disparado por comportamiento; etapas/triggers; retención y LTV).
- Fuentes (web, reference-only): MCP Analytics (2026), Improvado (2026), Sortment (2026), Enflow Digital (2025).
- Autónomo (cronjob). Reference-only (URL en frontmatter, sin raw/). **LOOP 2 de Round 3 (capa dominio — marketing).**

## [2026-07-10] ingest | Leyes — Derecho societario + laboral — iter 96-97
- 2 → `dominio/leyes`: `derecho-societario.md` (tipos LGSM SA/SAPI/SAS/SRL, órganos, gobierno corporativo, levantamiento del velo) y `derecho-laboral.md` (LFT vigente 14-05-2026; outsourcing/REPSE, jornada/salario/PTU, IMSS/INFONAVIT, rescisión, justicia laboral, reforma jornada 2026).
- Fuentes (web, reference-only): TYP Advisers, RMS Abogados (societario); Lledías Abogados, Cámara de Diputados LFT (laboral).
- Autónomo (cronjob). Reference-only (URL en frontmatter, sin raw/). **LOOP 3-4 de Round 3 (capa dominio — leyes).**

## [2026-07-10] ingest | Leyes — Cumplimiento y Regulación — iter 98
- 1 → `dominio/leyes/cumplimiento-regulacion.md`. Compliance transversal; ISO 37301 (CMS certificable, PDCA); enfoque basado en riesgo; DOJ/UK Bribery Act; vs ISO 37001.
- Fuentes (web, reference-only): ISO 37301:2021, Audit Advisor. **LOOP 5 de Round 3 (capa dominio — leyes).**

## [2026-07-10] ingest | Contabilidad — Consolidación + Tesorería — iter 99
- 2 → `dominio/contabilidad`: `consolidacion.md` (control=obligación, métodos, eliminaciones intercompañía, NIIF 10/3) y `tesoreria.md` (liquidez, working capital, cash forecasting, TMS/ERP).
- Fuentes (web, reference-only): Rural Caja, DECAP, Growth Operators, J.P. Morgan. **LOOP 6 de Round 3 (capa dominio — contabilidad).**

## [2026-07-10] ingest | Diseño — Design systems + UX writing — iter 100
- 2 → `dominio/diseno`: `design-systems.md` (single source of truth, Atomic Design, design tokens, component/pattern library) y `ux-writing.md` (microcopy, voice & tone, claridad/conversión).
- Fuentes (web, reference-only): Bornfight, NN/g, Parallel, Designer Daily. **LOOP 7 de Round 3 (capa dominio — diseño).**

## [2026-07-10] ingest | NODO NUEVO dominio/juridico — Jurídico interno — iter 101
- Creado nodo `dominio/juridico` con superstructura completa (README, index, log, raw/).
- 1 página: `juridico-interno.md`. Función in-house; jerarquía GC/CLO → counsel → legal ops; contratos, M&A, gobernanza, litigios, investigaciones, abogados externos.
- Fuentes (web, reference-only): Streamline AI, CaseFox, Torchora. **LOOP 8 de Round 3 (capa dominio — juridico).**

## [2026-07-10] ingest | NODO NUEVO dominio/estrategia — Estrategia/OKRs — iter 102
- Creado nodo `dominio/estrategia` con superstructura completa (README, index, log, raw/).
- 1 página: `estrategia-okr.md`. OKRs (prioridades medibles, ciclo frecuente) + Hoshin Kanri (despliegue/catchball/PDCA); OGSM, Balanced Scorecard, KPIs lag; brecha de ejecución.
- Fuentes (web, reference-only): Operational Excellence Consulting, iSixSigma, Workpath. **LOOP 9 de Round 3 (capa dominio — estrategia).**

## [2026-07-10] ingest | NODO NUEVO rol/design-lead — Design Lead (LOOP 10)
- Creado nodo `rol/design-lead`. 1 página: `design-lead.md`. Visión/estrategia de diseño, liderazgo/mentoría, research, prototyping, abogacía UX. Fuentes: LinkedIn (reference-only). **LOOP 10 de Round 3 (capa rol).**

## [2026-07-10] ingest | NODO NUEVO rol/marketing-manager — Marketing Manager (LOOP 11)
- Creado nodo `rol/marketing-manager`. 1 página: `marketing-manager.md`. Estrategia/ejecución/optimización de marketing; brand, campañas, AI fluency, revenue. Fuentes: LHH, The Interview Guys (reference-only). **LOOP 11 de Round 3 (capa rol).**

## [2026-07-10] ingest | NODO NUEVO rol/ops-lead — Ops Lead (LOOP 12)
- Creado nodo `rol/ops-lead`. 1 página: `ops-lead.md`. Diseña/controla producción; eficiencia, procesos, cadena, mejora continua. Fuentes: Wikipedia 'Operations management' (reference-only). **LOOP 12 de Round 3 (capa rol).**

## [2026-07-10] ingest | NODO NUEVO rol/support-lead — Support / CX Lead (LOOP 13)
- Creado nodo `rol/support-lead`. 1 página: `support-lead.md`. Servicio al cliente; calidad por retención; CSAT/NPS; vs customer-success. Fuentes: Wikipedia 'Customer service' (reference-only). **LOOP 13 de Round 3 (capa rol).**

## [2026-07-10] ingest | NODO NUEVO rol/reclutador — Recruiter / Talent Acquisition (LOOP 14)
- 1 página: `reclutador.md`. Proceso identificar/sourcer/screening/entrevistar/contratar; AI sourcing. Fuentes: Wikipedia 'Recruitment' (reference-only). **LOOP 14 de Round 3 (capa rol).**

## [2026-07-10] ingest | sustrato/chile — Marco general del país (iter 108 / LOOP 15)
- Nodo existente `sustrato/chile`. 1 página añadida: `chile-general.md` (economía ingresos altos, miembro OCDE, competitividad, libertad económica, TLC). Fuentes: Wikipedia Economy of Chile (en/es). **LOOP 15 de Round 3 (capa sustrato — chile).**

## [2026-07-10] ingest | sustrato/chile — Ecosistema de emprendimiento (iter 109 / LOOP 16)
- Nodo existente `sustrato/chile`. 1 página añadida: `chile-emprendimiento.md` (Start-Up Chile/CORFO, PyMEs, Régimen SIMPLE 2025). Fuentes: Wikipedia, SII (reference-only). **LOOP 16 de Round 3 (capa sustrato — chile). Restan 1 (organización/caso: NovaTech ya existe).**

## [2026-07-10] Round 4 — ITER 111 | NODOS NUEVOS sustrato/peru + sustrato/uruguay (LOOP 1)
- Creados nodos `sustrato/peru` y `sustrato/uruguay` con superstructura completa (README, index, log, raw/).
- `sustrato/peru`: `proteccion-datos.md` (Ley N.° 29733 + Reglamento DS 003-2013-JUS; MINJUS/DIGEPDP, ANPD) e `impuestos.md` (SUNAT: IGV 18%, Renta 29,5%, RUC).
- `sustrato/uruguay`: `proteccion-datos.md` (Ley N.° 18.331 + URCDP) e `impuestos.md` (DGI: IVA 22%, IRAE 25%, IRPF, Patrimonio).
- Fuentes web (reference-only): MINJUS, SUNAT (gob.pe), URCDP/DGI (gub.uy), Wikipedia (es). **LOOP 1 de Round 4 (capa sustrato).**

## [2026-07-10] Round 4 — ITER 112 | NODOS NUEVOS dominio/economia, estadistica, project-management, negociacion (LOOP 2)
- Creados 4 nodos `dominio/` con superstructura completa (README, index, log, raw/).
- `dominio/economia`: `macroeconomia.md` (PIB, inflación, desempleo, política monetaria, bancos centrales) + `indicadores-ciclo-fiscal.md` (política fiscal, déficit/deuda, indicadores, ciclo).
- `dominio/estadistica`: `estadistica-ciencia-datos.md` (descriptiva, probabilidad, inferencia, data science).
- `dominio/project-management`: `gestion-proyectos.md` (ciclo de vida, triple restricción, waterfall/ágil, PMBOK/PMP).
- `dominio/negociacion`: `negociacion.md` (método Harvard, BATNA, ZOPA).
- Fuentes web (reference-only): Wikipedia (es), Program on Negotiation (Harvard). **LOOP 2 de Round 4 (capa dominio).**

## [2026-07-10] Round 4 — ITER 113 | NODOS NUEVOS rol/product-marketing-manager + rol/data-scientist (LOOP 3)
- Creados 2 nodos `rol/` con superstructura completa (README, index, log, raw/).
- `rol/product-marketing-manager`: `product-marketing-manager.md` (PMM: GTM, posicionamiento, mensaje, sales enablement).
- `rol/data-scientist`: `data-scientist.md` (estadística + ML + programación; modelado predictivo).
- Fuentes web (reference-only): Wikipedia (es), Product Marketing Alliance, IBM. **LOOP 3 de Round 4 (capa rol).**
- **Round 5 COMPLETO (10/10 temas en 3 bucles).** Siguiente paso: ejecutar `python3 scripts/gap_analysis.py` para abrir Round 6.

## [2026-07-11] Round 6 — ITER 118 | NODOS NUEVOS dominio/salud + dominio/educacion + dominio/transporte + dominio/telecomunicaciones (LOOP 1)
- Creados 4 nodos `dominio/` con superstructura completa (README, index, log, raw/).
- `dominio/salud`: `salud.md` (sistemas, seguros médicos, farmacia, telemedicina).
- `dominio/educacion`: `educacion.md` (modelos, niveles, edtech, política educativa).
- `dominio/transporte`: `transporte.md` (modos, logística urbana, aviación, regulación).
- `dominio/telecomunicaciones`: `telecomunicaciones.md` (redes fijas/móviles, 5G, espectro, regulación).
- Fuentes web (reference-only): Wikipedia (Health care/Education/Transport/Telecommunications), WHO, OECD, ITF, ITU. **LOOP 1 de Round 6 (capa dominio).** Cola Round 6 restante: 3 temas (rol x3).

## [2026-07-11] Round 6 — ITER 119 | NODOS NUEVOS rol/chief-data-officer + rol/chief-sustainability-officer + rol/chief-risk-officer (LOOP 2)
- Creados 3 nodos `rol/` con superstructura completa (README, index, log, raw/).
- `rol/chief-data-officer`: `chief-data-officer.md` (gobierno de datos, analítica, democratización, IA).
- `rol/chief-sustainability-officer`: `chief-sustainability-officer.md` (ESG, descarbonización, reporting climático, responsabilidad social).
- `rol/chief-risk-officer`: `chief-risk-officer.md` (riesgo enterprise, ERM, crédito/mercado/operativo, continuidad).
- Fuentes web (reference-only): Wikipedia (Chief data/sustainability/risk officer), DAMA, UNEP, GARP. **LOOP 2 de Round 6 (capa rol).** Cola Round 6 VACÍA (7/7 temas ingestados en 2 bucles).
- **Round 6 COMPLETO (7/7 temas: dominio x4 + rol x3).** Reabastecimiento: re-ejecutar `python3 scripts/gap_analysis.py` para abrir Round 7 (taxonomía probablemente agotada; extender si aplica).


## [2026-07-10] Round 5 — ITER 114 | gap_analysis (plan) + NODOS NUEVOS sustrato/ecuador + sustrato/portugal (LOOP 1)
- Reabastecimiento: extendida la taxonomía de `scripts/gap_analysis.py` (6 nodos nuevos sugeridos: seguros, energia, inmobiliario, retail, manufactura [+ roles cio/coo/cmo y países ecuador/portugal]). Re-ejecutado → 10 huecos/nodos nuevos. Abierta cola Round 5 (10 temas: sustrato x2, dominio x5, rol x3).
- Creados nodos `sustrato/ecuador` y `sustrato/portugal` con superstructura completa (README, index, log, raw/).
- `sustrato/ecuador`: `proteccion-datos.md` (LOPDP, R.O. Sup. 459/2021, vigencia 2023; Superintendencia de Protección de Datos Personales) e `impuestos.md` (SRI: IVA 15%/5%/0%, Renta ~25%, RUC).
- `sustrato/portugal`: `proteccion-datos.md` (RGPD + Lei 58/2019; CNPD) e `impuestos.md` (AT: IRS hasta 48%, IRC 21%, IVA 23%/13%/6%).
- Fuentes web (reference-only): Gob.ec, SRI, CNPD, Portal das Finanças, gov.pt, Wikipedia. **LOOP 1 de Round 5 (capa sustrato).** Cola Round 5 restante: 8 temas (dominio x5, rol x3).

## [2026-07-11] Round 5 — ITER 115 | NODOS NUEVOS dominio/seguros + dominio/energia + dominio/inmobiliario + dominio/retail + dominio/manufactura (LOOP 2)
- Creados 5 nodos `dominio/` con superstructura completa (README, index, log, raw/).
- `dominio/seguros`: `seguros.md` (vida, P&C, reaseguro, actuarial, Solvency II).
- `dominio/energia`: `energia.md` (renovables, oil&gas, redes, regulación FERC/CRE/SENER).
- `dominio/inmobiliario`: `bienes-raices.md` (residencial/comercial, REITs, cap rate, ciclos).
- `dominio/retail`: `retail.md` (omnicanal, merchandising, e-commerce, última milla).
- `dominio/manufactura`: `manufactura.md` (lean, Six Sigma/DMAIC, Industry 4.0, cadena de producción).
- Fuentes web (reference-only): Wikipedia (Insurance/Energy/Real estate/Retail/Manufacturing), EIOPA, FERC, REIT.com, McKinsey, SixSigma.us. **LOOP 2 de Round 5 (capa dominio).** Cola Round 5 restante: 3 temas (rol x3).

## [2026-07-11] Round 5 — ITER 116 | NODOS NUEVOS rol/cio + rol/coo + rol/cmo (LOOP 3)
- Creados 3 nodos `rol/` con superstructura completa (README, index, log, raw/).
- `rol/cio`: `cio.md` (estrategia de TI, transformación digital, datos/ciberseguridad; reporta a CEO; vs CTO).
- `rol/coo`: `coo.md` (ejecuta estrategia, opera día a día, excelencia operativa; tipologías integrator/heir apparent).
- `rol/cmo`: `cmo.md` (marca, demanda, GTM, customer insight, martech; ROI del marketing).
- Fuentes web (reference-only): Wikipedia (Chief information/operating/marketing officer), Investopedia (CIO). **LOOP 3 de Round 5 (capa rol).** Cola Round 5 VACÍA (8/8 temas ingestados en 3 bucles).
- **Round 5 COMPLETO (10/10 temas: sustrato x2 + dominio x5 + rol x3).** Reabastecimiento: re-ejecutar `python3 scripts/gap_analysis.py` para abrir Round 6.


## [2026-07-11] Round 7 — ITER 120 | gap_analysis extendido + 5 ingests (3 capas)
- Reabastecimiento: taxonomía de `scripts/gap_analysis.py` agotada (0 huecos) → extendida con
  3 huecos sustrato NA (mexico→energia, estados-unidos→healthcare, canada→healthcare) + 10 nodos
  nuevos (dominio: agronegocios, construccion, turismo, medios-comunicacion, automotriz,
  gobierno-publico; rol: ciso, general-counsel, brand-manager, business-development).
- Esta iter 120 ingestó 5 temas cubriendo las 3 capas:
  - [sustrato] `sustrato/mexico/energia.md` (página nueva en nodo existente): CFE, PEMEX,
    SENER/CRE/CNH/ASEA, reforma 2013, renovables (fuente: Wikipedia ES).
  - [dominio] `dominio/agronegocios/` (nuevo nodo): cadena agroalimentaria, agtech, commodities.
  - [dominio] `dominio/construccion/` (nuevo nodo): ciclo AEC, contratación, costos, tendencias.
  - [rol] `rol/ciso/` (nuevo nodo): CISO, dueño del riesgo de seguridad/ciberseguridad.
  - [rol] `rol/general-counsel/` (nuevo nodo): GC/CLO, asesor legal máximo, gobierno corporativo.
- Reference-only (URL en frontmatter; sin raw/). Superstructura completa en cada nodo nuevo.
- Cola Round 7 restante: 8 temas (sustrato x3, dominio x4, rol x2). Próxima corrida retoma iter 121.

## [2026-07-11] Round 7 — ITER 121 | 3 ingests (sustrato + sustrato + dominio)
- 3 temas ingestados cubriendo sustrato (x2) + dominio (x1). Cola Round 7 restante: 5 temas (sustrato x1, dominio x3, rol x2).
  - [sustrato] `sustrato/estados-unidos/salud.md` (nodo existente): healthcare EE.UU. — FDA, CMS, HIPAA, Medicare A/B/C/D, Medicaid, ACA; ~17.8% PIB; sin universal.
  - [sustrato] `sustrato/canada/salud.md` (nodo existente): medicare single-payer (Canada Health Act 1984), Health Canada, provincias, CADTH→Canada's Drug Agency.
  - [dominio] `dominio/turismo/` (nuevo nodo): turismo y hospitalidad — industria, segmentos, cadena de valor, sostenibilidad; superstructura completa.
- Reference-only (URL en frontmatter; sin raw/). Próxima corrida: iter 122 → dominio/medios-comunicacion.

## [2026-07-11] Round 7 — ITER 122 | 5 ingests (dominio x3 + rol x2) — CIERRA COLA ROUND 7
- 5 temas ingestados cubriendo dominio (x3) + rol (x2). **Cola Round 7 VACÍA (13/13 temas en 3 iteraciones: 120, 121, 122).**
  - [dominio] `dominio/medios-comunicacion/` (nuevo nodo): mass media, publishing, news media, modelos de negocio, concentración/media capture.
  - [dominio] `dominio/automotriz/` (nuevo nodo): industria automotriz y movilidad — OEM, Tier 1/2/3, VEs, autonomía, MaaS.
  - [dominio] `dominio/gobierno-publico/` (nuevo nodo): sector público, SOEs, administración pública, procurement, políticas.
  - [rol] `rol/brand-manager/` (nuevo nodo): Brand Manager — percepción de marca, brand equity, cadena de suministro.
  - [rol] `rol/business-development/` (nuevo nodo): Business Development — crecimiento vía relaciones, mercados, partnerships.
- Reference-only (URL en frontmatter; sin raw/). Superstructura completa en cada nodo nuevo.
- **Round 7 COMPLETO.** Siguiente paso de reabastecimiento: re-ejecutar `python3 scripts/gap_analysis.py` (taxonomía ya ampliada en iter 120); si devuelve 0, ampliar NEW_NODES/TAXONOMY para Round 8 o detener.

## [2026-07-11] Round 8 — ITER 123 | gap_analysis extendido + 13 ingests (3 capas) — REANUDA bucle
- Reabastecimiento: `gap_analysis.py` (iter 122) devolvió **0 huecos reales y 0 nodos nuevos** → se **EXTENDIÓ** la taxonomía de `scripts/gap_analysis.py` (Round 8) con 3 huecos sustrato NA (mexico→banca, estados-unidos→sector-tecnologia, canada→sector-bancario) + 10 nodos nuevos (dominio: biotecnologia, mineria, defensa-seguridad, aeroespacial, fintech; rol: chief-product-officer, vp-engineering, vp-sales, chief-of-staff, account-executive). **Alcance respetado:** sustrato = solo Norteamérica; NO se agregan países fuera de NA.
- 13 temas ingestados cubriendo las 3 capas:
  - [sustrato] `sustrato/mexico/banca-sistema-financiero.md` (nodo existente): Banxico, CNBV, banca múltiple, Sofipos/ITF, SPEI/CoDi.
  - [sustrato] `sustrato/estados-unidos/sector-tecnologia.md` (nodo existente): Big Tech, antitrust DOJ/FTC, Section 230, IA (EO/NIST RMF), CHIPS Act 2022, privacidad (CCPA), controles de chips (BIS).
  - [sustrato] `sustrato/canada/sector-bancario.md` (nodo existente): Big Six, OSFI, Bank of Canada, CDIC, Bank Act Schedule I/II/III.
  - [dominio] `dominio/biotecnologia/` (nuevo): biofármacos, agtech, genómica/CRISPR, CRO/CDMO, FDA/EMA.
  - [dominio] `dominio/mineria/` (nuevo): extracción, commodities, cadena de valor, minerales críticos, ESG.
  - [dominio] `dominio/defensa-seguridad/` (nuevo): industria armamentística, dual-use, primes, procurement/ITAR, drones/IA.
  - [dominio] `dominio/aeroespacial/` (nuevo): aeronáutica civil/defensa, NewSpace, lanzaderas, FAA/EASA.
  - [dominio] `dominio/fintech/` (nuevo): pagos, banca digital, lending, regtech, cripto, open banking.
  - [rol] `rol/chief-product-officer/` (nuevo): CPO, dueño de estrategia de producto.
  - [rol] `rol/vp-engineering/` (nuevo): VP Engineering, liderazgo de ingeniería y entrega.
  - [rol] `rol/vp-sales/` (nuevo): VP Sales, cuota/pipeline/GTM; vs CRO.
  - [rol] `rol/chief-of-staff/` (nuevo): Chief of Staff, socio estratégico del CEO.
  - [rol] `rol/account-executive/` (nuevo): Account Executive, cierre de venta y cuota.
- Reference-only (URL en frontmatter; sin raw/). Superstructura completa en cada nodo nuevo.
- **Round 8 COMPLETO (13/13 temas en 3 bucles: LOOP 1 sustrato, LOOP 2 dominio, LOOP 3 rol).** Cola Round 8 VACÍA. Siguiente paso: re-ejecutar `python3 scripts/gap_analysis.py`; si devuelve 0, ampliar taxonomía para Round 9 o pausar.

## [2026-07-11] ingest | Round 9 — 13 ingests (3 capas: sustrato/NA + dominio + rol)
- Gap analysis (iter 123) = 0 huecos → extendida la taxonomía de `scripts/gap_analysis.py` (Round 9):
  3 deepenings sustrato NA (mexico→pensiones-afore, estados-unidos→vivienda-real-estate, canada→recursos-naturales)
  + 10 nodos nuevos (dominio: emprendimiento, relaciones-publicas, innovacion, experiencia-cliente, comercio-internacional;
  rol: product-manager, financial-analyst, head-of-growth, vp-marketing, tech-lead).
- 13 temas ingestados cubriendo las 3 capas (LOOP 1 sustrato, LOOP 2 dominio, LOOP 3 rol).
- Reference-only (URL en frontmatter; sin raw/). Superstructura completa en cada nodo nuevo.
- Alcance respetado: sustrato = solo Norteamérica; NO se agregaron países fuera de NA.

## [2026-07-11] ingest | Round 10 — LOOP 1 (sustrato NA) — 3 ingests
- Gap analysis (iter 124) = 0 → extendida taxonomía Round 10 (iter 125): 3 deepenings NA + 10 nodos nuevos.
- 3 temas sustrato (deepening de nodos NA existentes):
  - `sustrato/mexico/telecomunicaciones.md` — IFT eliminado (reforma 2024); LMTR aprobada 01-07-2025 abroga LFTR 2014; CRT sustituye al IFT bajo la ATDT; espectro, concesiones, conectividad.
  - `sustrato/estados-unidos/energia.md` — DOE (política/confiabilidad grid), FERC (electricidad/gas interestatal, licencia hydro, PURPA), EIA (estadística); mix gas/nuclear~20%/renovables; mayor productor de petróleo y gas.
  - `sustrato/canada/comercio-exterior.md` — Global Affairs Canada + CUSMA; aranceles EE.UU. 2025-26 (35% sobre algunos bienes), Canadá elimina retaliación sobre bienes CUSMA desde 01-09-2025; revisión CUSMA julio 2026.
- Reference-only (URL en frontmatter; sin raw/). Alcance respetado: sustrato = solo Norteamérica.
- Siguiente: LOOP 2 (dominio) — analitica-negocio, gobierno-corporativo, ia-generativa, cultura-organizacional, gestion-cambio (iter 127).

## [2026-07-11] ingest | Round 10 — LOOP 2 (dominio) — 5 nodos nuevos
- 5 nodos `dominio/` creados con superstructura completa (README, index, log, raw/):
  - `dominio/analitica-negocio/` — Business Analytics/BI: dashboards, KPIs, descriptiva→prescriptiva, brecha insight→acción (90.5% Fortune 1000 prioriza data/AI, <24% cultura data-driven).
  - `dominio/gobierno-corporativo/` — Junta de directores, deberes fiduciarios (cuidado/lealtad), shareholder primacy vs stakeholder (Business Roundtable 2019), ESG como frontera fiduciaria, SOX.
  - `dominio/ia-generativa/` — GenAI: de predictiva→generativa (LLMs/difusión/multimodal), adopción empresarial 2025, riesgos (Deloitte 4 categorías), agentes.
  - `dominio/cultura-organizacional/` — Modelo de Schein (artefactos/valores/supuestos); la cultura es lo más difícil de cambiar.
  - `dominio/gestion-cambio/` — Lewin, Kotter 8 pasos, ADKAR (Prosci), McKinsey 7S; ~70% de transformaciones fallan (cultura barrera).
- Reference-only (URL en frontmatter; sin raw/). Cross-refs a finanzas, estrategia, sostenibilidad, rol/board-member, ciso, head-of-people, data-analyst.
- Siguiente: LOOP 3 (rol) — controller, project-manager, data-analyst, board-member, auditor-interno (iter 128).

## [2026-07-11] ingest | Round 10 — LOOP 3 (rol) — 5 nodos nuevos
- 5 nodos `rol/` creados con superstructura completa (README, index, log, raw/):
  - `rol/controller/` — Controlador financiero: reporting, cierre mensual (6-10 días mid-market), GAAP, controles internos, SOX, CPA/CMA.
  - `rol/project-manager/` — Gestor de proyectos: 5 responsabilidades (alcance, equipo, progreso, stakeholders, riesgos); ciclo de vida; PMP/PMBOK; agile/scrum.
  - `rol/data-analyst/` — Analista de datos: inspeccionar/limpiar/transformar/modelar datos para decisiones; SQL, BI, dashboards, data storytelling.
  - `rol/board-member/` — Miembro de la Junta: órgano rector, directores no ejecutivos elegidos por accionistas, responsabilidad última de gestión, deberes fiduciarios, comités.
  - `rol/auditor-interno/` — Auditor interno: aseguramiento independiente (reporta a comité de auditoría), tres líneas, COSO, normas IIA.
- Reference-only (URL en frontmatter; sin raw/). Cross-refs a contabilidad, gobierno-corporativo, cfo, ceo, chief-risk-officer, analitica-negocio, gestion-cambio.
- Siguiente (iter 129): Round 10 COMPLETA (cola 13/13). Ejecutar `scripts/gap_analysis.py`; si 0 huecos → extender taxonomía para Round 11.

## [2026-07-11] ingest | Round 11 — ITER 130 | LOOP 1 (sustrato NA) — 3 ingests
- 3 temas sustrato (deepening de nodos NA existentes):
  - `sustrato/mexico/inversion-extranjera.md` — IED en México: LIE (sectores reservados, RNIE), IMMEX (importación temporal sin IGI/IVA), >USD$40B IED 3T2025, maquila.
  - `sustrato/mexico/sector-manufacturero.md` — Manufactura MX: maquiladora/IMMEX, >USD$300B exportados 2024, clústeres, nearshoring.
  - `sustrato/estados-unidos/agricultura.md` — USDA, Farm Bill, subsidios/price supports, 2.04M granjas, exportador neto.
- Reference-only (URL en frontmatter; sin raw/). Alcance respetado: sustrato = solo Norteamérica (los 3 temas son NA). Restan 11 temas de Round 11 (canada/inmigracion + 5 dominio + 5 rol). Próxima tarea (iter 131): sustrato/canada/inmigracion (cierra LOOP 1 sustrato) → luego LOOP 2 dominio.

## [2026-07-11] ingest | Round 11 — ITER 131 | LOOP 1 (sustrato NA) cierra — inmigración Canadá
- 1 tema sustrato (deepening de nodo NA existente): `sustrato/canada/inmigracion.md` — IRCC/IRPA, Express Entry (CRS), PNP, TFWP (LMIA/ESDC), IMP, study permits, PGWP, doble ciudadanía, niveles >400k/año. **Cierra LOOP 1 sustrato (4/4).** Restan 10 temas (5 dominio + 5 rol).

## [2026-07-11] ingest | Round 11 — ITER 131 | LOOP 2 (dominio) — 5 nodos nuevos
- 5 nodos `dominio/` creados con superstructura completa (README, index, log, raw/):
  - `dominio/banca/` — Banca: comercial, inversión, central, digital; depósitos, crédito, pagos, Basilea III/IV.
  - `dominio/capital-riesgo/` — VC y Private Equity: ciclo del fondo (fundraising→exit), LP/GP, rondas, buyouts, J-curve.
  - `dominio/cadena-suministro/` — Supply Chain Management: plan-procure-make-deliver-return, S&OP/IBP, procurement, resiliencia.
  - `dominio/consultoria/` — Consultoría de gestión: estrategia, operaciones, M&A, tecnología; MBB/Big Four; up-or-out.
  - `dominio/servicios-profesionales/` — Servicios profesionales: derecho, contabilidad, arquitectura, ingeniería; partnership, billable hours.
- Reference-only (URL en frontmatter; sin raw/). Cross-refs a finanzas, logistica, estrategia, servicios-profesionales. **LOOP 2 dominio COMPLETO (5/5).** Restan 5 temas (rol).

## [2026-07-11] ingest | Round 11 — ITER 131 | LOOP 3 (rol) — 5 nodos nuevos
- 5 nodos `rol/` creados con superstructura completa (README, index, log, raw/):
  - `rol/chief-compliance-officer/` — CCO: dueño del programa de cumplimiento, AML/sanciones, reporte a CEO/junta; ISO 37301/37001.
  - `rol/treasurer/` — Treasurer: liquidez, cash management, financiamiento, cobertura riesgo tasa/divisa; reporta a CFO.
  - `rol/chief-investment-officer/` — CIO de inversiones: estrategia de inversión, asset allocation, portafolio, deber fiduciario.
  - `rol/head-of-research/` — Head of Research / I+D: estrategia de investigación, pipeline, IP; motor de innovación.
  - `rol/chief-digital-officer/` — CDO: estrategia y transformación digital, CX, e-commerce, datos; vs CIO/Chief Data Officer.
- Reference-only (URL en frontmatter; sin raw/). Cross-refs a cfo, cio, cto, cmo, compliance-officer, finanzas. **LOOP 3 rol COMPLETO (5/5).**
- **Round 11 COMPLETO (14/14 temas en 3 bucles: LOOP 1 sustrato NA, LOOP 2 dominio x5, LOOP 3 rol x5).** Cola Round 11 VACÍA → reabastecimiento (gap_analysis.py).

## [2026-07-12] ingest | Round 12 — ITER 132 | sustrato/mexico SAT (LOOP 1) — 1 ingest
- 1 tema sustrato (deepening de nodo NA existente): `sustrato/mexico/sat.md` — SAT (Servicio de Administración Tributaria): órgano desconcentrado de la SHCP (Ley del SAT, 1997), máxima autoridad fiscal; administra RFC, CFF, CFDI 4.0 (e.firma, CIEC, Buzón Tributario, Mi Contabilidad); recauda ISR/IVA/IEPS/aranceles y cuotas IMSS-ISSSTE; carga tributaria baja (~13-14% PIB). Complementa `regimen-fiscal.md`. Reference-only (URL en frontmatter; sin raw/).
- **Round 12 LOOP 1 sustrato NA (1/3):** mexico/sat hecho; restan estados-unidos/inmigracion y canada/transporte. Próxima tarea (iter 133): sustrato/estados-unidos/inmigracion.

## [2026-07-12] ingest | Round 12 — ITER 133 | sustrato/estados-unidos inmigración (LOOP 1) — 1 ingest
- 1 tema sustrato (deepening de nodo NA existente): `sustrato/estados-unidos/inmigracion.md` — USCIS (agencia DHS, sucesora del INS 2002), ICE/CBP; green card/LPR (~12.8M 2024, ~9M elegibles ciudadanía; vías familia/empleo/EB/diversity/refugiado; ajuste de estatus o consular; ciudadanía 1-5 años); H-1B (specialty occupation, cap 85k, patrocinio, dual intent, lottery); H-2A (agrícola temporal, sin cap, empleador paga vivienda/comida/transporte, DOL audita); VWP (42 países, ESTA). Reference-only.
- **Round 12 LOOP 1 sustrato NA (2/3):** estados-unidos/inmigracion hecho; resta canada/transporte. Próxima tarea (iter 134): sustrato/canada/transporte.

## [2026-07-12] ingest | Round 12 — ITER 134 | sustrato/canada transporte (LOOP 1) — 1 ingest
- 1 tema sustrato (deepening de nodo NA existente): `sustrato/canada/transporte.md` — Transport Canada (depto federal carretera/ferrocarril/marítimo/aéreo, desde 1935/36; reorg 1994 privatizó CN y descentralizó puertos/aeropuertos); ferrocarril 49,422 km (solo 129 km eléctricos), dos Class I (CN, CPKC — única que conecta CA-US-MX), Via Rail (corona) pasajeros; Port of Vancouver (mayor de Canadá, 4º NA, 170+ economías); aviación civil regulada por TC, ATC por NAV CANADA. Reference-only.
- **Round 12 LOOP 1 sustrato NA COMPLETO (3/3).** Restan 10 temas Round 12 (dominio x5, rol x5). Próxima tarea (iter 135): dominio/alimentos-bebidas (LOOP 2 dominio).

## [2026-07-12] ingest | Round 12 — ITER 135 | LOOP 2 (dominio x5) + LOOP 3 (rol x5) — 10 nodos nuevos
- 10 nodos creados con superstructura completa (README, index, log, raw/) cubriendo dominio y rol:
  - `dominio/alimentos-bebidas/` — F&B: cadena de suministro, seguridad alimentaria (FSMA/HACCP), mercado global.
  - `dominio/moda/` — Apparel/fashion: mercado ~USD 1.44T (2026)→1.68T (2031), cadena de valor, sostenibilidad.
  - `dominio/espacio/` — Space economy: upstream (lanzadores/satélites), downstream (EO, GNSS, satcom), NewSpace.
  - `dominio/agua/` — Agua y saneamiento: utilities públicas, potabilización, tratamiento, escasez, regulación.
  - `dominio/semiconductores/` — Semiconductores/chips: fabless, foundry, IDM, OSAT, CHIPS Act, cadena global.
  - `rol/chief-strategy-officer/` — CSO: estrategia corporativa, M&A, transformación; reporta al CEO.
  - `rol/chief-privacy-officer/` — CPO: riesgos de privacidad (GDPR/CPRA/LGPD); distinto de DPO.
  - `rol/chief-people-officer/` — CPO/CHRO: liderazgo estratégico de RRHH, talento y cultura (C-suite).
  - `rol/chief-client-officer/` — CCO: dueño de la relación y retención del cliente (CX).
  - `rol/head-of-operations/` — Head of Operations: procesos, eficiencia, calidad, SCM.
- Reference-only (URL en frontmatter; sin raw/). Cross-refs a logistica, retail, sostenibilidad, estrategia, operaciones, juridico, ciso, etc.
- **Round 12 COMPLETA (13/13 temas en 3 bucles: LOOP 1 sustrato NA x3, LOOP 2 dominio x5, LOOP 3 rol x5).** Todas las capas cubiertas. Cola Round 12 VACÍA → reabastecimiento (gap_analysis.py) para Round 13.

## [2026-07-12] ingest | Round 13 — ITER 136 | dominio x3 (farmaceutica, quimica, calidad) — 3 nodos nuevos
- 3 nodos `dominio/` creados con superstructura completa (README, index, log, raw/):
  - `dominio/farmaceutica/` — Industria farmacéutica: I+D/desarrollo (FDA/EMA, 10-15 años, USD 1.3-2.6B, 7-12% aprobación), patentes/Hatch-Waxman, genéricos/biosimilares, cadena de frío, CDMO.
  - `dominio/quimica/` — Industria química: petroquímica/commodities, especialidades, fine chemicals/API; REACH (UE, precautorio) vs TSCA (EE.UU., Lautenberg 2016); ESG/química verde.
  - `dominio/calidad/` — Gestión de la calidad: ISO 9001:2015, TQM, Six Sigma (DMAIC), Lean, herramientas (PDCA, FMEA, SPC, Pareto); GMP en industrias reguladas.
- Reference-only (URL en frontmatter; sin raw/). Cross-refs a biotecnologia, salud, energia, manufactura, operaciones, consultoria, auditor-interno, gestion-riesgos.
- **Round 13 (3/8 temas).** Cola restante: dominio/gestion-riesgos + rol x4 (chief-revenue-officer, chief-communications-officer, chief-analytics-officer, head-of-innovation). Próxima tarea (iter 137): dominio/gestion-riesgos.

## [2026-07-12] ingest | Round 13 — ITER 137 | 5 nodos nuevos (1 dominio + 4 rol) — CIERRA ROUND 13
- 5 nodos creados con superstructura completa (README, index, log, raw/), cubriendo dominio + rol:
  - `dominio/gestion-riesgos/` — ERM: ISO 31000, COSO 2017, categorías de riesgo, riesgo operativo, continuidad/resiliencia.
  - `rol/chief-revenue-officer/` — CRO: dueño de todos los ingresos (ventas+marketing+CS), RevOps, reporta a CEO.
  - `rol/chief-communications-officer/` — CCO: comunicaciones, PR, reputación, asesor del CEO (Arthur Page Society).
  - `rol/chief-analytics-officer/` — CAO: analítica y aporte a decisiones operativas; vs CIO/CDO.
  - `rol/head-of-innovation/` — Head of Innovation: gestión de innovación, labs, corporate venturing, ISO 56000.
- Reference-only (URL en frontmatter; sin raw/). Cross-refs a finanzas/riesgo-financiero, chief-risk-officer, calidad, ciberseguridad-gobierno, consultoria, auditor-interno, compliance-officer, board-member; ventas, marketing, vp-sales, cmo, chief-client-officer, head-of-growth, founder-ceo, cfo; relaciones-publicas, experiencia-cliente; chief-data-officer, data-scientist, data-analyst, analitica-negocio, ia-generativa, cio, chief-digital-officer; innovacion, estrategia, chief-product-officer, head-of-research, emprendimiento, chief-strategy-officer.
- **Round 13 COMPLETA (8/8 temas: dominio x4 + rol x4).** Cola Round 13 VACÍA → reabastecimiento (gap_analysis.py) para Round 14.

## [2026-07-12] ingest | Educación en Norteamérica (sustrato NA deepening — LOOP 1 Round 14)
- 3 → sustrato (deepening de nodos NA existentes), cubriendo las 3 jurisdicciones:
  - `sustrato/mexico/educacion.md` — SEP (1921), educación básica/media superior, superior (UNAM/IPN/TecNM/ANUIES), reformas 2013/2019, ~36M estudiantes, ~3% PIB.
  - `sustrato/estados-unidos/educacion.md` — sin sistema nacional; 50+ estatales + Dept of Education (1980, ~$250B 2024); K-12 (Title I/IDEA/ESSA), higher ed (Pell/FAFSA, deuda ~$1.7B).
  - `sustrato/canada/educacion.md` — competencia provincial (s.93 1867); PSE pública; bilingüe EN/FR; OCDE 2022 país más educado; ~5.3% PIB.
- Reference-only (URL en frontmatter; sin raw/). Alcance respetado: sustrato = solo Norteamérica. Cross-ref dominio/educacion.

## [2026-07-12] ingest | Round 14 LOOP 2 — 5 nodos de dominio nuevos
- 5 → dominio (nuevos):
  - `dominio/blockchain/blockchain.md` — ledger distribuido, consenso PoW/PoS, smart contracts, DAOs, DeFi, tokens; retos de escalabilidad y regulación (MiCA/SEC).
  - `dominio/etica-ia/etica-ia.md` — ética de la IA / IA responsable; EU AI Act (en vigor 1 ago 2024, 4 niveles de riesgo + GPAI); gobernanza (NIST AI RMF, ISO 42001).
  - `dominio/pricing/pricing.md` — estrategias (cost-plus, value-based, penetration, skimming, dynamic, freemium), elasticidad, discriminación de precios, límites antitrust.
  - `dominio/geopolitica/geopolitica.md` — geopolítica/geoeconomía para negocios: sanciones, bloques comerciales, nacionalismo de recursos, friend-shoring/nearshoring, riesgo país.
  - `dominio/inteligencia-competitiva/inteligencia-competitiva.md` — CI process (SCIP), fuentes, línea legal vs espionaje industrial, contrainteligencia.
- Reference-only (Wikipedia EN; URL en frontmatter; sin raw/). Cola Round 14: 8/13. Cross-ref sustrato (comercio exterior, controles de exportación, antitrust, privacidad).

## [2026-07-12] ingest | Round 14 LOOP 3 — 5 nodos de rol nuevos
- 5 → rol (nuevos):
  - `rol/program-manager/program-manager.md` — gobierna portafolio de proyectos alineados a estrategia (≠ project mgmt); PgMP/PMI; PMO.
  - `rol/solutions-architect/solutions-architect.md` — diseña solución IT que soporta el negocio; puente ventas-ingeniería/cliente (pre-sales); nube, TOGAF.
  - `rol/investor-relations/investor-relations.md` — IR: puente empresa-mercado financiero (def. NIRI); earnings, divulgación, valoración justa.
  - `rol/regulatory-affairs/regulatory-affairs.md` — RA: cumplimiento regulatorio y aprobación de productos (farma/dispositivos/alimentos/fintech); FDA/EMA.
  - `rol/actuario/actuario.md` — mide/gestiona riesgo e incertidumbre (seguros, pensiones); SOA/CAS/IFoA; Solvencia II.
- **Round 14 COMPLETA (13/13: sustrato x3 + dominio x5 + rol x5).** Reference-only (Wikipedia EN; sin raw/).
- Próximo: ejecutar `gap_analysis.py` → 0 gaps esperados; reabastecimiento cerrado.

## [2026-07-12] ingest | Round 15 — 13 ingests (3 loops: sustrato + dominio + rol)
- 3 → sustrato (deepenings, solo NA):
  - `sustrato/mexico/medio-ambiente.md` — SEMARNAT, LGEEPA, cambio climático, ESG, economía circular.
  - `sustrato/estados-unidos/politica-monetaria.md` — Federal Reserve, FOMC, tasa de fondos federales, dual mandate.
  - `sustrato/canada/politica-monetaria.md` — Bank of Canada, tasa de política, inflation targeting 2%.
- 5 → dominio (nuevos): `automatizacion`, `insurtech`, `legaltech`, `crowdfunding`, `iot` (superstructura recursiva completa).
- 5 → rol (nuevos): `enterprise-architect`, `head-of-corporate-development`, `chief-procurement-officer`, `head-of-tax`, `chief-diversity-officer` (superstructura recursiva completa).
- **Round 15 COMPLETA (13/13: sustrato x3 + dominio x5 + rol x5).** Reference-only (Wikipedia EN + fuentes oficiales gob/SAT/BoC/Fed; sin raw/).
- Próximo: ejecutar `gap_analysis.py` → 0 gaps esperados; reabastecimiento cerrado.

## [2026-07-12] ingest | Round 16 — 13 ingests (3 loops: sustrato NA + dominio + rol)
- 3 → sustrato (deepenings, solo NA):
  - `sustrato/mexico/seguridad-social.md` — IMSS, ISSSTE, regímenes, salud/pensiones laborales.
  - `sustrato/estados-unidos/labor.md` — DOL, FLSA, OSHA, NLRB, sindicatos.
  - `sustrato/canada/labor.md` — Labour Code federal, ESDC, estándares provinciales.
- 5 → dominio (nuevos, superstructura recursiva completa): `cloud-computing`, `robotica`, `realidad-extendida`, `infraestructura`, `seguridad-corporativa`.
- 5 → rol (nuevos, superstructura recursiva completa): `chief-security-officer` (CSO), `chief-learning-officer` (CLO), `chief-quality-officer` (CQO), `head-of-partnerships`, `chief-experience-officer` (CXO).
- **Round 16 COMPLETA (13/13: sustrato NA x3 + dominio x5 + rol x5).** ALCANCE sustrato = solo Norteamérica (respetado). Reference-only (Wikipedia EN + fuentes oficiales gob/SAT/BoC/Fed/ASIS/ATD/ASQ; sin raw/).
- Próximo: ejecutar `gap_analysis.py`; si 0 → Round 16 cierra; ampliar taxonomía para Round 17 (nuevos dominios/roles/países NA) o pausar enriquecimiento.

## [2026-07-12] ingest | Round 17 — ITER 148 | 13 ingests (3 loops: sustrato NA + dominio + rol)
- 3 → sustrato (deepenings, solo NA):
  - `sustrato/mexico/transporte.md` — SICT (antes SCT): carreteras ~377k km, APIs (Manzanillo/Lázaro Cárdenas/Veracruz), CPKC (CA-US-MX), AICM/AIFA, ~28 cruces fronterizos.
  - `sustrato/estados-unidos/defensa.md` — DoD (1947/Pentágono), presupuesto FY2025 ~USD 849.8B, primes (Lockheed/RTX/Boeing/Northrop/GD/L3Harris), DARPA, FMS, Goldwater-Nichols.
  - `sustrato/canada/seguridad-social.md` — CPP (contributivo ~5.95%), OAS (residencial ~$727-800/mes + GIS), EI (~55% hasta 45 semanas), Canada Health Transfer a provincias.
- 5 → dominio (nuevos, superstructura recursiva completa): `redes-sociales`, `deportes`, `entretenimiento`, `juegos-videojuegos`, `economia-circular`.
- 5 → rol (nuevos, superstructura recursiva completa): `chief-ai-officer` (CAIO), `chief-design-officer` (CDO design), `chief-transformation-officer`, `chief-ethics-officer`, `chief-knowledge-officer` (CKO).
- **Round 17 COMPLETA (13/13: sustrato NA x3 + dominio x5 + rol x5).** ALCANCE sustrato = solo Norteamérica (respetado). Reference-only (Wikipedia EN + fuentes oficiales gob/SICT/DoD/Canada.ca/Statista; sin raw/).
- Próximo: ejecutar `gap_analysis.py`; si 0 → Round 17 cierra; ampliar taxonomía para Round 18 (nuevos dominios/roles/países NA) o pausar enriquecimiento.

## [2026-07-12] ingest | Round 18 — 13 ingests (3 loops: sustrato NA + dominio + rol)
- 3 → sustrato (deepenings, solo NA):
  - `sustrato/mexico/agricultura.md` — SADER, producción agroalimentaria, seguridad alimentaria, T-MEC, riego, exportaciones.
  - `sustrato/estados-unidos/comercio-exterior.md` — USTR, Sección 301, aranceles, acuerdos comerciales, nearshoring.
  - `sustrato/canada/telecomunicaciones.md` — CRTC, espectro, banda ancha, Bell/Rogers/Telus, 5G.
- 5 → dominio (nuevos, superstructura recursiva completa): `energias-renovables`, `finanzas-publicas`, `economia-digital`, `gobierno-de-datos`, `propiedad-intelectual`.
- 5 → rol (nuevos, superstructura recursiva completa): `head-of-revops`, `chief-content-officer`, `head-of-sales-enablement`, `head-of-people-analytics`, `chief-pricing-officer`.
- **Round 18 COMPLETA (13/13: sustrato NA x3 + dominio x5 + rol x5).** ALCANCE sustrato = solo Norteamérica (respetado). Reference-only (Wikipedia EN + fuentes oficiales gob/SADER/USTR/CRTC; sin raw/).
- Próximo: ejecutar `gap_analysis.py`; si 0 → Round 18 cierra; ampliar taxonomía para Round 19 (nuevos dominios/roles/países NA) o pausar enriquecimiento.

## [2026-07-12] ingest | Round 19 — 13 nodos (3 sustrato NA + 5 dominio + 5 rol)
- 3 → sustrato (deepenings NA): `mexico/turismo.md` (SECTUR, sol y playa, médico, ~51M llegadas 2024), `estados-unidos/infraestructura.md` (IIJA, DOT, banda ancha, grid), `canada/energia.md` (hidro, oil sands, NRCan, net-zero).
- 5 → dominio (nuevos): `ciudades-inteligentes`, `healthtech`, `publicidad`, `franquicias`, `eventos`.
- 5 → rol (nuevos): `legal-ops`, `head-of-facilities`, `head-of-public-affairs`, `sales-engineer`, `business-analyst`.
- Superstructura recursiva completa en los 10 nodos nuevos (raw/, README, index, log). Reference-only (Wikipedia EN + fuentes oficiales gob/SECTUR/DOT/NRCAN; sin raw/).
- Round 19 COMPLETA (13/13). ALCANCE sustrato = solo Norteamérica (respetado).

## [2026-07-13] ingest | Round 20 — 13 nodos (3 sustrato NA + 5 dominio + 5 rol)
- 3 → sustrato (deepenings NA):
  - `sustrato/mexico/mineria.md` — CAMIMEX, plata/oro/cobre, Ley Minera, PIB ~2.4%.
  - `sustrato/estados-unidos/seguridad-social.md` — SSA/OASDI, Medicare, Medicaid, SSI, SNAP.
  - `sustrato/canada/medio-ambiente.md` — ECCC, cambio climático, net-zero.
- 5 → dominio (nuevos): `aviacion`, `maritimo`, `seguridad-nacional`, `ciberdefensa`, `auditoria-gubernamental`.
- 5 → rol (nuevos): `vp-product`, `chief-commercial-officer`, `chief-medical-officer`, `vp-operations`, `head-of-engineering`.
- Superstructura recursiva completa en los 10 nodos nuevos (raw/, README, index, log). Reference-only (Wikipedia EN + fuentes oficiales gob/SSA/Canada.ca/CAMIMEX/IMO/CISA/GAO/ASF; sin raw/).
- Round 20 COMPLETA (13/13). ALCANCE sustrato = solo Norteamérica (respetado).

## [2026-07-13] ingest | Round 21 — 13 nodos (3 sustrato NA + 5 dominio + 5 rol)
- 3 → sustrato (deepenings NA, finanzas públicas):
  - `sustrato/mexico/finanzas-publicas.md` — SHCP, PEF, deuda ~50% PIB, carga tributaria baja.
  - `sustrato/estados-unidos/finanzas-publicas.md` — Treasury, deuda >USD$36B, debt ceiling, entitlements.
  - `sustrato/canada/finanzas-publicas.md` — Dept of Finance, PBO, deuda/PIB (~30-45%).
- 5 → dominio (nuevos): `seguridad-alimentaria`, `derecho-penal`, `energia-nuclear`, `ciencias-materiales`, `derecho-ambiental`.
- 5 → rol (nuevos): `ml-engineer`, `security-engineer`, `fp-and-a-manager`, `product-designer`, `account-manager`.
- Superstructura recursiva completa en los 10 nodos nuevos (raw/, README, index, log). Reference-only (Wikipedia EN + fuentes oficiales gob/hacienda/Treasury/NRC/FDA/EPA/MRS/OWASP/NNGroup/Salesforce; sin raw/).
- Round 21 COMPLETA (13/13). ALCANCE sustrato = solo Norteamérica (respetado).

## [2026-07-13] ingest | Round 22 — 13 nodos (3 sustrato NA + 5 dominio + 5 rol)
## [2026-07-13] ingest | Round 23 — LOOP 1 (sustrato NA x3 ingest COMPLETOS)
- sustrato/mexico/salud.md (Sistema Nacional de Salud: Ssa, IMSS, ISSSTE, IMSS-Bienestar, Cofepris).
- sustrato/estados-unidos/telecomunicaciones.md (FCC, 5G/C-band, espectro, net neutrality).
- sustrato/canada/agricultura.md (AAFC, supply management, granos, CUSMA/CETA/CPTPP).
- Índices/logs de nodos + globales (root index.md/log.md) actualizados. Reference-only (gob/Wikipedia/fcc/AAFC; sin raw/).

## [2026-07-13] ingest | Round 23 — LOOP 2 (dominio x5 ingest COMPLETOS)
- dominio/dispositivos-medicos.md (FDA 510(k)/PMA/De Novo, COFEPRIS, Health Canada, MDR, ISO 13485).
- dominio/computacion-cuantica.md (qubits, NISQ, algoritmos, casos).
- dominio/investigacion-operaciones.md (optimización, colas, simulación).
- dominio/teoria-de-juegos.md (Nash, subastas, negocio).
- dominio/gobierno-de-ti.md (COBIT, alineación TI-negocio).
- Índices/logs de nodos + globales (root index.md/log.md) actualizados. Reference-only (FDA/COFEPRIS/Health Canada/Wikipedia/ISACA/INFORMS; sin raw/).

## [2026-07-13] ingest | Round 23 — LOOP 3 (rol x5 ingest COMPLETOS)
- rol/platform-engineer.md (IDP, golden paths, DevEx).
- rol/cloud-architect.md (arquitecturas cloud, well-architected, FinOps).
- rol/research-scientist.md (R&D, publicación, transferencia).
- rol/technical-program-manager.md (TPM, programas cross-funcionales).
- rol/community-manager.md (comunidad, redes sociales, advocacía).
- Índices/logs de nodos + globales (root index.md/log.md) actualizados. Reference-only (Wikipedia/Backstage/AWS/Nature/Hootsuite; sin raw/).
- 3 → sustrato (deepenings NA, solo Norteamérica):
  - `sustrato/mexico/propiedad-intelectual.md` — IMPI (Ley 27/2020), INDAUTOR, T-MEC cap.20.
  - `sustrato/estados-unidos/propiedad-intelectual.md` — USPTO, AIA 2011, US Copyright Office, Lanham Act.
  - `sustrato/canada/propiedad-intelectual.md` — CIPO/ISED, Patent Act, Trade-marks Act.
- 5 → dominio (nuevos): `arbitraje`, `tributacion-internacional`, `derecho-internacional`, `ingenieria`, `contabilidad-forense`.
- 5 → rol (nuevos): `chairman`, `partner`, `staff-engineer`, `delivery-manager`, `engagement-manager`.
- Superstructura recursiva completa en los 10 nodos nuevos (raw/, README, index, log). Reference-only (Wikipedia EN + fuentes oficiales gob/IMPI/USPTO/CIPO/OCDE/INCOSE/ACFE/staffeng; sin raw/).
- Round 22 COMPLETA (13/13). ALCANCE sustrato = solo Norteamérica (respetado).

