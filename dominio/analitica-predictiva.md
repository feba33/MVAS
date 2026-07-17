---
titulo: Analítica predictiva
capa: dominio
tema: analitica-predictiva
fuente: https://en.wikipedia.org/wiki/Predictive_analytics
fuente2: https://en.wikipedia.org/wiki/Predictive_modeling
fecha: 2026-07-17
confianza: alta
tags: [predictive-analytics, forecasting, scoring, churn, modelado-predictivo, machine-learning, bi]
rol: []
actividades: []
organizaciones: []
responsabilidades: []
tareas: []
profundidad: 2
estado: profundo
---

# Analítica predictiva

## 📝 Conocimiento

### Definición
La **analítica predictiva** usa técnicas estadísticas de minería de datos, modelado predictivo y aprendizaje automático para analizar hechos actuales e históricos y **predecir eventos futuros o desconocidos**. Difiere de la analítica descriptiva (qué pasó) y la prescriptiva (qué hacer): se centra en la probabilidad de outcomes.

### Componentes y métodos
- **Modelado predictivo:** regresión, árboles, bosques, gradient boosting, redes neuronales.
- **Minería de datos:** descubrimiento de patrones en grandes volúmenes.
- **Clasificación y regresión:** para etiquetas o valores continuos.
- **Series de tiempo / forecasting:** demanda, ventas, carga eléctrica.
- **Scoring:** propensión a comprar, riesgo de crédito, churn.
- **Validación:** holdout, cross-validation, métricas (AUC, RMSE, F1).

### Aplicaciones de negocio
- **Churn / attrition:** retención de clientes y empleados (vs `dominio/inteligencia-de-negocio.md`).
- **Riesgo de crédito / fraude:** scoring e detección de anomalías (vs `dominio/riesgo-de-credito.md`).
- **Demanda y cadena:** forecast de ventas, inventario (vs `dominio/gestion-de-la-demanda.md`).
- **Marketing:** propensión, segmentación, next-best-action.
- **Operaciones:** mantenimiento predictivo (vs `dominio/iot.md`).

### Ciclo y gobernanza
- **CRISP-DM / iterativo:** entendimiento → datos → modelo → evaluación → despliegue → monitoreo.
- **Deriva (drift):** los modelos se degradan; requieren reentrenamiento y monitoreo (vs `dominio/aprendizaje-automatico.md`).
- **Sesgo:** datos históricos pueden perpetuar discriminación (ver `dominio/gobernanza-etica-ia.md`).

### Riesgos
- **Calidad de datos:** basura entra, basura sale.
- **Overfitting:** buen desempeño en muestra, pobre en producción.
- **Explicabilidad:** modelos caja negra difíciles de defender ante reguladores.
- ** vs `dominio/ciencia-de-datos` y `dominio/analitica-negocio`:** ciencia de datos = disciplina amplia; analítica de negocio = reporting/BI; predictiva = enfoque en predecir.

### Cross-refs
- `dominio/ciencia-de-datos.md` · `dominio/analitica-negocio.md` · `dominio/inteligencia-de-negocio.md`
- `dominio/aprendizaje-automatico.md` · `dominio/inteligencia-de-mercado.md`
