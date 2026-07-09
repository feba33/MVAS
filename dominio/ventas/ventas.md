---
titulo: Ventas (metodología, funnel, CRM y métricas)
capa: dominio
tema: ventas
fuente: conocimiento general (reference-only)
fecha: 2026-07-09
confianza: alta
tags: [ventas, sales, funnel, crm]
---

# Ventas (metodología, funnel, CRM y métricas)

## 📝 Conocimiento

### Responsabilidades del proceso de ventas
- **Prospectar y calificar:** identificar leads con fit y necesidad real (alineado con el funnel de marketing).
- **Desarrollar la oportunidad:** descubrir necesidades, presentar valor y manejar objeciones.
- **Cerrar y hacer seguimiento:** firma del contrato, onboarding y retención/expansión (upsell/cross-sell).

### Proceso (ciclo de ventas)
1. **Lead → MQL → SQL:** marketing genera interés (TOFU/MOFU), ventas califica (BOFU).
2. **Descubrimiento:** se entiende el problema y el contexto del cliente.
3. **Propuesta y negociación:** se presenta la solución y se acuerda precio/condiciones.
4. **Cierre y post-venta:** contratación, activación y cuentas a largo plazo.

### Metodologías
- **SPIN Selling:** técnica de preguntas situacionales, de problema, implícitas y de necesidad (SPIN) para revelar el valor de la solución.
- **Challenger Sale:** el vendedor educa y desafía la visión del cliente, aportando perspectiva comercial propia en vez de solo responder a demanda.
- **MEDDIC:** marco de calificación — Metrics, Economic Buyer, Decision Criteria, Decision Process, Identify Pain, Champion.

### Funnel (TOFU / MOFU / BOFU)
- **TOFU (Top of Funnel):** awareness; contenido educativo y alcance (marketing).
- **MOFU (Middle of Funnel):** consideración; comparativas, demos, leads nutridos.
- **BOFU (Bottom of Funnel):** decisión; propuesta, negociación y cierre (dominio de ventas).

### Skills del vendedor
- Escucha activa y empatía; comunicación persuasiva.
- Calificación rigurosa y manejo de objeciones.
- Análisis de datos del pipeline y pronóstico (forecasting).

### Herramientas (CRM)
- **Salesforce:** CRM empresarial configurable, automatización y reporting avanzado.
- **HubSpot:** CRM inbound, integración marketing-ventas y pipelines visuales.
- Además: secuenciadores de email, inteligencia de cuentas y dashboards de pipeline.

### Métricas clave
- **Pipeline:** valor total de oportunidades abiertas en el embudo.
- **CAC (Customer Acquisition Cost):** costo de adquirir un cliente (marketing + ventas).
- **Win rate:** % de oportunidades ganadas sobre las calificadas.
- Complementarias: ciclo de ventas, tamaño medio de contrato (ACV), tasa de conversión por etapa.

### Cómo un LLM opera esta entidad
- Lee `raw/` (inmutable) y genera/refina páginas con YAML frontmatter en `dominio/ventas/`.
- Mantiene `index.md` y `log.md` (append-only) al ingerir conocimiento.
- Cruza referencias con `dominio/marketing/` (fuente de leads) y `rol/sales-lead` (quién ejecuta).
- Al responder, prioriza métricas y metodologías validadas; marca `confianza` según la fuente.

## 🔗 Referencia
- `dominio/marketing/marketing-mix.md` — origen de los leads que alimentan el funnel de ventas (TOFU/MOFU).
- `rol/sales-lead` — rol responsable de ejecutar y liderar el proceso de ventas descrito aquí.
