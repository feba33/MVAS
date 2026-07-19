---
titulo: Head of Payments Risk
capa: rol
tema: head-of-payments-risk
fuente: https://en.wikipedia.org/wiki/Payment_fraud
fuente2: https://www.fincen.gov
fecha: 2026-07-19
confianza: media
tags: [rol, payments-risk, fraude-pagos, aml, kyf, chargebacks, compliance]
profundidad: 2
estado: profundo
---

# Head of Payments Risk

El Head of Payments Risk dirige la gestión del riesgo de fraude y cumplimiento en los sistemas de pago (card, ACH, wires, wallets, stablecoins). Es la intersección de `rol/head-of-payments` (rails/operación) y `rol/head-of-fraud-prevention`, con fuerte componente regulatorio (AML/KYC).

## Responsabilidades
- **Detección de fraude:** modelos de scoring, reglas, y monitoring en tiempo real (transacciones, cuenta-a-cuenta).
- **Chargebacks y disputas:** gestión de reclamaciones y prevención (reducción de friendly fraud).
- **AML/KYC en pagos:** monitoreo de lavado, SAR/CTR filings (FinCEN en EE.UU.; FINTRAC en Canadá; UIF en MX).
- **Cumplimiento de sanciones:** listas OFAC, y screening de contrapartes.

## Habilidades y métricas
- False-positive rate, fraud loss rate, chargeback ratio (Visa/Mastercard thresholds), y tiempo de resolución.
- Reporta a CRO, Head of Payments, o Compliance; colabora con `rol/head-of-financial-risk`.

## Diferenciación
- vs. `rol/head-of-fraud-prevention`: foco específico en el flujo de pagos (no solo cuenta/identidad).
- vs. `rol/head-of-payments`: este entrega rails; Payments Risk protege los rails.

## Relación con otras capas
- **Dominio:** `dominio/fintech-regulatorio`, `dominio/seguridad-de-la-informacion`, `dominio/ciberseguridad-de-aplicaciones`.
- **Rol:** `rol/head-of-payments`, `rol/head-of-fraud-prevention`, `rol/head-of-financial-risk`.
- **Org:** `organizacion/Nolvorn` (riesgo de pagos).

## Fuentes
- Payment fraud — Wikipedia EN.
- FinCEN (BSA/AML) — fincen.gov.
