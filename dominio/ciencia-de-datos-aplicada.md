---
titulo: Ciencia de datos aplicada
capa: dominio
tema: ciencia-de-datos-aplicada
fuente: https://en.wikipedia.org/wiki/Data_science
fuente2: https://www.ibm.com/topics/data-science
fecha: 2026-07-16
confianza: alta
tags: [ciencia-de-datos-aplicada, data-science, crisp-dm, machine-learning, mlops, analytics, modelado-predictivo]
profundidad: 2
estado: profundo
rol: [head-of-data-science, data-scientist, data-analyst, ml-engineer, ai-engineer]
actividades: [modelado-predictivo, analitica-prescriptiva, mlops, data-storytelling]
organizaciones: [empresa, data-team, analytics]
responsabilidades: [construir-modelos, desplegar-ml, medir-impacto]
tareas: [feature-engineering, evaluacion-modelos, a-b-testing]
---

# Ciencia de datos aplicada

Disciplina que combina **estadística, programación y conocimiento de
negocio** para extraer valor de datos. Distinta de la *ciencia de datos*
teórica (`ciencia-de-datos`, disciplina) y de la *analítica de negocio*
(`analitica-negocio`): aquí el foco es **construir y desplegar modelos**
que cambian una decisión o acción.

## Método (CRISP-DM)
1. **Entendimiento de negocio** → 2. **Entendimiento de datos** →
3. **Preparación** (limpieza, feature engineering) → 4. **Modelado**
(regresión, clasificación, series de tiempo, clustering) → 5. **Evaluación**
→ 6. **Despliegue y monitoreo**. Ciclo iterativo, no lineal.

## Modelado predictivo
- **Supervisado:** regresión (precios, demanda), clasificación (churn,
  fraude, riesgo de crédito). **No supervisado:** segmentación, detección
  de anomalías. **Series de tiempo:** forecasting de ventas/inventario.
- **Deep learning:** visión por computadora (CV), NLP/LLMs (`ia-generativa`,
  `agentes-ia`) cuando hay muchos datos y señal compleja.

## MLOps (operacionalización)
Pasar del notebook a producción exige **MLOps**: versionado de datos/modelos
(DVC, MLflow), CI/CD para modelos, monitoreo de deriva (drift), re-entrenamiento
y evaluación continua (`aprendizaje-automatico`, `observabilidade`). El
**data scientist** entrena; el **ML engineer** / **head of ML** opera.

## Analítica de valor
La analítica desciende de descriptiva → diagnostic → predictiva →
prescriptiva. El entregable no es el modelo sino la **decisión mejorada**
(`inteligencia-de-mercado`, `analitica-negocio`).

## Riesgos
Sesgo/equidad (`etica-ia`, `gobierno-de-ia`), explicabilidad, calidad de
datos (`gobierno-de-datos`), y sobreajuste. Gobernanza vía `gobierno-de-riesgos`.

## 🔗 Relaciones
- `ciencia-de-datos` (disciplina base) · `analitica-negocio` (BI/descriptiva)
- `aprendizaje-automatico` · `mlops-engineer` · `ia-generativa`
- `gobierno-de-datos` · `inteligencia-de-mercado` · `etica-ia`
