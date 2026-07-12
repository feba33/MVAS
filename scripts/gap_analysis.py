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
