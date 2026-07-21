---
titulo: "Genética"
capa: "dominio"
tema: "genetica"
fuente: "https://en.wikipedia.org/wiki/Genetics"
fuente2: "https://www.nature.com/subjects/genetics"
fecha: "2026-07-21"
confianza: "alta"
tags: ["genética", "herencia", "genomas", "edición-genética", "CRISPR", "genética-molecular", "genética-poblacional", "medicina-genómica"]
profundidad: 3
estado: "profundo"
rol: ["head-of-rd", "head-of-medical-affairs", "head-of-clinical-data-management", "head-of-regulatory-affairs"]
actividades: ["investigación-genética", "medicina-genómica", "edición-genética", "farmacogenómica", "consejo-genético"]
organizaciones: ["nih", "nhgri", "ega", "gnomad", "clinvar", "omim", "hgvs", "ga4gh"]
responsabilidades: ["descubrimiento-diátas", "medicina-precisión", "terapia-génica", "cribado-poblacional", "ética-genómica"]
tareas: ["secuenciación", "análisis-variantes", "interpretación-clínica", "consejo-genético", "política-genómica"]
---

# Genética: herencia, genomas, edición genética (CRISPR), genética molecular/poblacional, medicina genómica

## Definición y alcance

**Genética** = rama de la biología que estudia la **herencia** (transmisión de caracteres entre generaciones), la **variación genética** y la **función de los genes** en individuos y poblaciones.

**Niveles de organización**:
- **Genética molecular**: estructura/replicación/reparación/expresión del ADN, ARN, proteínas; regulación génica, epigenética.
- **Genética clásica / mendeliana**: leyes herencia (segregación, assortment independiente), dominancia, epistasia, ligamiento, mapeo genético.
- **Genética poblacional**: frecuencias alélicas/genotípicas, deriva, flujo génico, selección natural, equilibrio Hardy-Weinberg, estructura poblacional.
- **Genética cuantitativa**: arquitectura base genética rasgos complejos (heredabilidad, QTL/GWAS, score poligénico).
- **Genómica**: análisis a escala genoma (secuenciación, ensamblaje, anotación, comparativa, funcional, translacional).
- **Genética clínica / medicina genómica**: diagnóstico, consejo, cribado, terapia génica/celular, farmacogenómica.

## Herencia mendeliana y extensiones

| Patrón | Ejemplos | Características clave |
|--------|----------|----------------------|
| **Autosómico dominante** | Neurofibromatosis tipo 1, Huntington, FH (LDLR) | Penetrancia variable, expressividad, *de novo* frecuente |
| **Autosómico recesivo** | Fibrosis quística (CFTR), anemia falciforme (HBB), PKU (PAH) | Portadores asintomáticos, consanguinidad aumenta riesgo |
| **Ligado a X recesivo** | Hemofilia A/B, Duchenne, daltonismo | Machos afectados, hembras portadoras (X-inactivación sesgada) |
| **Ligado a X dominante** | Hipofosfatemia X-ligada, Rett (MECP2) | Letalidad masculina frecuente (ej. Rett) |
| **Mitocondrial** | LHON, MELAS, MERRF | Herencia materna, heteroplasmia, umbral patogénico |

**Extensiones no-mendelianas**:
- **Penetrancia incompleta** / **expressividad variable** (modificadores genéticos/ambientales).
- **Anticipación** (expansión repeticiones: Huntington, DM1, FRDA, C9orf72 ALS/FTD).
- **Imprinting genómico** (Prader-Willi vs Angelman 15q11-q13; Silver-Russell 11p15; Beckwith-Wiedemann).
- **Mosaicismo** (gonadal/somático), **uniparental disomy (UPD)**, **deleciones/duplicaciones** (CNV patogénicos).
- **Herencia digenica/oligogénica** (ej. retinitis pigmentosa, sordera).

## Genómica humana: arquitectura y variación

**Genoma de referencia**: GRCh38 (hg38) / T2T-CHM13 (telómero-a-telómero, 2022) — ~3.1 Gb, ~19-20k genes codificantes, >200k elementos reguladores (ENCODE, Roadmap).

**Tipos variación**:
| Tipo | Rango tamaño | Frecuencia | Ejemplo patogénico |
|------|-------------|------------|-------------------|
| **SNV/indels** | 1-50 bp | ~4-5M/individuo | *BRCA1* c.68_69delAG (fundador ashkenazi) |
| **CNV** (deleción/duplicación) | 1 kb - varios Mb | ~1-2% genoma variable | *SMN1* deleción (AME), 16p11.2 (autismo/SCZ), 22q11.2 (DiGeorge) |
| **SV estructurales** (inversión, translocación, inserción) | >50 bp | ~20k/individuo | *BCR-ABL1* t(9;22) LMC; *PML-RARA* t(15;17) APL |
| **Repeticiones en tándem** (STR, VNTR) | 2-100+ unidades | Polimórficas | *HTT* CAG (Huntington), *DMPK* CTG (DM1), *C9orf72* GGGGCC (ALS/FTD) |
| **Variación móvil** (LINEs, SINEs, SVA, HERV) | 300-6 kb | ~50% genoma | Inserción *de novo* causante enfermedad (ej. hemofilia *F8* L1) |

**Bases de datos variación**:
- **gnomAD v4** (>730k exomas + 76k genomas) — frecuencias poblacionales, constraint (pLI, LOEUF, missense z).
- **ClinVar** — variantes con significado clínico (P/LP/VUS/LB/B); submitters (labs, clínicas, investigadores).
- **ClinGen** — curación experta genes/enfermedades, *dosage sensitivity*, *clinical validity*.
- **dbSNP** — catálogo general (rsIDs).
- **gnomAD-SV / dbVar / DGV** — variantes estructurales.
- **LOVD / HGMD** — genes/enfermedades específicos (curación clínica).
- **Genome Aggregation Database (gnomAD) constraint metrics** — predicción intolérancia LOF/missense.

## Tecnologías de secuenciación y análisis

| Plataforma | Lectura | Precisión | Rendimiento | Usos principales |
|------------|---------|-----------|-------------|------------------|
| **Illumina (NovaSeq X, NextSeq 2000)** | Corta (150-300 bp) | >Q30 (99.9%) | 16 Tb/run | WGS, WES, RNA-seq, paneles, NIPT, PGT-A |
| **PacBio HiFi (Revio, Sequel IIe)** | Larga alta fidelidad (15-25 kb, Q20-30) | >Q20 (99%) | 360 Gb/run | *De novo* assembly, SVs, *phasing*, HLA, metagenómica |
| **Oxford Nanopore (PromethION 48, P2 Solo)** | Ultra-larga (>100 kb, hasta Mb) | Q10-15 (raw), Q20+ (duplex) | 5-15 Tb/run | SVs complejos, metilación nativa (5mC, 6mA), *direct RNA*, epigenética |
| **10x Genomics / MGI / Element / Ultima** | Variadas | - | - | Single-cell, espacial, linked-reads, bajo coste |

**Análisis bioinformático estándar (WGS/WES)**:
1. **QC** (FastQC, MultiQC) → 2. **Alineamiento** (BWA-MEM2, minimap2) → 3. **Procesamiento** (MarkDuplicates, BQSR GATK) → 4. **Variant calling** (GATK HaplotypeCaller/DeepVariant, Strelka2, Mutect2 somático; Manta/Delly/SVIM SVs) → 5. **Filtrado/VQSR** → 6. **Anotación** (VEP, ANNOVAR, SnpEff; CADD, REVEL, AlphaMissense, SpliceAI, ClinVar, gnomAD) → 7. **Priorización** (fenotipo HPO, modo herencia, constraint, segregación) → 8. **Interpretación/clasificación** (ACMG/AMP 2015 + actualizaciones ClinGen/SVI).

## Edición genética: CRISPR y más allá

| Sistema | Mecanismo | Aplicaciones | Limitaciones |
|---------|-----------|--------------|--------------|
| **CRISPR-Cas9** (SpCas9, SaCas9, Cas9-NG, xCas9, SpRY) | DSB guiada por gRNA (20 nt + PAM NGG/NAG/NNG) | KO, KI (HDR/ssODN), activación/represión (CRISPRa/i), screening (KO/CRISPRi/a), edición base (BE), *prime editing* | Off-targets, efectos p53, inmunogenicidad Cas9, entrega, HDR baja eficiencia |
| **Base Editors (BE)** (CBE: APOBEC-nCas9; ABE: TadA*-nCas9) | Desaminación C→T / A→G sin DSB | Corrección puntual (ej. *HBB* E6V, *PCSK9*, *LDLR*), creación modelos | Ventana edición (4-8 nt), ediciones *bystander*, edición ARN (ABE), inmunogenicidad |
| **Prime Editing (PE)** (PE1-7, PEmax, PE6) | PegRNA + RT-nCas9 → edición precisa (todas transiciones/transversiones, indels ≤100 bp) | Corrección mutaciones patogénicas precisas, inserción etiquetas, *tagging* endógeno | Eficiencia variable, longitud pegRNA, entrega (AAV límite ~4.7 kb) |
| **CRISPR-Cas12/Cas13** | Cas12 (DNA), Cas13 (RNA) — colateral cleavage | Diagnóstico (SHERLOCK, DETECTR), edición RNA, *knockdown* transitorio | Menos desarrollado terapéutico |
| **Epigenome editing** (dCas9-DNMT3A/TET1, KRAB, p300, SunTag) | Metilación/demetilación, activación/represión sin cambio secuencia | Reprogramación epigenética, modelos enfermedad, terapia (ej. *FMR1* FXS) | Reversibilidad, especificidad, persistencia |
| **Entrega terapéutica** | AAV (dual/triple split), LNP (mRNA/gRNA/RNP), VLP, exosomas, HSC *ex vivo* electroporadas | *In vivo* (hígado, ojo, SNC, músculo), *ex vivo* (HSC, T-cells, iPSCs) | Inmunogenicidad, capacidad carga, tropismo, fabricación, coste |

**Terapias aprobadas/en fase avanzada**:
- **Casgevy (exa-cel, CRISPR-Cas9 *BCL11A* erythroid enhancer)** — β-talasemia / anemia falciforme (aprobado UK/US/EU 2023-24, *ex vivo* HSC).
- **Lyfgenia (lovo-cel, lentiviral *HBB* T87Q)** — anemia falciforme (FDA 2023).
- **Casgevy + Lyfgenia** primeros *gene editing* / *gene therapy* aprobados para hemoglobinopatías.
- **En pipeline**: *PCSK9* (Verve-101, base editing *in vivo* hígado), *CEP290* (EDIT-101, *in vivo* retina), *HBB* (BEAM-101, base editing HSC), *TRAC* CAR-T (CRISPR), *TTR* (NTLA-2001, CRISPR *in vivo* hígado).

## Genética de poblaciones y evolución

**Fuerzas evolutivas**:
- **Mutación**: fuente última variación (μ ~1.2×10⁻⁸/bp/gen; *de novo* ~70/individuo).
- **Deriva genética**: fluctuación aleatoria frecuencias (efecto fundador, cuello botella); *Nₑ* tamaño efectivo población.
- **Selección natural**: positiva (selective sweeps — *LCT* lactasa, *EPAS1* altitud, *HBB* malaria), purificadora (constraint), balanceada (heterocigoto ventajoso: *HBB* falciforme, *G6PD* malaria).
- **Flujo génico / migración**: admixtura (ej. latinoamericanos: europeo + amerindio + africano), *introgression* arcaica (Neandertal ~1-2% eurasiáticos, Denisova Oceanía/Asia).

**Estructura poblacional**: PCA, ADMIXTURE, fineSTRUCTURE, IBD sharing; corrección estratificación en GWAS (PCs, mixed models REGENIE, BOLT-LMM, SAIGE).

**GWAS + fine-mapping + colocalización + TWAS/PWAS + MR** → genes causales, mecanismos, dianas terapéuticas.

## Medicina genómica: aplicaciones clínicas

| Área | Estado actual | Ejemplos |
|------|---------------|----------|
| **Diagnóstico enfermedades raras** | WES/WGS primera línea (rendimiento 25-50%); trio bevorzugt | *Exome sequencing* neonatos UCI (rWGS 48-72h), paneles fenotípicos (HPO) |
| **Cribado poblacional** | Recién nacido (heel prick: ~50 condiciones core RUSP US; expansión WGS piloto), portadores (pan-étnico >500 genes), cáncer hereditario (BRCA1/2, Lynch, paneles multi-gene) | gnomAD constraint guía selección genes; VUS re-clasificación continua |
| **Oncología de precisión** | Perfilado tumoral (WES/RNA-seq/paneles 300-500 genes), *biomarcadores* acciónables (NTRK, RET, KRAS G12C, EGFR, ALK, ROS1, BRAF, MSI-H/dMMR, TMB-H) | NCCN/ESMO/AMP/CAP guidelines; FDA *companion diagnostics* (CDx), *tumor-agnostic* approvals (larotrectinib, entrectinib, pembrolizumab MSI-H, dostarlimab dMMR) |
| **Farmacogenómica** | Guías CPIC/DPWG implementadas (ver tabla arriba); paneles pre-emptivos 12-50 genes; CDS en EHR | *CYP2C19*-clopidogrel, *TPMT/NUDT15*-tiopurinas, *DPYD*-5FU, *HLA-B*57:01-abacavir |
| **Terapia génica / celular** | AAV *in vivo* (ojo: Luxturna *RPE65*, hemofilia B *F9* Hemgenix/Roctavian; SNC: Elevidys *DMD* micro-distrofina), lentiviral *ex vivo* HSC (Strimvelis ADA-SCID, Zynteglo β-talasemia, Skysona CALD, Casgevy), CAR-T (Kymriah, Yescarta, Tecartus, Breyanzi, Carvykti) | Manufactura, coste ($2-3.5M), acceso equitativo, seguimiento 15 años (FDA) |
| **Edición genética terapéutica** | CRISPR-Cas9 *ex vivo* HSC (Casgevy), *in vivo* hígado/ojo en ensayos | *Off-target* monitoring (GUIDE-seq, CIRCLE-seq, DISCOVER-Seq, DISCOVERY-seq, long-read sequencing) |
| **Consejo genético** | Pre/post-test, consentimiento informado, comunicación riesgo, apoyo psicosocial, cascada familiar | NSGC/ABGC certificación; telesalud post-COVID |

## Ética, legal y social (ELSI)

- **Privacidad genética**: GINA (US 2008), GDPR Art. 9 (UE), Ley 14/2007 (España), Ley General de Salud (México Art. 138-140), Bill S-201 (Canadá 2017) — no discriminación empleo/seguro.
- **Consentimiento**: amplio vs específico vs dinámico; *broad consent* biobancos; *dynamic consent* plataformas digitales.
- **Revelación hallazgos incidentales/secundarios** (ACMG SF v3.1: 73 genes accionables — *BRCA1/2, LDLR, MYH7, RYR1/2, TP53*, etc.); derecho a no saber.
- **Edición germinal**: moratoria internacional (OMS 2019-2021, Declaración Hong Kong 2019, OMS 2021 *governance framework*); distinción terapéutica vs mejora.
- **Equidad genómica**: subrepresentación poblaciones no europeas en GWAS/biobancos (∼80% europeos); iniciativas H3Africa, All of Us, Mexico Biobank, Biobank Japan, China Kadoorie, FinnGen, Qatar Genome, Singapore PRECISE.
- **Propiedad / beneficio compartido**: Convenio Diversidad Biológica (CDB), Protocolo Nagoya (acceso recursos genéticos + conocimientos tradicionales); datos genómicos humanos — *benefit sharing* debatido.
- **Puntuación poligénica (PRS) en cribado/selección**: *polygenic embryo screening* (PGT-P) — debate ético (selección no médica, desigualdad, validez predictiva limitada en ancestría diversa).

## Cross-refs

- [[dominio/biotecnologia]] — terapia génica, edición, biofármacos, CRISPR
- [[dominio/epidemiologia]] — MR, GWAS, colocalización, PRS, farmacogenómica
- [[dominio/farmacologia]] — farmacogenómica, CPIC, DPWG, PGx clínica
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