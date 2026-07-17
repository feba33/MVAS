---
titulo: Trading / Mercados de trading
capa: dominio
tema: trading
fuente: https://en.wikipedia.org/wiki/Trading_strategy
fuente2: https://en.wikipedia.org/wiki/High-frequency_trading
fecha: 2026-07-17
confianza: media
tags: [trading, mercados-financieros, ejecucion, algoritmico, hft, asset-classes, mesa]
organizaciones: [exchanges, broker-dealers, desks]
responsabilidades: [ejecucion-de-ordenes, gestion-de-riesgo-de-mercado, liquefaccion]
profundidad: 2
estado: profundo
---

# Trading / Mercados de trading

El **trading** es la actividad de comprar y vender instrumentos financieros para obtener
retorno, ya sea por cuenta propia (prop trading), de clientes (agencia) o de un fondo. Una
**estrategia de trading** es un plan fijo para lograr retorno yendo *long* o *short* en mercados.

## Clases de activos
- **Renta variable** (acciones, ETFs), **renta fija** (bonos), **divisas (FX)**, **commodities**,
  **derivados** (futuros, opciones, swaps).

## Tipos de operación
- **Execution / Agency**: ejecutar órdenes de clientes con mínimo impacto (best execution).
- **Proprietary (prop) trading**: la firma opera su propio capital.
- **Market making**: proveer liquidez cotizando bid/ask.
- **Algorítmico / HFT (High-Frequency Trading)**: sistemas automatizados de alta velocidad que
  aprovechan micro-ineficiencias; representa una fracción mayoritaria del volumen en mercados
  desarrollados. Requiere infraestructura de baja latencia (co-location, FPGA).
- **Quant / systematic**: señales derivadas de modelos estadísticos/ML.

## Mesa (desk) y organización
- Mesas por activo (equity desk, rates desk, FX desk), **front office** (genera P&L) vs
  **middle/back office** (riesgo, clearing, settle). Brokers y exchanges (p.ej. NYSE, Nasdaq,
  CME) proveen venues y matching.

## Riesgos y regulación
- Riesgo de mercado, de liquidez, **flash crashes**, y controles (pre-trade/post-trade).
- Regulación: **MiFID II** (UE), **Reg NMS** / **Dodd-Frank** (EE.UU.) sobre transparencia y
  acceso a mercados.

## Relación con otras capas
- vs `dominio/mercados-financieros`, `dominio/aprendizaje-automatico` (trading algorítmico),
  `dominio/derivados`, `dominio/banca-de-inversion` (sales & trading).
- Roles: `rol/head-of-trading` implícito, `rol/quant-research` implícito, `rol/risk-manager`.

## Fuentes
- Trading strategy (Wikipedia): <https://en.wikipedia.org/wiki/Trading_strategy>
- High-frequency trading (Wikipedia): <https://en.wikipedia.org/wiki/High-frequency_trading>
