#!/usr/bin/env python3
"""add_en_keywords.py — añade `english_keywords:` (k-words en inglés) al frontmatter
de todas las páginas de contenido de MVAS, traduciendo las `tags` ES->EN vía un
diccionario de dominio. Es incremental: no sobreescribe si el campo ya existe.

Regla de MVAS: cada página lleva `tags` (ES) + `english_keywords` (EN) para
retrieval cross-lingual (BM25 + embedding multilingüe). Ver esquema.md.

Uso:  python3 scripts/add_en_keywords.py [--dry-run]
"""
import argparse
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP_DIRS = {".git", "raw", "__pycache__", "node_modules", ".qmd"}

# Español -> inglés (términos de dominio MVAS). Los que no están se conservan
# tal cual (muchos son inicialismos/proper nouns ya en inglés: ISR, IVA, SEC...).
ES_EN = {
    "lgsm": "LGSM (Ley General de Sociedades Mercantiles)",
    "codigo-de-comercio": "Commercial Code",
    "regimen-fiscal": "tax regime",
    "isr": "ISR (Impuesto Sobre la Renta, income tax)",
    "iva": "VAT (Value Added Tax)",
    "resico": "RESICO (Régimen Simplificado de Confianza, simplified tax regime)",
    "lfpdpdp": "LFPDPPP (personal data protection law)",
    "privacidad": "privacy",
    "regulacion-ia": "AI regulation",
    "ia": "AI (artificial intelligence)",
    "derecho-digital": "digital law",
    "riesgo": "risk",
    "cofece": "COFECE (antitrust authority)",
    "competencia": "competition / antitrust",
    "lft": "LFT (Federal Labor Law)",
    "laboral": "labor",
    "outsourcing": "outsourcing",
    "ptu": "PTU (profit sharing)",
    "profeco": "PROFECO (consumer protection)",
    "condusef": "CONDUSEF (financial consumer protection)",
    "consumidor": "consumer",
    "pld": "AML (anti-money laundering)",
    "uif": "UIF (Financial Intelligence Unit)",
    "aml": "AML (anti-money laundering)",
    "delaware-gcl": "Delaware General Corporation Law (DGCL)",
    "dgcl": "DGCL (Delaware corporate law)",
    "llc": "LLC (Limited Liability Company)",
    "irs": "IRS (Internal Revenue Service, taxation)",
    "empleo-at-will": "at-will employment",
    "at-will": "at-will employment",
    "copyright": "copyright",
    "patente": "patent",
    "fintech": "fintech",
    "fintech-regulacion": "fintech regulation",
    "sec-valores": "SEC (Securities and Exchange Commission)",
    "sec": "SEC / securities",
    "valores": "securities",
    "antitrust": "antitrust",
    "sherman": "Sherman Act",
    "bankruptcy": "bankruptcy",
    "concursal": "insolvency / bankruptcy",
    "pipeda": "PIPEDA (Personal Information Protection, Canada)",
    "impuestos": "taxes / taxation",
    "cra": "CRA (Canada Revenue Agency)",
    "lgpd": "LGPD (Lei Geral de Proteção de Dados, Brazil)",
    "proteccion-datos": "data protection",
    "niif": "IFRS",
    "gaap": "US GAAP",
    "pe": "private equity",
    "vc": "venture capital",
    "fundraising": "fundraising",
    "cripto": "crypto",
    "blockchain": "blockchain",
    "behavioral": "behavioral finance",
    "finanzas": "finance",
    "valoracion": "valuation",
    "instrumentos-financieros": "financial instruments",
    "ciberseguridad": "cybersecurity",
    "cia": "CIA triad (confidentiality, integrity, availability)",
    "nist": "NIST (cybersecurity framework)",
    "data-engineering": "data engineering",
    "etl": "ETL (extract transform load)",
    "data-eng": "data engineering",
    "ml": "machine learning",
    "mlops": "MLOps",
    "testing": "testing",
    "qa": "QA (quality assurance)",
    "tdd": "TDD (test-driven development)",
    "content": "content marketing",
    "seo": "SEO (search engine optimization)",
    "cro": "CRO (conversion rate optimization)",
    "ab-testing": "A/B testing",
    "brand": "branding",
    "branding": "branding",
    "marketing": "marketing",
    "derecho-contratos": "contract law",
    "contratos": "contracts",
    "propiedad-intelectual": "intellectual property",
    "ip": "intellectual property",
    "costos": "costing",
    "auditoria": "auditing",
    "contabilidad-fiscal": "tax accounting",
    "diseno": "design",
    "design-thinking": "design thinking",
    "ux-research": "UX research",
    "accesibilidad": "accessibility",
    "wcag": "WCAG (accessibility guidelines)",
    "service-design": "service design",
    "ventas": "sales",
    "funnel": "funnel",
    "crm": "CRM (customer relationship management)",
    "producto": "product",
    "aarrr": "AARRR (pirate metrics)",
    "pmf": "PMF (product-market fit)",
    "rr-hh": "HR (human resources) / people",
    "people": "people / HR",
    "operaciones": "operations",
    "supply-chain": "supply chain",
    "lean": "lean",
    "growth": "growth",
    "product": "product management",
    "engineering-manager": "engineering manager",
    "data-lead": "data lead",
    "ux-ui": "UX/UI",
    "marketing-lead": "marketing lead",
    "finance-lead": "finance lead",
    "operations-lead": "operations lead",
    "agile-coach": "agile coach",
    "sales-lead": "sales lead",
    "customer-success": "customer success",
    "people-lead": "people lead",
    "legal-counsel": "legal counsel",
    "founder-ceo": "founder / CEO",
    "cto": "CTO (chief technology officer)",
    "data-engineer": "data engineer",
    "qa-engineer": "QA engineer",
}


def translate_tag(t):
    t = t.strip()
    if not t:
        return None
    return ES_EN.get(t, t)


def process(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    if not text.startswith("---"):
        return False
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return False
    fm = m.group(1)
    if "titulo:" not in fm:
        return False  # not a content page
    if "english_keywords:" in fm:
        return False  # already present
    tag_m = re.search(r"^(\s*🏷️\s*)?tags:\s*(.*)$", fm, re.M)
    if not tag_m:
        return False  # no tags to translate
    en = [translate_tag(x) for x in tag_m.group(2).split(",")]
    en = [x for x in en if x]
    en_str = ", ".join(en)
    insert = tag_m.group(0) + "\nenglish_keywords: " + en_str
    fm2 = fm[: tag_m.start()] + insert + fm[tag_m.end():]
    new_text = "---\n" + fm2 + "\n---\n" + text[m.end():]
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    count = 0
    for dp, ds, fs in os.walk(ROOT):
        ds[:] = [d for d in ds if d not in SKIP_DIRS]
        for fn in fs:
            if not fn.endswith(".md"):
                continue
            p = os.path.join(dp, fn)
            if args.dry_run:
                with open(p, encoding="utf-8") as f:
                    t = f.read()
                if t.startswith("---") and "titulo:" in t and "english_keywords:" not in t:
                    count += 1
            else:
                if process(p):
                    count += 1
    print(f"Páginas con english_keywords añadidos: {count}")


if __name__ == "__main__":
    main()
