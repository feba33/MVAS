#!/usr/bin/env python3
ROOT = "/opt/data/MVAS"
p = ROOT + "/working.md"
s = open(p, encoding="utf-8").read()

# 1) Insert Round 67 queue block right before the progress index section header.
queue = """## ✅ COLA ROUND 67 — COMPLETA (10/10 páginas nuevas)
> gap_analysis.py (iter 205) reportó 1 hueco real en nodo existente (deepening NA: estados-unidos/vivienda) + 9 nodos nuevos. NOTA dedup: mexico/educacion-superior y canada/comercio-exterior ya existían (Round 50, planas) y dominio/gestion-de-la-demanda ya existía (Round 57) → 1 sustrato real. Taxonomía extendida con NEW_NODES_ROUND_67 + 3 TAXONOMY appends.
> Alcance sustrato: solo Norteamérica (EE.UU. deepening). Modelo centralizado: página plana + index.md/log.md raíz. Reference-only (sin raw/).
### Sustrato (deepening nodo NA existente)
- [x] sustrato/estados-unidos/vivienda.md — Vivienda EE.UU.: Fannie Mae/Freddie Mac (GSE), FHA/HUD, MBS, mercado inmobiliario, vivienda asequible
### Dominio (nuevos nodos)
- [x] dominio/salud-digital.md — Salud digital (telemedicina, wearables, EHR, HL7/FHIR, IA en salud, FDA/COFEPRIS/Health Canada)
- [x] dominio/psicologia.md — Psicología (cognitiva, clínica, organizacional, del consumidor, neurociencia)
- [x] dominio/seguridad-alimentaria-mexico.md — Seguridad alimentaria México (SADER/SENASICA, COFEPRIS, HACCP, trazabilidad)
- [x] dominio/evaluacion-de-impacto.md — Evaluación de impacto (contrafactual, RCT, dif-en-dif, medición de políticas)
- [x] dominio/bioeconomia.md — Bioeconomía (biomasa, bioindustria, economía circular biológica)
### Rol (nuevos nodos)
- [x] rol/head-of-clinical-affairs.md — Head of Clinical Affairs (puente clínico-regulatorio farma/biotech, evidencia, KOLs)
- [x] rol/head-of-regulatory-affairs.md — Head of Regulatory Affairs (aprobaciones FDA/EMA/COFEPRIS, CMC, compliance técnico)
- [x] rol/head-of-sales-development.md — Head of Sales Development (lidera SDR/BDR, pipeline temprano, outbound)
- [x] rol/head-of-product-design.md — Head of Product Design (UX/UI/interaction, design system, research embed)

### ITER 205 — Round 67 (2026-07-18)
- gap_analysis.py (iter 205) reportó 1 hueco real (estados-unidos/vivienda) + 9 nodos nuevos; 3 deepenings planificados (mexico/educacion-superior, canada/comercio-exterior, dominio/gestion-de-la-demanda) ya existían → dedup a 1 sustrato real. Extendida taxonomía (Round 67).
- 10 páginas ingeridas cubriendo las 3 capas (centralizado — página plana + index.md/log.md raíz; reference-only, sin raw/):
  - [sustrato] `sustrato/estados-unidos/vivienda.md`: Fannie Mae/Freddie Mac (GSE), FHA/HUD, MBS, mercado inmobiliario, vivienda asequible.
  - [dominio] `dominio/salud-digital/salud-digital.md`: telemedicina, wearables, EHR, HL7/FHIR, IA en salud, FDA/COFEPRIS/Health Canada.
  - [dominio] `dominio/psicologia/psicologia.md`: cognitiva/clínica/organizacional/consumidor, neurociencia.
  - [dominio] `dominio/seguridad-alimentaria-mexico/seguridad-alimentaria-mexico.md`: SADER/SENASICA, COFEPRIS, HACCP, trazabilidad.
  - [dominio] `dominio/evaluacion-de-impacto/evaluacion-de-impacto.md`: contrafactual, RCT, dif-en-dif, medición de políticas.
  - [dominio] `dominio/bioeconomia/bioeconomia.md`: biomasa, bioindustria, economía circular biológica.
  - [rol] `rol/head-of-clinical-affairs/head-of-clinical-affairs.md`: puente clínico-regulatorio farma/biotech, evidencia, KOLs.
  - [rol] `rol/head-of-regulatory-affairs/head-of-regulatory-affairs.md`: aprobaciones FDA/EMA/COFEPRIS, CMC, compliance técnico.
  - [rol] `rol/head-of-sales-development/head-of-sales-development.md`: lidera SDR/BDR, pipeline temprano, outbound.
  - [rol] `rol/head-of-product-design/head-of-product-design.md`: UX/UI/interaction, design system, research embed.
- Reference-only (Wikipedia EN + autoridades: Fannie Mae, FHA/HUD, COFEPRIS, SENASICA, HL7/FHIR, FDA; sin raw/). ALLOWED_SUSTRATO respetado (solo Norteamérica; 1 deepening EE.UU.).
- **Round 67 COMPLETA (10/10 temas).** Cola Round 67 VACÍA. Siguiente paso: re-ejecutar `python3 scripts/gap_analysis.py`; si devuelve 0, ampliar taxonomía para Round 68 o pausar.

"""

marker = "## 📊 ÍNDICE DE PROGRESO (acumulado)"
assert marker in s, "progress marker not found"
s = s.replace(marker, queue + marker, 1)

# 2) Update progress index counts.
import re
# topics 959 -> 969
s = s.replace("| **Tópicos ingeridos (acumulado): 959** (Round 65: 955; Round 66: 959/4 nuevas). |",
              "| **Tópicos ingeridos (acumulado): 969** (Round 66: 959; Round 67: 969/10 nuevas). |")
# rounds 66 -> 67
s = s.replace("| **Rondas:** 66 completas (Round 1..66). |",
              "| **Rondas:** 67 completas (Round 1..67). |")
# nodos dominio ~244 -> ~249
s = s.replace("| **Nodos dominio:** ~244 (sin cambio en Round 66; los 9 dominio de NEW_NODES_ROUND_66 ya existían). |",
              "| **Nodos dominio:** ~249 (Round 67 +5: salud-digital, psicologia, seguridad-alimentaria-mexico, evaluacion-de-impacto, bioeconomia). |")
# nodos rol ~228 -> ~232
s = s.replace("| **Nodos rol:** ~228 (Round 66 +1: head-of-portfolio-management). |",
              "| **Nodos rol:** ~232 (Round 67 +4: clinical-affairs, regulatory-affairs, sales-development, product-design). |")
# iteraciones 204 -> 205
s = s.replace("| **Iteraciones totales:** 204. |",
              "| **Iteraciones totales:** 205. |")

# 3) Update ESTADO block.
s = s.replace("| - **Iteración actual:** 204 (Round 66 COMPLETA — 4/4 ingestados e integrados). |",
              "| - **Iteración actual:** 205 (Round 67 COMPLETA — 10/10 ingestados e integrados). |")
s = s.replace("| - **Cola:** Round 66 COMPLETA (4/4). |",
              "| - **Cola:** Round 67 COMPLETA (10/10). |")
old_ult = "| - **Última ação:** Round 66 iter 204 — gap_analysis.py reportó 3 huecos en nodos existentes (deepenings NA) + 1 nodo nuevo real (rol/head-of-portfolio-management); 9 nodos restantes de NEW_NODES_ROUND_66 ya existían → dedup a 4 reales. Ingestó 4 páginas (3 sustrato + 1 rol) con modelo centralizado (página plana + index.md root + log.md root). Integración y commit. Reference-only (Wikipedia + autoridades; sin raw/). ALLOWED_SUSTRATO respetado (solo Norteamérica). |"
new_ult = "| - **Última ação:** Round 67 iter 205 — gap_analysis.py (iter 205) reportó 1 hueco real (estados-unidos/vivienda) + 9 nodos nuevos; 3 deepenings planificados ya existían (dedup a 1 sustrato real). Ingestó 10 páginas (1 sustrato + 5 dominio + 4 rol) con modelo centralizado (página plana + index.md root + log.md root). Integración y commit. Reference-only (Wikipedia + autoridades; sin raw/). ALLOWED_SUSTRATO respetado (solo Norteamérica; 1 deepening EE.UU.). |"
assert old_ult in s, "estado ultima acao not found"
s = s.replace(old_ult, new_ult, 1)

# 4) Update PRÓXIMA TAREFA.
s = s.replace("- Round 66 COMPLETA (4 páginas nuevas ingeridas y commiteadas). Próximo: ejecutar `python3 scripts/gap_analysis.py`; si 0 huecos -> extender taxonomía (Round 67) e ingerir en la siguiente corrida. Sustrato NA = solo Norteamérica (respetado).",
              "- Round 67 COMPLETA (10 páginas nuevas ingeridas y commiteadas). Próximo: ejecutar `python3 scripts/gap_analysis.py`; si 0 huecos -> extender taxonomía (Round 68) e ingerir en la siguiente corrida. Sustrato NA = solo Norteamérica (respetado).")

open(p, "w", encoding="utf-8").write(s)
print("working.md updated")
