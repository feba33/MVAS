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
    ],
    "sustrato/estados-unidos": [
        ("sec-valores", "SEC y regulación de valores"),
        ("antitrust", "Antitrust (Sherman / Clayton)"),
        ("bankruptcy", "Derecho concursal / bancarrotas"),
    ],
    "sustrato/canada": [
        ("competition-bureau", "Competencia / antitrust (Competition Bureau Canada)"),
        ("provincial-federal", "Divisiones de poder provincial vs federal en Canadá"),
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
