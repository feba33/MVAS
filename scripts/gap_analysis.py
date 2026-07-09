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
        ("privacidad", "Privacidad (PIPEDA)"),
        ("impuestos", "Impuestos federales Canadá (CRA)"),
    ],
    "sustrato/brasil": [
        ("lgpd", "LGPD (protección de datos Brasil)"),
        ("impuestos", "Impuestos Brasil (Receita Federal)"),
    ],
    "dominio/finanzas": [
        ("private-equity-vc", "Private Equity / Venture Capital / fundraising"),
        ("cripto-activos", "Criptoactivos / activos digitales"),
        ("behavioral-finance", "Finanzas conductuales"),
    ],
    "dominio/computacion": [
        ("ciberseguridad", "Ciberseguridad"),
        ("data-engineering", "Ingeniería de datos"),
        ("ml-engineering", "ML / AI engineering"),
        ("testing-qa", "Testing / QA"),
    ],
    "dominio/marketing": [
        ("content-marketing", "Content marketing"),
        ("cro", "Conversion Rate Optimization (CRO)"),
        ("brand", "Branding / marca"),
    ],
    "dominio/leyes": [
        ("derecho-contratos", "Derecho de contratos"),
        ("propiedad-intelectual", "Propiedad intelectual (profundización)"),
    ],
    "dominio/contabilidad": [
        ("costos", "Contabilidad de costos"),
        ("auditoria", "Auditoría"),
        ("impuestos", "Contabilidad fiscal"),
    ],
    "dominio/diseno": [
        ("ux-research", "UX research (métodos)"),
        ("accesibilidad", "Accesibilidad (WCAG)"),
        ("service-design", "Service design"),
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
    ],
}

# Nodos sugeridos que aún no existen en el repo
NEW_NODES = [
    ("dominio/ventas", "Ventas (sales): metodología, funnel, CRM"),
    ("dominio/producto", "Producto (dominio): discovery, métricas AARRR, PMF"),
    ("dominio/recursos-humanos", "Recursos Humanos / People"),
    ("dominio/operaciones", "Operaciones (supply chain, lean)"),
    ("organización/ejemplo-empresa", "Empresa ejemplo (capa organización)"),
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
    print("\n## Nodos sugeridos (no existen aún)")
    for path, desc in NEW_NODES:
        mark = "" if os.path.isdir(os.path.join(ROOT, path)) else "  <- NUEVO"
        print(f"- {path}: {desc}{mark}")
    print(f"\nTOTAL huecos en nodos existentes: {total}")


if __name__ == "__main__":
    main()
