---
titulo: Finanzas cuantitativas
capa: dominio
tema: finanzas
fuente: https://en.wikipedia.org/wiki/Quantitative_finance
fuente2: https://en.wikipedia.org/wiki/Mathematical_finance
fecha: 2026-07-20
confianza: alta
tags: [finanzas, cuantitativo, derivados, riesgo, modelos-estocasticos, trading-algoritmico]
organizaciones: []
profundidad: 2
estado: profundo
---

# Finanzas cuantitativas

Disciplina que aplica matemáticas, estadística y programación para modelar mercados
financieros, valorar instrumentos y gestionar riesgo. El profesional es el *quant*.

## Áreas principales
- **Pricing de derivados:** modelos de valoración (Black-Scholes-Merton, árboles binomiales,
  diferencias finitas, Monte Carlo) para opciones, futuros, swaps y estructurados.
- **Riesgo cuantitativo:** VaR, CVaR/ES, modelos de tasas (Vasicek, Hull-White, CIR), riesgo
  de crédito (modelos estructurales de Merton, reducidos de Jarrow-Turnbull), y métricas
  regulatorias (FRTB).
- **Trading algorítmico / ejecución:** estrategias sistemáticas, market-making, arbitraje
  estadístico, optimización de carteras (Markowitz, Black-Litterman).
- **Investigación cuantitativa:** señales alternativas, machine learning aplicado a alpha.

## Métodos
- **Cálculo estocástico:** cálculo de Itô, ecuaciones diferenciales estocásticas para dinámicas
  de precios.
- **Procesos y simulación:** cadenas de Markov, Monte Carlo, bootstrapping.
- **Programación:** C++/Rust (baja latencia), Python (research), y bibliotecas numéricas.

## Riesgos y límites
- Riesgo de modelo (model risk): supuestos que fallan en colas (ej. crisis 2008, LTCM).
- Dependencia de datos de calidad y de la validación continua (SR 11-7 en EE.UU.).

## Relación con otras capas
- Vincula con `dominio/instrumentos-derivados`, `dominio/analitica-financiera`,
  `dominio/riesgo-financiero`.
- Rol: `rol/head-of-quantitative-research` (cuando exista), `rol/head-of-strategic-finance`,
  `rol/chief-risk-officer`.

## Fuentes
- Quantitative finance (Wikipedia EN): https://en.wikipedia.org/wiki/Quantitative_finance
- Mathematical finance (Wikipedia EN): https://en.wikipedia.org/wiki/Mathematical_finance
