---
titulo: Pagamentos (Payment Rails)
capa: dominio
tema: pagamentos
fuente: https://en.wikipedia.org/wiki/Payment
fuente2: https://en.wikipedia.org/wiki/FedNow
fecha: 2026-07-15
confianza: alta
tags: [pagos, payment-rails, tarjetas, ach, rtps, pix, sepa, instant-payments, bancos]
english_keywords: [payments, payment rails, credit cards, ACH, RTP, FedNow, Pix, SEPA, instant payments, wire, SWIFT]
profundidad: 2
estado: profundo
---

# Pagamentos (Payment Rails)

## 📝 Conocimiento
- **Definición:** un pago es la entrega de algo de valor (dinero) por una parte
  (pagador) a otra (beneficiario) a cambio de bienes/servicios o para cumplir una
  obligación. Los **payment rails** son las redes/infraestructuras que mueven el dinero
  entre instituciones. (Wikipedia — *Payment*, *FedNow*)
- **Tarjetas (cards):** Visa / Mastercard / Amex — red de autorización de 4 partes
  (titular, comercio, emisor, adquirente); dominan el consumo y el e-commerce.
- **ACH (Automated Clearing House, EE.UU.):** red *batch* para pagos domésticos de
  bajo valor (nómina, débitos directos). Eficiente y de bajo costo. (Wikipedia — *ACH*)
- **RTP (Real-Time Payments, The Clearing House, EE.UU.):** primer rail de **pagos
  instantáneos** 24/7/365 en EE.UU.; contraparte del FedNow.
- **FedNow (Federal Reserve, lanzado 20-jul-2023):** servicio de **pagos instantáneos**
  del Fed para instituciones en EE.UU.; las instituciones construyen productos encima.
  (Federal Reserve; Wikipedia — *FedNow*)
- **Pix (Brasil, Banco Central do Brasil):** plataforma de pagos instantáneos
  (2020) que permite transferencias 24/7 en reales, sin interrupciones ni comisiones
  para personas; las personas jurídicas pueden tener comisiones. Es el rail instantáneo
  más adoptado de LATAM y base del Open Finance brasileño. (Wikipedia — *Pix (payment system)*)
- **SEPA (Single Euro Payments Area, UE):** integración de transferencias en euros
  entre 41 miembros (2025: 27 UE + EFTA + Reino Unido + candidatos). Simplifica el
  pago minorista en euros. (Wikipedia — *Single Euro Payments Area*)
- **Wire / SWIFT:** pagos de alto valor y transfronterizos (Fedwire, SWIFT gpi);
  rápidos pero más caros; columna del comercio internacional.
- **SPEI (México, Banxico):** red de pagos electrónicos interbancarios en tiempo
  real; clave del sistema de pagos mexicano. Ver `sustrato/mexico/banca-sistema-financiero`.
- **Stablecoins / blockchain:** rails emergentes (USD stablecoins en L2) para
  liquidación programable — ver `dominio/blockchain`.
- **Tendencia:** convergencia de rails en **pagos instantáneos** siempre activos,
  interoperabilidad (p.ej. Brasil Transferencias 3.0), y la capa de **open/embedded
  finance** por encima de los rails — ver `dominio/open-banking` y
  `dominio/embedded-finance`.

## 🔗 Referencia
- Wikipedia — *Payment*, *FedNow*, *Pix (payment system)*, *Single Euro Payments Area*,
  *Automated Clearing House* (reference-only).
- Federal Reserve — FedNow; Banco Central do Brasil — Pix; Banxico — SPEI.
- Cross-ref: `dominio/open-banking`, `dominio/embedded-finance`, `dominio/fintech`,
  `dominio/banca`, `dominio/blockchain`, `dominio/servicios-financieros`,
  `sustrato/mexico/banca-sistema-financiero`.
