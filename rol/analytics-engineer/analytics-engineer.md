---
titulo: Analytics Engineer
capa: rol
tema: analytics-engineer
fuente: https://www.getdbt.com/what-is-analytics-engineering/
fuente2: https://en.wikipedia.org/wiki/Data_modeling
fecha: 2026-07-14
confianza: alta
tags: [analytics-engineer, data-modeling, dbt, sql, data-warehouse, analytics, etl]
english_keywords: [analytics engineering, dbt, data modeling, data warehouse, ELT, data transformation]
---

# Analytics Engineer

## 📝 Conocimiento
- **Qué es:** rol que aplica **prácticas de ingeniería de software** (control de versiones, testing, modularidad, CI/CD) a la **transformación y modelado de datos** dentro del data warehouse. Acuñado por dbt Labs ~2018 para cubrir el hueco entre ingeniería de datos y analistas.
- **Responsabilidades:** construir modelos de datos *confiables y documentados* (capas staging → intermediate → marts), tests de calidad, documentación, lineage (DAG), optimización de consultas, y exponer "tablas limpias" para `rol/data-analyst` / `rol/data-scientist`.
- **Stack típico:** **dbt** (SQL + Jinja), SQL avanzado, data warehouse (Snowflake/BigQuery/Redshift/Databricks), Git, Airflow/Ciudad. Trabaja sobre datos ya ingestados (ELT: el *T* lo hace el analytics engineer).
- **vs** `rol/data-engineer` (construye pipelines/infra de ingesta, el *E* y *L*), `rol/data-analyst` (analiza/visualiza), `rol/data-scientist` (modela/estadística). El analytics engineer es el puente DE↔DS.
- **Relevancia MVAS:** depende de `dominio/ciencia-de-datos`, `dominio/gobierno-de-datos`, `dominio/analitica-negocio`, `rol/data-engineer`.

## 🔗 Referencia
- dbt Labs — What is analytics engineering: https://www.getdbt.com/what-is-analytics-engineering/
- Wikipedia EN — Data modeling: https://en.wikipedia.org/wiki/Data_modeling
- Cross-ref: `rol/data-engineer`, `rol/data-analyst`, `rol/data-scientist`, `dominio/ciencia-de-datos`, `dominio/gobierno-de-datos`.
