---
titulo: Analítica predictiva de cliente
capa: dominio
tema: Analítica predictiva de cliente (churn scoring, propensión, LTV prediction, ML cliente)
fuente: https://en.wikipedia.org/wiki/Predictive_analytics
fuente2: https://en.wikipedia.org/wiki/Customer_lifetime_value
fecha: 2026-07-20
confianza: alta
tags: [analitica-predictiva-cliente, churn-scoring, propension, ltv, ml-cliente, crm]
rol: []
actividades: []
organizaciones: []
responsabilidades: []
tareas: []
profundidad: 2
estado: profundo
---

# Analítica predictiva de cliente

La **analítica predictiva de cliente** aplica modelos estadísticos y de aprendizaje
automático sobre datos de comportamiento, transaccionales y demográficos para anticipar
acciones del cliente (comprar, cancelar, hacer upgrade) y actuar sobre ellas.

## Modelos clave
- **Churn scoring**: probabilidad de baja en ventana T; inputs = frecuencia de uso,
  soporte, NPS, eventos de facturación. Habilita campañas de retención dirigidas.
- **Propensión a comprar / next-best-offer**: modelos de clasificación para
  cross-sell/upsell (ej. propensity-to-buy en e-commerce y SaaS).
- **Customer Lifetime Value (LTV/CLV)**: predicción de valor futuro descontado; guía
  gasto de adquisición (CAC) y segmentación.
- **Lead scoring**: priorización de oportunidades en B2B.

## Ciclo de valor
Ingesta (CDP/CRM) → feature engineering → entrenamiento (gradient boosting, redes,
survival analysis para churn) → deploy → monitoreo de deriva → cierre del loop con
acciones (triggers en journey orchestration).

## Privacidad (Norteamérica)
GDPR (UE, aplica a mexicanos con datos en UE), **CCPA/CPRA** (California), **PIPEDA**
(Canadá) y **LFPDPPP** (México) limitan uso de PII para modelado; requieren
consentimiento y opt-out. Ver `dominio/regulacion-de-datos`.

## Relación con otros nodos
Se vincula con `dominio/analitica-web`, `dominio/analitica-de-ventas`,
`dominio/comercio-electronico`, `rol/head-of-customer-lifecycle-ops` y
`rol/head-of-data-strategy`.
