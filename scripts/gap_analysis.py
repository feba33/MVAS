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
        # Round 28 — deepening NA (economía MX).
        ("economia", "Economía México: PIB, INEGI, Banxico, sectores (manufactura, servicios, petróleo), informalidad, comercio exterior, perspectivas macro"),
        # Round 29 — deepening NA (demografía MX).
        ("demografia-poblacion", "Demografía y población México: INEGI, CONAPO, censo, estructura por edad, migración interna/internacional, crecimiento, densidad"),
        # Round 30 — deepening NA (infraestructura MX).
        ("infraestructura", "Infraestructura México: transporte (SICT), energía (CFE/PEMEX), agua (CONAGUA), vivienda, inversión"),
        # Round 31 — deepening NA (ciencia e innovación MX).
        ("ciencia-e-innovacion", "Ciencia e innovación México: CONAHCYT, SNCTI, I+D, nearshoring de conocimiento"),
        # Round 32 — deepening NA (competitividad MX).
        ("competitividad", "Competitividad México: IMCO, WEF, Doing Business (hist.), clústeres, facilitación de negocios, ranking global"),
        # Round 33 — deepening NA (gobierno federal MX).
        ("gobierno-federal", "Gobierno federal de México: federalismo, Poder Ejecutivo (Presidente y secretarías de Estado), Congreso de la Unión (Cámara de Diputados y Senado), división de poderes; vs poder-judicial"),
        # Round 34 — deepening NA (trabajo MX).
        ("trabajo", "Trabajo / mercado laboral México: STPS, empleo, salario mínimo, outsourcing/subscontratación (Ley 2021), seguridad social asociada, productividad, informalidad; vs derecho-laboral/seguridad-social"),
        # Round 35 — deepening NA (vivienda MX).
        ("vivienda", "Vivienda México: INFONAVIT, SHF, FOVISSSTE, mercado inmobiliario, déficit habitacional, política de vivienda, crédito hipotecario; vs sustrato/estados-unidos/vivienda-real-estate"),
        # Round 36 — deepening NA (banca de desarrollo MX).
        ("banca-desarrollo", "Banca de desarrollo México: NAFIN (hoy Banco Nacional de Comercio Exterior), BANCOMEXT, Banobras, SHF, Banco del Bienestar, Bansefi; banca de segundo piso, fomento productivo, PyMEs, infraestructura; vs sustrato/mexico/banca-sistema-financiero"),
        # Round 37 — deepening NA (entidades federativas MX).
        ("entidades-federativas", "Entidades federativas de México / estados: gobiernos estatales, gobernadores, congresos locales, coordinación fiscal (Sistema Nacional de Coordinación Fiscal), impuestos estatales (IEPS estatal, ISN, predial), permisos y regulación subnacional; vs gobierno-federal"),
        # Round 38 — deepening NA (sector servicios por país).
        ("sector-servicios", "Sector servicios México: comercio, turismo, financiero, telecom, transporte, gobierno; peso en el PIB, informalidad, productividad; vs economia/trabajo"),
        # Round 39 — deepening NA (pobreza y desigualdad).
        ("pobreza-desigualdad", "Pobreza y desigualdad México: CONEVAL (medición multidimensional: ingresos y carencias sociales), líneas de pobreza, programas sociales ( Prospera/atención a adultos mayores), desigualdad de ingreso; vs seguridad-social/trabajo"),
        # Round 40 — deepening NA (fronteras por país).
        ("fronteras", "Fronteras de México: frontera norte con EE.UU. (3,155 km, 14 cruces oficiales, TMEC/USMCA, aduanas, maquiladoras, Programa Frontera Norte, Plan Frontera Sur/control migratorio sur), migración, comercio transfronterizo, seguridad; vs relaciones-exteriores/comercio-exterior"),
        # Round 41 — deepening NA (agua por país).
        ("agua", "Agua y recursos hídricos México: CONAGUA, SEMARNAT, sequía, infraestructura hídrica, presas, agua potable/saneamiento, cuencas, retos de escasez"),
        # Round 42 — deepening NA (gobierno digital por país).
        ("gobierno-digital", "Gobierno digital de México: Gob.mx, Agenda Digital Nacional, México Digital, INEGI (datos abiertos), e.firma, identidad digital, servicios digitales ciudadanos; vs gobierno-federal/relaciones-institucionales"),
        # Round 43 — deepening NA (industria aeroespacial MX).
        ("industria-aeroespacial", "Industria aeroespacial México: ensamble de aeronaves y MRO, clústeres (Querétaro, Baja California, Sonora), OEMs y Tier-1, FAA/EASA, exportación; vs dominio/aeroespacial"),
        # Round 44 — deepening NA (seguros por país).
        ("seguros", "Seguros México: CNSF, sector asegurador, seguros obligatorios (auto, gastos médicos mayores, vida), RySO/SOAT; vs dominio/seguros"),
        # Round 45 — deepening NA (pueblos indígenas MX).
        ("pueblos-indigenas", "Pueblos indígenas de México: Art. 2 Constitucional, INPI (Instituto Nacional de los Pueblos Indígenas), derechos indígenas, autonomía, lenguas originarias, consulta previa; vs derechos-humanos"),
        # Round 46 — deepening NA (empleo MX).
        ("empleo", "Empleo / mercado laboral México: tasa de desempleo (INEGI/ENOE), informalidad, subempleo, salario mínimo, población económicamente activa (PEA), productividad laboral; vs trabajo (laboral) y seguridad-social"),
        # Round 47 — deepening NA (economía creativa MX).
        ("economia-creativa", "Economía creativa / industrias culturales México: cine, música, diseño, artes, videojuegos, edtech creativo, contribución al PIB, políticas culturales; vs cultura (solo CA) y sector-servicios"),
        # Round 48 — deepening NA (PyMEs MX).
        ("pymes", "PyMEs México: economía de las pequeñas y medianas empresas, acceso a financiamiento (NAFIN/Bancomext), productividad, digitalización, encadenamientos, políticas de apoyo (IMMEX para PYME, REP); vs sustrato/mexico/emprendimiento y dominio/pymes"),
        # Round 49 — deepening NA (impuestos MX).
        ("impuestos", "Sistema tributario México: SHCP/SAT, ISR, IVA, IEPS, impuesto al depósito bancario, federales/estatales/municipales, regímenes (RESICO, SIMPLE), tratados de doble tributación; vs sat y finanzas-publicas"),
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
        # Round 28 — deepening NA (ciencia e innovación US).
        ("ciencia-e-innovacion", "Ciencia e innovación EE.UU.: NSF, DOE national labs, NIH, I+D, CHIPS Act, ecosistema de investigación y desarrollo"),
        # Round 29 — deepening NA (demografía US).
        ("demografia-poblacion", "Demografía y población EE.UU.: Census Bureau, estructura por edad, migración, diversidad, proyecciones, densidad"),
        # Round 30 — deepening NA (sector manufacturero US).
        ("sector-manufacturero", "Sector manufacturero EE.UU.: manufactura, CHIPS Act, IRA, reshoring, empleo, subsectores"),
        # Round 31 — deepening NA (relaciones exteriores US).
        ("relaciones-exteriores", "Relaciones exteriores EE.UU.: Department of State, diplomacia, tratados, USAID, soft power"),
        # Round 32 — deepening NA (transporte US).
        ("transporte", "Transporte EE.UU.: DOT, FAA, FHWA, FRA, USCG; modos carretero/ferroviario/aéreo/marítimo, infraestructura de transporte"),
        # Round 33 — deepening NA (impuestos federales US).
        ("impuestos", "Sistema tributario federal EE.UU.: IRS, Internal Revenue Code, federal income tax, payroll (FICA), corporate tax, estate/gift; vs finanzas-publicas"),
        # Round 34 — deepening NA (elecciones US).
        ("elecciones", "Sistema electoral EE.UU.: Constitución, Electoral College, voto popular, FEC, derechos de voto, primarias, midterms, ciclo electoral, votación por correo; vs poder-judicial"),
        # Round 35 — deepening NA (seguridad pública US).
        ("seguridad-publica", "Seguridad pública EE.UU.: law enforcement, DOJ (Civil Rights Division, OPD), FBI, policía estatal/local, crimen, reforma policial, armas de fuego; vs seguridad-nacional (homeland/intel)"),
        # Round 36 — deepening NA (banca de desarrollo US).
        ("banca-desarrollo", "Banca de desarrollo EE.UU.: SBA (Small Business Administration), DFC (Development Finance Corporation, antes OPIC), EXIM Bank (Export-Import Bank), USDA Rural Development; crédito a PyMEs, exportaciones, desarrollo; vs sustrato/estados-unidos/sistema-financiero"),
        # Round 37 — deepening NA (estados US).
        ("estados", "Estados de EE.UU. / federalismo: gobiernos estatales, poderes estatales, división federal-state (Commerce Clause, Supremacy Clause), state law, regulación subnacional, federalismo estadounidense; vs poder-judicial"),
        # Round 38 — deepening NA (protección al consumidor por país).
        ("proteccion-consumidor", "Protección al consumidor EE.UU.: FTC, CFPB, CPSC, fiscales estatales (AG), engaño, privacidad, reembolsos; vs derecho-del-consumidor"),
        # Round 39 — deepening NA (pobreza y desigualdad).
        ("pobreza-desigualdad", "Pobreza y desigualdad EE.UU.: Census poverty line (federal/state), income inequality (Gini), safety net (SNAP/TANF/earned income tax credit), disparidades raciales; vs seguridad-social/trabajo"),
        # Round 40 — deepening NA (fronteras por país).
        ("fronteras", "Fronteras de EE.UU.: frontera sur con México (CBP/USBP, muros, puertos de entrada) y frontera norte con Canadá (puertos de entrada, comercio USMCA), aduanas (CBP/OEA), migración, seguridad fronteriza; vs inmigracion/seguridad-nacional"),
        # Round 41 — deepening NA (agua por país).
        ("agua", "Agua y recursos hídricos EE.UU.: EPA Office of Water, Clean Water Act, Safe Drinking Water Act, sequía del Oeste, río Colorado, USGS, infraestructura de agua"),
        # Round 42 — deepening NA (gobierno digital por país).
        ("gobierno-digital", "Gobierno digital EE.UU.: US Digital Service, 18F, Login.gov, cloud.gov, federal IT modernization (FITARA), e-gov, identidad digital federal; vs poder-judicial/seguridad-nacional"),
        # Round 43 — deepening NA (industria espacial US).
        ("industria-espacial", "Industria espacial EE.UU.: NASA, Space Force, comercial (SpaceX/Blue Origin/ULA), FCC (espectro orbital), Artemis, satélites; vs dominio/espacio"),
        # Round 44 — deepening NA (seguros por país).
        ("seguros", "Seguros EE.UU.: NAIC, regulación estatal (McCarran-Ferguson), tipos (auto/life/health/P&C), guaranty funds, solvencia; vs dominio/seguros"),
        # Round 45 — deepening NA (pueblos indígenas US).
        ("pueblos-indigenas", "Pueblos indígenas EE.UU. (Native Americans / American Indians): Bureau of Indian Affairs (BIA), tribal sovereignty, trust lands, tratados, NCAI, consulta; vs derechos-humanos"),
        # Round 46 — deepening NA (política fiscal US).
        ("politica-fiscal", "Política fiscal EE.UU.: postura fiscal (estímulo/austeridad), déficit y deuda, CBO, presupuesto discrecional/mandatorio, recortes/gastos, efecto multiplicador, vs impuestos (IRS) y finanzas-publicas (Treasury/deuda)"),
        # Round 47 — deepening NA (energía nuclear US).
        ("energia-nuclear", "Energía nuclear EE.UU.: NRC, DOE Office of Nuclear Energy, plantas comerciales, SMR/advanced reactors, residuos (Yucca/WIPP), seguridad, vs dominio/energia-nuclear (disciplina)"),
        # Round 48 — deepening NA (small business / PyMEs US).
        ("pymes", "Small business / PyMEs EE.UU.: SBA, pequeñas empresas (<500 empleados), acceso a capital, 8(a)/HUBZone, gobierno federal como cliente, emprendimiento, impacto en empleo; vs sustrato/estados-unidos/emprendimiento y dominio/pymes"),
        # Round 49 — deepening NA (turismo US).
        ("turismo", "Turismo EE.UU.: Travel & Tourism (Brand USA, NTTO/Commerce, parques nacionales NPS), contribución al PIB/empleo, destinos, turismo médico/lazer, hotelería y aviación; vs sector-servicios y sustrato/mexico/turismo"),
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
        # Round 28 — deepening NA (demografía/población CA).
        ("demografia-poblacion", "Demografía y población Canadá: Statistics Canada, censo, crecimiento impulsado por inmigración, estructura por edad, densidad"),
        # Round 29 — deepening NA (seguridad pública CA).
        ("seguridad-publica", "Seguridad pública Canadá: Public Safety Canada, RCMP, CBSA, gestión de emergencias, policía, fronteras, crimen"),
        # Round 30 — deepening NA (relaciones exteriores CA).
        ("relaciones-exteriores", "Relaciones exteriores Canadá: Global Affairs Canada, multilateralismo, paz, comercio, diplomacia"),
        # Round 31 — deepening NA (economía CA).
        ("economia", "Economía de Canadá: PIB, sectores, recursos, comercio, Bank of Canada, CAD, G7"),
        # Round 32 — deepening NA (sector manufacturero CA).
        ("sector-manufacturero", "Sector manufacturero Canadá: Ontario (auto), Quebec (aeroespacial), Alberta (petroquímica), empleo, exportación"),
        # Round 33 — deepening NA (elecciones CA).
        ("elecciones", "Sistema electoral Canadá: Elections Canada, democracia, voto, Cámara de los Comunes, Senado, provincias, reforma electoral"),
        # Round 34 — deepening NA (cultura CA).
        ("cultura", "Cultura Canadá: Canadian Heritage, industrias culturales (radiodifusión, cine, música, libros), Ley de Radiodifusión, políticas bilingües (FR/EN), identidad y diversidad; vs turismo/medios-comunicacion"),
        # Round 35 — deepening NA (vivienda CA).
        ("vivienda", "Vivienda Canadá: CMHC, Estrategia Nacional de Vivienda (2017), asequibilidad, Fondo Nacional de Vivienda, crisis de vivienda, provincias/municipios; vs sustrato/estados-unidos/vivienda-real-estate"),
        # Round 36 — deepening NA (banca de desarrollo CA).
        ("banca-desarrollo", "Banca de desarrollo Canadá: BDC (Business Development Bank of Canada), EDC (Export Development Canada), FCC (Farm Credit Canada); financiamiento a PyMEs, exportaciones, agronegocio; vs sustrato/canada/sector-bancario"),
        # Round 37 — deepening NA (pueblos indígenas CA).
        ("pueblos-indigenas", "Pueblos indígenas de Canadá: First Nations, Inuit, Métis; tratados, Constitución s.35, UNDRIP, duty to consult, autogobierno, impacto en recursos/energía/infra; vs derechos-humanos"),
        # Round 38 — deepening NA (sector servicios por país).
        ("sector-servicios", "Sector servicios Canadá: comercio minorista, financiero, salud, educación, TIC, gobierno, turismo; peso en el PIB, productividad, empleo; vs economia/trabajo"),
        # Round 39 — deepening NA (pobreza y desigualdad).
        ("pobreza-desigualdad", "Pobreza y desigualdad Canadá: Market Basket Measure (MBM), Canada's Poverty Reduction Strategy, Ontario/Quebec poverty lines, desigualdad de ingreso; vs seguridad-social/trabajo"),
        # Round 40 — deepening NA (fronteras por país).
        ("fronteras", "Fronteras de Canadá: frontera terrestre más larga del mundo con EE.UU. (8,891 km incl. Alaska), CBSA, puertos de entrada, comercio USMCA, cruces (Windsor-Detroit, Peace Bridge), migración y seguridad; vs relaciones-exteriores/comercio-exterior"),
        # Round 41 — deepening NA (agua por país).
        ("agua", "Agua y recursos hídricos Canadá: agua dulce/Grandes Lagos, gestión de cuencas, ECCC agua, First Nations (agua potable), infraestructura hídrica"),
        # Round 42 — deepening NA (gobierno digital por país).
        ("gobierno-digital", "Gobierno digital Canadá: Canadian Digital Service (CDS), GC digital standards, Service Canada en línea, identidad digital federada, GC Forms, digital gov; vs gobierno-federal/relaciones-institucionales"),
        # Round 43 — deepening NA (industria automotriz CA).
        ("industria-automotriz", "Industria automotriz Canadá: Ontario (Windsor, Oshawa, Ingersoll), OEMs (GM/Ford/Stellantis/Toyota/Honda), USMCA reglas de origen auto, transición EV; vs dominio/automotriz"),
        # Round 44 — deepening NA (seguros por país).
        ("seguros", "Seguros Canadá: OSFI (federación), regulación provincial (FSRA Ontario, AMF Québec), P&C/life, seguro de auto provincial, solvencia; vs dominio/seguros"),
        # Round 45 — deepening NA (lenguas oficiales CA).
        ("lenguas-oficiales", "Lenguas oficiales Canadá: Official Languages Act, bilingüismo francés/inglés, Comisionado de Lenguas Oficiales, servicios en ambos idiomas, equilibrio; vs cultura"),
        # Round 46 — deepening NA (competitividad CA).
        ("competitividad", "Competitividad Canadá: ranking WEF/Bank (World Bank Doing Business hist., IQC), clima de negocios, productividad, facilitación, infraestructura, talento, innovación; vs economia y ciencia-e-innovacion"),
        # Round 47 — deepening NA (política fiscal CA).
        ("politica-fiscal", "Política fiscal Canadá: Department of Finance, presupuesto federal, déficit y deuda/PIB, gasto en programas (salud/transferencias), estímulo, vs impuestos (CRA) y finanzas-publicas"),
        # Round 48 — deepening NA (PyMEs CA).
        ("pymes", "PyMEs Canadá: pequeñas y medianas empresas (Statistics Canada define PME <500 empleados), apoyo (BDC, Canadá Emprende), acceso a financiamiento, productividad, exporteras; vs sustrato/canada/emprendimiento y dominio/pymes"),
        # Round 49 — deepening NA (minería CA).
        ("mineria", "Minería Canadá: NRCan, oro/plata/níquel/uránio, mining clusters (Ontario, Québec, BC), regulación (federal/provincial), impacto indígena, exportación; vs dominio/mineria y sustrato/mexico/mineria"),
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
    # Round 28 — reabastecimiento (alcance: sustrato solo Norteamérica: deepenings economia MX, ciencia-e-innovacion US, demografia-poblacion CA; dominio/rol generales).
    ("dominio/aduanas", "Aduanas / despacho aduanero: aranceles, valoración en aduana, OMA, SIAVI, clasificación arancelaria, import/export"),
    ("dominio/finanzas-sostenibles", "Finanzas sostenibles / green & sustainable finance: bonos verdes, taxonomía climática (UE/ICMA), ESG investing, IFRS S1/S2"),
    ("dominio/cadena-de-valor", "Cadena de valor (Porter): actividades primarias y de soporte, ventaja competitiva, análisis de costo/valor"),
    ("dominio/inteligencia-de-mercado", "Inteligencia de mercado: market sizing (TAM/SAM/SOM), tendencias, voice of customer, estudios de mercado"),
    ("dominio/clima-organizacional", "Clima organizacional: engagement, encuestas, satisfacción, cultura percibida; vs cultura-organizacional (valores profundos)"),
    ("rol/software-engineer", "Software Engineer — ingeniería de software: diseño/codificación, clean code, testing, agile, arquitectura de software"),
    ("rol/prompt-engineer", "Prompt Engineer — diseño de prompts para LLMs, evaluación de modelos, ingeniería de IA generativa; vs ml-engineer/data-scientist"),
    ("rol/fractional-executive", "Ejecutivo fraccionario / Fractional CXO — liderazgo part-time por retainer, advisory, scale-ups; vs founder-ceo/consultor"),
    ("rol/head-of-customer-experience", "Head of Customer Experience (CX) — journey, VoC, NPS/CSAT, operación de CX; vs chief-experience-officer y customer-success-lead"),
    ("rol/category-manager", "Category Manager — gestión de categoría (retail/compras): assortment, pricing, proveedores, P&L de categoría; vs supply-chain-manager"),
    # Round 29 — reabastecimiento (alcance: sustrato solo Norteamérica: deepenings demografia MX/US, seguridad-publica CA; dominio/rol generales).
    ("dominio/i-d", "I+D / Investigación y Desarrollo: función empresarial y sector, intensidad de I+D, open innovation, pipelines, labs, transferencia tecnológica"),
    ("dominio/compras", "Compras / Procurement & Strategic Sourcing: sourcing estratégico, P2P, gestión de proveedores, categorías, ahorro, riesgo de suministro"),
    ("dominio/juego-azar", "Industria del juego y apuestas (gambling & betting): casinos, loterías, apuestas deportivas online, regulación, juego responsable; vs videojuegos"),
    ("dominio/tercer-sector", "Tercer sector / organizaciones sin fines de lucro: ONG, fundaciones, asociaciones, filantropía, gobernanza, impacto social"),
    ("dominio/servicios-ambientales", "Servicios ambientales: gestión de residuos, tratamiento de agua, remediación, reciclaje, economía circular como industria"),
    ("rol/country-manager", "Country Manager — P&L de un país/subsidiaria, operaciones locales, relación con HQ; vs regional-director y managing-director"),
    ("rol/regional-director", "Regional Director — gestión de múltiples países/regiones, P&L regional, coordinación de subsidiarias; vs country-manager y vp-operations"),
    ("rol/data-architect", "Data Architect — modelado de datos, arquitectura de información, gobierno técnico de datos, calidad/linaje; vs data-engineer y chief-data-officer"),
    ("rol/network-engineer", "Network Engineer — diseño/operación de redes, conectividad, routing/seguridad de red, LAN/WAN/SD-WAN; vs cloud-architect y security-engineer"),
    ("rol/dba", "Database Administrator (DBA) — administración de bases de datos, backup/recovery, rendimiento, seguridad de datos; vs data-engineer"),
    # Round 30 — reabastecimiento (alcance: sustrato solo Norteamérica: deepenings infraestructura MX, sector-manufacturero US, relaciones-exteriores CA; dominio/rol generales).
    ("dominio/salud-publica", "Salud pública: prevención, epidemiología, determinantes, sistemas de salud poblacional, OMS/OPS"),
    ("dominio/derecho-tributario", "Derecho tributario: potestad del Estado, impuestos, procedimiento, controversias, defensa"),
    ("dominio/agrotech", "AgTech / tecnología agrícola: agricultura de precisión, IoT, biotec, maquinaria conectada, decision support"),
    ("dominio/movilidad-urbana", "Movilidad urbana sostenible: modos, última milla, MaaS, impacto CO2, planeación urbana"),
    ("dominio/gestion-del-conocimiento", "Gestión del conocimiento (KM): crear, capturar, compartir y aplicar conocimiento organizacional"),
    ("rol/paralegal", "Paralegal / asistente legal: soporte legal (investigación, redacción, casos) bajo supervisión de abogado"),
    ("rol/wealth-manager", "Wealth Manager / asesor de patrimonio: asesoría integral a HNW/UHNW (inversión, sucesión, fiscal)"),
    ("rol/procurement-manager", "Procurement Manager / jefe de compras: abastecimiento, sourcing, negociación, gestión de proveedores, P2P"),
    ("rol/executive-assistant", "Executive Assistant / asistente ejecutivo: soporte directo a ejecutivo senior (agenda, documentos, gatekeeping)"),
    ("rol/learning-manager", "Learning & Development Manager (L&D): capacitación y desarrollo del talento, diseño instruccional, upskilling"),
    # Round 31 — reabastecimiento (alcance: sustrato solo Norteamérica: deepenings ciencia-e-innovacion MX, relaciones-exteriores US, economia CA; dominio/rol generales).
    ("dominio/derechos-humanos", "Derechos humanos: marco internacional (ONU/ONU-DH), constitucionales, empresariales (UNGP), debido proceso"),
    ("dominio/comportamiento-del-consumidor", "Comportamiento del consumidor: psicología del consumidor, journey, factores, nudge; vs marketing/economia-comportamental"),
    ("dominio/trabajo-remoto", "Trabajo remoto / remote & hybrid work: teletrabajo, política, herramientas, productividad, legal laboral"),
    ("dominio/desarrollo-organizacional", "Desarrollo organizacional (OD): diagnóstico, intervenciones, cambio planeado, adult learning; vs gestion-cambio/cultura"),
    ("dominio/inteligencia-emocional", "Inteligencia emocional (EQ): autoconciencia, regulación, empatía, habilidades sociales; liderazgo y equipos"),
    ("rol/agile-coach", "Agile Coach — facilita transformación ágil a nivel org, coaching a líderes/equipos; vs scrum-master/chief-transformation-officer"),
    ("rol/devsecops-engineer", "DevSecOps Engineer — security as code, shift-left, SAST/DAST, supply chain (SBOM); vs devops-engineer/security-engineer"),
    ("rol/account-director", "Account Director — dueño de relación estratégica de cuenta grande, retención/expansión; vs account-manager/account-executive"),
    ("rol/social-media-manager", "Social Media Manager — gestión de canales sociales, contenido, comunidad, métricas; vs community-manager/redes-sociales"),
    ("rol/plant-manager", "Plant Manager — opera planta de manufactura, P&L de planta, seguridad/calidad/prod; vs head-of-operations/vp-operations"),
    # Round 32 — reabastecimiento (alcance: sustrato solo Norteamérica: deepenings competitividad MX, transporte US, sector-manufacturero CA; dominio/rol generales).
    ("dominio/metodologias-agiles", "Metodologías ágiles: Scrum, Kanban, SAFe, Lean, XP; frameworks de entrega, ceremonies, roles; vs waterfall"),
    ("dominio/gobierno-de-ia", "Gobierno de IA / AI governance: regulación, riesgo, frameworks (EU AI Act, NIST AI RMF, ISO/IEC 42001), model risk; vs etica-ia/ia-generativa"),
    ("dominio/ciencia-de-datos", "Ciencia de datos (data science): ciclo CRISP-DM, modelado predictivo, ML aplicado, herramientas (Python/R); vs estadistica/analitica-negocio"),
    ("dominio/derecho-concursal", "Derecho concursal / insolvencia: reestructura y liquidación empresarial (Chapter 11/15 US, LCM MX, BIA CA); vs sustrato/bankruptcy"),
    ("dominio/mercados-de-carbono", "Mercados de carbono: cap-and-trade/ETS, bonos de carbono, precios de carbono, verificación, mercados voluntarios; vs finanzas-sostenibles/medio-ambiente"),
    ("rol/ai-engineer", "AI Engineer — construye productos/agentes de IA sobre modelos (vs ml-engineer que entrena); prompt/API, RAG, evals, MLOps de producto"),
    ("rol/customer-success-manager", "Customer Success Manager (CSM) — gestión de cuenta post-venta, onboarding, salud de cuenta, retención/expansión; vs customer-success-lead"),
    ("rol/compliance-manager", "Compliance Manager — operacionaliza el programa de cumplimiento (monitoreo, AML/KYC, reportes, controles); vs compliance-officer/chief-compliance-officer"),
    ("rol/sales-manager", "Sales Manager — lidera equipo de ventas IC, cuotas, coaching, pipeline; vs sales-lead/vp-sales/account-executive"),
    ("rol/field-marketing-manager", "Field Marketing Manager — marketing regional/eventos, campañas locales, ABM táctico; vs marketing-manager/head-of-marketing-ops/demand-generation"),
    # Round 33 — reabastecimiento (alcance: sustrato solo Norteamérica: deepenings gobierno-federal MX, impuestos US, elecciones CA; dominio/rol generales).
    ("dominio/inteligencia-artificial", "Inteligencia artificial: historia, tipos (ANI/AGI/ASI), machine learning/deep learning, aplicaciones empresariales, riesgos; vs ia-generativa/etica-ia/gobierno-de-ia"),
    ("dominio/derecho-civil", "Derecho civil: personas, familia, obligaciones, bienes, sucesiones, contratos civiles; vs leyes/derecho-contratos (mercantil)"),
    ("dominio/cosmetica", "Industria cosmética / belleza: mercado global, regulación (FDA/COFEPRIS/EU), supply chain, marcas, D2C; vs alimentos-bebidas/moda"),
    ("dominio/empaque", "Industria del empaque / packaging: materiales (plástico/papel/metal/vidrio), sostenibilidad, regulación, cadena de valor; vs manufactura"),
    ("dominio/textil", "Industria textil / confección: cadena (fibra-hilo-tejido-confección), mercado, sostenibilidad, nearshoring; vs moda (retail)"),
    ("rol/accountant", "Accountant / Contador: contabilidad financiera, conciliación, estados financieros, impuestos operativos, cierre; vs controller/financial-analyst"),
    ("rol/team-lead", "Team Lead / Líder de equipo técnico: supervisión directa de IC, mentoring, entrega de equipo; vs engineering-manager/tech-lead"),
    ("rol/content-manager", "Content Manager: estrategia de contenido, calendario editorial, producción y distribución; vs chief-content-officer/marketing-manager"),
    ("rol/it-manager", "IT Manager: operación de TI, infraestructura, soporte, proveedores; vs head-of-it/ciso"),
    ("rol/head-of-design", "Head of Design: lidera la organización de diseño (producto/brand/UX), cartera y equipo; vs design-lead/chief-design-officer"),
    # Round 34 — reabastecimiento (alcance: sustrato solo Norteamérica: deepenings trabajo MX, elecciones US, cultura CA; dominio/rol generales).
    ("dominio/salud-mental", "Salud mental: bienestar psicológico, psiquiatría/psicología clínica, prevención, salud mental en el trabajo, políticas de salud mental, destigmatización; vs salud/salud-publica"),
    ("dominio/gamificacion", "Gamificación: mecánicas de juego (puntos, badges, leaderboards, bucles de progreso) aplicadas a producto, aprendizaje, marketing y engagement; vs comportamiento-del-consumidor/economia-comportamental"),
    ("dominio/urbanismo", "Urbanismo / planeación urbana: zonificación, uso de suelo, movilidad, vivienda, infraestructura urbana, sostenibilidad, smart cities; vs ciudades-inteligentes/movilidad-urbana"),
    ("dominio/arquitectura", "Arquitectura: diseño del entorno construido, arquitectura sostenible/verde, AEC, códigos, BIM; vs construccion"),
    ("dominio/biometria", "Biometría: reconocimiento facial/huella/iris/voice, identidad digital, autenticación, privacidad y regulación (GDPR/bans), aplicaciones (fronteras, fintech); vs proteccion-de-datos"),
    ("rol/chief-administrative-officer", "CAO — Chief Administrative Officer: lidera funciones administrativas (facilities, legal ops, RH operativo, procurement, IT interna), backbone operativo; vs COO/CFO"),
    ("rol/head-of-data-science", "Head of Data Science — lidera equipos de ciencia de datos, estrategia de modelado/ML, embed en producto y decisiones; vs data-scientist/chief-analytics-officer/chief-data-officer"),
    ("rol/head-of-employer-branding", "Head of Employer Branding — marca empleadora, talent brand, recruitment marketing, propuesta de valor al empleado; vs head-of-talent/reclutador/head-of-people"),
    ("rol/director-of-operations", "Director of Operations — liderazgo operativo de nivel medio/alto, ejecución de procesos y P&L de operaciones; vs head-of-operations/vp-operations/coo"),
    ("rol/head-of-communications", "Head of Communications — comms funcional (internas/externas, medios, crisis), ejecución de relaciones públicas; vs chief-communications-officer/relaciones-publicas"),
    # Round 35 — reabastecimiento (alcance: sustrato solo Norteamérica: deepenings vivienda MX, seguridad-publica US, vivienda CA; dominio/rol generales).
    ("dominio/edtech", "EdTech / tecnología educativa: plataformas de aprendizaje, LMS, contenido digital, tutoría IA, mercado global, modelos freemium/B2B/B2G; vs educacion"),
    ("dominio/foodtech", "FoodTech: tecnología alimentaria (alt-proteínas, agricultura vertical, fermentación, delivery tech, trazabilidad), cadena de valor de alimentos, startups; vs agrotech/alimentos-bebidas"),
    ("dominio/deep-tech", "Deep tech: empresas basadas en avances científicos/técnicos profundos (materiales avanzados, fotónica, espacio, biotech, computación), ciclos largos, IP, capital de riesgo especializado; vs innovacion/startups"),
    ("dominio/pymes", "PyMEs / small and medium enterprises: segmento de empresas, acceso a financiamiento, productividad, digitalización, políticas públicas de apoyo, encadenamientos; vs emprendimiento/empresa-familiar"),
    ("dominio/impresion-3d", "Impresión 3D / manufactura aditiva: tecnologías (FDM/SLA/SLS/SLM), prototipado rápido, producción on-demand, aplicaciones médica/aeroespacial, vs manufactura tradicional; vs manufactura"),
    ("rol/chief-innovation-officer", "Chief Innovation Officer (CINO) — lidera la innovación corporativa, pipelines de innovación, corporate/venture/client, cultura innovadora; vs head-of-innovation/chief-technology-officer"),
    ("rol/system-administrator", "System Administrator (SysAdmin) — administra infraestructura TI (servidores, redes, SO, backups, seguridad básica), operación estable; vs network-engineer/dba/cloud-architect"),
    ("rol/risk-manager", "Risk Manager — gestiona riesgo operativo/empresarial (ERM), identificación/mitigación/monitoreo, continuidad, reporta a CRO; vs chief-risk-officer/compliance-manager"),
    ("rol/sales-development-representative", "Sales Development Representative (SDR) — prospección y calificación de leads (B2B), outbound, pasa a AE; vs account-executive/sales-lead"),
    ("rol/bookkeeper", "Bookkeeper / tenedor de libros — registro contable operativo (diario/mayor, conciliaciones, cuentas por pagar/cobrar), base para accountant/controller; vs accountant/contador"),
    # Round 36 — reabastecimiento (alcance: sustrato solo Norteamérica: deepenings banca-desarrollo MX/US/CA; dominio/rol generales).
    ("dominio/banca-de-inversion", "Banca de inversión (investment banking): advisory M&A, suscripción/underwriting (ECM/DCM), sales & trading, bulge bracket vs boutiques; vs capital-riesgo/mercados-capitales"),
    ("dominio/mercados-emergentes", "Mercados emergentes (emerging markets): clasificación (MSCI/FTSE), BRICS, riesgo país, inversión, volatilidad, frontera; vs economia/finanzas"),
    ("dominio/contratacion-publica", "Contratación pública / public procurement: licitaciones, bids, procurement law, e-procurement, WTO GPA, compras gubernamentales; vs compras (empresarial)"),
    ("dominio/it-service-management", "IT Service Management (ITSM): ITIL v4, service desk, incident/problem/change, SLA/OLA, SIAM, puente a DevOps/SRE; vs plataforma-sre/gobierno-de-ti"),
    ("dominio/modelos-de-negocio", "Modelos de negocio: Business Model Canvas, subscription, freemium, platform/marketplace, razor-and-blades, circular, innovación de modelo; vs estrategia/emprendimiento"),
    ("rol/developer-advocate", "Developer Advocate / DevRel — puente ingeniería-comunidad: developer relations, evangelism, docs, comunidad técnica; vs solutions-architect/sales-engineer"),
    ("rol/security-architect", "Security Architect — diseña arquitectura de seguridad, threat modeling a nivel sistema, zerotrust; vs security-engineer (implementa) y ciso (ejecutivo)"),
    ("rol/analytics-engineer", "Analytics Engineer — transforma datos en modelos de confianza (dbt/SQL), puente data-eng y data-science; vs data-engineer (pipelines) y data-analyst (análisis)"),
    ("rol/ux-researcher", "UX Researcher — investigación de usuarios, métodos cualitativos/cuantitativos, usabilidad, descubrimiento; vs product-designer/design-lead/head-of-design"),
    ("rol/economist", "Economist — macro/micro, política económica, forecasting, análisis de mercado; vs dominio/economia y data-scientist"),
    # Round 37 — reabastecimiento (alcance: sustrato solo Norteamérica: deepenings entidades-federativas MX, estados US, pueblos-indigenas CA; dominio/rol generales).
    ("dominio/centros-de-datos", "Centros de datos (data centers): infraestructura TI, siting, power/cooling, estándares Tier (Uptime Institute), colocation, hyperscalers, sostenibilidad energética; vs cloud-computing/infraestructura"),
    ("dominio/economia-social", "Economía social y solidaria: cooperativas, mutuales, empresas sociales, tercer sector económico, comercio justo, finanzas éticas; vs tercer-sector/pymes"),
    ("dominio/finanzas-descentralizadas", "Finanzas descentralizadas (DeFi): protocolos on-chain, DEX, lending/staking, stablecoins, yield, riesgo inteligente, regulación (SEC/ MiCA); vs fintech/blockchain"),
    ("dominio/investigacion-clinica", "Investigación clínica / ensayos clínicos: fases I-IV, FDA/EMA/COFEPRIS, CROs, protocolo, consentimiento, farmacovigilancia; vs salud/farmaceutica"),
    ("dominio/derecho-del-consumidor", "Derecho del consumidor: protección al consumidor como disciplina (engaño, prácticas comerciales, garantías, recursos), agencias, vs profeco-condusef (MX)"),
    ("rol/copywriter", "Copywriter / Redactor: redacción publicitaria y de contenido, UX writing, tono de marca, conversión; vs content-manager/chief-content-officer"),
    ("rol/underwriter", "Underwriter / Suscriptor: evaluación de riesgo y suscripción (seguros, crédito, préstamos), pricing de riesgo, límites; vs actuario/seguros"),
    ("rol/credit-analyst", "Credit Analyst / Analista de crédito: evaluación de riesgo de crédito, scoring, capacidad de pago, estructuración; vs financial-analyst/underwriter"),
    ("rol/mlops-engineer", "MLOps Engineer — despliega, monitoriza y opera modelos ML en producción (CI/CD para ML, feature store, model registry, observabilidad); vs ml-engineer/ai-engineer"),
    ("rol/deal-desk", "Deal Desk — pricing y aprobaciones de ventas, descuentos, estructuración de propuestas, quote-to-cash; vs sales-manager/head-of-sales-ops"),
    # Round 38 — reabastecimiento (alcance: sustrato solo Norteamérica: deepenings sector-servicios MX/CA + proteccion-consumidor US; dominio/rol generales).
    ("dominio/marketing-digital", "Marketing digital: SEO/SEM, performance, social paid, email automation, CRO, analytics, atribución; vs publicidad/demand-generation/marketing"),
    ("dominio/diversidad-equidad-inclusion", "Diversidad, Equidad e Inclusión (DEI): estrategia de inclusión, equidad salarial, pertenencia, métricas; vs chief-diversity-officer/tercer-sector"),
    ("dominio/bienestar-laboral", "Bienestar laboral / employee wellbeing: salud física/mental, beneficios de bienestar, equilibrio, engagement; vs salud-mental/compensacion-beneficios"),
    ("dominio/gestion-del-talento", "Gestión del talento / talent management: atracción, desarrollo, retención, sucesión, movilidad interna; vs recursos-humanos/desarrollo-organizacional/head-of-talent"),
    ("dominio/customer-success", "Customer Success (como disciplina): health score, renovaciones, expansión, adopción, modelo de ingresos recurrente; vs experiencia-cliente/customer-success-lead"),
    ("rol/head-of-customer-success", "Head of Customer Success — lidera la org de CS, estrategia de retención/expansión, operación de cuentas; vs customer-success-lead/customer-success-manager"),
    ("rol/payroll-manager", "Payroll Manager — gestión de nómina, impuestos laborales, cumplimiento de pago, sistemas de payroll; vs bookkeeper/controller/benefits-manager"),
    ("rol/data-governance-lead", "Data Governance Lead — calidad, linaje, política y cumplimiento de datos, privacidad by design; vs data-architect/chief-data-officer/gobierno-de-datos"),
    ("rol/investment-banker", "Investment Banker — M&A, underwriting (ECM/DCM), sales & trading en banca de inversión; vs banca-de-inversion/chief-investment-officer"),
    ("rol/quality-manager", "Quality Manager — gestión de la calidad operativa, ISO 9001, auditorías, mejora continua; vs chief-quality-officer/calidad"),
    # Round 39 — reabastecimiento (alcance: sustrato solo Norteamérica: deepenings pobreza-desigualdad MX/US/CA; dominio/rol generales).
    ("dominio/fidelizacion", "Fidelización de clientes / customer loyalty: programas de recompensas, retención, puntos/tiers, churn reduction, lifetime value; vs customer-success/marketing/retail"),
    ("dominio/logistica-inversa", "Logística inversa: gestión de devoluciones, reposición, reciclaje y reacondicionamiento, economía circular, costo y sostenibilidad; vs logistica/cadena-suministro"),
    ("dominio/comercio-mayorista", "Comercio mayorista / distribución: B2B, intermediarios, distribuidores, cadena de valor, márgenes de distribución; vs retail/comercio-electronico"),
    ("dominio/pesca-acuicultura", "Pesca y acuicultura: captura, acuicultura (piscicultura, maricultura), industria, sostenibilidad, cuotas/regulación, seguridad alimentaria; vs agronegocios/alimentos-bebidas"),
    ("dominio/salud-animal", "Salud animal / veterinary: medicina veterinaria, zoonosis, bioseguridad, industria (vacunas, fármacos veterinarios), bienestar animal; vs salud/farmaceutica"),
    ("rol/hr-generalist", "HR Generalist — operaciones de RRHH de extremo a extremo (contratación, nómina, beneficios, relaciones laborales, cumplimiento), generalista por unidad; vs people-lead/head-of-people/reclutador"),
    ("rol/penetration-tester", "Penetration Tester / Red Team — pruebas de intrusión, ethical hacking, simulación de adversario, reporte de vulnerabilidades; vs security-engineer/security-analyst"),
    ("rol/credit-manager", "Credit Manager — gestión de crédito comercial, políticas de crédito, cobranza, riesgo de crédito, anticipos; vs credit-analyst/underwriter"),
    ("rol/process-engineer", "Process Engineer — diseño/mejora de procesos industriales (manufactura, química, farmacéutica), rendimiento, calidad, seguridad de procesos; vs quality-manager/manufactura"),
    ("rol/event-manager", "Event Manager — producción y gestión de eventos (MICE: conferencias, ferias, corporativos), logística, presupuesto, ROI; vs eventos (dominio)"),
    # Round 40 — reabastecimiento (alcance: sustrato solo Norteamérica: deepening fronteras MX/US/CA; dominio/rol generales).
    ("dominio/liderazgo", "Liderazgo: teorías (situacional, transformacional, servicial), estilos, liderazgo de equipos, desarrollo de líderes, vs management; aplicado a todas las capas"),
    ("dominio/mercados-financieros", "Mercados financieros: exchanges, trading, microestructura, liquidez, precio de activos, renta fija/variable, derivados cotizados, regulación de mercados; vs banca/finanzas"),
    ("dominio/finanzas-personales", "Finanzas personales: presupuesto, ahorro, inversión personal, retiro, endeudamiento, planificación financiera, educación financiera; vs finanzas/gestion-de-activos"),
    ("dominio/comunicacion-corporativa", "Comunicación corporativa: relaciones con medios, comunicación interna, reputación, crisis, mensaje corporativo; vs relaciones-publicas/head-of-communications"),
    ("dominio/empresa-familiar", "Empresa familiar: gobierno familiar, protocolo familiar, sucesión, consejo de familia, profesionalización, continuidad; vs gobierno-corporativo/emprendimiento"),
    ("rol/principal-engineer", "Principal Engineer — ladder IC senior (sobre Staff), autoridad técnica, arquitectura a nivel org, mentoria de elites; vs staff-engineer/engineering-manager"),
    ("rol/talent-acquisition-manager", "Talent Acquisition Manager — lidera la función de adquisición de talento (equipo de reclutadores, estrategia de sourcing, employer brand, pipeline); vs reclutador/head-of-talent"),
    ("rol/compensation-manager", "Compensation Manager — diseña estructuras salariales, bandas, job grading, encuestas de mercado, equity; vs benefits-manager/payroll-manager/head-of-people"),
    ("rol/financial-planner", "Financial Planner / Planificador financiero — asesoría de finanzas personales (CFP), retiro, inversiones, seguros, planeación patrimonial; vs wealth-manager/finanzas-personales"),
    ("rol/general-manager", "General Manager (GM) — dueño de P&L de una unidad de negocio/país, P&L completo, operación+comercial; vs managing-director/director-of-operations/country-manager"),
    # Round 41 — reabastecimiento (alcance: sustrato solo Norteamérica: deepenings agua MX/US/CA; dominio/rol generales).
    ("dominio/musica", "Industria musical: grabación, publishing, discográficas, streaming, live/gira, derechos de autor, mercado global, sincronización"),
    ("dominio/cleantech", "Clean technology / tecnologías limpias: eficiencia energética, descarbonización, agua, economía circular, climatetech, inversión en cleantech"),
    ("dominio/nutricion", "Nutrición: nutrición clínica, salud pública, dietética, suplementos, regulación de etiquetado, alimentos funcionales, obesidad"),
    ("dominio/metaverso", "Metaverso: mundos virtuales persistentes, VR/AR, economía virtual, activos digitales, adopción empresarial, plataformas (Horizon/Roblox)"),
    ("dominio/periodismo", "Periodismo / journalism: medios, redacción, ética informativa, fact-checking, modelo de negocio (suscripción/digital), libertad de prensa"),
    ("rol/office-manager", "Office Manager — gestión de oficina/instalaciones, vendors, workplace, facilities operativos, experiencia del empleado en sitio; vs head-of-facilities/executive-assistant"),
    ("rol/esg-manager", "ESG Manager — programas ESG, reporting (GRI/SASB/TCFD/ISSB), materialidad, datos de sostenibilidad; vs chief-sustainability-officer/chief-risk-officer"),
    ("rol/equity-research-analyst", "Equity Research Analyst — análisis de acciones, ratings (buy/hold/sell), modelos financieros, informes de cobertura, sell-side; vs economist/portfolio-manager"),
    ("rol/security-analyst", "Security Analyst — SOC/monitorización de amenazas, triaje de alertas, análisis de vulnerabilidades; vs penetration-tester/security-engineer/security-architect"),
    ("rol/corporate-secretary", "Corporate Secretary / Company Secretary — actas de consejo/junta, gobierno corporativo, cumplimiento de estatutos, relación con accionistas; vs chief-administrative-officer/board-member"),
    # Round 42 — extensiones en capas generales (dominio/rol) + sustrato NA (deepening). Sin nuevos países.
    ("dominio/ciberseguridad", "Ciberseguridad: threat landscape, frameworks (NIST CSF, MITRE ATT&CK), operaciones (SOC, Blue/Red Team), gestión de riesgo, vs ciberdefensa estatal/seguridad-corporativa"),
    ("dominio/almacenamiento", "Almacenamiento / warehousing & fulfillment: DC ops, WMS, inventario, cross-docking, última milla, automatización de almacén; vs cadena-suministro/logistica-inversa"),
    ("dominio/experiencia-de-empleado", "Experiencia del empleado (EX): journey del empleado, espacio/facilities, herramientas/IT, bienestar, cultura, vs clima-organizacional/bienestar-laboral"),
    ("dominio/relaciones-institucionales", "Relaciones institucionales: gobierno, reguladores, asociaciones industriales, stakeholder management, vs relaciones-publicas/comunicacion-corporativa"),
    ("dominio/servicios-financieros", "Servicios financieros: bancos, aseguradoras, gestores de activos, fintechs, banca múltiple, regulación prudencial, vs banca/seguros/fintech"),
    ("rol/head-of-strategy", "Head of Strategy — lidera la estrategia corporativa (planificación, M&A screening, inteligencia competitiva), reporta a CSO/CEO; vs chief-strategy-officer"),
    ("rol/head-of-developer-experience", "Head of Developer Experience (DevEx) — plataforma interna, golden paths, satisfacción de desarrolladores, documentación/tooling; vs platform-engineer/sre"),
    ("rol/head-of-medical-affairs", "Head of Medical Affairs — puente ciencia-clínica-negocio (farmacéutica/biotech), MSLs, evidencia médica, KOLs; vs chief-medical-officer"),
    ("rol/head-of-threat-intelligence", "Head of Threat Intelligence — CTI, inteligencia de amenazas, IOC/ATT&CK mapping, apoyo a SOC/IR; vs security-analyst/penetration-tester"),
    ("rol/head-of-talent-mobility", "Head of Talent Mobility — movilidad interna, asignaciones, promoción interna, sucesión de talento, vs head-of-talent/gestion-del-talento"),
    # Round 43 — reabastecimiento (alcance: sustrato solo Norteamérica: deepenings industria aeroespacial MX, industria espacial US, industria automotriz CA; dominio/rol generales).
    ("dominio/open-banking", "Open banking / open finance: APIs bancarias, PSD2 / Open Banking Standard, Brasil Open Finance, México Ley Fintech/open finance, consent-driven data sharing; vs fintech/servicios-financieros/embedded-finance"),
    ("dominio/embedded-finance", "Embedded finance / Banking-as-a-Service (BaaS): pagos/seguros/crédito integrados en plataformas no-financieras, infraestructura fintech, Railsr/Treasury Prime; vs fintech/open-banking/pagos"),
    ("dominio/agentes-ia", "Agentes de IA (agentic AI): asistentes autónomos, orchestration, MCP/tools, enterprise agents, evals/guardrails, agentic workflows; vs ia-generativa/gobierno-de-ia/ai-engineer"),
    ("dominio/observabilidade", "Observabilidad (observability): OpenTelemetry, métricas/logs/traces, APM, SLO/error budget, vs plataforma-sre/devops-engineer/site-reliability-engineer"),
    ("dominio/pagamentos", "Pagos (payments): esquemas y rails (cards, ACH, RTP, PIX, FedNow, SEPA), clearing/settlement, PSPs, pagos instantáneos, regulación; vs fintech/open-banking/embedded-finance"),
    ("rol/head-of-trust-and-safety", "Head of Trust & Safety — moderación de contenido, seguridad de plataforma, policy enforcement, abuso/fraude, vs ciso/seguridad-corporativa/seguridad-y-salud-ocupacional"),
    ("rol/head-of-public-policy", "Head of Public Policy — relación con gobierno y políticas públicas, advocacy, regulación anticipada, vs head-of-public-affairs/relaciones-institucionales"),
    ("rol/head-of-design-ops", "Head of DesignOps — operaciones de diseño, escalar la org de diseño, tooling/procesos, ops de equipo; vs head-of-design/design-lead/creative-director"),
    ("rol/head-of-franchise", "Head of Franchise — desarrollo y operación de franquicias, FDD, relación con franquiciatarios, expansión; vs franquicias (dominio)/retail"),
    ("rol/head-of-ecommerce", "Head of Ecommerce — P&L de comercio electrónico, marketplace/D2C, conversión, fulfillment digital, vs comercio-electronico (dominio)/retail/head-of-marketing-ops"),
    # Round 44 — reabastecimiento (alcance: sustrato solo Norteamérica: deepenings seguros MX/US/CA; dominio/rol generales).
    ("dominio/gestion-de-crisis", "Gestión de crisis / crisis management: BCM (ISO 22301), crisis comms, reputación, resiliencia; vs seguridad-corporativa/comunicacion-corporativa"),
    ("dominio/aprendizaje-automatico", "Aprendizaje automático / Machine Learning: supervisado/no-supervisado, deep learning, MLOps, ciclo de modelos; vs ciencia-de-datos/ia-generativa"),
    ("dominio/energia-distribuida", "Energía distribuída (DER): microredes, VPP, prosumidores, grid edge, almacenamento distribuído, vs energias-renovables/energia"),
    ("dominio/mineria-de-datos", "Minaría de datos / data mining: KDD, pattern mining, asociación/clustering, BI, descubrimiento de conocimiento; vs ciencia-de-datos/analitica-negocio"),
    ("dominio/mercado-laboral", "Mercado laboral / labor market: oferta/demanda, desempleo, empleo, informalidad, migración laboral, políticas ativas; vs sustrato trabajo/relaciones-laborales"),
    ("rol/chief-executive-officer", "CEO — Chief Executive Officer: máxima autoridade ejecutiva, estrategia, liderazgo del conselho-equiv; vs founder-ceo"),
    ("rol/head-of-total-rewards", "Head of Total Rewards — compensación+benefícios+reconhecimento, filosofía de recompensa, bandas; vs compensation-manager/benefits-manager"),
    ("rol/head-of-merchandising", "Head of Merchandising — assortment, categoría, pricing, surtido, experiencia en tienda (retail/CPG); vs category-manager/retail"),
    ("rol/head-of-real-estate", "Head of Real Estate / Corporate Real Estate (CRE): portafolio inmobiliário, transações, arrendamientos, workplace; vs head-of-facilities"),
    ("rol/head-of-continuous-improvement", "Head of Continuous Improvement / OpEx: lean, Six Sigma, kaizen, eficiência de procesos; vs quality-manager/chief-quality-officer"),
    # Round 45 — reabastecimiento (alcance: sustrato solo Norteamérica: deepenings pueblos-indigenas MX/US + lenguas-oficiales CA; dominio/rol generales).
    ("dominio/forense-digital", "Forence digital / digital forensics: adquisición y preservación de evidencia, análisis de dispositivos, respuesta a incidentes, cadena de custodia, vs ciberseguridad/ciberdefensa"),
    ("dominio/auditoria-interna", "Auditoría interna: IPPF/IIA, aseguramiento y consultoría, evaluación de controles y riesgo, gobierno, vs contabilidad/auditoria (financiera) y rol/auditor-interno"),
    ("dominio/politica-publica", "Política pública: análisis, formulación, implementación y evaluación de políticas (evidence-based), ciclo de política, instrumentos; vs relaciones-institucionales/head-of-public-policy"),
    ("dominio/administracion-publica", "Administración pública: New Public Management, burocracia, gestión pública, sector público como disciplina; vs gobierno-publico/contratacion-publica"),
    ("dominio/ferroviario", "Industria ferroviaria: transporte de carga/pasajeros, FRA/FTA (US), TTC (CA), regulación, señalización, vs transporte/aviacion/maritimo"),
    ("rol/head-of-workforce-planning", "Head of Workforce Planning — planeación de fuerza laboral, headcount, oferta/demanda de talento, org design, analítica de personal; vs hr-business-partner/head-of-people/talent-acquisition-manager"),
    ("rol/head-of-customer-marketing", "Head of Customer Marketing — marketing a base instalada, lifecycle, lealtad, advocacía, comunidad de clientes; vs lifecycle-email/marketing-manager/head-of-marketing-ops"),
    ("rol/head-of-incident-response", "Head of Incident Response — lidera CSIRT/IR, respuesta a brechas, containment/eradication, post-mortem, vs security-analyst/penetration-tester/ciso"),
    ("rol/head-of-business-technology", "Head of Business Technology — sistemas empresariales (ERP, CRM), puente negocio-TI, habilitación digital de operación; vs cio/head-of-it/enterprise-architect"),
    ("rol/head-of-manufacturing", "Head of Manufacturing — red de plantas, excelencia de producción, calidad/costo/entrega a escala, vs plant-manager/vp-operations/head-of-operations"),
    # Round 46 — reabastecimiento (alcance: sustrato solo Norteamérica: deepenings empleo MX, politica-fiscal US, competitividad CA; dominio/rol generales).
    ("dominio/geopolitica-energetica", "Geopolítica energética: seguridad energética, mercados de petróleo/gas, OPEP+, transición, minerales críticos, soberanía; vs energia/geopolitica/medio-ambiente"),
    ("dominio/capital-natural", "Capital natural / naturaleza: servicios ecosistémicos, valoración de la naturaleza, TNFD, biodiversidad en negocios; vs medio-ambiente/economia-circular"),
    ("dominio/ciberseguridad-ot", "Ciberseguridad OT / industrial (ICS/SCADA): seguridad de sistemas de control industrial, NERC CIP, ISA/IEC 62443, vs ciberseguridad TI"),
    ("dominio/gobierno-de-riesgos", "Gobernanza de riesgos (enterprise risk governance): rol del consejo en riesgo, apetito de riesgo, tres líneas, vs gestion-riesgos/chief-risk-officer"),
    ("dominio/educacion-ejecutiva", "Educación ejecutiva / executive education: programas de desarrollo de líderes, MBAs ejecutivos, capacitación C-level, vs educacion/edtech"),
    ("rol/head-of-sustainability", "Head of Sustainability — estrategia de sostenibilidad, descarbonización, reporting ESG, vs chief-sustainability-officer/esg-manager"),
    ("rol/head-of-people-analytics", "Head of People Analytics — lidera la función de people analytics/HR analytics; vs hr-business-partner/data-analyst"),
    ("rol/head-of-revenue-operations", "Head of Revenue Operations (RevOps) — lidera RevOps a nivel org (ventas+marketing+CS), datos y proceso de ingresos; vs head-of-sales-ops/chief-revenue-officer"),
    ("rol/head-of-ai", "Head of AI — lidera la función de IA/ML aplicada, estrategia de modelos, adopción, puente con producto; vs chief-ai-officer/ml-engineer"),
    ("rol/head-of-infrastructure", "Head of Infrastructure — lidera infraestructura TI (cloud/on-prem), confiabilidad, capacidad, costo; vs head-of-it/cloud-architect/sre"),
    # Round 47 — reabastecimiento (alcance: sustrato solo Norteamérica: deepenings economia-creativa MX, energia-nuclear US, politica-fiscal CA; dominio/rol generales).
    ("dominio/forestal", "Silvicultura / forestry: manejo forestal, cadena de valor maderera, restauración, carbono azul/verde, regulación (SEMARNAT/USFS/CFS), economía forestal; vs medio-ambiente/agricultura"),
    ("dominio/banca-central", "Banca central / central banking: mandatos (precios/empleo), instrumentos de política monetaria, reservas, supervisor bancario, independencia, vs politica-monetaria (sustrato) y sistema-financiero"),
    ("dominio/economia-institucional", "Economía institucional: papel de las instituciones en el desempeño económico, costos de transacción, derechos de propiedad, new institutional economics; vs economia/estrategia"),
    ("dominio/geografia-economica", "Geografía económica: localización, aglomeración/clústeres, desarrollo regional, economía espacial, infraestructura y comercio; vs urbanismo/economia"),
    ("dominio/demografia", "Demografía (como disciplina de dominio): estructura por edad/sexo, fecundidad/mortalidad/migración, transición demográfica, proyecciones, vs sustrato/*/demografia-poblacion"),
    ("rol/head-of-legal", "Head of Legal — lidera el departamento legal operativo (litigios, contratos, cumplimiento legal), reporta al General Counsel/CLO; vs legal-counsel/general-counsel/chief-legal-officer"),
    ("rol/head-of-demand-generation", "Head of Demand Generation — lidera la generación de demanda (paid, content, events, ABM), pipeline de marketing, atribución, vs marketing-manager/demand-generation/cmo"),
    ("rol/head-of-clinical-operations", "Head of Clinical Operations — opera ensayos clínicos (site management, CRO oversight, accrual, compliance GCP), farma/biotech; vs head-of-medical-affairs/chief-medical-officer"),
    ("rol/head-of-quality-assurance", "Head of Quality Assurance (QA) — asegura la calidad de producto/software (test strategy, QA org, release gates), vs quality-manager (calidad operativa)/test-engineer"),
    ("rol/head-of-machine-learning", "Head of Machine Learning — lidera equipos de ML/MLOps, estrategia de modelos a escala, plataforma de ML, vs head-of-data-science/chief-ai-officer/ml-engineer"),
    # Round 48 — reabastecimiento (alcance: sustrato solo Norteamérica: deepenings pymes MX/US/CA; dominio/rol generales).
    ("dominio/telemedicina", "Telemedicina / telehealth: consulta remota, regulación (COFEPRIS/FDA/Health Canada), reembolso, privacidad, modelos de negocio, adopción post-COVID; vs salud/healthtech"),
    ("dominio/ciberseguridad-cadena-suministro", "Ciberseguridad de la cadena de suministro / supply-chain security: SBOM, SCA, terceros/4th-party risk, EO 14028, EU CRA, provenance; vs ciberseguridad/seguridad-corporativa"),
    ("dominio/arte", "Mercado del arte / art market: subastas (Sothebys/Christies), galerías, coleccionismo, arte digital/NFT, valoración, regulación (AML en arte), vs economia-creativa/musica"),
    ("dominio/seguros-de-personas", "Seguros de personas: vida, salud (GMM), gastos médicos, pensiones/annuities, ahorro prepago, vs seguros (sustrato) y gestion-de-activos"),
    ("dominio/riesgo-de-credito", "Riesgo de crédito (disciplina): scoring, PD/LGD/EAD, provisiones (IFRS 9/CECL), carteras, mitigación (garantías, seguro de crédito), vs finanzas/riesgo-financiero"),
    ("rol/head-of-treasury", "Head of Treasury — tesorería corporativa: liquidez, cash management, financiamiento, riesgo de tasa/divisa, relación con bancos; vs treasurer/cfo/fp-and-a-manager"),
    ("rol/head-of-fraud", "Head of Fraud — antifraude: detección, prevención, investigación, AML/KYC, chargebacks, vs compliance-manager/risk-manager/head-of-trust-and-safety"),
    ("rol/head-of-partner-engineering", "Head of Partner Engineering — integraciones y APIs para partners/ISVs, developer platforms, co-engineering, vs developer-advocate/solutions-architect"),
    ("rol/head-of-platform", "Head of Platform — lidera la plataforma de producto/ingeniería (APIs, SDKs, servicios compartidos), vs platform-engineer/head-of-developer-experience"),
    ("rol/head-of-customer-ops", "Head of Customer Operations — operaciones de cliente (CX ops, billing/support ops, order-to-cash), eficiencia de servicio; vs head-of-customer-success/customer-success-manager"),
    # Round 49 — reabastecimiento (alcance: sustrato solo Norteamérica: deepenings impuestos MX, turismo US, minería CA; dominio/rol generales).
    ("dominio/politica-comercial", "Política comercial / trade policy: aranceles, barreras no arancelarias, OMC, acuerdos comerciales (USMCA), defensa comercial (antidumping/subsidios), políticas de exportación; vs comercio-internacional/sustrato/*/comercio-exterior"),
    ("dominio/criptografia", "Criptografía / cryptography: cifrado simétrico/asimétrico, clave pública, hashing, PKI, TLS, criptografía post-cuántica, firmas digitales; vs ciberseguridad/seguridad-corporativa"),
    ("dominio/comercio-mayorista-b2b", "Comercio mayorista B2B / wholesale distribution (profundización): gestión de canal, distribuidores, márgenes de distribución, cadena de suministro mayorista; vs comercio-mayorista (Round 39)"),
    ("dominio/reaseguro", "Reaseguro / reinsurance: cesión, tratado/facultativo, retrocesión, Lloyd's, solvencia de reaseguradores; vs seguros/seguros-de-personas"),
    ("dominio/real-estate-capital-markets", "Real estate capital markets / mercado de capitales inmobiliario: CMBS, REIT listings, deuda inmobiliaria, inversión institucional en real estate; vs inmobiliario/vivienda"),
    ("rol/head-of-executive-development", "Head of Executive Development — desarrollo de liderazgo C-suite/sucesión, coaching ejecutivo, succession planning; vs educacion-ejecutiva/head-of-people"),
    ("rol/head-of-esg-risks", "Head of ESG Risks — riesgos ESG materiales, climate risk, disclosure de riesgos, integración en ERM; vs esg-manager/chief-sustainability-officer/gobierno-de-riesgos"),
    ("rol/head-of-investor-relations", "Head of Investor Relations — lidera IR (earnings, disclosure, relación con inversionistas institucionales), reporting al CFO/CEO; vs investor-relations (Round 14)"),
    ("rol/head-of-clinical-development", "Head of Clinical Development — lidera desarrollo clínico (fases I-IV, estrategia de trial, regulatory submissions), farma/biotech; vs head-of-clinical-operations/chief-medical-officer"),
    ("rol/head-of-customer-insights", "Head of Customer Insights — voz del cliente (VoC), research de mercado interno, analítica de comportamiento, puente investigación-producto/marketing; vs ux-researcher/head-of-customer-experience"),
    ("rol/head-of-product-marketing", "Head of Product Marketing — lidera PMM org (GTM, posicionamiento, mensaje, enablement); vs product-marketing-manager/chief-marketing-officer"),
    ("rol/head-of-security-operations", "Head of Security Operations (SecOps) — lidera SOC/SecOps, monitorización, respuesta operativa; vs ciso/head-of-incident-response/security-analyst"),
    ("rol/head-of-business-development", "Head of Business Development — lidera BD (alianzas, M&A corporativo, canales, expansión); vs business-development (Round 8)/head-of-corporate-development"),
    # Round 49 (extra) — 3 nodos rol adicionais ingeridos en la misma iteración para completar la capa rol.
    ("rol/head-of-product-marketing", "Head of Product Marketing — lidera PMM org (GTM, posicionamiento, mensaje, enablement); vs product-marketing-manager/chief-marketing-officer [ingrido en Round 49 como extra]"),
    ("rol/head-of-security-operations", "Head of Security Operations (SecOps) — lidera SOC/SecOps, monitorización, respuesta operativa; vs ciso/head-of-incident-response/security-analyst [ingrido en Round 49 como extra]"),
    # Round 50 (iter 188) — 3 deepenings NA + 10 nodos nuevos dominio/rol
    ("sustrato/mexico/educacion-superior", "Educación superior México (UNAM/IPN/ANUIES, autonomía, PRODEP, posgrado); vs educacion"),
    ("sustrato/estados-unidos/economia", "Economía EE.UU. (GDP, sectores, Fed/BEA/Census, ciclo, empleo, comercio); vs macroeconomia"),
    ("sustrato/mexico/cultura", "Cultura México (industrias culturales, derechos culturales, políticas culturales, patrimonio); vs economia-creativa"),
    ("dominio/ciencia-de-datos-aplicada", "Data science aplicada a negocio (CRISP-DM, modelado predictivo, MLOps); vs ciencia-de-datos/analitica-negocio"),
    ("dominio/finanzas-climaticas", "Finanzas climáticas (green bonds, transition finance, TCFD/ISSB); vs finanzas-sostenibles"),
    ("dominio/urbanismo-tactico", "Urbanismo táctico / tactical urbanism (intervenciones leves, placemaking); vs urbanismo"),
    ("dominio/derecho-de-familia", "Derecho de familia (matrimonio, divorcio, custodia, sucesiones); vs derecho-civil"),
    ("dominio/biotecnologia-agricola", "Biotecnología agrícola (semillas biotech, edición genómica, regulación); vs biotecnologia/agrotech"),

    ("rol/head-of-experience-design", "Head of Experience Design (XD, unificar UX/CX/service design, research); vs design-lead/chief-design-officer"),
    ("rol/head-of-information-security", "Head of Information Security (CISO adjunto, InfoSec program, GRC, data protection); vs ciso/security-analyst"),
    ("rol/head-of-workforce-experience", "Head of Workforce Experience (EX de empleado en todas las journeys, bienestar, engagement); vs head-of-employee-experience"),
    ("rol/head-of-brand-experience", "Head of Brand Experience (unificar marca y experiencia vivida, brand + CX + marketing); vs chief-brand-officer/head-of-customer-experience"),
    ("rol/head-of-supply-chain-planning", "Head of Supply Chain Planning (demand/supply planning, S&OP, IBP, inventario); vs supply-chain-manager"),
]

# Round 51 (iter 189) — 3 deepenings NA + 10 nodos nuevos dominio/rol
TAXONOMY["sustrato/mexico"].append(("economia-informal", "Economia informal Mexico: informalidad laboral, sector informal, economia sumergida, recaudacion, transicion a formalidad; vs empleo/trabajo"))
TAXONOMY["sustrato/estados-unidos"].append(("energia-renovables", "Energia renovable EE.UU.: solar, eolica, almacenamiento, IRA, grid, vs energia"))
TAXONOMY["sustrato/canada"].append(("educacion-superior", "Educacion superior Canada: universities/colleges (PSE), provincias, acreditacion, investigacion, transferencia; vs educacion/mexico/estados-unidos"))
NEW_NODES += [
    ("dominio/derecho-laboral-colectivo", "Derecho laboral colectivo: sindicatos, contratacion colectiva, huelgas, negociacion colectiva; vs relaciones-laborales/derecho-laboral"),
    ("dominio/gestion-de-talento-tech", "Gestion de talento de tecnologia (tech talent): atraccion/desarrollo de ingenieros, skills, retencion; vs gestion-del-talento"),
    ("dominio/movilidad", "Movilidad / mobility: transporte de personas, MaaS, micro-movilidad, EVs compartidos; vs movilidad-urbana/electromovilidad"),
    ("dominio/cuentas-por-cobrar", "Cuentas por cobrar (accounts receivable): ciclo O2C, factoring, credito a clientes, cobranza; vs riesgo-de-credito"),
    ("dominio/privacidad-diferencial", "Privacidad diferencial / PETs: differential privacy, federated learning, homomorfico, anonymization; vs proteccion-de-datos/criptografia"),
    ("rol/head-of-finance-ops", "Head of Finance Operations (FinOps) — cierre, cuentas por pagar/cobrar, conciliacion, automatizacion financiera; vs controller/fp-and-a-manager"),
    ("rol/head-of-brand", "Head of Brand — estrategia de marca, identidad, brand equity, narrativa; vs brand-manager/chief-brand-officer"),
    ("rol/vp-people", "VP of People — lidera RRHH a nivel ejecutivo (CHRO adjunto), talento, cultura, comp; vs chief-people-officer/head-of-people"),
    ("rol/head-of-data-platform", "Head of Data Platform — lidera la plataforma de datos (lakehouse, pipelines, gobierno tecnico); vs data-engineer/data-architect"),
    ("rol/head-of-customer-lifecycle", "Head of Customer Lifecycle — onboarding, adopcion, retencion, expansion, churn; vs customer-success/customer-marketing"),
]

# Round 52 (iter 190) — 3 deepenings NA + 10 nodos nuevos dominio/rol
TAXONOMY["sustrato/mexico"].append(("transparencia", "Transparencia y acceso a la informacion Mexico: INAI, Ley Federal de Transparencia (LFTAIPG), datos abiertos, fiscalizacion, rendicion de cuentas, vs gobierno-digital/auditoria-gubernamental"))
TAXONOMY["sustrato/estados-unidos"].append(("derechos-civiles", "Derechos civiles EE.UU.: Civil Rights Act, DOJ Civil Rights Division, EEOC, voting rights, discriminacion, vs seguridad-publica/poder-judicial"))
TAXONOMY["sustrato/canada"].append(("ciudadania", "Ciudadania Canada: Citizenship Act, IRCC, juramento, derechos/derechos de ciudadania, naturalizacion, vs inmigracion"))
NEW_NODES += [
    ("dominio/ciberseguridad-ciudadana", "Ciberseguridad ciudadana / consumer privacy & safety: phishing, proteccion al consumidor digital, identidad, estafas online, alfabetizacion digital, vs proteccion-de-datos/seguridad-consumidor"),
    ("dominio/derecho-procesal", "Derecho procesal: proceso civil/mercantil/penal, litigio, recursos, carga de la prueba, jurisdiccion, vs derecho-civil/derecho-penal/derecho-administrativo"),
    ("dominio/satelites", "Satelites / satellite industry: manufactura de satelites, lanzamiento, downstream (earth observation, comunicaciones), regulacion orbital (FCC/ITU), vs espacio/industria-espacial"),
    ("dominio/ciencia-espacial", "Ciencia espacial: astrofisica, planetologia, observatorios, misiones cientificas (NASA science), vs espacio/industria-espacial"),
    ("dominio/gestion-portuaria", "Gestion portuaria / port management: operacion de puertos, terminales, carga/contenerizacion, regulacion portuaria (Puerto Authority), vs maritimo/transporte"),
    ("rol/director-of-product", "Director of Product — lidera grupo de PMs / area de producto, estrategia de producto por dominio, roadmap, vs product-manager/head-of-product/chief-product-officer"),
    ("rol/head-of-customer-communications", "Head of Customer Communications — comunicacion con base de clientes (lifecycle, notificaciones, crisis de producto), vs head-of-communications/customer-marketing"),
    ("rol/head-of-analytics", "Head of Analytics — lidera la funcion de analitica (BI + datos + experimentacion), embed en negocio, vs chief-analytics-officer/data-lead"),
    ("rol/head-of-revenue", "Head of Revenue — dueno del top-line operativo (ventas+CS+expansion), quota, retencion, vs chief-revenue-officer/vp-sales"),
    ("rol/head-of-corporate-affairs", "Head of Corporate Affairs — asuntos corporativos, relacion con gobierno/reguladores/medios, sustentabilidad corporativa, vs head-of-public-affairs/relaciones-institucionales"),
]


SKIP = {"index.md", "log.md", "README.md", "raw"}

# Round 53 (iter 191) — 3 deepenings NA + 10 nodos nuevos dominio/rol
TAXONOMY["sustrato/mexico"].append(("seguridad-nacional", "Seguridad nacional Mexico: CNS, Consejo de Seguridad Nacional, SEDENA/SSEM, Guardia Nacional, intelligence, amenazas hibridas, ciberdefensa; vs seguridad-publica/defensa"))
TAXONOMY["sustrato/estados-unidos"].append(("industria-manufacturera", "Industria manufacturera EE.UU.: sector manufacturero, reshoring/nearshoring, CHIPS/IRA, semiconductors, automotriz, aeroespacial, PMI, Census; vs sector-manufacturero (canada) y dominio/manufactura"))
TAXONOMY["sustrato/canada"].append(("industria-aeroespacial", "Industria aeroespacial Canada: Quebec (Montreal), Bombardier, Bell Textron Canada, MDA, Pratt & Whitney Canada, MRO, Transport Canada, EASA/FAA, exportacion; vs dominio/aeroespacial y sustrato/estados-unidos industria-espacial"))
NEW_NODES += [
    ("dominio/banca-privada", "Banca privada / private banking: gestion de patrimonio para HNW/UHNW, family office, wealth structuring, vs gestion-de-activos/servicios-financieros"),
    ("dominio/arbitraje-internacional", "Arbitraje internacional de inversiones y comercial: CIADI/ICSID, CNUDMI/UNCITRAL, TLC/ISDS, laudo extranjero, vs arbitraje/comercio-internacional"),
    ("dominio/telecomunicaciones-corporativas", "Telecomunicaciones corporativas / enterprise telecom: UCaaS, VoIP, redes MPLS/SD-WAN, carrier, vs telecomunicaciones"),
    ("dominio/ciberseguridad-industrial", "Ciberseguridad industrial / ICS ot: ISA/IEC 62443, NERC CIP, SCADA, OT security, vs ciberseguridad-ot/ciberdefensa"),
    ("dominio/monetizacion", "Monetizacion / revenue monetization: modelos de ingresos, pricing, ads, subscription, freemium, marketplace take-rate; vs pricing/modelos-de-negocio"),
    ("dominio/neumaticos", "Industria de neumaticos / tire industry: fabricacion, distribucion, retail, reciclaje, marcas globales; vs automotriz/manufactura"),
    ("dominio/seguros-de-credito", "Seguros de credito / credit insurance: trade credit, export credit (ECAs), factoring con seguro, vs reaseguro/riesgo-de-credito"),
    ("dominio/gestoria", "Gestoria / corporate secretarial & compliance local: registros mercantiles, permisos, poder notarial, pymes; vs administracion-publica/contabilidad"),
    ("rol/head-of-underwriting", "Head of Underwriting — lidera suscripcion de riesgo (seguros/credito), pricing de riesgo, portafolio, vs underwriter/chief-risk-officer"),
    ("rol/head-of-trade-compliance", "Head of Trade Compliance — export controls (EAR/ITAR), sanciones (OFAC), aduanas, vs regulatory-affairs/compliance-officer"),
]


# Round 54 (iter 192) — 3 deepenings NA + 10 nodos nuevos dominio/rol
TAXONOMY["sustrato/mexico"].append(("infraestructura-digital", "Infraestructura digital Mexico: fibra optica, data centers, conectividad, Agenda Digital, Estrategia Nacional de Inteligencia Artificial, vs gobierno-digital/telecomunicaciones"))
TAXONOMY["sustrato/mexico"].append(("hidrocarburos", "Hidrocarburos Mexico: PEMEX, CNH, regulacion de hidrocarburos, petroleros, gas, reforma energetica, vs energia/transporte"))
TAXONOMY["sustrato/canada"].append(("politica-inmigratoria", "Politica de inmigracion Canada: niveles de inmigracion, planes de migracion, Express Entry, PNP, refugiados, integracion, vs inmigracion/ciudadania/poblacion"))
NEW_NODES += [
    ("dominio/finanzas-ventas", "Finanzas de ventas / sales finance: credito al consumo, financing de equipos, leasing, BNPL, subprime auto, vs finanzas/bancarios"),
    ("dominio/tecnologia-financiera", "Tecnologia financiera aplicada a dominios (fintech vertical: insurtech/regtech/payments ya cubiertos; aqui: neobancos, wealthtech, proptech-finance, embedded lending); vs fintech"),
    ("dominio/gestion-de-la-cadena-de-suministro", "Gestion de la cadena de suministro (SCM operativo): planificacion, sourcing, make, entrega, retorno, S&OP, resiliencia, vs cadena-suministro/cadena-de-valor"),
    ("dominio/propiedad-intelectual-empresarial", "IP empresarial / IP management: portafolio de patentes, licencias, due diligence de IP, trade secrets, litigios de patentes, vs propiedad-intelectual/derecho-de-la-competencia"),
    ("dominio/salud-ocupacional", "Salud ocupacional / occupational health: vigilancia de la salud, exposicion laboral, ergonomia, enfermedades de trabajo, vs seguridad-y-salud-ocupacional/bienestar-laboral"),
    ("rol/head-of-sales-enablement-mkt", "Head of Sales Enablement (deepening rol): capacitacion, contenido y herramientas de ventas, playbooks, onboarding de reps; vs sales-manager/head-of-sales-ops"),
    ("rol/head-of-customer-education", "Head of Customer Education — educacion del cliente (onboarding, academy, docs, certificaciones), adopcion y retencion; vs customer-success/head-of-customer-experience"),
    ("rol/head-of-talent-brand", "Head of Talent Brand (deepening): marca empleadora, recruitment marketing, propuesta de valor; vs head-of-employer-branding/reclutador"),
    ("rol/head-of-legal-operations", "Head of Legal Operations (Legal Ops): eBilling, proveedores externos, tecnologia legal, gestao de contratos a escala; vs legal-ops/head-of-legal/general-counsel"),
    ("rol/head-of-strategy-corporate-development", "Head of Strategy & Corporate Development (deepening): M&A screening, capital allocation, due diligence, integracion; vs head-of-corporate-development/chief-strategy-officer"),
]

# Round 55 (iter 192) — 3 deepenings NA + 10 nodos nuevos dominio/rol
TAXONOMY["sustrato/mexico"].append(("energia-renovables", "Energia renovable Mexico: solar, eolica, almacenamiento, hidro, CELs, SENER/CRE, subastas, vs energia/transicion"))
TAXONOMY["sustrato/estados-unidos"].append(("mineria", "Mineria EE.UU.: USGS, minerales criticos, hardrock leasing, coal, IRA/DOE, vs industria-manufacturera/recursos"))
TAXONOMY["sustrato/canada"].append(("defensa-seguridad", "Defensa y seguridad Canada: DND/CAF, NATO, NORAD, procurement de defensa, vs defensa-seguridad dominio"))
NEW_NODES_ROUND_55 = [
    ("dominio/banca-corporativa", "Banca corporativa / corporate banking: prestamos sindicados, cash management, trade finance, relaciones con grandes empresas; vs banca-privada/sistema-financiero"),
    ("dominio/energia-electrica", "Energia electrica / power generation: generacion, transmision, distribucion, ISO/RTO, tarifas, grid; vs energia/energia-renovables"),
    ("dominio/sanidad", "Sanidad / healthcare ops: sistemas de salud, hospitales, aseguradores, farmaceuticos, regulation FDA/COFEPRIS/Health Canada; vs salud/healthtech"),
    ("dominio/economia-maritima", "Economia maritima / blue economy: puertos, shipping, acuicultura, energia offshore, proteccion costera; vs maritimo/gestion-portuaria"),
    ("dominio/regulacion-financiera", "Regulacion financiera: Basilea, SEC/CMA, CNBV, conducta, resolucion bancaria, macroprudential; vs sistema-financiero/servicios-financieros"),
    ("rol/head-of-procurement", "Head of Procurement: estrategia de compras, sourcing, proveedores, P2P, ahorro; vs procurement-manager/supply-chain-manager"),
    ("rol/director-of-it", "Director of IT: operaciones de TI, infraestructura, help desk, seguridad IT, vs head-of-business-technology/cto"),
    ("rol/head-of-internal-audit", "Head of Internal Audit: aseguramiento independiente, COSO/IIA, riesgo, cumplimiento, reporte a auditoria; vs auditoria-interna/control-interno"),
    ("rol/chief-operating-officer", "Chief Operating Officer (COO): operaciones end-to-end, ejecucion, escalabilidad, liderazgo de unidades; vs vp-operations/coo"),
    ("rol/head-of-field-operations", "Head of Field Operations: operaciones de campo/territorio, fuerza de ventas field, servicios in-situ; vs regional-director/operations"),
]

def node_exists(path: str) -> bool:
    """True si el nodo ya existe en el repo, sea como directorio
    (dominio/foo/), como archivo plano (dominio/foo.md) o como página dentro
    de subcarpeta (dominio/foo/foo.md). Evita falsos positivos en NEW_NODES
    cuando el nodo fue ingestado con layout plano o con slug diverso."""
    full = os.path.join(ROOT, path)
    if os.path.isdir(full):
        return True
    if os.path.isfile(full + ".md"):
        return True
    base = os.path.basename(path)
    if os.path.isfile(os.path.join(full, base + ".md")):
        return True
    return False


# La ronda activa de extensión de taxonomía es la Round 56.
NEW_NODES_ROUND_56 = [
    ("dominio/automatizacion-procesos", "Automatizacion de procesos / BPA & RPA: BPMN, workflows, hyperautomation, IA agentes, vs automatizacion/operaciones"),
    ("dominio/ciberseguridad-de-la-informacion", "Ciberseguridad de la informacion / InfoSec: CIA, gestion de vulnerabilidades, GRC, vs ciberseguridad/seguridad-corporativa"),
    ("dominio/derecho-de-las-telecomunicaciones", "Derecho de las telecomunicaciones: espectro, concesiones, neutralidad de red, reguladores (IFT/FCC/CRTC); vs telecomunicaciones"),
    ("dominio/gestion-de-proyectos-it", "Gestion de proyectos de TI / IT project management: metodologias, PMO, presupuesto TI, entrega de valor; vs project-management/it-service-management"),
    ("dominio/logistica-de-medios", "Logistica de medios / media supply chain: ad operations, trafficking, distribucion de contenido, vs medios-comunicacion/publicidad"),
    ("rol/head-of-growth-marketing", "Head of Growth Marketing: adquisicion, retencion, experimentacion, full-funnel, vs head-of-growth/marketing-manager"),
    ("rol/head-of-platform-engineering", "Head of Platform Engineering: plataforma interna, golden paths, developer experience, vs platform-engineer/devops-engineer"),
    ("rol/head-of-risk-and-compliance", "Head of Risk & Compliance: riesgo operativo + cumplimiento regulatorio, 2nd line, vs chief-risk-officer/chief-compliance-officer"),
    ("rol/head-of-customer-success-ops", "Head of Customer Success Operations: CS ops, escalabilidad de CS, tech-touch, health scoring; vs customer-success/customer-success-manager"),
    ("rol/head-of-digital-transformation", "Head of Digital Transformation: liderazgo de transformacion digital, CRM/ERP, cultura digital; vs chief-digital-officer/chief-transformation-officer"),
]
# Round 57 (iter 195) — 3 deepenings NA + 10 nodos sugeridos (7 nuevos reales + 3 ya existían en Rounds 45/47)
TAXONOMY["sustrato/mexico"].append(("agricultura", "Agricultura Mexico: SADER, campesinos, seguridad alimentaria, produccion, vs canada/estados-unidos agricultura"))
TAXONOMY["sustrato/estados-unidos"].append(("agricultura", "Agricultura EE.UU.: USDA, farm policy, subsidies, crop insurance, vs mexico/canada agricultura"))
TAXONOMY["sustrato/canada"].append(("recursos-naturales", "Recursos naturales Canada: NRCan, forestry, minerals, energy, fisheries, vs estados-unidos mineria"))
NEW_NODES_ROUND_57 = [
    ("dominio/bioetica", "Bioetica: etica biomedica, consentimiento, IRB, dilemas fin de vida, vs sanidad/salud-ocupacional"),
    ("dominio/educacion-corporativa", "Educacion corporativa / L&D: aprendizaje y desarrollo, capacitacion, academies, vs recursos-humanos/head-of-people"),
    ("dominio/gestion-de-la-demanda", "Gestion de la demanda / demand planning: forecasting, S&OP demanda, vs gestion-de-la-cadena-de-suministro"),
    ("dominio/alianzas-estrategicas", "Alianzas estrategicas: JV, partnerships, alianzas, co-development, vs fusiones-adquisiciones"),
    ("dominio/telemedicina", "Telemedicina / telehealth: consulta remota, telehealth, telecare, regulacion, vs sanidad"),
    ("rol/head-of-learning-development", "Head of Learning & Development: L&D, capacitacion, upskilling, academia corporativa; vs head-of-people"),
    ("rol/head-of-partnerships", "Head of Partnerships / Alliances: alianzas estrategicas, JV, canales, ecosistema; vs business-development"),
]
NEW_NODES = NEW_NODES_ROUND_57

# Round 58 (iter 196) — 3 deepenings NA + 10 nodos nuevos dominio/rol
TAXONOMY["sustrato/mexico"].append(("politica-fiscal", "Politica fiscal Mexico: SHCP, gasto publico, deficit, deuda, estimulo/austeridad, vs finanzas-publicas/impuestos"))
TAXONOMY["sustrato/estados-unidos"].append(("criminalistica", "Criminalistica EE.UU.: DOJ/FBI forensics, crime labs, NIST forensic science, evidencia, medicina legal; vs derechos-civiles/seguridad-publica"))
TAXONOMY["sustrato/canada"].append(("turismo", "Turismo Canada: Destination Canada, parques, contribucion al PIB/empleo, hotelería, turismo de naturaleza; vs sector-servicios"))
NEW_NODES_ROUND_58 = [
    ("dominio/tributos", "Tributos / impuestos como disciplina: teoria impositiva, impuestos directos/indirectos, federal/estatal/municipal, procedimiento, defensa; vs derecho-tributario/finanzas-publicas"),
    ("dominio/defensa-civil", "Defensa civil / emergency management: proteccion civil, desastres naturales, respuesta, continuidad, vs gestion-de-crisis/seguridad-publica"),
    ("dominio/gestion-del-riesgo-de-desastres", "Gestion del riesgo de desastres (DRR): marco Sendai, reduccion, resiliencia, vs defensa-civil/gestion-de-crisis"),
    ("dominio/derecho-de-las-telecomunicaciones", "Derecho de las telecomunicaciones (profundizacion): espectro, concesiones, neutralidad, reguladores, privacidad, vs telecomunicaciones-corporativas"),
    ("dominio/relaciones-diplomaticas", "Relaciones diplomaticas: diplomatico, embajadas, consulados, inmunidad, tratados, multilateralismo, vs relaciones-exteriores"),
    ("dominio/biomedicina", "Biomedicina: investigacion traslacional, dispositivos, terapias, regulation, vs bioetica/salud"),
    ("dominio/economia-del-trabajo", "Economia del trabajo / labor economics: salarios, empleo, capital humano, desempleo, mercado laboral; vs mercado-laboral/empleo"),
    ("dominio/competitividad-empresarial", "Competitividad empresarial: ventaja competitiva, estrategia, productividad, benchmarking, vs liderazgo/estrategia"),
    ("rol/head-of-tax", "Head of Tax / Tax Director: estrategia fiscal, transfer pricing, cumplimiento, planificacion, vs controller/cfo"),
    ("rol/head-of-government-relations", "Head of Government Relations: relacion con gobierno, lobbying legal, regulatory affairs, vs head-of-public-affairs/head-of-public-policy"),
    ("rol/head-of-credit", "Head of Credit: credito comercial, cobranza, riesgo de credito, politicas, vs credit-manager/head-of-treasury"),
    ("rol/head-of-commercial", "Head of Commercial: estrategia comercial, ventas+marketing+BD, GTM, ingresos, vs chief-commercial-officer/vp-sales"),
]
NEW_NODES = NEW_NODES_ROUND_58

# Round 59 (iter 197) — 3 deepenings NA + 10 nodos nuevos dominio/rol
TAXONOMY["sustrato/mexico"].append(("participacion-ciudadana", "Participacion ciudadana Mexico: INE, consultas, presupuesto participativo, democracia directa, asambleas; vs transparencia/poder-judicial"))
TAXONOMY["sustrato/estados-unidos"].append(("defensa-civil", "Defensa civil EE.UU.: FEMA, emergency management, preparacion/response/recovery, NRF, vs seguridad-publica/gestion-de-crisis"))
TAXONOMY["sustrato/canada"].append(("economia-creativa", "Economia creativa Canada: industrias culturales, politica CANCON, telefilm, music/film/games, vs cultura/economia-creativa-mexico"))
NEW_NODES_ROUND_59 = [
    ("dominio/domotica", "Domotica / smart home: IoT residencial, asistentes de voz, seguridad hogar, automatizacion, vs iot/ciudades-inteligentes"),
    ("dominio/jurimetria", "Jurimetria / legal analytics: datos en el derecho, prediccion de litigios, estadistica judicial, vs leyes/legaltech/derecho-procesal"),
    ("dominio/neurociencia", "Neurociencia: cognicion, neuroeconomia, aplicaciones clinicas/consumo, vs comportamiento-del-consumidor/inteligencia-emocional"),
    ("dominio/economia-de-la-salud", "Economia de la salud / health economics: outcomes, costo-efectividad, pricing farmaceutico, sistemas de pago; vs salud-publica/sanidad"),
    ("dominio/ingenieria-financiera", "Ingenieria financiera: estructuracion, derivados exoticos, securitizacion, ABS/MBS, vs derivados/finanzas-corporativas"),
    ("rol/head-of-engineering", "Head of Engineering: lidera org de ingenieria (varios equipos), delivery tecnico, vs vp-engineering/engineering-manager"),
    ("rol/head-of-digital-product", "Head of Digital Product: producto nativo digital, plataformas digitales, vs producto/product-manager/director-of-product"),
    ("rol/head-of-solutions-consulting", "Head of Solutions Consulting / Pre-Sales: demo tecnica, POCs, cierre tecnico, vs sales-engineer/solutions-architect"),
    ("rol/head-of-people-operations", "Head of People Operations: HR ops, payroll, sistemas RRHH, compliances laboral, vs hr-generalist/head-of-people"),
    ("rol/head-of-partner-marketing", "Head of Partner Marketing: co-marketing, canal/ecosistema, MDF, vs channel-manager/marketing-manager"),
]
NEW_NODES = NEW_NODES_ROUND_59

# Round 60 (iter 198) — 3 deepenings NA + 10 nodos nuevos dominio/rol
TAXONOMY["sustrato/mexico"].append(("defensa", "Defensa Mexico: SEDENA, SEMAR, Guardia Nacional, industria de defensa, procurement, vs seguridad-nacional/seguridad-publica"))
TAXONOMY["sustrato/estados-unidos"].append(("relaciones-laborales", "Relaciones laborales EE.UU.: NLRB, sindicatos, negociacion colectiva, huelgas, Taft-Hartley, vs labor/seguridad-social"))
TAXONOMY["sustrato/canada"].append(("defensa-civil", "Defensa civil Canada: Public Safety Canada, emergency management, Response Framework, vs gestion-del-riesgo-de-desastres/seguridad-publica"))
NEW_NODES_ROUND_60 = [
    ("dominio/gestion-documental", "Gestion documental / document management: ciclo de vida del documento, ECM, records management, ISO 15489, e-discovery, vs juridico/legaltech"),
    ("dominio/teatro", "Industria del teatro / performing arts: produccion teatral, ticket, touring, financiamiento, vs musica/deporte/entretenimiento"),
    ("dominio/economia-creativa", "Economia creativa (disciplina de dominio): industrias culturales y creativas, valor economico, politicas, vs cultura (sustrato) y entretenimiento/musica/medios-comunicacion"),
    ("dominio/sector-agroalimentario", "Sector agroalimentario: cadena de valor agroalimentaria, procesamiento de alimentos, distribucion, seguridad alimentaria, vs agricultura/alimentos-bebidas/pesca-acuicultura"),
    ("dominio/ciberseguridad-educativa", "Ciberseguridad educativa / edtech security: proteccion de datos estudiantiles (FERPA/COPPA), LMS security, identidad educativa, vs educacion/edtech/proteccion-de-datos"),
    ("rol/head-of-ux", "Head of UX — lidera la organizacion de UX/research/design de producto, estrategia de experiencia, vs design-lead/head-of-design/ux-researcher"),
    ("rol/head-of-sales-finance", "Head of Sales Finance — credito/comercial y financiacion de ventas, estructuracion de deals, vs finanzas-ventas/head-of-credit"),
    ("rol/head-of-engineering-excellence", "Head of Engineering Excellence — calidad tecnica, plataformas de dev, estandares, DORA/DevEx, vs head-of-platform-engineering/chief-technology-officer"),
    ("rol/head-of-regulatory", "Head of Regulatory — relacion con reguladores, aprobaciones, compliance tecnico, vs regulatory-affairs/head-of-government-relations"),
    ("rol/head-of-customer-success-strategy", "Head of Customer Success Strategy — estrategia de CS, modelos de retencion/expansion, enablement de CS, vs customer-success/head-of-customer-success"),
]
NEW_NODES = NEW_NODES_ROUND_60

# Round 61 (iter 199) — 3 deepenings NA + 10 nodos nuevos dominio/rol
TAXONOMY["sustrato/mexico"].append(("criminalistica", "Criminalistica Mexico: Ciencia Forense (UNAM), SEMEFO, peritos ministeriales/fiscales, cadena de custodia, laboratorios crime, vs seguridad-publica/poder-judicial"))
TAXONOMY["sustrato/estados-unidos"].append(("trabajo", "Trabajo / mercado laboral EE.UU.: BLS, empleo/desempleo, salario minimo federal, FLSA, productividad, informalidad (gig), vs labor/seguridad-social"))
TAXONOMY["sustrato/canada"].append(("energia-electrica", "Energia electrica Canada: generacion (hidro/nuke/gas/eolica), transmision (hidroquebec, provincial utilities), regulacion, tarifas, electrificacion; vs energia/infraestructura"))
NEW_NODES_ROUND_61 = [
    ("dominio/privacidad", "Privacidad / data protection (disciplina): principios, consentimiento, transferencias, autoridades, vs proteccion-de-datos/etica-ia"),
    ("dominio/arquitectura-empresarial", "Arquitectura empresarial: frameworks (TOGAF, Zachman, BIZBOK), alineacion estrategia-TI, capacidades, vs enterprise-architect/gobierno-de-ti"),
    ("dominio/banca-de-inversion", "Banca de inversion (profundizacion): underwriting, M&A advisory, ECM/DCM, trading, vs banca/banca-corporativa/capital-riesgo"),
    ("dominio/trading", "Trading / mercados: execution, algoritmico/HFT, asset classes, mesa, vs mercados-financieros/aprendizaje-automatico"),
    ("dominio/finanzas-corporativas-analisis", "Analisis de finanzas corporativas: valuation, modelado financiero, credit rating, vs finanzas-corporativas/finanzas-cuantitativas"),
    ("rol/vp-people-operations", "VP People Operations: lidera HR ops a escala, HRIS, payroll, compliances, vs head-of-people-operations/head-of-people"),
    ("rol/head-of-corporate-communications", "Head of Corporate Communications: comms corporativas internas/externas, reputation, media relations, vs chief-communications-officer/head-of-customer-communications"),
    ("rol/head-of-partner-success", "Head of Partner Success: exito del ecosistema partner, salud de canal, co-selling, vs partner/head-of-partnerships/channel-manager"),
    ("rol/head-of-technical-program", "Head of Technical Program: TPM org, cross-functional delivery, vs technical-program-manager/program-manager"),
    ("rol/head-of-strategy-and-ops", "Head of Strategy & Operations: estrategia + operaciones, BI/planning, vs head-of-strategy/chief-operating-officer/head-of-revops"),
]
NEW_NODES = NEW_NODES_ROUND_61

# Round 62 (iter 200) — 3 deepenings NA + 10 nodos nuevos dominio/rol
TAXONOMY["sustrato/mexico"].append(("estados", "Estados de México / federalismo subnacional: 32 entidades federativas, constituciones locales, congresos estatales, gobernadores, coordinacion fiscal (CFE/Ramo 33), vs gobierno-federal/entidades-federativas"))
TAXONOMY["sustrato/estados-unidos"].append(("recursos-naturales", "Recursos naturales EE.UU.: DOI, USGS, BLM, USFS, BOEM, minerales criticos, tierras publicas, agua, energia de tierras publicas, vs mineria/medio-ambiente"))
TAXONOMY["sustrato/canada"].append(("pesca-acuicultura", "Pesca y acuacultura Canada: DFO, pesca comercial (salmon, cangrejo, bacalao), acuicultura, cuotas/IFMP, tratados (NAFO/UNCLOS), vs sector-agroalimentario/medio-ambiente"))
NEW_NODES_ROUND_62 = [
    ("dominio/gobernanza-de-datos-empresarial", "Gobernanza de datos empresarial / enterprise data governance: DAMA-DMBOK, data stewardship, data quality, lineage, catalogo, data products, vs gobierno-de-datos/proteccion-de-datos"),
    ("dominio/etiquetado-producto", "Etiquetado de producto / product labeling: nutricion (FDA/COFEPRIS/Health Canada), country-of-origin, normas de etiqueta, lenguaje, vs empaque/alimentos-bebidas/regulacion"),
    ("dominio/seguros-de-responsabilidad", "Seguros de responsabilidad / liability insurance: CGL, D&O, E&O/profesional, product liability, cyber liability, vs seguros/reaseguro/seguros-de-credito"),
    ("dominio/inteligencia-de-negocio", "Inteligencia de negocio / business intelligence: BI, dashboards, self-service analytics, data viz, decision support, vs analitica-negocio/analitica-de-marketing"),
    ("dominio/formacion-profesional", "Formacion profesional / TVET: educacion tecnica y vocacional, capacitacion tecnica, certificacion de oficios, upskilling tecnico, vs educacion/educacion-corporativa"),
    ("rol/head-of-product-strategy", "Head of Product Strategy: estrategia de producto, vision/roadmap a nivel portafolio, market/customer insights, priorizacion, vs chief-product-officer/director-of-product/head-of-strategy"),
    ("rol/head-of-sales-strategy", "Head of Sales Strategy: estrategia de ventas, GTM planning, segmentacion, comp plans, canal, vs vp-sales/head-of-revops/head-of-sales-ops"),
    ("rol/head-of-engineering-strategy", "Head of Engineering Strategy: direccion tecnica, arquitectura/plataforma, tech radar, estandares, vs head-of-engineering/chief-technology-officer/vp-engineering"),
    ("rol/head-of-financial-planning", "Head of Financial Planning / FP&A lead: planificacion financiera, forecast, presupuesto, modelado, analisis de variaciones, vs vp-finance/fp-and-a-manager/head-of-finance-ops"),
    ("rol/head-of-solutions-engineering", "Head of Solutions Engineering: lidera org de SE pre-venta, POCs/demos tecnicas, cierre tecnico, puente ventas-producto, vs solutions-architect/sales-engineer/head-of-solutions-consulting"),
]
NEW_NODES = NEW_NODES_ROUND_62

# Round 63 (iter 201) — 3 deepenings NA + 10 nodos nuevos dominio/rol
TAXONOMY["sustrato/mexico"].append(("comercio-exterior", "Comercio exterior Mexico: BANCOMEXT, economia, USMCA/T-MEC, IMMEX, aduanas/OCDE, tratados, exportacion, vs inversion-extranjera"))
TAXONOMY["sustrato/estados-unidos"].append(("energia-nuclear", "Energia nuclear EE.UU.: NRC, DOE Office of Nuclear Energy, plantas comerciales, SMR/advanced reactors, residuos (Yucca/WIPP), seguridad; vs dominio/energia-nuclear"))
TAXONOMY["sustrato/canada"].append(("infraestructura", "Infraestructura Canada: Infrastructure Canada, planificacion de capital, transporte, banda ancha, vivienda, vs energia/transporte"))
NEW_NODES_ROUND_63 = [
    ("dominio/blockchain-empresarial", "Blockchain empresarial / enterprise blockchain: consorcios, Hyperledger, tokens de activos reales (RWA), trazabilidad de cadena de suministro, contratos inteligentes B2B, vs blockchain/deep-tech"),
    ("dominio/ciberseguridad-cloud", "Ciberseguridad de nube / cloud security: Shared Responsibility Model, CSPM, IAM, secrets, postura multicloud, vs ciberseguridad/ciberseguridad-de-la-informacion"),
    ("dominio/derecho-de-datos", "Derecho de datos / data law: titularidad, portabilidad, acceso, soberania de datos, transferencias transfronterizas, vs proteccion-de-datos/derecho-internacional"),
    ("dominio/economia-regional", "Economia regional: desarrollo regional, clústeres territoriales, desigualdad regional, fondos de cohesion, vs geografia-economica/economia-institucional"),
    ("dominio/logistica-urbana", "Logistica urbana / last-mile: microfulfillment, zonas de carga, movilidad de carga, CEP, sostenibilidad de entregas, vs movilidad-urbana/almacenamiento"),
    ("dominio/gobernanza-etica-ia", "Gobernanza etica de la IA: comites de etica, model risk, human-in-the-loop, auditabilidad, alineacion con EU AI Act/NIST RMF, vs etica-ia/gobierno-de-ia"),
    ("dominio/analitica-predictiva", "Analitica predictiva / predictive analytics: forecasting, scoring, churn/attrition, modelado predictivo aplicado, vs ciencia-de-datos/analitica-negocio"),
    ("rol/head-of-ai-product", "Head of AI Product: dueno de producto de IA/ML (agentes, features de ML), estrategia de modelos en producto, eval/seguridad, vs product-manager/head-of-ai/chief-ai-officer"),
    ("rol/head-of-operations-excellence", "Head of Operations Excellence / OpEx: lean, Six Sigma, kaizen a nivel org, eficiencia de procesos, vs head-of-continuous-improvement/quality-manager"),
    ("rol/head-of-customer-growth", "Head of Customer Growth: retencion + expansion + upsell/cross-sell, lifecycle, monetizacion de base, vs customer-success/customer-marketing/head-of-growth"),
]
NEW_NODES = NEW_NODES_ROUND_63

# Round 64 (iter 202) — 3 deepenings NA + 10 nodos nuevos dominio/rol
TAXONOMY["sustrato/mexico"].append(("educacion-basica", "Educacion basica Mexico: SEP, preescolar/primaria/secundaria, reformas educativas, escuelas, docentes, evaluacion, vs educacion/educacion-superior"))
TAXONOMY["sustrato/estados-unidos"].append(("energia-solar", "Energia solar EE.UU.: DOE/SEIA, ITC, utility-scale, rooftop/distributed, interconnection, manufacturing (IRA), vs energia-renovables/energia"))
TAXONOMY["sustrato/canada"].append(("transporte-ferroviario", "Transporte ferroviario Canada: CN, CPKC, VIA Rail, Transport Canada, FRA-equivalent, ferrocarriles de carga/pasajeros, vs transporte/ferroviario(dominio)"))
NEW_NODES_ROUND_64 = [
    ("dominio/financiacion-structurada", "Financiacion estructurada / structured finance: titulizacion (ABS/MBS/CDO/CLO), syndication, project finance, SPVs, vs ingenieria-financiera/derivados"),
    ("dominio/seguros-agricolas", "Seguros agricolas / crop insurance: FCIP (USDA-RMA), indemnizacion, parametrico, vs seguros/seguros-de-credito/sector-agroalimentario"),
    ("dominio/derecho-mercantil", "Derecho mercantil / commercial law: sociedades, titulos de credito, contratos mercantiles, comercio, concursal (vs derecho-civil/societario)"),
    ("dominio/medicina-regenerativa", "Medicina regenerativa: terapia celular, terapia génica, ingenieria de tejidos, medicina personalizada, regulacion FDA/COFEPRIS/Health Canada; vs biomedicina/dispositivos-medicos"),
    ("dominio/ciberseguridad-vehicular", "Ciberseguridad vehicular / automotive security: ISO/SAE 21434, UN R155/R156, ECU, V2X, vs ciberseguridad-ot/electromovilidad"),
    ("dominio/reciclaje", "Reciclaje / recycling industry: plastico, papel, metal, electronicos, economia circular, regulacion (EPR), vs servicios-ambientales/economia-circular"),
    ("rol/head-of-esg", "Head of ESG: lidera estrategia y reporte ESG (GRI/SASB/TCFD/ISSB), materialidad, engagement de stakeholders, vs chief-sustainability-officer/esg-manager/head-of-esg-risks"),
    ("rol/head-of-corporate-venturing", "Head of Corporate Venturing / CVC: corporate venture capital, scouting, co-inversion, incubacion, vs head-of-innovation/chief-innovation-officer"),
    ("rol/head-of-clinical-trials", "Head of Clinical Trials: lidera la ejecucion de ensayos clinicos (fases, sites, pacientes, enrollment), farma/biotech; vs head-of-clinical-operations/dev"),
    ("rol/head-of-user-research", "Head of User Research: lidera la org de UX research (metodos, operacion de estudios, impacto en producto), vs ux-researcher/head-of-ux/head-of-customer-insights"),
]
NEW_NODES = NEW_NODES_ROUND_64

# Round 65 (iter 203) — 3 deepenings NA + 10 nodos nuevos dominio/rol
TAXONOMY["sustrato/mexico"].append(("sistema-de-justicia", "Sistema de justicia Mexico: Ministerio Publico (FGR), defensoria, procuracion/administracion de justicia, juicio de amparo, vs poder-judicial/seguridad-publica/criminalistica"))
TAXONOMY["sustrato/estados-unidos"].append(("defensa-antimonopolio", "Antitrust EE.UU.: DOJ Antitrust Division, FTC, Sherman/Clayton Act, merger review (HSR), vs competencia/sector-tecnologia"))
TAXONOMY["sustrato/canada"].append(("politica-monetaria", "Politica monetaria Canada (profundizacion): Bank of Canada, tasa de politica, inflation targeting 2%, operaciones de mercado abierto, vs economia/bancos"))
NEW_NODES_ROUND_65 = [
    ("dominio/arbitraje-comercial", "Arbitraje comercial (profundizacion): arbitraje domestico/mercantil, CAM (Mexico), AAA/ICDR (US), ADR Chambers (Canada), vs arbitraje-internacional/litigio"),
    ("dominio/ciberseguridad-supply-chain", "Ciberseguridad de la cadena de suministro (profundizacion): SBOM, SCA, EO 14028, EU CRA, TISAX, terceros/4ta linea, vs ciberseguridad/seguridad-corporativa"),
    ("dominio/macroprudencia", "Macroprudencia / financial stability: regulacion macroprudencial, buffer contraciclico, FSB, Consejo de Estabilidad del Sistema Financiero, vs regulacion-financiera/basilea"),
    ("dominio/ciencia-de-materiales-aplicada", "Ciencia de materiales aplicada (profundizacion): materiales avanzados, composites, nanomateriales, baterias solid-state, semiconductores, vs ciencias-materiales/nanotecnologia"),
    ("dominio/gestion-de-inventarios", "Gestion de inventarios / inventory management: EOQ, JIT, MRP, ABC, safety stock, WMS, vs almacenamiento/cadena-de-valor/logistica"),
    ("rol/head-of-corporate-development", "Head of Corporate Development (profundizacion): M&A, due diligence, asignacion de capital, scouting de deals, vs chief-corporate-development/head-of-strategy-and-ops"),
    ("rol/head-of-information-technology", "Head of Information Technology / IT Director (CIO-adjacent): operacion TI, infraestructura, service desk, presupuesto TI, vs cio/head-of-it/director-of-it"),
    ("rol/head-of-employer-branding", "Head of Employer Branding (profundizacion): marca empleadora, talent brand, recruitment marketing, vs head-of-talent-brand/talent-acquisition-manager"),
    ("rol/head-of-credit-risk", "Head of Credit Risk: modelo de credito, PD/LGD/EAD, provisiones, limites, morosidad, vs riesgo-de-credito/credit-manager/chief-risk-officer"),
    ("rol/head-of-field-marketing", "Head of Field Marketing: marketing regional/territorial, eventos locales, co-marketing con partners, vs marketing-manager/head-of-growth-marketing/head-of-partner-marketing"),
]
NEW_NODES = NEW_NODES_ROUND_65

# Round 66 (iter 204) — 3 deepenings NA + 10 nodos nuevos dominio/rol
TAXONOMY["sustrato/mexico"].append(("politica-exterior", "Politica exterior Mexico: SRE, diplomacia, tratados internacionales, ONU/OEA, cooperacion, bloques (USMCA, ALADI), vs relaciones-exteriores/mexico"))
TAXONOMY["sustrato/estados-unidos"].append(("poder-legislativo", "Poder legislativo EE.UU.: Congreso (House/Senate), comites, proceso de ley, presupuesto, vs poder-judicial/estados"))
TAXONOMY["sustrato/canada"].append(("justicia-penal", "Justicia penal Canada: sistema de justicia criminal federal/provincial, Police (RCMP), Crown prosecutors, Charter, vs sistema-de-justicia/poder-judicial"))
NEW_NODES_ROUND_66 = [
    ("dominio/comercio-electronico", "Comercio electronico / e-commerce: marketplaces, D2C, omnicanal digital, fulfillment, pagos en linea, retencion online, CX digital; vs retail/marketing-digital"),
    ("dominio/inteligencia-emocional", "Inteligencia emocional (EQ) (profundizacion): autoconciencia, regulacion, empatia, habilidades sociales, liderazgo y equipos; vs desarrollo-organizacional/clima-organizacional"),
    ("dominio/control-interno", "Control interno (profundizacion): COSO 2013, ICFR, SOX 404, monitoreo, aseguramiento de operaciones; vs auditoria-interna/gobierno-de-riesgos"),
    ("dominio/derecho-de-la-competencia", "Derecho de la competencia / antitrust (profundizacion): control de concentraciones, carteles, abuso de dominancia, autoridades (COFECE/FTC/EC/Competition Bureau); vs defensa-antimonopolio/politica-comercial"),
    ("dominio/seguridad-y-salud-ocupacional", "Seguridad y salud ocupacional (profundizacion): ISO 45001, OSHA/CSST, prevencion de riesgos, bienestar laboral; vs salud-ocupacional/bienestar-laboral"),
    ("dominio/etica-empresarial", "Etica empresarial (profundizacion): codigos de conducta, programas de etica y compliance, anticorrupcion, transparencia, cultura etica; vs gobierno-de-riesgos/compliance"),
    ("dominio/compensacion-beneficios", "Compensacion y beneficios / total rewards (profundizacion): salario, variable pay, beneficios, equity, pensiones, bandas salariales; vs head-of-total-rewards/bienestar-laboral"),
    ("dominio/inteligencia-competitiva", "Inteligencia competitiva (profundizacion): vigilancia, benchmarking, CI legal, market intelligence; vs inteligencia-de-mercado/relaciones-institucionales"),
    ("dominio/transformacion-digital", "Transformacion digital (profundizacion): adopcion de tecnologia, roadmap digital, reingenieria de procesos, cultura digital, habilitadores (cloud, data, IA); vs chief-digital-officer/gobierno-de-ti"),
    ("rol/head-of-data-science", "Head of Data Science: lidera equipos de ciencia de datos, estrategia de modelado/ML, embed en producto y decisiones; vs data-scientist/chief-analytics-officer/chief-data-officer"),
    ("rol/head-of-portfolio-management", "Head of Portfolio Management: gestion de portafolio de inversion/products, priorizacion, PMO, capital allocation; vs portfolio-manager/chief-investment-officer"),
]
NEW_NODES = NEW_NODES_ROUND_66

# Round 67 (iter 205) — 3 deepenings NA + 10 nodos nuevos dominio/rol
TAXONOMY["sustrato/mexico"].append(("educacion-superior", "Educacion superior Mexico: UNAM/IPN/ANUIES, autonomia, PRODEP, posgrado, investigacion; vs educacion/educacion-basica"))
TAXONOMY["sustrato/estados-unidos"].append(("vivienda", "Vivienda EE.UU. (profundizacion): Fannie Mae/Freddie Mac, FHA/HUD, MBS, mercado inmobiliario, vivienda asequible; vs vivienda-real-estate"))
TAXONOMY["sustrato/canada"].append(("comercio-exterior", "Comercio exterior Canada (profundizacion): Global Affairs Canada, exportaciones, USMCA/CUSMA, aranceles, OMC; vs estados-unidos/mexico comercio-exterior"))
NEW_NODES_ROUND_67 = [
    ("dominio/salud-digital", "Salud digital / digital health: telemedicina, wearables, apps de salud, historia clinica electronica (EHR), interoperabilidad (HL7/FHIR), IA en salud, regulacion (FDA Digital Health, COFEPRIS, Health Canada); vs telemedicina/medicina-regenerativa"),
    ("dominio/psicologia", "Psicologia (disciplina de dominio): cognitiva, clinica, organizacional, del consumidor, neurociencia cognitiva, aplicaciones empresariales; vs neurociencia/comportamiento-del-consumidor/salud-mental"),
    ("dominio/seguridad-alimentaria-mexico", "Seguridad alimentaria Mexico: SADER, SENASICA, COFEPRIS, inocuidad, trazabilidad, HACCP, alimentacion/nutricion nacional; vs agricultura/sector-agroalimentario/nutricion"),
    ("dominio/gestion-de-la-demanda", "Gestion de la demanda / demand planning: forecasting, S&OP de demanda, pronostico de ventas, vs gestion-de-la-cadena-de-suministro"),
    ("dominio/evaluacion-de-impacto", "Evaluacion de impacto / impact evaluation: metodos controfactuales (experimentos, dif-en-dif, matching), medicion de politicas, vs analitica-negocio/politica-publica"),
    ("dominio/bioeconomia", "Bioeconomia: uso sostenible de recursos biologicos, biomasa, bioindustria, economia circular biologica, vs biotecnologia/agronegocios/forestal"),
    ("rol/head-of-clinical-affairs", "Head of Clinical Affairs: puente clinico-regulatorio (farma/biotech), estrategia de desarrollo clinico, evidencia, KOLs; vs head-of-medical-affairs/chief-medical-officer"),
    ("rol/head-of-regulatory-affairs", "Head of Regulatory Affairs: lidera asuntos regulatorios, aprobaciones (FDA/EMA/COFEPRIS/Health Canada), CMC, compliance tecnico; vs regulatory-affairs/head-of-regulatory"),
    ("rol/head-of-sales-development", "Head of Sales Development: lidera SDR/BDR org, pipeline temprano, outbound, paso a AE; vs sales-development-representative/sales-manager"),
    ("rol/head-of-product-design", "Head of Product Design: lidera diseno de producto (UX/UI/interaction), design system, research embed, vs head-of-design/head-of-ux/product-designer"),
]
NEW_NODES = NEW_NODES_ROUND_67


# Round 68 (iter 206) — 3 deepenings NA + 10 nodos nuevos dominio/rol
TAXONOMY["sustrato/mexico"].append(("energia-electrica", "Energia electrica Mexico: SENER/CENACE/CRE, CFE (generacion/transmision/distribucion), mercado electrico, tarifas, reforma energetica 2025 (recentralizacion), vs energia/energia-renovables"))
TAXONOMY["sustrato/estados-unidos"].append(("telecomunicaciones", "Telecomunicaciones EE.UU. (profundizacion): FCC, banda ancha, 5G, espectro, neutralidad de red, BEAD, vs telecomunicaciones/telecomunicaciones-corporativas"))
TAXONOMY["sustrato/canada"].append(("energia-nuclear", "Energia nuclear Canada: CNSC, AECL, CANDU, Bruce/Darlington/Point Lepreau, SMR, vs dominio/energia-nuclear"))
NEW_NODES_ROUND_68 = [
    ("dominio/criptoactivos", "Criptoactivos / cryptoassets: BTC/ETH, stablecoins, tokenizacion, DeFi, regulacion (SEC/CFTC, Banxico, AMF), tratamiento fiscal, vs blockchain/blockchain-empresarial/finanzas-descentralizadas"),
    ("dominio/finanzas-corporativas-operaciones", "Finanzas corporativas (operaciones): cierres, consolidacion, reporting, relaciones con inversionistas, vs finanzas-corporativas/finanzas-corporativas-analisis/treasury"),
    ("dominio/gestion-de-la-cadena-de-valor", "Gestion de la cadena de valor / value chain management: upstream/downstream, analisis de valor, outsourcing de cadena, vs cadena-de-valor/cadena-suministro"),
    ("dominio/economia-del-transporte", "Economia del transporte / transport economics: modos, costos de transporte, externalidades, tarifacion, vs transporte/movilidad/logistica-urbana"),
    ("dominio/derecho-de-la-competencia-internacional", "Derecho de la competencia internacional: cooperacion antitrust transnacional, OCDE, acuerdos multilaterales, vs defensa-antimonopolio/derecho-de-la-competencia/politica-comercial"),
    ("dominio/capital-privado", "Capital privado / private equity (profundizacion): fundraising, LBO, exit (IPO/trade sale), gestores de fondos, vs capital-riesgo/banca-de-inversion"),
    ("rol/head-of-customer-lifecycle-marketing", "Head of Customer Lifecycle Marketing: onboarding, retencion, reactivacion, churn, automatizacion de lifecycle, vs head-of-customer-marketing/customer-success"),
    ("rol/head-of-sales-enablement-strategy", "Head of Sales Enablement (profundizacion): estrategia de enablement, playbooks, contenido, coaching, tech stack, vs sales-enablement/sales-manager"),
    ("rol/head-of-engineering-productivity", "Head of Engineering Productivity: developer productivity, DORA metrics, tooling interno, vs head-of-platform-engineering/head-of-engineering-excellence"),
    ("rol/head-of-corporate-strategy", "Head of Corporate Strategy: estrategia corporativa, M&A screening, business development, planning, vs head-of-strategy/chief-strategy-officer"),
]
NEW_NODES = NEW_NODES_ROUND_68


# Round 69 (iter 207) — 3 deepenings NA + 10 nodos nuevos dominio/rol
TAXONOMY["sustrato/mexico"].append(("energia-hidrocarburos", "Energia e hidrocarburos Mexico (profundizacion): PEMEX, CNH, regulacion de hidrocarburos, upstream/downstream, gas natural, refino, vs energia/energia-electrica"))
TAXONOMY["sustrato/estados-unidos"].append(("telecomunicaciones-5g", "Telecomunicaciones 5G EE.UU. (profundizacion): FCC, espectro C-Band/mmWave, despliegue, BEAD, Open RAN, vs telecomunicaciones/telecomunicaciones-corporativas"))
TAXONOMY["sustrato/canada"].append(("pueblos-indigenas", "Pueblos indigenas Canada (profundizacion): First Nations, Inuit, Metis, tratados, duty to consult, reconciliacion, tierra y autonomia, vs derechos-humanos"))
NEW_NODES_ROUND_69 = [
    ("dominio/seguros-de-vida", "Seguros de vida / life insurance: productos (term/whole/UL), actuarial (mortalidad, reservas), reaseguro de vida, bancaseguros, vs seguros-de-personas/seguros"),
    ("dominio/contraloria", "Contraloria / internal audit function publica: control gubernamental, auditoria superior (ASF), fiscalizacion, rendicion de cuentas, vs auditoria-gubernamental/auditoria-interna"),
    ("dominio/seguros-maritimos", "Seguros maritimos / marine insurance: casco, carga, responsabilidad (P&I clubs), averia gruesa, Lloyds, vs maritimo/seguros/seguros-de-credito"),
    ("dominio/derecho-de-agua", "Derecho de agua / water law: derechos de agua, concesiones, cuencas, tratados transfronterizos, vs agua/servicios-publicos/derecho-ambiental"),
    ("dominio/planificacion-urbana", "Planificacion urbana / urban planning: zonificacion, uso de suelo, planificacion territorial, densificacion, vs urbanismo/urbanismo-tactico/movilidad-urbana"),
    ("dominio/redes-5g-moviles", "Redes 5G y moviles / mobile networks: 5G NR, espectro, densificacion, edge, network slicing, vs telecomunicaciones/telecomunicaciones-corporativas"),
    ("dominio/deporte-profesional", "Deporte profesional / pro sports: ligas, franquicias, derechos mediaticos, contratos de jugadores, salary cap, vs deportes/entretenimiento"),
    ("dominio/finanzas-de-proyecto", "Finanzas de proyecto / project finance: SPV, debt/equity, off-take, garantias, riesgo de construccion, vs financiacion-structurada/infraestructura"),
    ("rol/head-of-field-services", "Head of Field Services: operaciones de campo, despacho de tecnicos, SLA in-situ, vs head-of-operations/head-of-field-operations"),
    ("rol/head-of-trade-finance", "Head of Trade Finance: cartas de credito, factoring, garantias, compliance de comercio exterior, vs head-of-trade-compliance/treasurer"),
    ("rol/head-of-regional-sales", "Head of Regional Sales: ventas por region/territorio, cuotas regionales, canales locales, vs vp-sales/sales-manager"),
    ("rol/head-of-it-security", "Head of IT Security: seguridad de la informacion operativa, SOC, GRC, vs head-of-information-security/security-engineer/ciso"),
    ("rol/head-of-sustainability-reporting", "Head of Sustainability Reporting: divulgacion ESG (GRI/SASB/ISSB/CSRD), materialidad, datos no financieros, vs head-of-esg/chief-sustainability-officer"),
    ("rol/head-of-brand-communications", "Head of Brand Communications: narrativa de marca, media relations, contenido de marca, vs chief-communications-officer/head-of-brand"),
]
NEW_NODES = NEW_NODES_ROUND_69


# Round 70 (iter 208) — 3 deepenings NA + 10 nodos nuevos dominio/rol
TAXONOMY["sustrato/mexico"].append(("economia-servicios", "Economia de servicios Mexico: sector terciario, comercio, turismo, financiero, telecom, gobierno, peso en PIB, informalidad, vs economia/trabajo"))
TAXONOMY["sustrato/estados-unidos"].append(("clima", "Clima EE.UU.: EPA, NOAA, climate policy, descarbonizacion, adaptacion/resiliencia, vs medio-ambiente/energia"))
TAXONOMY["sustrato/canada"].append(("inversion-extranjera", "Inversion extranjera Canadá: Investment Canada Act, revisión de inversiones (net benefit, security), Global Affairs Canada, IED, vs mexico/estados-unidos inversion-extranjera"))
NEW_NODES_ROUND_70 = [
    ("dominio/gestion-de-riesgos-it", "Gestion de riesgos de TI / IT risk management: riesgo tecnologico, CIA, marco de riesgo TI, continuidad, vs gobierno-de-ti/seguridad-corporativa"),
    ("dominio/derecho-de-internet", "Derecho de internet / cyber law: jurisdiccion online, contenido, responsabilidad de plataformas, libertad de expresion digital, vs derecho-de-datos/proteccion-de-datos"),
    ("dominio/gestion-de-activos-de-ti", "Gestion de activos de TI / IT asset management (ITAM): inventario hardware/software, licencias, CMDB, ciclo de vida, vs gobierno-de-ti"),
    ("dominio/seguros-de-caucion", "Seguros de caucion / surety & guarantee: fianzas, bonos de cumplimiento, garantias, vs seguros/seguros-de-responsabilidad"),
    ("dominio/economia-del-deporte", "Economia del deporte / sports economics: mercado, ligas, derechos mediaticos, ciudades/estadios, impacto economico, vs deporte-profesional"),
    ("dominio/analitica-web", "Analitica web / web analytics: GA4, tag management, comportamiento de usuario, conversion funnels, vs analitica-marketing/analitica-negocio"),
    ("dominio/gestion-de-precios", "Gestion de precios (price management): pricing execution, list price, discounting governance, MSRP, vs pricing/monetizacion"),
    ("dominio/derecho-de-las-tecnologias", "Derecho de las tecnologias / technology law: regulacion de software, IA, ciber, telecom, e-commerce, vs derecho-de-internet/derecho-de-datos"),
    ("rol/head-of-sales-effectiveness", "Head of Sales Effectiveness: productividad de ventas, coaching, metodologia, enablement de performance, vs head-of-sales-enablement/sales-manager"),
    ("rol/head-of-design-research", "Head of Design Research: lidera org de UX research, metodos, operacion de estudios, impacto en producto, vs head-of-user-research/ux-researcher"),
    ("rol/head-of-mobile-engineering", "Head of Mobile Engineering: lidera desarrollo movil (iOS/Android/cross-platform), release, performance, vs head-of-engineering/engineering-manager"),
    ("rol/head-of-data-engineering", "Head of Data Engineering: lidera plataforma de datos, pipelines, lakehouse, gobierno tecnico, vs data-engineer/data-architect"),
]
NEW_NODES = NEW_NODES_ROUND_70

# Round 71 (iter 209) — 3 deepenings NA + 10 nodos nuevos dominio/rol
TAXONOMY["sustrato/mexico"].append(("seguros", "Seguros Mexico (profundizacion): CNSF, sector asegurador, seguros obligatorios (auto, GMM, vida), RySO/SOAT, vs dominio/seguros"))
TAXONOMY["sustrato/estados-unidos"].append(("seguridad-publica", "Seguridad publica EE.UU. (profundizacion): law enforcement, DOJ (Civil Rights Division, OPD), FBI, policia estatal/local, crimen, reforma policial, vs seguridad-nacional"))
TAXONOMY["sustrato/canada"].append(("salud", "Salud Canada (profundizacion): Health Canada, provincias, CADTH, sistema de salud publico universal, vs salud-publica/dominio/sanidad"))
NEW_NODES_ROUND_71 = [
    ("dominio/ciberseguridad-de-aplicaciones", "Ciberseguridad de aplicaciones / AppSec: SDLC seguro, SAST/DAST/IAST, seguridad de codigo, OWASP Top 10, devsecops, vs ciberseguridad/security-engineer"),
    ("dominio/derecho-bancario", "Derecho bancario / banking law: regulacion de entidades, licencias bancarias, depositos, basilea, resolucion bancaria, vs sistema-financiero/regulacion-financiera"),
    ("dominio/finanzas-de-tesoreria", "Finanzas de tesoreria / corporate treasury: liquidez, cash management, financiamiento, riesgo de tasa/divisa, inversiones de excedentes, vs tesoreria/fp-and-a-manager"),
    ("dominio/seguros-de-inversion", "Seguros de inversion / investment-type insurance: unit-linked, variables, annuities, ahorro-prevision, vs seguros-de-personas/gestion-de-activos"),
    ("dominio/auditoria-de-estados-financieros", "Auditoria de estados financieros / financial statement audit: NIA/ISA, opinion, controles, vs auditoria/contabilidad/auditoria-interna"),
    ("dominio/regulacion-de-aviacion", "Regulacion de aviacion / aviation regulation: FAA (US), TCCA/Transport Canada, EASA, OACI, certificacion de aeronaves, seguridad aerea, vs aviacion/transporte"),
    ("dominio/transparencia-corporativa", "Transparencia corporativa / corporate transparency: disclosure, gobierno abierto empresarial, ESG disclosure, whistleblowing, vs gobierno-corporativo/auditoria-gubernamental"),
    ("rol/head-of-application-security", "Head of Application Security: lidera AppSec (SDLC seguro, SAST/DAST, threat modeling), vs security-engineer/head-of-information-security/devsecops-engineer"),
    ("rol/head-of-capital-markets", "Head of Capital Markets: levantamiento de capital (ECM/DCM), relacion con bancos de inversion, cotizacion, vs banca-de-inversion/chief-investment-officer"),
    ("rol/head-of-tax-strategy", "Head of Tax Strategy: planificacion fiscal internacional, estructura de grupo, precios de transferencia, M&A tax, vs head-of-tax/cfo"),
]
NEW_NODES = NEW_NODES_ROUND_71

# Round 72 (iter 210) — 3 deepenings NA + 10 nodos nuevos dominio/rol
TAXONOMY["sustrato/mexico"].append(("seguridad-cibernetica", "Seguridad cibernetica Mexico: coordinacion cibernetica (CSIRT Mexico, Segob), estrategia nacional de ciberseguridad, incidentes, vs seguridad-nacional/seguridad-publica"))
TAXONOMY["sustrato/estados-unidos"].append(("telecomunicaciones-cloud", "Telecomunicaciones en la nube EE.UU. (profundizacion): FCC, cloud connectivity, neutralidad, despliegue de redes nativas de cloud, espectro compartido, vs telecomunicaciones/telecomunicaciones-corporativas"))
TAXONOMY["sustrato/canada"].append(("energia-renovables", "Energia renovable Canada (profundizacion): hydro, eolica, solar, almacenamiento, transicion, provincial utilities, vs energia/energia-electrica"))
NEW_NODES_ROUND_72 = [
    ("dominio/teoria-monetaria", "Teoria monetaria / monetary theory: oferta/demanda de dinero, multiplicador, canales de transmision, monetarismo vs keynesianismo, neutralidad, inflacion; vs politica-monetaria(sustrato)/banca-central"),
    ("dominio/politica-industrial", "Politica industrial / industrial policy: subsidios, aranceles, seleccion de ganadores, clusters, nearshoring, CHIPS/IRA (US), PROSEC (MX), vs competitividad-empresarial/estrategia"),
    ("dominio/economia-del-turismo", "Economia del turismo / tourism economics: demanda turistica, multiplicador, turismo internacional, sostenibilidad, vs turismo(sustrato)/sector-servicios"),
    ("dominio/derecho-del-entretenimiento", "Derecho del entretenimiento / entertainment law: derechos de autor en medios, contratos de talento, licensing, deportes/musica/cine, vs derecho-de-las-telecomunicaciones/derecho-civil"),
    ("dominio/gestion-de-la-calidad-software", "Gestion de la calidad de software / software quality: SQA, testing strategy, calidad de codigo, defectos, SLA de calidad, vs testing-qa/calidad"),
    ("dominio/ciberseguridad-de-ot", "Ciberseguridad OT / operational technology security (profundizacion): ICS/SCADA, NERC CIP, ISA/IEC 62443, IVA/IACS, plantas/redes industriales, vs ciberseguridad-industrial/ciberdefensa"),
    ("dominio/biometria-financiera", "Biometria financiera / financial biometrics: KYC biometrico, autenticacion, identidad digital, fraude, regulacion (GDPR/biometric bans), vs biometria/proteccion-de-datos/fintech"),
    ("dominio/movilidad-electrica", "Movilidad electrica / e-mobility (profundizacion): EVs, cargadores, V2G, baterias, politica de movilidad, vs electromovilidad/energia-distribuida"),
    ("dominio/servicios-de-consultoria-it", "Servicios de consultoria IT / IT consulting: integradores, SI, advisory, outsourcing de TI, modelos de entrega, vs consultoria/servicios-profesionales"),
    ("dominio/gestion-de-la-demanda-energetica", "Gestion de la demanda energetica / demand-side management: eficiencia, DSM, respuesta a la demanda, smart grid, vs energia/energia-distribuida"),
    ("rol/head-of-payments", "Head of Payments: esquemas/rails (cards, ACH, RTP/FedNow/PIX), clearing/settlement, PSPs, fraud payments, vs pagamentos/finanzas-de-tesoreria/treasurer"),
    ("rol/head-of-corporate-development-strategy", "Head of Corporate Development (profundizacion estrategica): M&A, due diligence, capital allocation, scouting, vs head-of-corporate-development/head-of-strategy-and-ops"),
    ("rol/head-of-mobile-product", "Head of Mobile Product: producto movil (iOS/Android), app growth, release, performance, vs head-of-digital-product/head-of-product"),
    ("rol/head-of-commercial-excellence", "Head of Commercial Excellence: enablement comercial, pricing, go-to-market, analitica de ventas, vs head-of-sales-effectiveness/chief-commercial-officer"),
    ("rol/head-of-customer-ops-strategy", "Head of Customer Operations Strategy: CX ops, order-to-cash, billing/support ops, eficiencia de servicio, vs head-of-customer-ops/customer-success-strategy"),
    ("rol/head-of-data-governance", "Head of Data Governance: calidad, linaje, politica y compliance de datos, privacidad by design, vs data-governance-lead/chief-data-officer/gobierno-de-datos"),
    ("rol/head-of-workforce-experience-strategy", "Head of Workforce Experience (estrategia): EX del empleado, bienestar, engagement, journey del empleado, vs head-of-workforce-experience/head-of-people"),
    ("rol/head-of-brand-strategy", "Head of Brand Strategy: estrategia de marca, posicionamiento, arquitectura de marca, vs head-of-brand/chief-brand-officer"),
    ("rol/head-of-ai-strategy", "Head of AI Strategy: estrategia de adopcion de IA/ML, roadmaps de modelos, governance, vs head-of-ai/chief-ai-officer"),
    ("rol/head-of-risk-and-controls", "Head of Risk & Controls: riesgo operativo + controles (1st/2nd line), SOX, ICFR, vs head-of-risk-and-compliance/chief-risk-officer"),
]
NEW_NODES = NEW_NODES_ROUND_72



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
        if not node_exists(path):
            print(f"- {path}: {desc}  <- NUEVO")
            _any_new = True
    if not _any_new:
        print("- (ninguno: todos los nodos sugeridos ya existen)")
    print(f"\nTOTAL huecos en nodos existentes: {total}")


if __name__ == "__main__":
    main()
