#!/usr/bin/env python3
import sys
ROOT = "/opt/data/MVAS"
p = ROOT + "/index.md"
s = open(p, encoding="utf-8").read()
lines = s.split("\n")

def block_end(start):
    for j in range(start + 1, len(lines)):
        if lines[j].startswith("### "):
            return j
    return len(lines)

# 1) sustrato/estados-unidos (last occurrence)
us_start = None
for i, l in enumerate(lines):
    if l.startswith("### sustrato/estados-unidos"):
        us_start = i
us_end = block_end(us_start)

entries_us = "- [vivienda](sustrato/estados-unidos/vivienda.md) — Vivienda EE.UU.: Fannie Mae/Freddie Mac (GSE), FHA/HUD, MBS, mercado inmobiliario, vivienda asequible; vs vivienda-real-estate · eeuu,vivienda,housing,fannie-mae,freddie-mac,fha,hud,mbs · 2026-07-18"

lines = lines[:us_end] + [entries_us] + lines[us_end:]

# 2) dominio (last occurrence)
dom_start = None
for i, l in enumerate(lines):
    if l.startswith("### dominio"):
        dom_start = i
dom_end = block_end(dom_start)

entries_dom = [
"- [salud-digital](dominio/salud-digital/salud-digital.md) — Salud digital: telemedicina, wearables, EHR, interoperabilidad HL7/FHIR, IA en salud, regulacion FDA/COFEPRIS/Health Canada · salud-digital,digital-health,telemedicina,fhir,ehr,ia-salud · 2026-07-18",
"- [psicologia](dominio/psicologia/psicologia.md) — Psicologia (disciplina): cognitiva, clinica, organizacional, del consumidor, neurociencia; vs neurociencia/comportamiento-del-consumidor · psicologia,cognitiva,clinica,organizacional,consumidor · 2026-07-18",
"- [seguridad-alimentaria-mexico](dominio/seguridad-alimentaria-mexico/seguridad-alimentaria-mexico.md) — Seguridad alimentaria Mexico: SADER/SENASICA, COFEPRIS, inocuidad, trazabilidad, HACCP · seguridad-alimentaria,mexico,senasica,cofepris,inocuidad,haccp · 2026-07-18",
"- [evaluacion-de-impacto](dominio/evaluacion-de-impacto/evaluacion-de-impacto.md) — Evaluacion de impacto: contrafactual, RCT, dif-en-dif, medicion de politicas; vs analitica-negocio/politica-publica · evaluacion-de-impacto,contrafactual,rct,metodos,politicas-publicas · 2026-07-18",
"- [bioeconomia](dominio/bioeconomia/bioeconomia.md) — Bioeconomia: biomasa, bioindustria, biotecnologia aplicada, economia circular biologica · bioeconomia,biomasa,bioindustria,biotecnologia,economia-circular · 2026-07-18",
]

lines = lines[:dom_end] + entries_dom + lines[dom_end:]

# 3) rol (last occurrence)
rol_start = None
for i, l in enumerate(lines):
    if l.startswith("### rol"):
        rol_start = i
rol_end = block_end(rol_start)

entries_rol = [
"- [head-of-clinical-affairs](rol/head-of-clinical-affairs/head-of-clinical-affairs.md) — Head of Clinical Affairs: puente clinico-regulatorio (farma/biotech), evidencia, KOLs; vs head-of-medical-affairs/CMO · head-of-clinical-affairs,clinical-affairs,farma,biotech,evidencia,kol · 2026-07-18",
"- [head-of-regulatory-affairs](rol/head-of-regulatory-affairs/head-of-regulatory-affairs.md) — Head of Regulatory Affairs: aprobaciones FDA/EMA/COFEPRIS, CMC, compliance tecnico; vs regulatory-affairs/head-of-regulatory · head-of-regulatory-affairs,regulatory,aprobaciones,fda,ema,cmc · 2026-07-18",
"- [head-of-sales-development](rol/head-of-sales-development/head-of-sales-development.md) — Head of Sales Development: lidera SDR/BDR, pipeline temprano, outbound; vs sales-development-representative/sales-manager · head-of-sales-development,sdr,bdr,pipeline,outbound,prospeccion · 2026-07-18",
"- [head-of-product-design](rol/head-of-product-design/head-of-product-design.md) — Head of Product Design: UX/UI/interaction, design system, research embed; vs head-of-design/head-of-ux · head-of-product-design,product-design,ux,ui,design-system,research · 2026-07-18",
]

lines = lines[:rol_end] + entries_rol + lines[rol_end:]

open(p, "w", encoding="utf-8").write("\n".join(lines))
print("index.md updated; new line count:", len(lines))
