---
titulo: Financiación estructurada
capa: dominio
tema: financiacion-structurada
fuente: https://en.wikipedia.org/wiki/Structured_finance
fuente2: https://www.investopedia.com/terms/s/structuredfinance.asp
fecha: 2026-07-17
confianza: alta
tags: [finanzas, financiacion-estructurada, titulizacion, abs, mbs, cdo, clo, sindicacion, project-finance, spv]
organizaciones: [bancos-de-inversion, agencias-de-rating, monoline, spv]
responsabilidades: [estructuracion-financiera, gestion-de-riesgo-de-credito, captacion-de-capital]
profundidad: 2
estado: profundo
---

# Financiación estructurada

La **financiación estructurada** (structured finance) es el sector de las finanzas y
del derecho financiero que gestiona apalancamiento y riesgo mediante instrumentos
que van más allá de la deuda corporativa convencional. Las estrategias suelen
implicar contabilidad fuera de balance (off-balance-sheet) o el uso de instrumentos
financieros para gestionar el riesgo de crédito y facilitar flujos de capital.

## Mecanismos principales
1. **Titulización (securitization)**: empaquetar activos (hipotecas, préstamos
   auto, tarjetas, recibos) en valores negociables.
   - **MBS** (Mortgage-Backed Securities), **ABS** (Asset-Backed), **CDO**
     (Collateralized Debt Obligation), **CLO** (Collateralized Loan Obligation).
2. **SPV / SPE** (Special Purpose Vehicle): entidad aislada que contiene los
   activos y emite los valores, protegiendo del riesgo del originador.
3. **Tranching**: dividir la emisión en tramos con distinta prioridad de pago y
   riesgo (senior / mezzanine / equity).
4. **Sindicación**: préstamos sindicados donde un grupo de bancos comparte un
   crédito grande.
5. **Project finance**: deuda sin recurso (non-recourse) respaldada por flujos del
   proyecto (infraestructura, energía, PPP).

## Agencias y mercado
- **Agencias de rating** (S&P, Moody's, Fitch) califican los tramos; las
  aseguradoras **monoline** garantizaban tramos senior (colapso en 2008).
- Mercado predominante en EE.UU. y Europa; usado por bancos, aseguradoras y
  financieras para liberar capital regulatorio.

## Riesgos y la crisis de 2008
- La estructuración excesiva y opaca (CDOs de CDOs) amplificó la crisis
  subprime. La titulización mal calibrada generó contagio sistémico.
- Post-crisis: **Dodd-Frank** (EE.UU.) y **reglas de retención de riesgo**
  (risk-retention) exigieron al originador conservar parte del riesgo.

## Relación con otras capas
- vs `dominio/ingenieria-financiera` (derivados exóticos), `dominio/derivados`,
  `dominio/banca-de-inversion` (underwriting de MBS/CDO), `dominio/mercados-capitales`.
- Sustrato: `sustrato/estados-unidos/regulacion-financiera`.
- Rol: `rol/investment-banker`, `rol/structurer` implícito, `rol/risk-manager`.

## Fuentes
- Structured finance (Wikipedia): <https://en.wikipedia.org/wiki/Structured_finance>
- Structured finance (Investopedia): <https://www.investopedia.com/terms/s/structuredfinance.asp>
