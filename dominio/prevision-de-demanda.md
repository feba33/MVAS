---
titulo: Previsión de demanda
capa: dominio
tema: prevision-de-demanda
fuente: https://en.wikipedia.org/wiki/Demand_forecasting
fuente2: https://en.wikipedia.org/wiki/Sales_and_operations_planning
fecha: 2026-07-20
confianza: alta
tags: [prevision-de-demanda, demand-forecasting, s&op, series-de-tiempo, ml, inventarios]
rol: [head-of-demand-planning, supply-chain-manager, head-of-operations, cfo]
actividades: [planificacion, prevision, s&op, inventarios]
organizaciones: []
responsabilidades: [planificacion-de-la-demanda, niveles-de-inventario]
tareas: []
profundidad: 2
estado: profundo
---

# Previsión de demanda

La **previsión de demanda** (demand forecasting) estima la cantidad de producto/servicio que
los clientes requerirán en el futuro, para planificar producción, inventario, capacidad y
finanzas.

## Métodos
- **Cualitativos:** juicio experto, método **Delphi**, investigación de mercado, escenarios
  (útiles sin datos históricos).
- **Cuantitativos — series de tiempo:** medias móviles, suavizamiento exponencial, **ARIMA**,
  descomposición estacional.
- **Causales:** regresión (demanda en función de precio, macro, promoción).
- **Machine learning:** gradient boosting, redes neuronales para patrones no lineales y datos
  ricos.

## Integración
- **S&OP / IBP** (Sales & Operations Planning / Integrated Business Planning): alinea
  previsión con plan de suministro, finanzas y comercial.
- Métricas de error: **MAPE**, sesgo (bias), RMSE.

## Cruce
Base de la **gestión de inventarios** y la cadena de suministro; alimenta compras (ver
`dominio/gestion-de-compras`) y la analítica de negocio.

## Cross-refs
- `dominio/cadena-de-suministro`, `dominio/logistica`, `dominio/operaciones`,
  `dominio/gestion-de-compras`, `dominio/analitica-negocio`.
