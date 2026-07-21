---
titulo: "Head of Sales Analytics"
capa: "rol"
tema: "head-of-sales-analytics"
fuente: "https://en.wikipedia.org/wiki/Sales_analytics"
fuente2: "https://www.gartner.com/en/sales/insights/sales-analytics"
fecha: "2026-07-21"
confianza: "alta"
tags: ["sales-analytics", "revenue-operations", "revops", "pipeline", "forecasting", "win-rate", "cohort-analysis"]
profundidad: 3
estado: "profundo"
rol: ["head-of-revenue-operations", "head-of-sales-operations", "vp-sales", "chief-revenue-officer"]
actividades: ["análisis-pipeline", "forecasting", "win-rate-analysis", "cohort-analysis", "sales-performance-dashboards", "territory-planning"]
organizaciones: ["salesforce", "hubspot", "outreach", "gong", "clari", "tableau", "powerbi", "looker"]
responsabilidades: ["motor-insights-ventas", "precisión-forecast", "optimización-pipeline", "compensación-ventas"]
tareas: ["modelado-predictivo", "attribution-modeling", "quota-setting", "territory-optimization", "sales-capacity-planning"]
---

# Head of Sales Analytics: analítica de ventas, pipeline, forecast, win-rate, cohortes, vs head-of-revenue-operations/analitica-de-ventas

## Definición y alcance

**Head of Sales Analytics** = líder de la función analítica dedicada a **ventas** (B2B/B2C), responsable de transformar datos comerciales en **insights accionables** para mejorar: precisión de forecast, eficiencia pipeline, productividad vendedores, diseño territorios, compensación y estrategia go-to-market.

**Diferenciación vs roles adyacentes**:
| Rol | Foco principal | Relación |
|-----|----------------|----------|
| **Head of Revenue Operations (RevOps)** | Operaciones end-to-end (ventas + marketing + CS), procesos, tech stack, datos unificados | Sales Analytics es *sub-función* o *partner* clave; RevOps owns *process/tech*, Sales Analytics owns *insights/modeling* |
| **Head of Sales Operations** | Ejecución operativa (CRM, quotas, territories, comp plans, onboarding, enablement) | Sales Ops *implementa* lo que Sales Analytics *recomienda* (ej. territory design, quota setting) |
| **Head of Sales Analytics** (este rol) | **Motor analítico**: modelos predictivos, pipeline intelligence, win/loss, cohort analysis, forecasting, pricing analytics, rep productivity | Genera *evidencia* para decisiones RevOps/Sales Ops/VP Sales/CRO |

**Reporting típico**: VP Sales, CRO, o Head of RevOps (según madurez org). En orgs maduras, reporta a **Head of RevOps** con *dotted line* a CRO/VP Sales.

## Pilares analíticos (Core Analytics Pillars)

### 1. Pipeline Intelligence & Forecasting
- **Pipeline health**: coverage ratio (3-4x), velocity (días etapa), aging, stuck deals, risk scoring.
- **Forecasting models**: *bottom-up* (rep commit + manager adjust) + *top-down* (statistical: ARIMA, Prophet, XGBoost/LightGBM con features: historical close rates, seasonality, pipeline composition, rep tenure, deal size, competitor, stage duration).
- **Forecast accuracy**: MAPE, WMAPE, bias (systematic over/under), *forecast vs actual* por rep/region/segment/producto/trimestre.
- **Predictive scoring**: *deal propensity to close* (logistic regression, gradient boosting) usando features: engagement (emails/calls/meetings), stakeholders, MEDDIC/MEDDPICC score, competitor, timing, firmographics.

### 2. Win/Loss & Competitive Intelligence
- **Win-rate analysis**: overall, por segmento (Enterprise/Mid-market/SMB), región, producto, rep, canal, competitor.
- **Loss reason taxonomy**: standardized (price, product gaps, competitor, timing, no decision, relationship) — *required field* en CRM etapa Closed-Lost.
- **Competitive win-rates**: head-to-head vs top 5-10 competidores; *battlecard* effectiveness tracking.
- **Win-loss interviews**: programa estructurado (tercero neutral o interno) → insights producto/precio/proceso.

### 3. Rep Productivity & Capacity Planning
- **Productivity metrics**: quota attainment (% reps @ 100%+), ramp time (months to full productivity), activities per deal (emails/calls/meetings/demos/POCs), sales cycle length (by segment/deal size).
- **Capacity model**: headcount plan → *quota capacity* (reps × quota) vs *revenue target* → gap analysis → hiring plan (accounting ramp, attrition ~15-20%/año).
- **Territory design**: account scoring (TAM/SAM/SOM, firmographics, technographics, intent data) → equitable distribution (workload index: #accounts × revenue potential × travel time) → *territory optimization* (genetic algorithms, linear programming).
- **Quota setting**: *top-down* (revenue target / #reps) + *bottom-up* (territory potential, historical attainment, market growth) → *quota fairness* (Gini coefficient attainment distribution).

### 4. Cohort & Retention Analysis (Post-sales)
- **Cohort retention**: logo retention (logos renovados / logos inicio período), GRR (Gross Revenue Retention), NRR (Net Revenue Retention = GRR + expansion).
- **Expansion analysis**: upsell/cross-sell rates, time-to-expansion, multi-product attachment, seat/usage growth.
- **Churn prediction**: survival analysis (Cox PH, Weibull), ML classification (XGBoost) features: usage/adoption (DAU/MAU, feature adoption), health score, NPS/CSAT, support tickets, contract terms, champion turnover.
- **LTV/CAC by cohort**: payback period, LTV:CAC ratio (>3x target), CAC payback (<12 meses).

### 5. Compensation & Incentive Analytics
- **Plan design modeling**: simulación Monte Carlo escenarios (quota, accelerators, decelerators, caps, SPIFs) → *cost of sales* (% revenue*), *earnings at risk* (variable/total), *attainment distribution* projected.
- **Accelerator effectiveness**: correlación accelerator rate vs over-attainment; *gaming* detection (deal pull-forward, sandbagging).
- **SPIF ROI**: incremental revenue / SPIF spend; atribución causal (DiD vs control group no elegible).
- **Equity/refresh grants**: vesting schedules, dilution modeling, retention impact (Cox model tenure vs grant size).

## Tech Stack & Data Architecture

| Capa | Herramientas típicas | Responsabilidad Sales Analytics |
|------|---------------------|----------------------------------|
| **CRM (System of Record)** | Salesforce, HubSpot, Dynamics 365, Pipedrive | Definición objetos/campos, validaciones, *field history tracking*, *field audit trail* |
| **Data Warehouse / Lake** | Snowflake, BigQuery, Redshift, Databricks, Azure Synapse | Modelado dimensional (star schema: fact_deals, dim_rep, dim_account, dim_date, dim_product), *dbt* transformations, tests |
| **ELT / Reverse ETL** | Fivetran, Airbyte, dbt, Hightouch, Census | *Reverse ETL* → CRM (account scores, propensity, health scores, next best action) |
| **BI / Visualization** | Tableau, Power BI, Looker, Mode, Sigma, ThoughtSpot | Dashboards executive (CRO/VP Sales), operational (Sales Ops/Managers), self-service (reps) |
| **Sales Engagement / Activity Capture** | Outreach, Salesloft, Apollo, Groove, Gong, Chorus, Clari, Ebsta | *Activity capture* automático (emails, calls, meetings, calendar) → enriquece pipeline data |
| **Forecasting / RevOps Platforms** | Clari, Gong Forecast, BoostUp, Aviso, Anaplan, Varicent, Xactly | *Forecast submission workflow*, *AI-driven risk alerts*, *deal inspection* |
| **Advanced Analytics / ML** | Python (pandas, scikit-learn, XGBoost, LightGBM, Prophet, statsmodels), R, Databricks MLflow, SageMaker, Vertex AI | *Feature store* (Feast), *model registry* (MLflow), *MLOps* (CI/CD, monitoring drift, retraining schedule) |
| **Intent / Third-party Data** | 6sense, Bombora, ZoomInfo, Clearbit, Apollo, HG Insights, G2 | *Account intent scoring*, *technographic fit*, *buying group identification* |

**Data quality & governance**: *data contracts* (Great Expectations, dbt tests), *SLAs* freshness (pipeline data <4h lag), *lineage* (dbt docs), *access control* (RBAC: rep sees own, manager sees team, exec sees all).

## Métricas clave (KPIs) — Dashboard Ejecutivo

| Categoría | Métrica | Target típico | Frecuencia |
|-----------|---------|---------------|------------|
| **Forecast** | Forecast Accuracy (MAPE) | <10% (Enterprise), <15% (SMB) | Semanal/Mensual |
| | Forecast Bias | -5% a +5% | Mensual |
| **Pipeline** | Pipeline Coverage Ratio | 3-4x (Enterprise), 4-5x (SMB) | Semanal |
| | Pipeline Velocity (€/día) | Trend ↑ | Semanal |
| | Stage Conversion Rates | Benchmark por etapa/segmento | Mensual |
| **Productivity** | Quota Attainment (% reps ≥100%) | >70% reps @ quota | Trimestral |
| | Ramp Time (meses a 100% quota) | 3-6 (Enterprise), 2-4 (SMB) | Por cohorte |
| | Sales Cycle Length (días) | Benchmark segmento | Mensual |
| **Win/Loss** | Win Rate (overall) | 20-30% (Enterprise), 30-40% (SMB) | Mensual |
| | Competitive Win Rate | >50% vs top 3 competidores | Trimestral |
| **Retention/Expansion** | GRR | >90% (Enterprise), >85% (SMB) | Trimestral |
| | NRR | >110% (best-in-class SaaS) | Trimestral |
| | Logo Churn | <5-10% anual | Trimestral |
| **Compensation** | Cost of Sales (% revenue) | 15-25% (varía modelo) | Trimestral |
| | Attainment Distribution Gini | <0.3 (equitativo) | Anual |

## Organización y carrera

**Estructura típica equipo** (según escala):
- **Analista Sales Analytics** (1-3): dashboards, reporting operativo, ad-hoc, data prep.
- **Senior Analyst / Scientist** (1-2): modelado predictivo (forecast, propensity, churn), experimentación (A/B testing comp plans, territory changes), *feature engineering*.
- **Analytics Engineer** (0-1): *dbt* models, data quality, *reverse ETL*, *data contracts*, *MLOps* básico.
- **Sales Analytics Manager** (si >5 personas): priorización roadmap, stakeholder management (VP Sales, RevOps, Finance, Marketing), comunicación insights a CRO/Board.

**Habilidades core**: SQL avanzado (CTEs, window functions, pivot/unpivot), Python/R (pandas, scikit-learn, statsmodels, XGBoost, Prophet), modelado dimensional (Kimball), storytelling con datos (Pyramid Principle, *action-oriented insights*), conocimiento dominio ventas (MEDDIC, Challenger, Sandler, *sales process*), comunicación ejecutiva.

**Carrera**: Senior Sales Analyst → Lead/Principal Sales Analyst → Head of Sales Analytics → Head of RevOps / VP Sales Strategy / Chief Revenue Officer (track ejecutivo) o Head of Data Science / VP Analytics (track técnico).

## Cross-refs

- [[rol/head-of-revenue-operations]] — RevOps end-to-end, alineación ventas/marketing/CS
- [[rol/head-of-sales-operations]] — ejecución operativa CRM, quotas, territories, comp
- [[rol/vp-sales]] / [[rol/chief-revenue-officer]] — liderazgo comercial, estrategia GTM
- [[rol/head-of-sales-strategy]] — estrategia comercial, GTM, pricing, analítica revenue
- [[rol/head-of-sales-effectiveness]] — coaching, metodología, productividad
- [[rol/head-of-sales-enablement]] — capacitación, contenido, playbooks, onboarding
- [[dominio/analitica-de-ventas]] — sales analytics como disciplina, pipeline, forecast, cohortes
- [[dominio/analitica-predictiva]] — forecasting, scoring, churn, ML aplicado
- [[dominio/gestion-de-la-demanda]] — demand planning, forecasting, S&OP/IBP
- [[dominio/compensacion-beneficios]] — diseño planes comp, equity, bandas salariales
- [[dominio/mercados-de-capitales]] — métricas SaaS (ARR, NRR, GRR, CAC, LTV) para investors
- [[rol/head-of-fp-and-a]] — planificación financiera, forecast revenue, variaciones