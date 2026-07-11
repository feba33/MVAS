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

