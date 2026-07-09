---
titulo: Valoración de empresas — métodos (DCF, múltiplos, WACC)
capa: dominio
tema: finanzas
fuente: https://financeinterviewprep.com/blog/company-valuation-methods-complete-guide
fuente2: https://ctacquisitions.com/company-valuation-methods/
fecha: 2026-07-09
confianza: alta
tags: [finanzas, valoracion, dcf, multiples, wacc, capital-structure, mna, enterprise-value, equity-value]
english_keywords: [finanzas, valuation, dcf, multiples, wacc, capital-structure, mna, enterprise-value, equity-value]
---

## Resumen condensado
La **valoración de empresas** responde a "¿qué vale esta compañía?". Se agrupa en tres
enfoques estándar (reconocidos por AICPA SSVS-1, ASA y NACVA):

1. **Enfoque de valor intrínseco (Income / DCF)** — descuenta flujos futuros de caja al
   presente.
2. **Enfoque de valor relativo (Market / Comps)** — compara con empresas y transacciones
   similares.
3. **Enfoque de activos (Asset-Based)** — valor de los activos netos; típico en
   negocios intensivos en activos o en dificultades.

### Base: Enterprise Value vs Equity Value
- **Enterprise Value (EV)** = Capitalización + Deuda + Intereses minoritarios + Acciones
  preferentes − Efectivo. Representa el valor total de las operaciones para todos los
  inversionistas (deuda + capital).
- **Equity Value** = Capitalización de mercado (precio × acciones). Valor residual para
  los accionistas tras la deuda.

### DCF (flujo de caja descontado)
- Pronostica flujos de caja `CF_t` para `t = 1…T` y los descuenta a tasa `r`:
  `Valor = Σ CF_t / (1+r)^t + Valor Terminal / (1+r)^T`.
- La tasa `r` suele ser el **WACC** (costo promedio ponderado de capital) para EV, o el
  **costo del capital (CAPM)** para valorar equity directamente.
- Muy sensible a supuestos (crecimiento, márgenes, tasa de descuento) → método más
  defendible teóricamente pero frágil a hipótesis.

### Múltiplos (Market Approach)
- **EV/EBITDA** — estándar para empresas con EBITDA > $1M; típico 4-15x según sector.
- **SDE (Seller's Discretionary Earnings)** — estándar para < $1M; típico 1.5-5x.
- **EV/Revenue (o EV/ARR)** — SaaS y pre-utilidad.
- **Transacciones precedentes** — múltiplos pagados en M&A comparables.
- En M&A para fundadores con EBITDA > $1M, el **EBITDA múltiple** es dominante,
  cruzado contra DCF y transacciones recientes.

### Estructura de capital y WACC
El **WACC** pondera el costo de la deuda (post-impuestos) y el costo del capital según las
proporciones de la estructura de capital; la elección de deuda vs capital afecta tanto el
riesgo como el valor. Un apalancamiento mayor reduce WACC (escudo fiscal) pero sube el
riesgo de quiebra.

## Puntos clave para el LLM operando en `finanzas`
- Nunca dependas de UN solo método: triangula DCF + comps + (activos si aplica).
- Elige el múltiplo según madurez/escala (EBITDA para grandes, SDE para micro, revenue
  para SaaS).
- Recuerda el puente EV→Equity (resta deuda neta) al comunicar "valor de la acción".
- Cross-ref: `sustrato/mexico/lgsm.md` (implicaciones societarias), y disciplinas de
  contabilidad (NIF/IFRS) para los insumos de los flujos.

## Fuentes
- Finance Interview Prep (guía 2026): los 3 enfoques, EV vs Equity, DCF y comps:
  https://financeinterviewprep.com/blog/company-valuation-methods-complete-guide
- CT Acquisitions (guía 2026): múltiplos EBITDA/SDE/revenue, rangos por sector, WACC:
  https://ctacquisitions.com/company-valuation-methods/
