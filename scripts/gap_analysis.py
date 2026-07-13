#!/usr/bin/env python3
"""gap_analysis.py — Analiza MVAS y reporta huecos vs una taxonomía esperada.

Uso:
    python3 scripts/gap_analysis.py [ruta_a_MVAS]

Imprime un reporte de huecos (temas faltantes por nodo existente) y nodos
sugeridos (nuevos). Se usa en el procedimiento de REABASTECIMIENTO AUTOMÁTICO
del bucle: cuando `working.md` se queda sin temas `pending`, correr este script,
tomar la lista de huecos, convertirla en temas en `working.md` y continuar.

La taxonomía es la visión de qué debería tener cada nodo; se puede editar para
ampliar la cobertura objetivo.
"""
import os
import sys
import glob

ROOT = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

# Taxonomía esperada: nodo -> [(slug, título)]
# ALCANCE SUSTRATO: solo Norteamérica (México, EE.UU., Canadá). No se sugieren otros países.
ALLOWED_SUSTRATO = {"mexico", "estados-unidos", "canada"}
TAXONOMY = {
    "sustrato/mexico": [
        ("lft", "Ley Federal del Trabajo (laboral, outsourcing, reparto de utilidades)"),
        ("profeco-condusef", "Protección al consumidor (PROFECO, CONDUSEF)"),
        ("pld-uif", "Prevención de lavado / UIF (AML)"),
        ("energia", "Sector energía (CRE/SENER, PEMEX/CFE, renovables)"),
        ("banca-sistema-financiero", "Sistema financiero / banca (Banxico, CNBV, banca múltiple, Sofipos)"),
        ("pensiones-afore", "Sistema de pensiones (AFORE, CONSAR, SAR, SIEFOREs)"),
        ("telecomunicaciones", "Telecomunicaciones (IFT, sector telecom, banda ancha, despacho)"),
        ("inversion-extranjera", "Inversión extranjera directa (IMMEX, maquiladora, regulación de IED)"),
        ("sector-manufacturero", "Sector manufacturero (industria, exportación, cadenas)"),
        ("sat", "SAT / sistema tributario (ISR, IVA, impuestos federales)"),
        ("educacion", "Educación México: SEP, sistema educativo, reformas, educación superior (UNAM/IPN/tecnológicos), ANUIES"),
        ("medio-ambiente", "Medio ambiente (SEMARNAT, LGEEPA, cambio climático, ESG México, economía circular)"),
        ("seguridad-social", "Seguridad social México: IMSS, ISSSTE, seguro social, salud y pensiones laborales"),
        ("transporte", "Transporte e infraestructura México: SCT, carreteras, puertos, aeropuertos, fronteras"),
        ("agricultura", "Agricultura México: SADER, sector agroalimentario, autosuficiencia, tratados, cadena de valor"),
        ("turismo", "Turismo México: SECTUR, destinos, turismo de sol y playa, turismo médico, contribución al PIB"),
        ("mineria", "Minería México: CAMIMEX, plata/oro/cobre, regulación minera, contribución al PIB"),
        ("finanzas-publicas", "Finanzas públicas México: SHCP, Presupuesto de Egresos, deuda pública, política fiscal"),
        # Round 22 — deepening NA (propiedad intelectual por país).
        ("propiedad-intelectual", "Propiedad intelectual México: IMPI, Ley Federal del Derecho de Autor, patentes/marcas, tratados"),
        # Round 23 — deepening NA (salud por país).
        ("salud", "Salud / sistema de salud México: Secretaría de Salud, IMSS/INSABI, Cofepris, seguro popular, cobertura"),
        # Round 24 — deepening NA (política monetaria por país).
        ("politica-monetaria", "Política monetaria México: Banxico, tasa de referencia, inflation targeting, Junta de Gobierno, tipo de cambio USD/MXN"),
        # Round 25 — deepening NA (seguridad pública por país).
        ("seguridad-publica", "Seguridad pública México: Guardia Nacional, SSP, Fiscalía General de la República (FGR), crimen organizado"),
        # Round 26 — deepening NA (poder judicial por país).
        ("poder-judicial", "Poder judicial México: PJF, Suprema Corte (SCJN), Consejo de la Judicatura (CJF), reforma judicial 2024-2025, juicios orales"),
        # Round 27 — deepening NA (relaciones exteriores).
        ("relaciones-exteriores", "Relaciones exteriores México: SRE, política exterior, diplomacia, tratados, cooperación internacional, ONU/OEA"),
    ],
    "sustrato/estados-unidos": [
        ("sec-valores", "SEC y regulación de valores"),
        ("antitrust", "Antitrust (Sherman / Clayton)"),
        ("bankruptcy", "Derecho concursal / bancarrotas"),
        ("salud", "Salud / healthcare (FDA, CMS, HIPAA, Medicare-Medicaid)"),
        ("sector-tecnologia", "Sector tecnológico (Big Tech, antitrust, IA, CHIPS Act)"),
        ("vivienda-real-estate", "Vivienda y mercado inmobiliario (Fannie/Freddie Mac, FHA/HUD, MBS)"),
        ("energia", "Energía (DOE, FERC, grid, oil & gas, renovables, nuclear)"),
        ("agricultura", "Agricultura (USDA, Farm Bill, subsidios, comercio agrícola)"),
        ("inmigracion", "Inmigración EE.UU. (USCIS, H-1B, H-2A, green card, visas)"),
        ("educacion", "Educación EE.UU.: Dept of Education, K-12 (Title I), higher ed (FAFSA, Pell, acreditación), estatales"),
        ("politica-monetaria", "Política monetaria (Federal Reserve, FOMC, tasa de fondos federales, balance, dual mandate)"),
        ("labor", "Trabajo / laboral EE.UU.: DOL, FLSA, OSHA, NLRB, derechos del trabajador, sindicatos"),
        ("defensa", "Defensa / Department of Defense: Pentagon, presupuesto, contratos, industria de defensa"),
        ("comercio-exterior", "Comercio exterior EE.UU.: USTR, política comercial, aranceles, USMCA, Sección 301/232"),
        ("infraestructura", "Infraestructura EE.UU.: IIJA, DOT, carreteras, puentes, banda ancha, red eléctrica"),
        ("seguridad-social", "Seguridad social EE.UU.: SSA, Social Security, Medicare, Medicaid, SSI, SNAP"),
        ("finanzas-publicas", "Finanzas públicas EE.UU.: Treasury, presupuesto federal, deuda nacional, debt ceiling"),
        # Round 22 — deepening NA (propiedad intelectual por país).
        ("propiedad-intelectual", "Propiedad intelectual EE.UU.: USPTO, Patent Act, America Invents Act, US Copyright Office"),
        # Round 23 — deepening NA (telecomunicaciones por país).
        ("telecomunicaciones", "Telecomunicaciones EE.UU.: FCC, banda ancha, 5G, espectro, competencia, net neutrality"),
        # Round 24 — deepening NA (medio ambiente por país).
        ("medio-ambiente", "Medio ambiente EE.UU.: EPA, Clean Air/Water Act, NEPA, climate policy, descarbonización, emisiones vehiculares"),
        # Round 25 — deepening NA (sistema financiero por país).
        ("sistema-financiero", "Sistema financiero EE.UU.: Federal Reserve, OCC, FDIC, banca comercial, Dodd-Frank, regulación prudencial"),
        # Round 26 — deepening NA (poder judicial por país).
        ("poder-judicial", "Poder judicial EE.UU.: federal judiciary (SCOTUS, Courts of Appeals, District Courts, Article III), DOJ, nombramientos, federal vs state"),
        # Round 27 — deepening NA (seguridad nacional).
        ("seguridad-nacional", "Seguridad nacional EE.UU.: DHS, FBI, intelligence community (ODNI/CIA/NSA), homeland security, ciberseguridad nacional, contrainterligencia"),
    ],
    "sustrato/canada": [
        ("competition-bureau", "Competencia / antitrust (Competition Bureau Canada)"),
        ("provincial-federal", "Divisiones de poder provincial vs federal en Canadá"),
        ("salud", "Salud / healthcare (Health Canada, provincias, CADTH)"),
        ("sector-bancario", "Sector bancario (Big Six, OSFI)"),
        ("recursos-naturales", "Recursos naturales (NRCan, energía, minerales, bosques)"),
        ("comercio-exterior", "Comercio exterior (Global Affairs Canada, export, USMCA, aranceles)"),
        ("inmigracion", "Inmigración (IRCC, permisos de trabajo, residentes permanentes)"),
        ("impuestos", "Impuestos Canadá (CRA, T1, GST/HST, tributario federal)"),
        ("transporte", "Transporte Canadá (Transport Canada, ferrocarriles, aviación, puertos)"),
        ("educacion", "Educación Canadá: provincias (currículo), PSE (universidades/colleges), student aid, bilingüe FR/EN"),
        ("politica-monetaria", "Política monetaria (Bank of Canada, tasa de política, inflation targeting 2% CPI)"),
        ("labor", "Trabajo / laboral Canadá: Labour Code federal, ESDC, estándares provinciales, sindicatos"),
        ("seguridad-social", "Seguridad social Canadá: CPP, OAS, EI, financiamiento de salud provincial"),
        ("telecomunicaciones", "Telecomunicaciones Canadá: CRTC, Bell/Rogers/Telus, 5G, espectro, competencia"),
        ("energia", "Energía Canadá: hidroeléctrica, oil sands, gas, red eléctrica, NRCan, transición energética"),
        ("medio-ambiente", "Medio ambiente Canadá: Environment and Climate Change Canada (ECCC), climate change, net-zero, regulación"),
        ("finanzas-publicas", "Finanzas públicas Canadá: Department of Finance, presupuesto federal, deuda/PIB, PBO"),
        # Round 22 — deepening NA (propiedad intelectual por país).
        ("propiedad-intelectual", "Propiedad intelectual Canadá: CIPO, Patent Act, Trade-marks Act, Copyright Act"),
        # Round 23 — deepening NA (agricultura por país).
        ("agricultura", "Agricultura Canadá: Agriculture and Agri-Food Canada (AAFC), supply management, granos, ganadería"),
        # Round 24 — deepening NA (defensa por país).
        ("defensa", "Defensa Canadá: Department of National Defence (DND), Canadian Armed Forces (CAF), NORAD, procurement, política industrial de defensa"),
        # Round 25 — deepening NA (infraestructura por país).
        ("infraestructura", "Infraestructura Canadá: Infrastructure Canada, transporte, banda ancha, vivienda, planificación de capital"),
        # Round 26 — deepening NA (poder judicial por país).
        ("poder-judicial", "Poder judicial Canadá: Supreme Court of Canada, cortes provinciales/territoriales, nombramiento, Carta de Derechos y Libertades"),
        # Round 27 — deepening NA (ciencia e innovación).
        ("ciencia-e-innovacion", "Ciencia e innovación Canadá: NRC, ISED, Innovation, Science and Economic Development, políticas de CTI, investigación federal"),
    ],
    "dominio/finanzas": [
        ("private-equity-vc", "Private Equity / Venture Capital / fundraising"),
        ("cripto-activos", "Criptoactivos / activos digitales"),
        ("behavioral-finance", "Finanzas conductuales"),
        ("derivados", "Derivados (futuros, opciones, swaps)"),
        ("mercados-capitales", "Mercados de capitales / IPO / emisión de deuda"),
        ("finanzas-corporativas", "Finanzas corporativas (M&A, valoración, tesorería)"),
        ("riesgo-financiero", "Gestión de riesgo financiero"),
    ],
    "dominio/computacion": [
        ("ciberseguridad", "Ciberseguridad (CIA, NIST, Zero Trust)"),
        ("data-engineering", "Ingeniería de datos (ETL, lakehouse)"),
        ("ml-engineering", "ML / AI engineering (MLOps, RAG)"),
        ("testing-qa", "Testing / QA (unit, e2e, SDET)"),
        ("estilos-arquitectura", "Arquitectura de software (microservicios, event-driven)"),
        ("plataforma-sre", "Plataforma / DevOps / SRE"),
        ("frontend", "Frontend (frameworks, performance)"),
        ("bases-datos", "Bases de datos (SQL, NoSQL, distribuidas)"),
    ],
    "dominio/marketing": [
        ("content-marketing", "Content marketing"),
        ("cro", "Conversion Rate Optimization (CRO)"),
        ("brand", "Branding / marca"),
        ("demand-generation", "Demand generation / paid media"),
        ("analitica-marketing", "Analítica de marketing (atribución)"),
        ("lifecycle-email", "Lifecycle / email marketing"),
    ],
    "dominio/leyes": [
        ("derecho-contratos", "Derecho de contratos"),
        ("propiedad-intelectual", "Propiedad intelectual (profundización)"),
        ("derecho-societario", "Derecho societario / corporativo"),
        ("derecho-laboral", "Derecho laboral (profundización)"),
        ("cumplimiento-regulacion", "Compliance / regulación"),
    ],
    "dominio/contabilidad": [
        ("costos", "Contabilidad de costos"),
        ("auditoria", "Auditoría"),
        ("impuestos", "Contabilidad fiscal"),
        ("consolidacion", "Consolidación / reportes financieros"),
        ("tesoreria", "Tesorería / flujo de efectivo"),
    ],
    "dominio/diseno": [
        ("ux-research", "UX research (métodos)"),
        ("accesibilidad", "Accesibilidad (WCAG)"),
        ("service-design", "Service design"),
        ("design-systems", "Design systems / componentes"),
        ("ux-writing", "UX writing / microcopy"),
    ],
    "rol": [
        ("sales-lead", "Sales Lead"),
        ("customer-success-lead", "Customer Success Lead"),
        ("people-lead", "People / HR Lead"),
        ("legal-counsel", "Legal Counsel"),
        ("founder-ceo", "Founder / CEO"),
        ("cto", "CTO"),
        ("data-engineer", "Data Engineer"),
        ("qa-engineer", "QA Engineer / SDET"),
        ("product-owner", "Product Owner / PO"),
        ("scrum-master", "Scrum Master"),
        ("engineering-manager", "Engineering Manager"),
        ("design-lead", "Design Lead / UX Lead"),
        ("data-lead", "Data Lead / Analytics Lead"),
        ("marketing-manager", "Marketing Manager"),
        ("finance-lead", "Finance Lead / Controller"),
        ("ops-lead", "Operations Lead"),
        ("support-lead", "Support / CX Lead"),
        ("reclutador", "Recruiter / Talent Acquisition"),
        ("engineering-manager", "Engineering Manager"),
        ("growth-lead", "Growth Lead"),
        ("ux-ui-lead", "UX / UI Lead"),
        ("product-marketing-manager", "Product Marketing Manager (PMM)"),
        ("finance-lead", "Finance Lead / Controller"),
        ("data-scientist", "Data Scientist"),
    ],
}

# Nodos sugeridos que aún no existen en el repo
NEW_NODES = [
    ("dominio/ventas", "Ventas (sales): metodología, funnel, CRM"),
    ("dominio/producto", "Producto (dominio): discovery, métricas AARRR, PMF"),
    ("dominio/recursos-humanos", "Recursos Humanos / People"),
    ("dominio/operaciones", "Operaciones (supply chain, lean)"),
    ("dominio/juridico", "Jurídico / legal interno de empresa"),
    ("dominio/estrategia", "Estrategia / OKRs / planeación"),
    ("organización/ejemplo-empresa", "Empresa ejemplo (capa organización)"),
    ("dominio/economia", "Economía / macroeconomía (PIB, inflación, bancos centrales, ciclo)"),
    ("dominio/estadistica", "Estadística y ciencia de datos (inferencia, probabilidad, visualización)"),
    ("dominio/project-management", "Gestión de proyectos (PMP, agile/waterfall, triple restricción)"),
    ("dominio/negociacion", "Negociación (método Harvard, BATNA, ZOPA)"),
    ("dominio/seguros", "Seguros (insurance): vida, P&C, actuarial, reaseguro, Solvency II"),
    ("dominio/energia", "Energía: renovables, oil&gas, redes, regulación"),
    ("dominio/inmobiliario", "Bienes raíces / real estate: mercado, financiamiento, REITs"),
    ("dominio/retail", "Retail / comercio: omnicanal, merchandising, e-commerce"),
    ("dominio/manufactura", "Manufactura: lean, Six Sigma, cadena de producción"),
    ("rol/cio", "CIO — Chief Information Officer"),
    ("rol/coo", "COO — Chief Operating Officer"),
    ("rol/cmo", "CMO — Chief Marketing Officer"),
    # Round 6 — extensiones en capas generales (dominio/rol), dentro del alcance.
    ("dominio/salud", "Salud / healthcare: sistemas de salud, seguros médicos, farmacia, telemedicina"),
    ("dominio/educacion", "Educación: modelos, edtech, política educativa"),
    ("dominio/transporte", "Transporte / movilidad: logística urbana, aviación, regulación"),
    ("dominio/telecomunicaciones", "Telecomunicaciones: redes, 5G, regulación"),
    ("rol/chief-data-officer", "CDO — Chief Data Officer"),
    ("rol/chief-sustainability-officer", "CSO — Chief Sustainability Officer"),
    ("rol/chief-risk-officer", "CRO — Chief Risk Officer"),
    # Round 7 — extensiones nuevas (dentro del alcance; sustrato solo NA).
    ("dominio/agronegocios", "Agroindustria / agronegocios: granos, ganadería, agtech, cadenas de valor rurales"),
    ("dominio/construccion", "Construcción / ingeniería AEC: ciclo de obra, contratos, costos, infraestructura"),
    ("dominio/turismo", "Turismo / hospitalidad: hotelería, OTA, destinos, experiencias"),
    ("dominio/medios-comunicacion", "Medios de comunicación / publishing: prensa, broadcast, digital, streaming"),
    ("dominio/automotriz", "Industria automotriz / movilidad: OEM, proveedores, maquiladoras, EVs"),
    ("dominio/gobierno-publico", "Sector público / gobierno: presupuesto, contratación, política pública"),
    ("rol/ciso", "CISO — Chief Information Security Officer"),
    ("rol/general-counsel", "General Counsel — máximo ejecutivo legal de la organización"),
    ("rol/brand-manager", "Brand Manager — gestión de marca y portafolio"),
    ("rol/business-development", "Business Development — alianzas, canales, expansión de negocio"),
    # Round 8 — extensiones en capas generales (dominio/rol) + sustrato NA (deepening). Sin nuevos países.
    ("dominio/biotecnologia", "Biotecnología: industria, genómica, fármacos, agtech, biofarmacéutica"),
    ("dominio/mineria", "Minería: extracción, commodities, regulación ambiental, metales"),
    ("dominio/defensa-seguridad", "Defensa y seguridad: industria armamentística, militar, dual-use"),
    ("dominio/aeroespacial", "Aeroespacial: aeronáutica, espacio, fabricantes, lanzaderas"),
    ("dominio/fintech", "Fintech: pagos, banca digital, lending, regtech, cripto"),
    ("rol/chief-product-officer", "CPO — Chief Product Officer"),
    ("rol/vp-engineering", "VP Engineering — Vicepresidente de Ingeniería"),
    ("rol/vp-sales", "VP Sales — Vicepresidente de Ventas / Revenue"),
    ("rol/chief-of-staff", "Chief of Staff — jefe de gabinete ejecutivo"),
    # Round 9 — extensiones en capas generales (dominio/rol) + sustrato NA (deepening). Sin nuevos países.
    ("dominio/emprendimiento", "Emprendimiento: creación de valor, ciclo, ecosistema, financiamiento"),
    ("dominio/relaciones-publicas", "Relaciones públicas: PR, earned media, media relations, reputación"),
    ("dominio/innovacion", "Innovación: gestión de la innovación, ISO 56000, tipos incremental/disruptiva"),
    ("dominio/experiencia-cliente", "Experiencia del cliente (CX): cognitiva/emocional, journey, lealtad"),
    ("dominio/comercio-internacional", "Comercio internacional: aranceles, TLC, OMC, teorías comparativas"),
    ("rol/product-manager", "Product Manager — dueño de estrategia de producto, requisitos, lanzamientos"),
    ("rol/financial-analyst", "Financial Analyst — análisis financiero, valoración, crédito, modelado"),
    ("rol/head-of-growth", "Head of Growth — crecimiento vía experimentación cross-funcional"),
    ("rol/vp-marketing", "VP of Marketing — lidera org de marketing, brand, GTM, demanda, ROI"),
    ("rol/tech-lead", "Tech Lead — liderazgo técnico IC, arquitectura, calidad, mentoría"),
    ("rol/account-executive", "Account Executive — ejecutivo de cuentas (ventas)"),
    # Round 10 — extensiones en capas generales (dominio/rol) + sustrato NA (deepening). Sin nuevos países.
    ("dominio/analitica-negocio", "Analítica de negocio / Business Analytics / BI: datos, dashboards, toma de decisiones"),
    ("dominio/gobierno-corporativo", "Gobierno corporativo: consejo, accionistas, deberes fiduciarios, ESG"),
    ("dominio/ia-generativa", "IA generativa: LLMs, adopción empresarial, gobernanza de IA"),
    ("dominio/cultura-organizacional", "Cultura organizacional: valores, comportamiento, cultura de alto desempeño"),
    ("dominio/gestion-cambio", "Gestión del cambio: ADKAR, Kotter, transformación"),
    ("rol/controller", "Controller — controlador financiero, reporting, cumplimiento contable"),
    ("rol/project-manager", "Project Manager — gestión de proyectos, triple restricción, stakeholder"),
    ("rol/data-analyst", "Data Analyst — análisis de datos, reporting, BI"),
    ("rol/board-member", "Board Member / Consejero — consejo de administración, gobierno"),
    ("rol/auditor-interno", "Auditor Interno — internal audit, aseguramiento, riesgo"),
    # Round 11 — extensiones en capas generales (dominio/rol) + sustrato NA (deepening). Sin nuevos países.
    ("dominio/banca", "Banca: comercial, múltiple, digital, regulación prudencial, Basilea"),
    ("dominio/capital-riesgo", "Capital de riesgo / Venture Capital / Private Equity: fundraising, ciclo, term sheets"),
    ("dominio/cadena-suministro", "Cadena de suministro / Supply Chain: procurement, logística, inventario, riesgo"),
    ("dominio/consultoria", "Consultoría de gestión: estrategia, operaciones, big four, modelos de entrega"),
    ("dominio/servicios-profesionales", "Servicios profesionales: firmas, facturación, utilización, práctica"),
    ("rol/chief-compliance-officer", "CCO — Chief Compliance Officer"),
    ("rol/treasurer", "Treasurer — Tesorero corporativo: liquidez, financiamiento, riesgo de tasa/divisa"),
    ("rol/chief-investment-officer", "CIO — Chief Investment Officer (inversiones, portafolio, activos)"),
    ("rol/head-of-research", "Head of Research / R&D — I+D, pipeline, innovación técnica"),
    ("rol/chief-digital-officer", "CDO — Chief Digital Officer (transformación digital, canales digitales)"),
    # Round 12 — reabastecimiento (alcance: sustrato solo Norteamérica; dominio/rol generales).
    ("dominio/alimentos-bebidas", "Alimentos y bebidas (F&B): industria, regulación, cadena, marca"),
    ("dominio/moda", "Moda / apparel & retail fashion: industria, supply chain, marca"),
    ("dominio/espacio", "Espacio / space economy: satélites, lanzamiento, downstream"),
    ("dominio/agua", "Agua y saneamiento: infraestructura, regulación, escasez"),
    ("dominio/semiconductores", "Semiconductores / chips: fabs, diseño, cadena, CHIPS Act"),
    ("rol/chief-strategy-officer", "CSO — Chief Strategy Officer (estrategia corporativa)"),
    ("rol/chief-privacy-officer", "DPO — Chief Privacy Officer / Data Protection Officer (GDPR, CPRA)"),
    ("rol/chief-people-officer", "CHRO — Chief People Officer (talento, cultura, RRHH)"),
    ("rol/chief-client-officer", "Chief Client Officer (CX, retención, cuentas)"),
    ("rol/head-of-operations", "Head of Operations (operaciones, entrega, eficiencia)"),
    # Round 13 — reabastecimiento (alcance: sustrato solo Norteamérica; dominio/rol generales). Taxonomía ampliada.
    ("dominio/farmaceutica", "Industria farmacéutica: I+D, FDA/EMA, patentes, cadena de frío, precios, genéricos"),
    ("dominio/quimica", "Industria química: petroquímica, especialidades, REACH/TSCA, seguridad de procesos"),
    ("dominio/calidad", "Gestión de la calidad: ISO 9001, TQM, Six Sigma, auditorías de calidad"),
    ("dominio/gestion-riesgos", "Gestión de riesgos empresariales (ERM): ISO 31000, riesgo operativo, continuidad de negocio"),
    ("rol/chief-revenue-officer", "CRO — Chief Revenue Officer (dueño del top-line, ventas+marketing+CS)"),
    ("rol/chief-communications-officer", "CCO — Chief Communications Officer (comms internas/externas, reputación, PR)"),
    ("rol/chief-analytics-officer", "CAO — Chief Analytics Officer (función de analítica y ciencia de datos)"),
    ("rol/head-of-innovation", "Head of Innovation — gestión de la innovación, labs, corporate venturing"),
    # Round 14 — reabastecimiento (alcance: sustrato solo Norteamérica: sustrato NA deepening en educación; dominio/rol generales).
    ("dominio/blockchain", "Blockchain & web3: consenso, contratos inteligentes, DAOs, tokens, criptoactivos, DeFi"),
    ("dominio/etica-ia", "Ética de la IA / IA responsable: fairness, sesgo, transparencia, gobernanza, EU AI Act"),
    ("dominio/pricing", "Estrategia de precios: value-based, dinámico, psicológico, elasticidad, bundling"),
    ("dominio/geopolitica", "Geopolítica de negocios / geoeconomía: riesgo macro, sanciones, bloques comerciales, soberanía"),
    ("dominio/inteligencia-competitiva", "Inteligencia competitiva / market intelligence: vigilancia, benchmarking, CI legal"),
    ("rol/program-manager", "Program Manager — gestiona múltiples proyectos/PMO, dependencias, portafolio"),
    ("rol/solutions-architect", "Solutions Architect — arquitectura de solución, pre-venta, puente técnico-negocio"),
    ("rol/investor-relations", "Investor Relations — relación con inversionistas, disclosure, earnings, ESG reporting"),
    ("rol/regulatory-affairs", "Regulatory Affairs / Asuntos regulatorios — relación con reguladores, aprobaciones, compliance técnico"),
    ("rol/actuario", "Actuario — modelado actuarial, riesgo, seguros/pensiones, certificación (SOA/CAS/AAA)"),
    # Round 15 — reabastecimiento (alcance: sustrato solo Norteamérica: deepenings en medio-ambiente MX y política monetaria US/CA; dominio/rol generales).
    ("dominio/automatizacion", "Automatización / RPA / hyperautomation / BPA: IA agentes, intelligent automation, low-code"),
    ("dominio/insurtech", "Insurtech: modelos de negocio, telematics, IA en seguros, distribución digital"),
    ("dominio/legaltech", "Legaltech: contract lifecycle management, e-discovery, IA legal, regulatory tech"),
    ("dominio/crowdfunding", "Crowdfunding: reward/equity/debt/crowdlending, plataformas, regulación"),
    ("dominio/iot", "Internet de las Cosas (IoT): industrias, edge, seguridad, IIoT"),
    ("rol/enterprise-architect", "Enterprise Architect — arquitectura empresarial (TOGAF, alineación TI-negocio)"),
    ("rol/head-of-corporate-development", "Head of Corporate Development — M&A, BD corporativo, asignación de capital"),
    ("rol/chief-procurement-officer", "CPO — Chief Procurement Officer (sourcing, supplier management, spend)"),
    ("rol/head-of-tax", "Head of Tax / Tax Director — estrategia fiscal, transfer pricing, cumplimiento tributario"),
    ("rol/chief-diversity-officer", "CDO — Chief Diversity Officer (DEI, equidad, inclusión, pertenencia)"),
    # Round 16 — extensiones en capas generales (dominio/rol) + sustrato NA (deepening). Sin nuevos países.
    ("dominio/cloud-computing", "Cloud computing: IaaS/PaaS/SaaS, hyperscalers, IaC, FinOps, multi-cloud"),
    ("dominio/robotica", "Robótica: industrial, colaborativa (cobot), logística, móvil, RPA es distinto"),
    ("dominio/realidad-extendida", "Realidad extendida (XR): VR/AR/MR, metaverso, casos industriales"),
    ("dominio/infraestructura", "Infraestructura: concesiones, APP/PPP, transporte, energética, social"),
    ("dominio/seguridad-corporativa", "Seguridad corporativa: física, crisis, resiliencia, continuidad (vs ciberseguridad)"),
    ("rol/chief-security-officer", "CSO — Chief Security Officer (seguridad corporativa/física, crisis, resiliencia)"),
    ("rol/chief-learning-officer", "CLO — Chief Learning Officer (L&D, desarrollo de talento, upskilling)"),
    ("rol/chief-quality-officer", "CQO — Chief Quality Officer (calidad, excelencia operativa, mejora continua)"),
    ("rol/head-of-partnerships", "Head of Partnerships — alianzas estratégicas, canales, ecosistema, co-ventures"),
    ("rol/chief-experience-officer", "CXO — Chief Experience Officer (experiencia de cliente + empleado + marca)"),
    # Round 17 — reabastecimiento (alcance: sustrato solo Norteamérica: deepenings en transporte MX, defensa US, seguridad-social CA; dominio/rol generales).
    ("dominio/redes-sociales", "Redes sociales: plataformas, algoritmos, monetización, regulación, marketing social"),
    ("dominio/deportes", "Industria del deporte: derechos de medios, patrocinios, ligas, mercado global, eSports"),
    ("dominio/entretenimiento", "Entretenimiento: filmed entertainment, streaming, música, industrias creativas"),
    ("dominio/juegos-videojuegos", "Industria de videojuegos: consolas, mobile, PC, eSports, modelos de monetización"),
    ("dominio/economia-circular", "Economía circular: modelos de negocio circulares, reciclaje, diseño para circularidad, residuos"),
    ("rol/chief-ai-officer", "CAIO — Chief AI Officer (estrategia de IA, gobernanza, adopción, ética de IA)"),
    ("rol/chief-design-officer", "Chief Design Officer — liderazgo de diseño a nivel ejecutivo, experiencia, marca"),
    ("rol/chief-transformation-officer", "Chief Transformation Officer — lidera transformación digital/organizacional"),
    ("rol/chief-ethics-officer", "Chief Ethics Officer / Chief Integrity Officer (ética, cumplimiento ético, conducta)"),
    ("rol/chief-knowledge-officer", "CKO — Chief Knowledge Officer (gestión del conocimiento, KM, aprendizaje organizacional)"),
    # Round 18 — extensiones en capas generales (dominio/rol) + sustrato NA (deepening). Sin nuevos países.
    ("dominio/energias-renovables", "Energías renovables: solar, eólica, almacenamiento, hidrógeno, políticas de descarbonización"),
    ("dominio/finanzas-publicas", "Finanzas públicas: deuda soberana, política fiscal, presupuestos, multilaterales"),
    ("dominio/economia-digital", "Economía digital / plataformas: mercados de dos lados, gig economy, CBDC"),
    ("dominio/gobierno-de-datos", "Gobierno de datos: DAMA/DCAM, calidad, linaje, privacidad by design"),
    ("dominio/propiedad-intelectual", "Propiedad intelectual: patentes, marcas, derechos de autor, secretos comerciales, licencias"),
    ("rol/head-of-revops", "Head of RevOps — operaciones de ingresos: alinear ventas+marketing+CS, datos, proceso, tech stack"),
    ("rol/chief-content-officer", "Chief Content Officer — estrategia de contenido, editorial, narrativa de marca"),
    ("rol/head-of-sales-enablement", "Head of Sales Enablement — capacitación, contenido y herramientas de ventas"),
    ("rol/head-of-people-analytics", "Head of People Analytics — People Analytics/HR Analytics: attrition, engagement, workforce planning"),
    ("rol/chief-pricing-officer", "Chief Pricing Officer — estrategia de precios, elasticidad, monetización"),
    # Round 19 — reabastecimiento (alcance: sustrato solo Norteamérica: deepenings turismo MX, infraestructura US, energía CA; dominio/rol generales).
    ("dominio/ciudades-inteligentes", "Ciudades inteligentes / smart cities: IoT urbano, movilidad, datos, sostenibilidad, gobernanza"),
    ("dominio/healthtech", "Healthtech / salud digital: telemedicina, wearables, IA en salud, startups, regulación sanitaria digital"),
    ("dominio/publicidad", "Publicidad / advertising: medios, programática, agencias, medición, creatividad, CTV/digital"),
    ("dominio/franquicias", "Franquicias / franchising: modelo, royalties, FDD, regulación, expansión"),
    ("dominio/eventos", "Industria de eventos / MICE: meetings, incentives, conferences, exhibitions, congresos"),
    ("rol/legal-ops", "Legal Operations (legal ops): eBilling, proveedores externos, tecnología legal, gestión de contratos a escala"),
    ("rol/head-of-facilities", "Head of Facilities / Facilities Management: instalaciones, workplace, FM, ISO 41001, servicios generales"),
    ("rol/head-of-public-affairs", "Head of Public Affairs / Government Relations: relación con gobierno, lobbying legal, políticas públicas, trade associations"),
    ("rol/sales-engineer", "Sales Engineer: pre-venta técnica, demos, POCs, puente ingeniería-cliente; vs solutions-architect y AE"),
    ("rol/business-analyst", "Business Analyst: requisitos, procesos, BPM, puente negocio-TI; vs data-analyst y product-manager"),
    # Round 20 — reabastecimiento (alcance: sustrato solo Norteamérica: deepenings seguridad-social US, medio-ambiente CA, minería MX; dominio/rol generales).
    ("dominio/aviacion", "Aviación comercial: aerolíneas, aeropuertos, OEM (Airbus/Boeing), MRO, regulación FAA/EASA/ICAO"),
    ("dominio/maritimo", "Sector marítimo: navieras, puertos, logística portuaria, comercio marítimo, regulación OMI/flag states"),
    ("dominio/seguridad-nacional", "Seguridad nacional: inteligencia, contrainteligencia, infraestructura crítica, amenazas híbridas"),
    ("dominio/ciberdefensa", "Ciberdefensa: SOC nacional, threat intel, operaciones ofensivas/defensivas, vs ciberseguridad corporativa"),
    ("dominio/auditoria-gubernamental", "Auditoría pública / rendición de cuentas: entes fiscalizadores (ASF, GAO), auditabilidad del gasto"),
    ("rol/vp-product", "VP of Product — dueño de la org de producto, estrategia-a-entrega; vs CPO y Product Manager"),
    ("rol/chief-commercial-officer", "Chief Commercial Officer — estrategia comercial, ingresos, GTM, ventas+marketing+bizdev"),
    ("rol/chief-medical-officer", "Chief Medical Officer — liderazgo clínico/médico (salud/biotech); distinto de CMO de marketing"),
    ("rol/vp-operations", "VP of Operations — escala la función de operaciones; vs COO"),
    ("rol/head-of-engineering", "Head of Engineering — dirige managers de ingeniería; vs VP Eng y CTO"),
    # Round 21 — reabastecimiento (alcance: sustrato solo Norteamérica: deepenings finanzas-públicas MX/US/CA; dominio/rol generales).
    ("dominio/seguridad-alimentaria", "Seguridad alimentaria: HACCP, FSMA, Codex, COFEPRIS/SENASICA"),
    ("dominio/derecho-penal", "Derecho penal: delitos, white-collar crime, responsabilidad corporativa"),
    ("dominio/energia-nuclear", "Energía nuclear: fisión, SMR, NRC/CNSC/IAEA, residuos"),
    ("dominio/ciencias-materiales", "Ciencias de materiales: metales, polímeros, compuestos, semiconductores"),
    ("dominio/derecho-ambiental", "Derecho ambiental: NEPA, LGEEPA, CEPA, ESG"),
    ("rol/ml-engineer", "ML Engineer: entrena/despliega modelos en producción (MLOps)"),
    ("rol/security-engineer", "Security Engineer: AppSec, cloud security, threat modeling"),
    ("rol/fp-and-a-manager", "FP&A Manager: planificación, presupuesto, forecast, análisis de variaciones"),
    ("rol/product-designer", "Product Designer / UX: diseña experiencias de producto"),
    ("rol/account-manager", "Account Manager: relación post-venta, retención, crecimiento de cuenta"),
    # Round 22 — reabastecimiento (alcance: sustrato solo Norteamérica: deepening IP MX/US/CA; dominio/rol generales).
    ("dominio/arbitraje", "Arbitraje: comercial e de inversión (UNCITRAL/CIADI, laudo, tratados de protección de inversiones)"),
    ("dominio/tributacion-internacional", "Tributación internacional: BEPS/OCDE, tratados, precios de transferencia, paraísos fiscales, doble tributación"),
    ("dominio/derecho-internacional", "Derecho internacional público: tratados, costumbre, CJI, derecho de la OMC, derechos humanos"),
    ("dominio/ingenieria", "Ingeniería: disciplinas (civil/mecánica/sistemas/industrial), gestión de ingeniería, estándares"),
    ("dominio/contabilidad-forense", "Contabilidad forense: fraude, litigios, auditoría forense, evidencia, fraud examination"),
    ("rol/chairman", "Chairman / Presidente del Consejo: liderazgo de la junta, gobernanza, independencia del consejo"),
    ("rol/partner", "Partner / Socio: equity partner en firmas de servicios profesionales, profit sharing, governance"),
    ("rol/staff-engineer", "Staff/Principal Engineer: ladder IC senior, arquitectura técnica, influencia sin autoridad"),
    ("rol/delivery-manager", "Delivery Manager: entrega de servicios/proyectos, calidad y satisfacción del cliente, operación"),
    ("rol/engagement-manager", "Engagement Manager: consultoría, cuenta + entrega, equipo y margen del proyecto"),
    # Round 23 — reabastecimiento (alcance: sustrato solo Norteamérica: deepenings salud MX, telecom US, agricultura CA; dominio/rol generales).
    ("dominio/dispositivos-medicos", "Dispositivos médicos: regulación FDA 510(k)/PMA, COFEPRIS, Health Canada, MDR UE, calidad/QA"),
    ("dominio/computacion-cuantica", "Computación cuántica: qubits (supuesta/fotónica/iones atrapados), algoritmos, ventajas, casos empresariales"),
    ("dominio/investigacion-operaciones", "Investigación de operaciones (OR): optimización, programación lineal/entera, teoría de colas, simulación, cadena"),
    ("dominio/teoria-de-juegos", "Teoría de juegos: decisiones estratégicas, equilibrio de Nash, dilema del prisionero, subastas, aplicaciones de negocio"),
    ("dominio/gobierno-de-ti", "Gobierno de TI: COBIT, alineación TI-negocio, gestión de riesgo de TI, comités, value of IT"),
    ("rol/platform-engineer", "Platform Engineer — construye plataformas internas, golden paths, DevEx; vs SRE/DevOps"),
    ("rol/cloud-architect", "Cloud Architect — diseña arquitecturas cloud (IaaS/PaaS), multi-cloud, well-architected, costo/seguridad"),
    ("rol/research-scientist", "Research Scientist — investigación aplicada/básica, publicación, transferencia a producto, R&D"),
    ("rol/technical-program-manager", "Technical Program Manager (TPM) — coordina programas técnicos cross-funcionales, planning, riesgos"),
    ("rol/community-manager", "Community Manager — gestiona comunidad de usuarios/marca, redes sociales, advocasia, eventos"),
    # Round 24 — reabastecimiento (alcance: sustrato solo Norteamérica: deepenings politica-monetaria MX, medio-ambiente US, defensa CA; dominio/rol generales).
    ("dominio/derecho-administrativo", "Derecho administrativo / regulatory law: permisos, licencias, procedimientos administrativos, sanciones, revisión judicial"),
    ("dominio/control-interno", "Control interno: COSO 2013, ICFR, SOX 404, monitoreo, aseguramiento de operaciones"),
    ("dominio/seguridad-y-salud-ocupacional", "Seguridad y salud ocupacional (OHS): ISO 45001, OSHA/CSST, prevención de riesgos, bienestar laboral"),
    ("dominio/proteccion-de-datos", "Protección de datos / privacidad como disciplina transversal: GDPR/CCPA/CPRA/LGPD/PIPL, derechos ARCO, transferencias, privacy by design"),
    ("dominio/gestion-de-activos", "Gestión de activos / asset & wealth management: fondos, AUM, gestión de inversión, industria financiera"),
    ("rol/vp-finance", "VP of Finance — reporta al CFO, lidera FP&A/controller/treasury, planeación financiera"),
    ("rol/devops-engineer", "DevOps Engineer — CI/CD, infraestructura como código, pipelines, observabilidad, colaboración Dev+Ops"),
    ("rol/supply-chain-manager", "Supply Chain Manager — planificación de demanda/oferta, sourcing, logística, inventario, resiliencia de cadena"),
    ("rol/hr-business-partner", "HR Business Partner (HRBP) — socio de negocio de RRHH por unidad, people analytics, talento, cultura"),
    ("rol/channel-manager", "Channel Manager — gestión de canales de venta (partner/reseller/distributor), ecología de canal, incentivos"),
    # Round 25 — reabastecimiento (alcance: sustrato solo Norteamérica: deepenings seguridad-publica MX, sistema-financiero US, infraestructura CA; dominio/rol generales).
    ("dominio/proptech", "PropTech: tecnología inmobiliaria, smart buildings, plataformas de marketplaces, proptech/construcción, proptech financiero"),
    ("dominio/regtech", "RegTech: tecnología regulatoria, automatización de cumplimiento, AML/KYC, reporting regulatorio, supervisor tech"),
    ("dominio/nanotecnologia", "Nanotecnología: materiales a nanoescala, nanomedicina, electrónica, aplicaciones industriales y riesgos"),
    ("dominio/derecho-de-la-competencia", "Derecho de la competencia / antitrust: control de concentraciones, carteles, abuso de dominancia, autoridades (COFECE/FTC/EC/Competition Bureau)"),
    ("dominio/microfinanzas", "Microfinanzas: microcrédito, inclusión financiera, microseguros, instituciones de microfinanzas (IMF), impacto social"),
    ("rol/engineering-manager", "Engineering Manager — liderazgo de personas + técnico, entrega de equipos de ingeniería; vs Tech Lead/Head of Engineering"),
    ("rol/creative-director", "Creative Director — visión creativa de marca/producto, dirección de arte, campañas, contenido; vs Design Lead/CDO"),
    ("rol/site-reliability-engineer", "Site Reliability Engineer (SRE) — fiabilidad, SLO/error budget, operaciones de software; vs DevOps/Platform Engineer"),
    ("rol/vp-human-resources", "VP of Human Resources — lidera función RRHH a nivel ejecutivo; vs CHRO/Head of People"),
    ("rol/managing-director", "Managing Director — dueño de P&L de una unidad de negocio/país; vs CEO/General Manager"),
    # Round 26 — reabastecimiento (alcance: sustrato solo Norteamérica: deepening poder-judicial MX/US/CA; dominio/rol generales).
    ("dominio/etica-empresarial", "Ética empresarial / corporate ethics: códigos de conducta, programas de ética y compliance, anticorrupción, transparencia, cultura ética"),
    ("dominio/compensacion-beneficios", "Compensación y beneficios / total rewards: salario, variable pay, beneficios, equity, pensiones, filosofía de recompensa, bandas salariales"),
    ("dominio/transformacion-digital", "Transformación digital: adopción de tecnología, roadmap digital, reingeniería de procesos, cultura digital, habilitadores (cloud, data, IA)"),
    ("dominio/finanzas-cuantitativas", "Finanzas cuantitativas / quantitative finance: modelado estocástico, pricing de derivados, riesgo de mercado, quants, matemáticas financieras"),
    ("dominio/relaciones-laborales", "Relaciones laborales / industrial relations: sindicatos, contratación colectiva, huelgas, relación empresa-trabajador-representación, negociación colectiva"),
    ("rol/head-of-talent", "Head of Talent — estrategia de talento, employer brand, adquisición de talento, movilidad; vs reclutador/people-lead"),
    ("rol/head-of-sales-ops", "Head of Sales Operations — analítica de ventas, compensación de ventas, tooling/CRM, forecast; vs sales-lead/vp-sales"),
    ("rol/head-of-marketing-ops", "Head of Marketing Operations — martech, analítica de marketing, ops de campaña, presupuesto; vs marketing-manager/cmo"),
    ("rol/head-of-it", "Head of IT / IT Director — operación de TI interna, infraestructura, soporte, seguridad de TI; vs CIO/CTO"),
    ("rol/chief-brand-officer", "Chief Brand Officer — estrategia de marca a nivel ejecutivo, identidad, posicionamiento, brand equity; vs brand-manager/cmo"),
    # Round 27 — reabastecimiento (alcance: sustrato solo Norteamérica: deepening relaciones-exteriores MX, seguridad-nacional US, ciencia-e-innovacion CA; dominio/rol generales).
    ("dominio/electromovilidad", "Electromovilidad: vehículos eléctricos (EV), baterías, cargadores, movilidad eléctrica, autos eléctricos, V2G"),
    ("dominio/comercio-electronico", "Comercio electrónico / e-commerce: marketplaces, D2C, omnicanal digital, fulfillment, pagos en línea, retención online"),
    ("dominio/outsourcing", "Outsourcing / subcontratación y offshoring: BPO, nearshoring, modelo de entrega, gestión de proveedores, ITO/BPO/KPO"),
    ("dominio/gobierno-abierto", "Gobierno abierto / open government: transparencia, datos abiertos, participación ciudadana, civic tech, rendición de cuentas"),
    ("dominio/economia-comportamental", "Economía conductual / behavioral economics: sesgos cognitivos, heurísticas, nudge, decisiones económicas, economía y psicología"),
    ("rol/technical-writer", "Technical Writer — documentación técnica, manuals, knowledge base, docs-as-code, API docs; vs content/customer-success"),
    ("rol/portfolio-manager", "Portfolio Manager — gestión de carteras de inversión, asset allocation, riesgo, rendimiento, gestión de activos"),
    ("rol/change-manager", "Change Manager — gestión del cambio organizacional, ADKAR/Prosci, gestión de impacts, adopción; vs chief-transformation-officer"),
    ("rol/benefits-manager", "Benefits Manager — gestión de beneficios y compensación, pensiones, seguros de salud, bienestar, total rewards; vs head-of-people"),
    ("rol/consultor", "Consultor / Management Consultant — asesoría de gestión, estrategia/operaciones, entregables, firms; vs chief-* y head-of-*"),
]

SKIP = {"index.md", "log.md", "README.md", "raw"}


def existing_pages(node: str) -> set:
    base = os.path.join(ROOT, node)
    if not os.path.isdir(base):
        return set()
    out = set()
    for f in glob.glob(os.path.join(base, "**", "*.md"), recursive=True):
        rel = os.path.relpath(f, base)
        parts = rel.split(os.sep)
        if "raw" in parts:
            continue
        name = parts[-1]
        if name in SKIP:
            continue
        out.add(name[:-3])  # quita .md
    return out


def main() -> None:
    print("# Análisis de huecos — MVAS\n")
    total = 0
    for node, topics in TAXONOMY.items():
        have = existing_pages(node)
        missing = [(s, t) for (s, t) in topics if s not in have]
        if missing:
            print(f"## {node} — faltan {len(missing)}")
            for s, t in missing:
                print(f"- [{s}] {t}")
            total += len(missing)
    print("\n## Nodos sugeridos (que aún no existen)")
    _any_new = False
    for path, desc in NEW_NODES:
        if path.startswith("sustrato/") and path.split("/", 1)[1] not in ALLOWED_SUSTRATO:
            continue  # fuera de alcance: no es país de Norteamérica
        if not os.path.isdir(os.path.join(ROOT, path)):
            print(f"- {path}: {desc}  <- NUEVO")
            _any_new = True
    if not _any_new:
        print("- (ninguno: todos los nodos sugeridos ya existen)")
    print(f"\nTOTAL huecos en nodos existentes: {total}")


if __name__ == "__main__":
    main()
