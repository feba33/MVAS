---
titulo: Aprendizaje automático / Machine Learning
capa: dominio
tema: aprendizaje-automatico
fuente: https://en.wikipedia.org/wiki/Machine_learning
fuente2: https://en.wikipedia.org/wiki/Supervised_learning
fecha: 2026-07-15
confianza: alta
tags: [machine-learning, aprendizaje-automatico, supervised, unsupervised, deep-learning, mlops, modelos]
english_keywords: [machine learning, supervised learning, unsupervised learning, deep learning, reinforcement learning, MLOps, model lifecycle]
profundidad: 2
estado: profundo
---

# Aprendizaje automático / Machine Learning

## 📝 Conocimiento
- **Definición:** subdisciplina de la IA que construye **sistemas que aprenden de datos** para realizar tareas sin ser programados explícitamente (Arthur Samuel, 1959; definición formal de Tom Mitchell: "mejorar en una tarea T con respecto a una medida P a partir de experiencia E"). Ver `dominio/inteligencia-artificial`.
- **Aprendizaje supervisado:** se entrena con datos **etiquetados**; tareas de **clasificación** (spam/no-spam, diagnóstico) y **regresión** (precio, demanda). Algoritmos: regresión logística, árboles/SVM, bosques aleatorios, gradient boosting, redes neuronales.
- **Aprendizaje no supervisado:** sin etiquetas; **agrupamiento (clustering)** (k-means, DBSCAN), **reducción de dimensionalidad** (PCA, t-SNE) y detección de anomalías. Útil para segmentación y descubrimiento.
- **Semi-supervisado y por refuerzo (RL):** el RL aprende por **recompensa** (agentes, juegos, control); es la base de sistemas como AlphaGo y del RLHF en LLMs.
- **Deep learning:** redes neuronales profundas (CNNs visión, RNNs/Transformers lenguaje, autoencoders); requiere gran volumen de datos y cómputo (GPUs).
- **Ciclo de modelos / MLOps:** definición del problema → ingeniería de datos → entrenamiento → evaluación (métricas: accuracy/F1/AUC, RMSE) → **despliegue** → monitoreo/drift → re-entrenamiento. Ver `rol/ml-engineer`, `rol/mlops-engineer`, `dominio/ia-generativa`.
- **vs disciplinas vecinas:** se diferencia de `dominio/ciencia-de-datos` (más amplio: negocio + estadística + despliegue) y de `dominio/mineria-de-datos` (descubrimiento de patrones en bases); el ML es el motor predictivo. La `dominio/ia-generativa` es una aplicación del deep learning.
- **Riesgos:** sesgo, explicabilidad, sobreajuste (overfitting), y gobernanza — ver `dominio/gobierno-de-ia`, `dominio/etica-ia`.

## 🔗 Referencia
- Wikipedia — *Machine learning*, *Supervised learning*, *Unsupervised learning*, *Reinforcement learning* (reference-only).
- Cross-ref: `dominio/inteligencia-artificial`, `dominio/ia-generativa`, `dominio/ciencia-de-datos`, `dominio/mineria-de-datos`, `dominio/gobierno-de-ia`, `rol/ml-engineer`, `rol/mlops-engineer`.
