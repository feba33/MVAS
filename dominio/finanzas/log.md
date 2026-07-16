# Registro de finanzas (log.md)

Registro cronológico **append-only** de la entidad `finanzas`.
Prefijo de entrada: `## [YYYY-MM-DD] <tipo> | <título>`
(parseable: `grep "^## \[" log.md | tail -5` → últimas 5 entradas).

## [2026-07-09] setup | Nodo wiki de finanzas
- Creada la superstructura recursiva de la entidad `finanzas` dentro de `dominio/`:
  `raw/`, `index.md`, `log.md` y `README.md`.
- Demuestra el principio: toda la info de finanzas vive solo en esta carpeta.

## [2026-07-09] ingest | Incertidumbre (T-MEC y México)
- Fuente: El Financiero (opinión, G. Knochenhauer). T-MEC vigente hasta 2036, revisiones anuales, retiro anticipado posible.

## [2026-07-16] ingest | Trump impondrá aranceles del 25% a Brasil por censura a tecnológicas de EE.UU.
- Fuente: El Financiero (mundo, 2026-07-15). EE.UU. estaría por imponer aranceles del 25% contra Brasil.
- Entidad: dominio/finanzas (política comercial / aranceles). Cross-ref sustrato/mexico/comercio-exterior.
- Relevancia: cambia supuestos de comercio regional y volatilidad arancelaria para México.

## [2026-07-09] ingest | El T-MEC no va — revisión anual e inversión
- Fuente: El Financiero (opinión). Revisión anual del T-MEC genera incertidumbre para inversionistas; urgir industria mexicana.

## [2026-07-09] ingest | De rentas, stock y otros desafíos en vivienda
- Fuente: El Financiero (opinión, C. Olguín). Mercado inmobiliario mayor del país; nuevo ciclo de vivienda para sectores medio/social.

## [2026-07-09] ingest | Valoración de empresas (métodos)
- Fuentes: Finance Interview Prep (guía 2026) + CT Acquisitions (guía 2026).
- Página: `valoracion.md`. Los 3 enfoques (intrínseco/DCF, relativo/comps, activos); EV vs Equity; WACC y estructura de capital; múltiplos EBITDA/SDE/revenue y rangos por sector. Reference-only.

## [2026-07-09] ingest | Instrumentos Financieros
- Fuente: Wikipedia (en) — reference-only.
- Página: `instrumentos-financieros.md`. Definición IAS 32/39; clases: deuda (bonos), capital (acciones), derivados (opciones/futuros).

## [2026-07-09] ingest | Libros clave de finanzas
- Fuente: Wikipedia (en) The Intelligent Investor + conocimiento general (Principles, R. Dalio) — reference-only.
- Página: `libros-clave.md`. Value investing (Graham) y principios de trabajo/vida (Dalio).

## [2026-07-09] ingest | Private Equity y Venture Capital
- Fuente: Wikipedia (en) Venture capital / Private equity + conocimiento general (reference-only).
- Página: `private-equity-vc.md`. PE/VC: fundraising, rondas (seed/A/B/C), term sheets, dilución, salidas (IPO/M&A).

## [2026-07-09] ingest | Criptoactivos y activos digitales
- Fuente: Wikipedia (en) Cryptocurrency — reference-only.
- Página: `cripto-activos.md`. Bitcoin, Ethereum, exchanges, regulación (SEC); mecanismos PoW/PoS.

## [2026-07-09] ingest | Finanzas conductuales
- Fuente: Wikipedia (en) Behavioral economics — reference-only.
- Página: `behavioral-finance.md`. Sesgos, Kahneman/Tversky, prospect theory.

## [2026-07-10] ingest | Gravar Afores heredadas con ISR — JUFED lo rechaza
- Fuente: El Financiero (2026-07-09) — reference-only (URL en frontmatter, sin raw/).
- Página: `afores-herencia-isr.md`. JUFED rechaza gravar Afores heredadas con ISR; pide a SCJN proteger patrimonio familiar/seguridad social. Ángulo: planeación patrimonial sucesoria de cuentas de retiro.
- Discernimiento: dominio/finanzas (Afores, ISR, retiro) + cross-ref sustrato/mexico (régimen fiscal) y dominio/leyes (JUFED/SCJN). Certeza alta.
- Nota: los otros 4 ítems del scrape (crónica criminal migrante/ICE, captura de sicario, desaparición adolescentes, reality show) se filtraron por gate de relevancia (coyuntura sin ángulo legal-corporativo-técnico).

## [2026-07-10] ingest | Derivados financieros
- Fuentes (web, reference-only): StrategyCenter, Estudyando, RuinsMag.
- Página: `derivados.md`. Definición, futuros/opciones/forwards/swaps, mercados (CME/Eurex/MEFF, OTC), cobertura vs especulación, apalancamiento y riesgo de contraparte.

## [2026-07-10] ingest | Mercados de capitales
- Fuentes (web, reference-only): BBVA (emisión de bonos), Rankia (underwriting).
- Página: `mercados-capitales.md`. ECM/IPO, DCM/bonos, underwriting (aseguramiento), actores.
- **LOOP 2 de Round 3 (capa dominio).**

## [2026-07-10] ingest | Finanzas corporativas (M&A, valoración, tesorería) — iter 90
- Fuentes (web, reference-only): Wikipedia (en) Corporate finance / M&A / Business valuation / Treasury management + conocimiento general.
- Página: `finanzas-corporativas.md`. Visión integrada de finanzas corporativas como 3 pilares (M&A, valoración, tesorería) sobre el objetivo de maximizar valor de accionista. Cruza con valoracion.md, mercados-capitales.md, private-equity-vc.md, derivados.md y rol/cfo.
- Discernimiento: dominio/finanzas (certeza alta). No duplica valoracion.md (lo enlaza).

## [2026-07-10] ingest | Riesgo financiero (mercado, crédito, liquidez, operativo) — iter 91
- Fuentes (web, reference-only): Santander Open Academy, BIS (Basilea III), LinkedIn (COSO ERM/ISO 31000/CNBV), Scribd (clase riesgos bancarios), EAE Barcelona.
- Página: `riesgo-financiero.md`. Los 4 tipos principales con sub-riesgos y mitigación; riesgos complementarios (legal, tecnológico, PLD); marcos de gobernanza (COSO ERM, ISO 31000, Basilea III/LCR/NSFR, CNBV); ciclo identificar-medir-mitigar-monitorear.
- Discernimiento: dominio/finanzas (certeza alta). No duplica derivados.md (lo enlaza para coberturas) ni finanzas-corporativas.md (lo enlaza para tesorería/liquidez).

## [2026-07-11] ingest | Mercado laboral formal de México (IMSS, junio 2026)
- Fuente: El Financiero (opinión, Víctor Piz, 2026-07-10) — reference-only (URL en frontmatter, sin raw/).
- Página: `mercado-laboral-formal.md`. Empleo formal afiliado al IMSS mejoró en junio 2026 tras debilidad en mayo; columna resalta las métricas menos visibles (calidad, salarios, rotación).
- Discernimiento: dominio/finanzas (certeza alta) + cross-ref sustrato/mexico (economía laboral) y dominio/leyes (derecho-laboral).
