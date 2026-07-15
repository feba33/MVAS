---
titulo: Embedded Finance / Banking as a Service
capa: dominio
tema: embedded-finance
fuente: https://www.alloy.com/guides/understanding-embedded-finance
fuente2: https://sdk.finance/blog/embedded-finance-solutions-how-businesses-are-integrating-financial-services/
fecha: 2026-07-15
confianza: alta
tags: [embedded-finance, baas, pagos, prestamos, seguros, fintech, integracion, api]
english_keywords: [embedded finance, banking as a service, BaaS, embedded payments, embedded lending, embedded insurance, API, fintech infrastructure]
profundidad: 2
estado: profundo
---

# Embedded Finance / Banking as a Service

## 📝 Conocimiento
- **Definición:** integración de **servicios financieros** (pagos, préstamos, cuentas,
  tarjetas, seguros) **dentro de productos no financieros** (e-commerce, marketplaces,
  super-apps, telecom, SaaS, flotas de vehículos) mediante APIs, sin que el usuario
  "vaya al banco". Elige el momento y el contexto de la transacción. (Alloy; sdk.finance)
- **Banking as a Service (BaaS):** capa de infraestructura que permite a una empresa
  no bancaria ofrecer productos regulados apoyada en un **banco patrocinador**
  (*sponsor bank*) que aporta la licencia bancaria y la cuenta nácle. La empresa no
  regulada maneja UX, adquisición y marca; el banco patrocinador cubre el *charter*.
  (Wikipedia — *Banking as a service*)
- **Cuatro modalidades principales:**
  1. **Embedded payments** — checkout nativo, wallets, split payments, P2P dentro de la
     plataforma (ver `dominio/pagamentos`).
  2. **Embedded lending** — financiamiento en el punto de venta (*BNPL*, crédito
     comercial), pre-aprobado con datos de la plataforma.
  3. **Embedded insurance** — *embedded insurance* / *insurance-as-a-service*,
     pólizas contextuales (viaje, logística, devices).
  4. **Embedded banking** — cuentas, tarjetas y tesorería para vendedores/usuarios
     (ej. cuentas de pago para conductores o vendedores de marketplace).
- **Arquitectura:** orquestador de identidad/KYC, motor de decisiones, core bancario
  empaquetado (*white-label*), emisión de tarjetas, procesamiento de pagos y
  *ledger*; expuesto vía APIs a los canales de la empresa no financiera. Proveedores
  típicos: BaaS platforms, PSPs, EMIs, neobancos con API.
- **¿Por qué crece?:** reduce fricción en el checkout, eleva conversión y LTV, genera
  nuevas líneas de comisión (*interchange*, *float*, *spread* de crédito) y aprovecha
  datos de comportamiento que el banco tradicional no tiene. Es la evolución natural de
  `dominio/open-banking` (los datos abiertos alimentan experiencias embebidas).
- **Riesgos y cumplimiento:** KYC/KYB, AML y *monitoring* transaccional, responsabilidad
  de la licencia (sponsor bank), protección de datos, y dependencia de terceros
  (*concentration risk*). Relación con `dominio/regtech`, `dominio/proteccion-de-datos`
  y `dominio/ciberseguridad`.
- **Ecosistema:** bancos patrocinadores, fintechs de infraestructura, marketplaces y
  super-apps (transporte, delivery, gobierno). Converge con `dominio/fintech` y
  `dominio/servicios-financieros`.

## 🔗 Referencia
- Alloy — *Understanding Embedded Finance* (guía).
- sdk.finance — *Embedded Finance Guide* (arquitectura y casos, 2026).
- Wikipedia — *Banking as a service* (reference-only).
- Cross-ref: `dominio/fintech`, `dominio/open-banking`, `dominio/pagamentos`,
  `dominio/servicios-financieros`, `dominio/regtech`, `dominio/proteccion-de-datos`,
  `dominio/ciberseguridad`.
