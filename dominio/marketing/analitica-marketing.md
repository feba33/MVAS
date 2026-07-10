---
titulo: Analítica de Marketing y Atribución (attribution models)
capa: dominio
tema: marketing
fuente: https://mcpanalytics.ai/articles/marketing-attribution-models-compared (reference-only)
fuente2: https://improvado.io/blog/b2b-marketing-attribution (reference-only)
fecha: 2026-07-10
confianza: alta
tags: [marketing, marketing-analytics, attribution, atribucion, roi, mmm, mediamix-modeling, data-driven]
english_keywords: [marketing, marketing analytics, attribution models, ROI, multi-touch attribution, media mix modeling (MMM), data-driven attribution]
---

# Analítica de Marketing y Atribución (attribution models)

## 📜 Cita
> "A customer sees your Instagram ad on Monday, clicks a Google search result on Wednesday, opens your email on Friday, and buys on Saturday. Which channel gets credit for the sale? The answer depends entirely on which attribution model you use — and each model will give you a different answer that leads to different budget decisions." — MCP Analytics (2026)
> "B2B attribution in 2026 has evolved from single-method reliance to method stacking — combining multi-touch attribution with media mix modeling." — Improvado (2026)

## 📝 Conocimiento
- **Definición:** la analítica de marketing mide el impacto de cada canal/touchpoint en los resultados de negocio para decidir la **asignación de presupuesto** y probar el **ROI**. La atribución es su subdisciplina central: repartir el crédito de conversión entre los contactos.
- **Los 5 modelos principales:**
  1. **First-touch (primera interacción):** 100% del crédito a la primera. Útil para medir **awareness** y entrada de funnel.
  2. **Last-touch (última interacción):** 100% a la última (típico de e-commerce/default de plataformas). Sobrestima cierre, ignora el viaje.
  3. **Lineal:** reparte crédito equitativamente a todos los touchpoints.
  4. **Por posición (U-shaped / time-decay):** pondera extremos o eventos recientes.
  5. **Data-driven (multitouch algorítmico):** usa modelos estadísticos/ML para asignar crédito por contribución real (p. ej. Shapley). El más preciso pero requiere volumen de datos.
- **Multitouch (MTA):** reconoce que el cliente necesita **todos** los puntos de contacto (Instagram+Search+Email) para convertir; ningún canal solo explica la venta.
- **Media Mix Modeling (MMM):** modelo agregado (regresión/series de tiempo) que mide efecto de medios pagados/online/offline a nivel macro; complementa a MTA y soporta *method stacking* (apilar MTA + MMM en 2026).
- **Ciclo B2B largo:** la atribución B2B es más compleja por ciclos largos y múltiples stakeholders; se apoya en CRM, intent data y RevOps.
- **Herramientas/stack:** warehouses (BigQuery/Snowflake), connectors (Improvado, Fivetran), BI (Looker/Tableau), MCP servers para agentes.
- **Riesgo:** modelo erróneo → decisiones de presupuesto erróneas (last-touch mata Instagram; first-touch mata email). Elegir según objetivo (ToF vs BoFu).
- **Relevancia MVAS:** consume los datos de `demand-generation.md` (paid media) y `cro`; alimenta reporting de `rol/marketing-lead` y `rol/growth-lead`; conecta con `dominio/finanzas` (ROI, CAC).

## 🔗 Referencia
- MCP Analytics (2026), *Marketing Attribution Models Compared*: https://mcpanalytics.ai/articles/marketing-attribution-models-compared (reference-only).
- Improvado (2026), *B2B Marketing Attribution Guide 2026*: https://improvado.io/blog/b2b-marketing-attribution (reference-only).
