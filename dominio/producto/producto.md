---
titulo: Producto (entidad de dominio)
capa: dominio
tema: producto
fuente: conocimiento general (reference-only)
fecha: 2026-07-09
confianza: alta
tags: [producto, discovery, aarrr, pmf]
---

# Producto (entidad de dominio)

Página principal de la entidad `producto` dentro de `dominio/`. Cubre el ciclo de vida del
producto: desde el **discovery** (oportunidad y problema) hasta las **métricas AARRR**,
el **product-market fit (PMF)** y el **roadmap**.

## 📜 Cita
> *(Se omite en esta página: no hay fuente citada — conocimiento general de reference-only. Si
> el usuario deposita una fuente en `raw/`, Hermes añadirá aquí la cita literal.)*

## 📝 Conocimiento

### Discovery (oportunidad y problema)
- **Oportunidad:** brecha de mercado, cambio de comportamiento o ineficiencia existente que un
  producto puede resolver. Se valida con tamaño de mercado (TAM/SAM/SOM) y evidencias cualitativas.
- **Problema:** dolor real y recurrente del usuario. Técnica clave: entrevistas de descubrimiento,
  *problem interviews* y observación; el objetivo es confirmar que el problema duele lo suficiente
  para pagar/usar una solución.
- **Skills/herramientas:** entrevistas estructuradas, *jobs-to-be-done* (JTBD), mapas de empatía,
  análisis competitivo, *opportunity solution tree*. Un LLM puede operar esto resumiendo
  transcripciones de entrevistas, extrayendo temas recurrentes y redactando hipótesis de problema.

### Métricas AARRR (Pirate Metrics)
- **Acquisition (no pedida aquí, marco de fondo):** cómo llegan los usuarios.
- **Activation:** primer valor percibido — % de nuevos usuarios que completan el *aha-moment*
  (onboarding exitoso, primer acto de valor).
- **Retention:** % de usuarios que vuelven tras N días; cohortes y *churn*. Es el motor de
  sostenibilidad del producto.
- **Revenue:** monetización — ARPU, LTV, conversión a paga, MRR/ARR.
- **Referral:** viralidad — k-factor, invitaciones por usuario, loops de crecimiento.
- **Operación con LLM:** el LLM puede sintetizar dashboards, explicar caídas de retención por
  cohorte y proponer experimentos de activación/referral a partir de datos crudos.

### PMF (Product-Market Fit)
- Grado en que el producto satisface una necesidad de mercado fuerte y consistente.
- Señal clásica (Sean Ellis): >40% de usuarios "muy decepcionados" si desapareciera el producto.
- Antes del PMF, optimiza retención y activación; después, escala adquisición y referral.
- Un LLM ayuda a triangular PMF cruzando encuestas de salida, NPS y retención de cohorte.

### Roadmap
- Secuencia priorizada de iniciativas alineadas al PMF y a las métricas AARRR.
- Marco: *now / next / later*; priorización por RICE o impacto en retención/revenue.
- El LLM puede generar borradores de épica/historias de usuario y detectar dependencias.

### Cómo un LLM opera esta entidad
- **Ingesta:** lee fuentes en `raw/`, extrae oportunidad/problema y métricas.
- **Síntesis:** redacta hipótesis de producto y propone experimentos AARRR.
- **Mantenimiento:** actualiza `index.md` y `log.md` en cada ingest, sin tocar `raw/`.

## 🔗 Referencia
- Rol / Product Lead: `../../rol/product-lead/product-lead.md` (cross-ref, aún por crear).
- Dominio / Marketing: `../marketing/README.md` — retención, referral y adquisición se nutren del embudo de marketing.
- Dominio / Diseño: `../diseno/README.md` — UX research y service design alimentan el discovery y la activation.
