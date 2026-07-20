---
titulo: Analítica financiera
capa: dominio
tema: analitica-financiera
fuente: https://en.wikipedia.org/wiki/Financial_services
fecha: 2026-07-20
confianza: media
tags: [analitica-financiera, fp-and-a, dashboards, reporting, kpis, business-intelligence]
profundidad: 2
estado: profundo
---

# Analítica financiera

## Definición
La **analítica financiera** aplica métodos cuantitativos y visualización a los
datos financieros para apoyar la toma de decisiones: reporting analítico,
dashboards, modelado de escenarios y KPIs de negocio. Puente entre contabilidad,
FP&A y estrategia.

## Componentes
- **Reporting analítico:** estados financieros enriquecidos con tendencias,
  variaciones (actual vs presupuesto vs forecast) y métricas de rentabilidad por
  línea, región o cliente.
- **Dashboards financieros:** cuadros de mando en tiempo (casi) real sobre flujo
  de efectivo, margen, working capital y quema de caja (burn rate).
- **FP&A analytics:** planeación de escenarios, sensibilidades, asignación de
  costos y modelado de capital.
- **KPIs de negocio:** EBITDA, ingreso neto, ROIC, CAC/LTV, rotación de activos,
  DSO/DPO.

## Tecnología y gobierno
- Herramientas: CPM/EPM (Anaplan, Oracle EPM, SAP BPC), BI (Power BI, Tableau),
  hojas y data warehouses.
- Gobierno: trazabilidad de los números, conciliación con el ledger, linaje de
  datos (`dominio/gestion-de-la-calidad-de-datos`).

## Relación con otros temas
Complementa `dominio/inteligencia-de-negocio` (BI general) y `dominio/finanzas-corporativas`
(modelado 3-statement). Alimenta a `rol/head-of-strategic-finance`,
`rol/fp-and-a-manager` y `rol/head-of-financial-planning`. Distinto de
`dominio/analitica-predictiva` (modelado forward-looking) y `dominio/analitica-de-negocio`.
