---
titulo: Minaría de datos / Data Mining
capa: dominio
tema: mineria-de-datos
fuente: https://en.wikipedia.org/wiki/Data_mining
fuente2: https://en.wikipedia.org/wiki/Association_rule_learning
fecha: 2026-07-15
confianza: alta
tags: [mineria-de-datos, data-mining, kdd, pattern-mining, clustering, asociacion, bi, descubrimiento]
english_keywords: [data mining, KDD, pattern mining, association rules, clustering, classification, knowledge discovery]
profundidad: 2
estado: profundo
---

# Minaría de datos / Data Mining

## 📝 Conocimiento
- **Definición:** la minaría de datos es el **descubrimiento de patrones** y conocimiento en grandes volúmenes de datos mediante métodos de estadística, aprendizaje automático e inteligencia artificial; parte del proceso **KDD** (Knowledge Discovery in Databases). vs `dominio/ciencia-de-datos` (más amplio: negocio+modelado+despliegue) y `dominio/analitica-negocio` (BI/decisiones).
- **Reglas de asociación:** encontrar relaciones entre ítems (p.ej. *market basket* — "clientes que compran A compran B"); algoritmos **Apriori** y **FP-Growth**; métricas soporte/confianza/lift.
- **Agrupamiento (clustering):** segmentación no supervisada — **k-means**, **DBSCAN**, clustering jerárquico; usado en segmentación de clientes, detección de anomalías y reducción de dimensionalidad (PCA).
- **Clasificación y predicción:** árboles de decisión, Naive Bayes, SVM, bosques; y **detección de anomalías** (fraude, intrusiones).
- **Patrones secuenciales y series de tiempo:** para cadenas de compra, mantenimiento predictivo y pronósticos.
- **Aplicaciones:** retail (cross-sell, surtido), **detección de fraude** (vs `dominio/contabilidad-forense` y `rol/compliance-manager`), CRM, salud (epidemiología), manufactura (calidad).
- **Riesgos y ética:** privacidad (re-identificación), sesgo, y cumplimiento de `dominio/proteccion-de-datos` (GDPR/CPRA/LGPD); requiere gobernanza de datos — ver `dominio/gobierno-de-datos`.
- **vs ML:** la minaría de datos enfatiza el **descubrimiento exploratorio** de patrones ya existentes; el `dominio/aprendizaje-automatico` enfatiza el modelo predictivo. Se solapan en la práctica.

## 🔗 Referencia
- Wikipedia — *Data mining*, *Association rule learning*, *K-means clustering*, *Anomaly detection* (reference-only).
- Cross-ref: `dominio/ciencia-de-datos`, `dominio/aprendizaje-automatico`, `dominio/analitica-negocio`, `dominio/proteccion-de-datos`, `dominio/gobierno-de-datos`, `dominio/contabilidad-forense`.
