---
titulo: "Farmacología"
capa: "dominio"
tema: "farmacologia"
fuente: "https://en.wikipedia.org/wiki/Pharmacology"
fuente2: "https://www.fda.gov/drugs"
fecha: "2026-07-21"
confianza: "alta"
tags: ["farmacología", "fármacos", "farmacocinética", "farmacodinamia", "ensayos-clínicos", "farmacovigilancia", "terapéutica", "desarrollo-fármacos"]
profundidad: 3
estado: "profundo"
rol: ["head-of-medical-affairs", "head-of-clinical-data-management", "head-of-rd", "head-of-regulatory-affairs", "head-of-clinical-operations", "head-of-clinical-data-management"]
actividades: ["descubrimiento-fármacos", "desarrollo-clínico", "farmacovigilancia", "medicina-precisión", "farmacogenómica", "regulación-fármacos"]
organizaciones: ["fda", "ema", "pmda", "cofepris", "health-canada", "ich", "who", "cibt"]
responsabilidades: ["perfil-seguridad", "eficacia", "dosificación", "interacciones", "acceso-mercado"]
tareas: ["fase-i-iv", "pk-pd-modeling", "risk-management", "labeling", "post-marketing"]
---

# Farmacología: fármacos, farmacocinética/farmacodinamia, ensayos clínicos, seguridad, farmacovigilancia

## Definición y alcance

**Farmacología** = ciencia que estudia la interacción entre **sustancias químicas (fármacos)** y **sistemas biológicos** para prevenir, diagnosticar, tratar o curar enfermedades.

**Dos ramas fundamentales** (Paul Ehrlich, Oswald Schmiedeberg):
- **Farmacocinética (PK)**: lo que el **organismo hace al fármaco** (ADME: Absorción, Distribución, Metabolismo, Excreción).
- **Farmacodinamia (PD)**: lo que el **fármaco hace al organismo** (mecanismo acción, relación dosis-respuesta, efectos terapéuticos/tóxicos).

**Farmacología clínica** = aplicación PK/PD en humanos (dosis, eficacia, seguridad, poblaciones especiales).
**Toxicología** = estudio efectos adversos (dosis, mecanismos, evaluación riesgo).

## Farmacocinética (ADME)

| Fase | Procesos clave | Parámetros | Factores modificadores |
|------|----------------|------------|------------------------|
| **Absorción** | Paso barreras biológicas (GI, piel, pulmón, mucosa) | Biodisponibilidad (F), Tmax, Cmax, AUC | pH GI, tránsito, formulaciones, transportadores (P-gp, OATP), primera pasada hepática |
| **Distribución** | Perfusión tejidos, unión proteínas, barreras (HEB, placentaria) | Vd (volumen distribución), fu (fracción libre), Kp (partición tejido/plasma) | Albumina/AGP, flujo sanguíneo, lipofilia, peso molecular, transportadores |
| **Metabolismo** | Biotransformación (Fase I: oxidación/reducción/hidrólisis; Fase II: conjugación) | CLint (clearance intrínseco), fm (fracción metabolizada), metabolitos activos/tóxicos | **CYP450** (1A2, 2B6, 2C8, 2C9, 2C19, 2D6, 3A4/5), UGTs, SULTs, GSTs, NATs; polimorfismos, inductores/inhibidores |
| **Excreción** | Renal (filtración glomerular, secreción tubular, reabsorción), biliar/heces, pulmonar, leche | CLr (clearance renal), fe (fracción excretada inalterada), CLh (hepático) | GFR, pH urinario, transportadores renales (OAT, OCT, MATE), función hepática |

**Modelado PK**: compartimental (1-2-3 comp., fisiológico - PBPK), no-compartimental (NCA: AUC, AUMC, MRT, Vss, CL). Software: NONMEM, Monolix, Phoenix WinNonlin, R (nlmixr, pkpainel), Stan/PyMC (bayesiano).

**Poblaciones especiales**: pediátrica (alometría, maduración enzimática), geriátrica (polifarmacia, fragilidad, función renal/hepática reducida), embarazo/lactancia (cambios fisiológicos, teratogenicidad), insuficiencia renal/hepática (ajuste dosis), obesidad (Vd lipofílicos).

## Farmacodinamia

**Receptores y mecanismos**:
- **Receptores acoplados a proteína G (GPCRs)**: ~34% blancos fármacos (β-adrenérgicos, opioides, muscarínicos, dopaminérgicos, serotoninérgicos, cannabinoides).
- **Canales iónicos**: voltaje/ligando dependientes (Na⁺, K⁺, Ca²⁺, Cl⁻, nAChR, GABAₐ, 5-HT₃).
- **Quinasa tirosina receptores (RTKs)**: EGFR, VEGFR, PDGFR, ALK, ROS1, NTRK — dianas oncológicas.
- **Receptores nucleares**: esteroides, tiroides, vitamina D, PPARs, FXR, LXR — regulación transcripción.
- **Enzimas**: inhibición competitiva/no-competitiva/irreversible (ej. IECA, estatinas, PPIs, PARP, BTK, JAK).
- **Proteínas estructurales/otras**: tubulina (taxanos), topoisomerasa (topotecán), ribosoma (macrólidos), ADN (alquilantes, platino).

**Relación dosis-respuesta**:
- **Graduada** (individuo): E = Emax × Cⁿ / (EC50ⁿ + Cⁿ) (Hill); potencia (EC50), eficacia (Emax), pendiente (n).
- **Cuantal** (población): % respondedores vs dosis/log-dosis; ED50, TD50, LD50; **índice terapéutico** = TD50/ED50 (o LD50/ED50); **ventana terapéutica** = rango concentraciones eficaz-seguro.

**Tipos agonismo/antagonismo**: agonista completo, parcial, inverso; antagonista competitivo (surmountable), no-competitivo/irreversible (insurmountable), alostérico (PAM/NAM/SAM).

**Farmacodinamia tiempo-dependiente**: tolerancia (desensibilización receptores, down-regulation), sensibilización, histeresis (efecto retardado vs concentración), ritmicidad circadiana (cronofarmacología).

## Desarrollo clínico de fármacos

### Fases (ICH E8/E11, FDA 21 CFR 312)

| Fase | Objetivo | Población | Tamaño típico | Duración |
|------|----------|-----------|---------------|----------|
| **Preclínica** | Seguridad (tox aguda/subcrónica/crónica, genotox, reprotox, safety pharmacology), PK/PD, formulación | In vitro, animales (roedor + no roedor) | - | 1-4 años |
| **Fase I** | Seguridad, tolerabilidad, PK, PD, MTD/RP2D | Voluntarios sanos / pacientes (oncológicos) | 20-100 | 6-12 meses |
| **Fase II** | Eficacia preliminar, dosis-respuesta, seguridad | Pacientes diana | 100-300 | 1-2 años |
| **Fase III** | Confirmar eficacia/seguridad en población representativa | Poblaciones amplias | 300-3000+ | 2-4 años |
| **Registro** | NDA/BLA (FDA), MAA (EMA), NMPA (China), PMDA (Japón), COFEPRIS (MX), ANVISA (BR), Health Canada | - | - | 6-12 meses revisión |
| **Fase IV / Post-marketing** | Vigilancia seguridad, efectividad real, nuevas indicaciones, poblaciones especiales | Uso real (RWE) | Miles-millones | Continuo |

**Diseños innovadores**:
- **Adaptativos** (I-SPY 2, BATTLE, FOCUS4): modificación pre-especificada (brazo, tamaño muestra, población) basado datos interinos.
- **Master protocols**: *Basket* (una mutación, múltiples tumores), *Umbrella* (un tumor, múltiples mutaciones), *Platform* (múltiples brazos vs control compartido).
- **Seamless Phase II/III**: transición sin pausa basado criterios futilidad/eficacia.
- **Ensayos pragmáticos / RWE**: criterios amplios, práctica habitual, desenlaces centrados paciente (PRECIS-2).

### Endpoints (ICH E9/E9(R1))
- **Primario**: variable principal eficacia (ej. OS, PFS, DFS, ORR, HbA1c, FEV1, PASI, ACR20).
- **Secundarios**: apoyo, seguridad, calidad vida (PROs), biomarcadores.
- **Compuestos**: tiempo a primer evento (MACE, muerte CV + hosp ICC + ACV).
- **Subrogados** (surrogates): validados (ej. HbA1c → complicaciones microvasculares; carga viral VIH → SIDA/muerte; LDL-C → eventos CV).

### Estadística regulatoria
- **Multiplicidad**: control error tipo I familiar (gatekeeping, Holm, Hochberg, Hommel, fallback, testing strategy pre-especificada).
- **Interim analyses**: límites O'Brien-Fleming, Pocock, Lan-DeMets (alpha spending); DSMC independiente.
- **Poblaciones análisis**: ITT (intent-to-treat), mITT, PP (per-protocol), safety; *estimands* framework (ICH E9(R1)): efecto tratamiento bajo estrategias intercurrentes (hipotéticas, tratamiento, compuesta, mientras en tratamiento).

## Farmacovigilancia y seguridad post-comercialización

**Sistema global**: OMS Programme for International Drug Monitoring (VigiBase, >30M ICSRs), centros nacionales (FAERS/FDA, EudraVigilance/EMA, PMDA/Japón, COFEPRIS/México, ANVISA/Brasil, Health Canada).

**Fuentes señal**:
- **Espontáneas** (ICSRs): notificación voluntaria proveedores/pacientes/literatura.
- **Activas**: estudios cohorte, registros, bases datos administrativas (claims, EHR).
- **Literatura / redes sociales / mining**.

**Evaluación señal**: disproportionalidad (PRR, ROR, IC, EBGM), análisis casos Serie, evaluación causalidad (Bradford Hill, OMS-UMC), *signal triage* → *signal validation* → *signal confirmation* → acción regulatoria.

**Acciones regulatorias**: actualización ficha técnica (SmPC/label), comunicación seguridad (DHPC, Dear HCP letter), restricción uso, suspensión/retirada (ej. rofecoxib, valdecoxib, troglitazona, cerivastatina, lumiracoxib).

**Planes gestión riesgo (RMP)**: EU-RMP (EMA), REMS (FDA), PBRER/PSUR periódicos (ICH E2C/E2E).

## Farmacogenómica y medicina de precisión

**Guías implementadas**: CPIC (Clinical Pharmacogenetics Implementation Consortium), DPWG (Dutch Pharmacogenetics Working Group), CPNDS (Canadian Pharmacogenomics Network for Drug Safety).

| Gen | Fármaco | Acción clínica |
|-----|---------|----------------|
| **CYP2C19** | Clopidogrel | *2/*3 LOF → alternativa (prasugrel, ticagrelor) |
| **TPMT/NUDT15** | Tiopurinas (azatioprina, 6-MP) | *TPMT* *3A/*3C o *NUDT15* *3 → reducir dosis 90-95% |
| **DPYD** | 5-FU / capecitabina | *2A, *13, D949V, rs67376798 → reducir dosis / evitar |
| **HLA-B*57:01** | Abacavir | Screening pre-tratamiento obligatorio (FDA/EMA) |
| **HLA-B*15:02** | Carbamazepina | Screening ascendencia asiática (SJS/TEN riesgo) |
| **CYP2C9/VKORC1** | Warfarina | Dosis guiada genotipo (opcional, guías CPIC) |
| **UGT1A1*28** | Irinotecán | Homocigoto *28 → reducir dosis inicial |

**Paneles pre-emptivos**: 12-50 genes; integración CDS en EHR (Epic, Cerner) → alerta punto atención.

## Terapias avanzadas y nuevas modalidades

| Modalidad | Mecanismo | Ejemplos aprobados | Retos |
|-----------|-----------|-------------------|-------|
| **Anticuerpos monoclonales (mAbs)** | Bloqueo ligandos/receptores, ADCC/CDC, bispecificos (BiTE, TCE), ADC | Keytruda, Opdivo, Herceptin, Darzalex, Hemlibra, Enhertu, Kadcyla | Inmunogenicidad, coste, resistencia |
| **Terapia génica (AAV/lentiviral)** | Reemplazo genético *in vivo* (ojo, hígado, SNC) / *ex vivo* (HSC) | Luxturna (RPE65), Zolgensma (SMN1), Hemgenix/Roctavian (F9/F8), Strimvelis (ADA-SCID), Zynteglo (β-talasemia), Skysona (CALD), Casgevy (CRISPR BCL11A) | Inmunogenicidad AAV, integración insertacional, manufactura, coste ($2-3.5M) |
| **Edición genética (CRISPR)** | Knockout/knockin preciso *ex vivo* (HSC) / *in vivo* (hígado, ojo) | Casgevy (exa-cel, CRISPR-Cas9 *BCL11A* enhancer eritroides) β-talasemia/SCD | Off-targets, p53, inmunogenicidad Cas9, entrega |
| **ARN terapéutico** | ASO (nusinersen, inotersen), siRNA (patisiran, givosiran, lumasiran, inclisiran), mRNA (vacunas COVID), aptámeros | Spinraza (SMA), Onpattro (hATTR), Oxlumo (PH1), Leqvio (PCSK9), Comirnaty/Spikevax | Entrega (LNP, GalNAc), estabilidad, inmunogenicidad |
| **Terapia celular (CAR-T/NK, TCR-T, TIL)** | Ingeniería células inmunes anti-tumoral | Kymriah, Yescarta, Tecartus, Breyanzi, Carvykti (CAR-T CD19/BCMA); lifileucel (TIL melanoma) | CRS/ICANS, manufactura personalizada, coste, tumores sólidos |
| **PROTACs / degradadores moleculares** | Reclutamiento E3 ligasa → ubiquitinación → proteasoma | Enzalutamida-AR PROTAC (ARV-110), BTK degradador (NX-2127), ER degradador (ARV-471) | Selectividad, hook effect, permeabilidad, resistencia |

## Cross-refs

- [[dominio/biotecnologia]] — terapia génica, edición, biofármacos, CRISPR
- [[dominio/epidemiologia]] — MR, GWAS, colocalización, PRS, farmacogenómica
- [[dominio/genetica]] — farmacogenómica, CPIC, DPWG, PGx clínica
- [[dominio/bioinformatica]] — pipelines WGS/WES, anotación, interpretación variantes
- [[dominio/etica-de-datos]] / [[dominio/etica-ia]] — privacidad, consentimiento, sesgo algorítmico, equidad
- [[dominio/medicina-regenerativa]] — terapia celular, iPSCs, edición *ex vivo*
- [[dominio/derecho-farmacologico]] / [[dominio/derecho-de-la-inteligencia-artificial]] — regulación terapia génica, IA genómica
- [[rol/head-of-rd]] — pipeline I+D genómica, go/no-go, traslacional
- [[rol/head-of-medical-affairs]] — evidencia médica genómica, KOLs, MSLs
- [[rol/head-of-clinical-data-management]] — datos genómicos ensayos, EDC, calidad, estandarización (GA4GH)
- [[rol/head-of-regulatory-affairs]] — aprobaciones FDA/EMA/COFEPRIS, CMC terapia génica, *companion diagnostics*
- [[rol/head-of-clinical-operations]] — ensayos terapia génica/celular, logística cadena frío, manufactura
- [[sustrato/estados-unidos/ciencia-de-datos]] — data.gov, NIH Genomic Data Sharing, All of Us
- [[sustrato/mexico/ciencia-e-innovacion]] — CONAHCYT, medicina genómica México, biobancos