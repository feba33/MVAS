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

