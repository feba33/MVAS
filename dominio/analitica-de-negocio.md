---
titulo: Analítica de negocio (business analytics)
capa: dominio
tema: analitica-de-negocio
fuente: https://en.wikipedia.org/wiki/Business_analytics
fuente2: https://www.gartner.com/en/business-analytics
fecha: 2026-07-18
confianza: alta
tags: [analitica-de-negocio, business-analytics, bi, dashboards, kpis, reporting-analitico, data-visualization, toma-de-decisiones]
rol: []
actividades: []
organizaciones: []
responsabilidades: []
tareas: []
profundidad: 2
estado: profundo
---

# Analítica de negocio (business analytics)

La **analítica de negocio** es el uso disciplinado de datos, métodos estadísticos y
herramientas de visualización para entender el desempeño pasado y presente de la
organización y apoyar la toma de decisiones operativas y estratégicas.

## Capas
- **BI (Business Intelligence):** reporting, cuadros de mando (dashboards), KPIs e
  indicadores operativos; describe **qué pasó** (descriptivo).
- **Analítica avanzada / predictiva:** modelado para anticipar (pronósticos de demanda,
  churn, riesgo) — se apoya en `dominio/analitica-predictiva` y `dominio/ciencia-de-datos`.
- **Analítica prescriptiva:** recomendación de acciones (optimización, simulación).

## Componentes
- **Datos y modelo de gobierno:** integración desde ERP/CRM, data warehouse/lakehouse,
  catálogo y linaje (ver `rol/head-of-data-governance`).
- **Visualización y self-service:** herramientas (Tableau, Power BI, Looker); democratizar
  el acceso a datos para usuarios de negocio.
- **Cultura data-driven:** literacia de datos, decisiones basadas en evidencia.

## Diferenciación
- vs `dominio/analitica-predictiva` (enfoque en modelado y forecasting),
  `dominio/analitica-de-marketing` (foco en canales/atribución),
  `dominio/ciencia-de-datos` (métodos estadísticos/ML más profundos).

## Conexiones
- `dominio/ciencia-de-datos` · `dominio/analitica-predictiva` · `dominio/analitica-de-marketing`
- `rol/head-of-data-science` · `rol/chief-analytics-officer` · `dominio/inteligencia-de-negocio`
