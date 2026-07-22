---
titulo: "Head of AI Governance"
capa: "rol"
tema: "head-of-ai-governance"
fuente: "https://en.wikipedia.org/wiki/Regulation_of_artificial_intelligence"
fecha: "2026-07-22"
confianza: "alta"
tags: ["ai-governance", "ai-risk-management", "eu-ai-act", "nist-rmf", "model-governance", "responsible-ai", "compliance"]
profundidad: 2
estado: "profundo"
---

# Head of AI Governance

## Definición

El **Head of AI Governance** (a veces titulado *Director of AI Governance*, *Responsible AI Lead*, *AI Risk Officer* o *Chief AI Ethics Officer* en organizaciones menores) es el líder responsable de **establecer, operacionalizar y hacer cumplir el marco de gobierno de la inteligencia artificial** en la organización. Su mandato: **asegurar que los sistemas de IA se desarrollen, desplieguen y monitoren de forma segura, ética, legal y alineada con los objetivos de negocio**.

> **AI Governance** = *Model Risk Management (MRM)* + *Responsible AI / Ethics* + *Regulatory Compliance* + *Data Governance* + *Security/Privacy* — aplicado al ciclo de vida completo de modelos de IA/ML (L0: reglas → L1: ML clásico → L2: DL → L3: GenAI/LLMs → L4: Agentes).

## Mandato y alcance

| Pilar | Responsabilidad del Head of AI Governance |
|-------|-------------------------------------------|
| **Marco de gobierno (Framework)** | Definir *AI Policy* corporativa, *principles* (fairness, transparency, accountability, privacy, security, robustness), *risk taxonomy*, *risk appetite*, *roles & responsibilities (RACI)* |
| **Ciclo de vida del modelo (MLOps + Governance)** | *Model Inventory/Registry* (catálogo único), *Model Cards / System Cards*, *Data Sheets*, *Risk Tiering* (prohibited/high/limited/minimal per EU AI Act), *Approval Gates* (dev→staging→prod), *Decommissioning* |
| **Risk Management** | *Identification* (bias, drift, hallucination, PII leakage, IP infringement, security, misuse), *Assessment* (cuantitativa/cualitativa), *Mitigation* (guardrails, human-in-the-loop, monitoring), *Monitoring* (continuo, alertas, *model observability*) |
| **Regulatory Compliance** | **EU AI Act** (phased 2025-2027), **NIST AI RMF 1.0**, **ISO/IEC 42001** (AI Management System), **SR 11-7 / OCC 2011-12** (banca EE.UU.), **Canada C-27/AIDA**, **China Generative AI Measures**, **Brasil PL 2338**, **Sectoriales** (FDA SaMD, MDR, FAA, NERC CIP) |
| **Ética y Responsible AI** | *AI Ethics Board/Committee* (preside/secretaría), *Impact Assessments* (DPIA + Algorithmic Impact Assessment), *Red Teaming*, *Bias Audits*, *Explainability/XAI* requirements, *Human Rights Due Diligence* (UNGPs) |
| **Data Governance para IA** | *Training data provenance*, *licensing/IP clearance*, *consent/privacy* (GDPR/CCPA), *data quality/lineage*, *synthetic data policies*, *RAG/knowledge base governance* |
| **Seguridad y Privacidad (AI Security)** | *Adversarial robustness*, *prompt injection defense*, *data extraction prevention*, *model theft/extraction*, *supply chain security* (SBOM para modelos, *model signing*), *red teaming* continuo |
| **Auditoría y Aseguramiento** | *Internal Audit* coordination, *Third-party audits* (ISO 42001, *algorithmic auditors*), *Regulatory examinations*, *Audit trails* inmutables (WORM logs, *model cards* versionados) |
| **Cultura y Capacitación** | *AI Literacy* obligatoria (EU AI Act Art. 4), *Responsible AI training* por rol (devs, PMs, legal, compliance, execs), *Champions network*, *Incident reporting culture* (blameless) |

## Estructura de gobierno típica (Three Lines of Defense adaptado a IA)

```
┌─────────────────────────────────────────────────────────────────┐
│                    AI ETHICS BOARD / COMMITTEE                  │
│  (C-suite, Legal, Compliance, Risk, CISO, CPO, External Experts)│
└──────────────────────────┬──────────────────────────────────────┘
                           │ Oversight, Policy Approval, Escalations
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│                  HEAD OF AI GOVERNANCE (1st/2nd Line)           │
│  AI Governance Office: Model Risk, Responsible AI, Compliance,  │
│  Security, Data Governance, Audit Coordination, Training        │
└──────────────────────────┬──────────────────────────────────────┘
                           │ Standards, Tooling, Review Gates
           ┌───────────────┼───────────────┐
           ▼               ▼               ▼
    ┌────────────┐  ┌────────────┐  ┌────────────┐
    │  DEV TEAMS │  │  MLOps /   │  │  BUSINESS  │
    │  (1st Line)│  │  Platform  │  │  OWNERS    │
    │            │  │  (1st Line)│  │  (1st Line)│
    │ Build,     │  │ Pipeline,  │  │ Define use │
    │ document,  │  │ Registry,  │  │ case, own  │
    │ test       │  │ Monitoring │  │ outcome    │
    └────────────┘  └────────────┘  └────────────┘
           ▲               ▲               ▲
           │               │               │
           └───────────────┴───────────────┘
                    Internal Audit (3rd Line) — Independent Assurance
```

## Matriz de *Risk Tiering* (ejemplo alineado EU AI Act + NIST)

| Tier | Definición | Ejemplos | Controles obligatorios |
|------|------------|----------|------------------------|
| **Prohibido** | Inaceptable riesgo | *Social scoring*, *manipulación subliminal*, *explotación vulnerables*, *biometric ID tiempo real espacio público* (excepciones) | **Ban** — no desarrollar/desplegar |
| **Alto (High)** | Riesgo significativo salud/seguridad/derechos fundamentales | *Medical devices (SaMD)*, *credit scoring*, *hiring/HR*, *education*, *critical infra*, *law enforcement*, *biometric ID*, *GenAI sistemas de propósito general (GPAI) con impacto sistémico* | *Conformity assessment* (QMS, technical documentation, data governance, transparency, human oversight, accuracy/robustness/cybersecurity, post-market monitoring), *CE marking*, *Notified Body* (si Anexo III) |
| **Limitado** | Transparencia requerida | *Chatbots*, *deepfakes*, *emotion recognition*, *biometric categorization*, *AI-generated content* | *Transparency obligations* (informar usuarios, *watermarking* contenido sintético) |
| **Mínimo** | Riesgo bajo/despreciable | *Spam filters*, *recommenders internos*, *predictive maintenance*, *code assistants* (bajo umbral) | *Voluntary codes of conduct*, *best practices* (NIST AI RMF, ISO 42001) |

> **Nota**: *General Purpose AI (GPAI)* — modelos fundacionales (LLMs, multimodales) — tienen régimen propio: *systemic risk* (>10^25 FLOPs) ⇒ *model evaluations, adversarial testing, incident reporting, cybersecurity, energy efficiency*.

## Herramientas y *Tech Stack* de AI Governance 2025

| Categoría | Herramientas representativas | Función clave |
|-----------|------------------------------|---------------|
| **Model Registry / Catalog** | MLflow, Weights & Biases, Neptune, Vertex AI Model Registry, Azure ML Model Catalog, Databricks Model Registry, **Credo AI**, **ModelOp**, **Monitaur**, **Holistic AI** | *Single source of truth*, *model cards*, *lineage*, *approval workflows* |
| **AI Risk / Compliance Platform** | **Credo AI**, **ModelOp**, **Monitaur**, **Holistic AI**, **Fairly AI**, **Datatron**, **Arthur AI**, **Fiddler**, **WhyLabs**, **Robust Intelligence** | *Risk tiering*, *policy-as-code*, *automated assessments*, *evidence collection*, *audit trails* |
| **Model Observability / Monitoring** | **WhyLabs**, **Fiddler**, **Arize**, **Evidently** (open source), **Gantry**, **Galileo**, **TruEra**, **Datadog/ML**, **Prometheus/Grafana + custom** | *Drift detection* (data/concept/prediction), *performance degradation*, *bias/fairness metrics*, *data quality*, *latency/availability* |
| **GenAI / LLM Specific** | **Guardrails AI**, **NeMo Guardrails** (NVIDIA), **Llama Guard** (Meta), **PromptFoo**, **LangSmith** (eval), **Ragas** (RAG eval), **Phoenix** (Arize), **TruLens**, **MLflow LLM Eval**, **OpenAI Evals** | *Prompt injection defense*, *PII redaction*, *hallucination detection*, *groundedness/faithfulness*, *RAG quality*, *token cost/latency* |
| **Red Teaming / Adversarial Testing** | **Garak**, **PromptFoo**, **Counterfit** (Microsoft), **Adversarial Robustness Toolbox (ART)**, **Robust Intelligence**, **HiddenLayer**, **Lakera**, **Protect AI** | *Automated red teaming*, *jailbreak testing*, *data extraction*, *backdoor detection* |
| **Data Governance / Lineage** | **Atlan**, **Alation**, **Collibra**, **DataHub** (Acryl), **Amundsen**, **dbt** (contracts), **Monte Carlo** (observability) | *Training data provenance*, *license compliance*, *PII tagging*, *consent lineage* |
| **SBOM / Supply Chain** | **SPDX**, **CycloneDX**, **Syft/Grype** (Anchore), **Chainguard**, **SLSA**, **Sigstore** (cosign), **SBOM for ML** (ML-BOM) | *Model composition*, *dependency vulnerabilities*, *provenance*, *signing/verification* |
| **Audit / Evidence Management** | **AuditBoard**, **Workiva**, **Vanta**, **Drata**, **Hyperproof**, **Credo AI** (audit module) | *Evidence collection*, *control mapping*, *regulatory mapping*, *auditor portal* |

## KPIs del Head of AI Governance

| Categoría | KPIs |
|-----------|------|
| **Cobertura** | % modelos en registry, % modelos con *model card*, % modelos *tiered*, % *high-risk* con *conformity assessment* |
| **Riesgo** | # incidentes IA/año (severidad), *MTTD/MTTR* incidentes IA, % modelos con *monitoring activo*, # *drift alerts* resueltas SLA |
| **Cumplimiento** | % *high-risk* con *assessment* completado, *audit findings* (critical/high/medium/low), *regulatory inquiries* resueltas a tiempo, *AI Act readiness score* |
| **Ética/Calidad** | *Bias audit* pass rate, *fairness metrics* (demographic parity, equalized odds) en producción, *explainability score* (SHAP/LIME coverage), *human oversight* adherence |
| **Seguridad** | *Red teaming* coverage, *vulnerability remediation* SLA, *penetration test* findings, *supply chain* vulnerabilities (CVEs en dependencies) |
| **Cultura** | % empleados completaron *AI Literacy training*, *responsible AI champions* activos, *incident reporting rate* (psychological safety), *AI Ethics Board* meetings/año |
| **Eficiencia** | *Time-to-approval* (dev→prod), *governance overhead* (% capacidad ingeniería), *tooling cost* vs. *risk reduction* |

## Retos críticos 2025-2027

| Reto | Por qué es crítico | Enfoque Head of AI Governance |
|------|-------------------|-------------------------------|
| **EU AI Act entry into force** (fases 2025-2027) | Multas hasta 7% facturación global / 35M€; *high-risk* = *conformity assessment* obligatorio | *Gap analysis* ya, *QMS* (ISO 42001), *technical documentation* automation, *notified body* engagement temprano |
| **GenAI / LLMs en producción** (RAG, agentes, *tool use*) | *Hallucination*, *PII leakage*, *prompt injection*, *unbounded autonomy*, *cost/latency* | *Guardrails* obligatorios, *eval frameworks* (Ragas, TruLens), *human-in-the-loop* por defecto, *budget guards* |
| **Regulatory fragmentation global** (EE.UU. *state-level* + *federal* + sectorial + EU + China + Canadá + Brasil + UK + ...) | *Compliance multiplicity*, *conflicting requirements* | *Harmonized framework* (NIST AI RMF como *lingua franca*), *modular policy packs* por jurisdicción, *regulatory intelligence* |
| **Terceros / *Vendor AI* (SaaS con IA embebida)** | *Shadow AI*, *data leakage*, *contractual liability* | *Vendor AI assessment questionnaire*, *DPA/DPAs específicos IA*, *right to audit*, *model card request*, *contractual guardrails* |
| **Talento *Responsible AI* escaso** | *Cross-disciplinary* (ML + Law + Ethics + Risk + Security + Domain) | *Upskilling interno*, *AI Governance Fellowship*, *partnerships* (academia, *specialized consultancies*), *centralized CoE* |
| **Métricas de *fairness/explainability* en producción** | *Static* ≠ *dynamic*; *proxy labels*, *distribution shift* | *Continuous monitoring*, *automated bias dashboards*, *stakeholder feedback loops*, *explainability by design* (interpretable models donde posible) |

## Diferenciación vs. roles afines

| Rol | Foco | Overlap | Diferencia clave |
|-----|------|---------|------------------|
| **Chief AI Officer (CAIO)** | *Estrategia IA, adopción, roadmap, valor negocio* | Gobierno habilita estrategia | CAIO = *gas pedal*; Head AI Governance = *brakes + steering* |
| **Head of ML Engineering / MLOps** | *Entrega técnica, pipelines, infra, rendimiento* | *Model registry, monitoring* compartidos | MLOps = *how to build/run*; AI Governance = *whether/under what conditions to run* |
| **Chief Risk Officer (CRO) / Head of Model Risk (MRM)** | *Riesgo modelo financiero (SR 11-7)* | *Model risk framework* | MRM = *banca/tradicional*; AI Governance = *todo IA (GenAI, no-financiero, ética, regulación emergente)* |
| **Chief Data Officer (CDO) / Data Governance** | *Datos como activo, calidad, linaje, privacidad* | *Training data governance* | CDO = *data*; AI Governance = *modelo + sistema + uso + impacto* |
| **CISO / Head of AI Security** | *Seguridad modelo/datos/infra* | *Adversarial robustness, supply chain* | CISO = *CIA triad*; AI Governance = *CIA + Ethics + Compliance + Societal Impact* |
| **Legal / Regulatory Affairs** | *Interpretación ley, contratos, litigation* | *Compliance evidence* | Legal = *what the law says*; AI Governance = *how to operationalize daily* |

## Carrera típica

```
Senior ML Engineer / Data Scientist / Risk Analyst / Legal Counsel (Tech)
    │
    ▼
AI Governance Specialist / Responsible AI Analyst / Model Risk Analyst
    │
    ▼
Senior AI Governance Manager / Lead Responsible AI / Model Risk Lead
    │
    ▼
Head of AI Governance / Director Responsible AI / Chief Model Risk Officer
    │
    ▼
VP AI Governance / Chief AI Risk Officer / CAIO (track dual)
```

## Fuentes
- [Wikipedia — Regulation of artificial intelligence](https://en.wikipedia.org/wiki/Regulation_of_artificial_intelligence)
- **EU AI Act** (Reglamento UE 2024/1689) — texto oficial, *recitals*, *annexes*
- **NIST AI RMF 1.0** (Jan 2023) + *Playbook* + *Crosswalks* (ISO 42001, EU AI Act, OECD)
- **ISO/IEC 42001:2023** — *Artificial intelligence — Management system*
- **SR 11-7 / OCC 2011-12** — *Supervisory Guidance on Model Risk Management* (Federal Reserve / OCC)
- **FDA** — *Good Machine Learning Practice (GMLP)*, *SaMD*, *Predetermined Change Control Plans (PCCP)*
- **OECD AI Principles** (2019) + *AI Policy Observatory*
- **UNESCO Recommendation on Ethics of AI** (2021)
- **Partnership on AI** — *Synthetic Media Framework*, *Case Studies*
- **MLCommons** — *AI Safety Benchmarks*, *MedPerf*, *MLPerf*
- **Credo AI / ModelOp / Monitaur / Holistic AI / Fairly AI** — *Platform whitepapers*
- **WhyLabs / Fiddler / Arize / Evidently / Galileo / TruEra** — *Observability blogs*
- **Microsoft / Google / Meta / NVIDIA / Anthropic / OpenAI** — *Responsible AI / Safety reports*
- **AI Governance Forum** (World Economic Forum), **Global Partnership on AI (GPAI)**
- *Lenny's Newsletter* — *AI Governance* editions; *Responsible AI Weekly*