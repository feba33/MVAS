---
titulo: Riesgo financiero
capa: dominio
tema: finanzas
fuente: https://www.santanderopenacademy.com/es/blog/riesgos-financieros.html
fuente2: https://www.bis.org/bcbs/basel3_es.htm
fecha: 2026-07-10
confianza: alta
tags: [finanzas, riesgo, riesgo-de-mercado, riesgo-de-credito, riesgo-de-liquidez, riesgo-operativo, gestion-de-riesgos, basilea]
english_keywords: [financial risk, market risk, credit risk, liquidity risk, operational risk, risk management, basel iii, coso, iso 31000]
---

# Riesgo financiero

> Toda actividad empresarial con **incertidumbre** que puede causar una consecuencia
> financiera negativa (pérdida de capital o capacidad de pago). Está ligado a la
> rentabilidad: a mayor apalancamiento/deuda, mayor riesgo financiero potencial [1].

## 📝 Conocimiento

### Definición y naturaleza
El riesgo financiero es la exposición a resultados adversos por fuerzas
macroeconómicas e internas. No se elimina (está ligado a la incertidumbre del
futuro), pero **se mide, se mitiga y se monitoriza** su impacto [1]. Es inherente
a operar, invertir y financiarse; la "no toma de riesgo" es en sí misma una
decisión de riesgo (Zuckerberg, citado por Santander Open Academy).

### Los 4 tipos principales

**1. Riesgo de mercado** — pérdidas por fluctuación de precios y condiciones de
mercado que afectan el valor de activos y posiciones [1].
- *Riesgo de tipo de cambio (FX):* movimiento de divisas en operaciones internacionales.
- *Riesgo de tasa de interés:* cambios en tasas que alteran valor de deuda/activos.
- *Riesgo de precio/equidad y materias primas:* caídas de índices, acciones, commodities.
- *Riesgo de inflación / consumo:* cambios en patrones de demanda del cliente.
- *Mitigación:* cobertura con [derivados](derivados.md) (futuros, opciones, swaps),
  diversificación, límites de posición.

**2. Riesgo de crédito (contraparte)** — que el deudor o contraparte no cumpla sus
obligaciones de pago [3].
- Incluye riesgo de incumplimiento (default), riesgo de downgrade y riesgo de
  concentración.
- *Mitigación:* evaluación crediticia, garantías/colaterales, límites por contraparte,
  diversificación de cartera, provisiones por incobrables.

**3. Riesgo de liquidez** — incapacidad de cumplir obligaciones de pago por falta
de efectivo o de activos líquidos convertibles a corto plazo [1][3].
- *Riesgo de financiamiento:* no obtener fondeo; *riesgo de mercado de liquidez:*
  no liquidar un activo sin pérdida de valor.
- *Mitigación:* [tesorería](finanzas-corporativas.md) (cash flow forecasting),
  líneas de crédito comprometidas, colchón de liquidez, gestión de capital de trabajo.

**4. Riesgo operativo** — pérdidas por fallos en procesos, personas, sistemas o
eventos externos (fraude, errores, ciberataques, desastres) [3].
- También: riesgo legal, tecnológico y de lavado de dinero (PLD) en entidades financieras [3].
- *Mitigación:* controles internos, [COSO ERM](finanzas-corporativas.md),
  continuidad de negocio, seguridad de la información (ver
  `dominio/ciberseguridad-gobierno/iso-27001.md`), segregación de funciones.

### Riesgos complementarios (sector financiero)
Bancos y fintechs añaden **riesgo legal**, **tecnológico** y **de lavado de
dinero (PLD/AML)**; se gestionan con la matriz de riesgos y marcos regulatorios [3].

### Marcos de gobernanza y gestión
- **COSO ERM (2017):** integra la gestión de riesgos con la estrategia y la
  cultura organizacional; lenguaje común de riesgo en toda la empresa [2].
- **ISO 31000:** enfoque integral y flexible, adaptable a cualquier organización,
  que trata el riesgo como oportunidad y no solo amenaza [2].
- **Basilea III (BIS):** marco global bancario post-crisis 2007-09 que refuerza
  capital, supervisión y gestión de riesgo; cubre **crédito, mercado y operativo**
  con requerimientos mínimos de capital, coeficiente de cobertura de liquidez (LCR)
  y financiación estable neta (NSFR) [2][4].
- **CNBV** (México): regulación nacional que aplica Basilea y supervisa riesgos en
  bancos, financieras y fintechs [2]. Ver `sustrato/mexico/`.

### Proceso de gestión (ciclo)
1. **Identificar** riesgos (matriz, mapa de riesgos).
2. **Medir** (VaR, expected loss, scoring, stress tests).
3. **Mitigar/transferir** (controles, coberturas, seguros, límites).
4. **Monitorear y reportar** (KRI — indicadores clave de riesgo) en continuo [3].

## 🔗 Referencia
- [1] Santander Open Academy — Riesgos financieros: qué son, tipos y consejos: https://www.santanderopenacademy.com/es/blog/riesgos-financieros.html
- [2] LinkedIn (F. Atilano) — Marcos normativos: ISO 31000, COSO ERM, Basilea, CNBV: https://es.linkedin.com/posts/fernando-atilano-383b6125_riesgos-iso31000-cosoerm-activity-7353589528831369218-xDP1
- [3] Scribd / clase Basilea — Gestión de Riesgos en bancos (tipos y matriz): https://es.scribd.com/document/480403401/Clase-2-Gestion-de-Riesgos-I
- [4] BIS — Basilea III (marco regulador internacional): https://www.bis.org/bcbs/basel3_es.htm
- [5] EAE Barcelona — Tipos de riesgo financiero y ejemplos: https://www.eaebarcelona.com/es/blog/tipos-de-riesgo-financiero-que-son-y-ejemplos-clave
- Cross-ref: `dominio/finanzas/derivados.md`, `dominio/finanzas/finanzas-corporativas.md`,
  `dominio/finanzas/valoracion.md`, `dominio/ciberseguridad-gobierno/nist-csf.md`,
  `rol/cfo/cfo.md`, `rol/compliance-officer/compliance-officer.md`, `sustrato/mexico/`.
