---
titulo: Open Banking / Open Finance
capa: dominio
tema: open-banking
fuente: https://en.wikipedia.org/wiki/Open_banking
fuente2: https://www.banxico.org.mx/
fecha: 2026-07-15
confianza: alta
tags: [open-banking, open-finance, apis, fintech, psd2, pagos, datos-financieros, competition]
english_keywords: [open banking, open finance, APIs, PSD2, open data, fintech, data sharing, account aggregation, payment initiation]
profundidad: 2
estado: profundo
---

# Open Banking / Open Finance

## 📝 Conocimiento
- **Definición:** modelo en el que las instituciones financieras comparten datos de sus
  clientes con terceros autorizados (TPP — *third-party providers*: proveedores de pagos,
  prestamistas, aseguradoras) a través de **APIs seguras**, con el **consentimiento
  explícito** del cliente. Sustituye el acceso por *screen-scraping* (credenciales
  compartidas) por un intercambio estandarizado y auditable. (Wikipedia — Open banking)
- **Tres pilares de datos (modelo México, Ley Fintech 2018, Art. 76):**
  1. **Datos abiertos** — información pública de productos y servicios (sucursales,
     cajeros, comisiones, tasas). No requieren consentimiento.
  2. **Datos agregados** — estadísticas anonimizadas sobre operaciones.
  3. **Datos transaccionales** — información de cuentas y movimientos del cliente.
     Requieren consentimiento explícito, autenticación reforzada y trazabilidad completa.
- **PSD2 (Unión Europea, Directiva (UE) 2015/2366, vigente 2018/2019):** crea las
  figuras de AISP (agregador de cuenta) y PISP (iniciador de pago), impone *Strong
  Customer Authentication* (SCA) con exenciones, y busca un mercado único de pagos.
  Es la base del open banking europeo y del *Open Finance Framework* posterior.
- **Brasil Open Finance (Resolução Conjunta BCB/CMN nº 1/2020):** uno de los
  ecosistemas más avanzados del mundo — **>800 instituciones participantes** y **~30
  millones de consentimientos** (2026); cubre banca, pagos vía **Pix**, seguros e
  inversiones. Referente en LATAM. (Fiskil Open Finance Tracker)
- **México:** la **Ley Fintech (2018, Art. 76)** fue pionera en LATAM al mandar APIs
  estandarizadas de intercambio de datos; sin embargo su implementación es parcial y
  retrasada: la CNBV solo publicó reglas para **datos abiertos** (cajeros/sucursales,
  2020); las reglas de datos agregados y transaccionales seguían sin publicar en 2026
  (con amparos por incumplimiento de plazos). Banxico lidera un **Open Finance** más
  amplio que PSD2 (cubre datos de producto, agregados y transaccionales).
- **Modelo de negocio / casos:** comparación de productos financieros, agregación de
  cuentas, préstamos pre-calificados, pagos iniciados por TPP (PISP), *underwriting*
  basado en datos en tiempo real, visión 360° del cliente. Habilita competencia,
  reduce costos de adquisición y fomenta la **inclusión financiera**.
- **Estándares de intercambio:** FDX (Financial Data Exchange, EE.UU.), Berlin Group
  (UE), DICT (Brasil), y los perfiles de la CNBV/Banxico. La interoperabilidad y la
  portabilidad de datos son clave.
- **Riesgos y gobernanza:** privacidad y seguridad de las APIs, consentimiento
  revocable, responsabilidad por fraude, trazabilidad, y mitigación de lock-in. Se
  entrelaza con `dominio/proteccion-de-datos`, `dominio/ciberseguridad` y
  `dominio/regtech`.
- **Open Finance vs Open Banking:** "Open Banking" enfatiza pagos y datos de cuenta;
  "Open Finance" extiende a préstamos, seguros, inversiones y patrimonio — el
  movimiento actual de mayor alcance. Relación estrecha con `dominio/pagamentos` y
  `dominio/embedded-finance`.

## 🔗 Referencia
- Wikipedia — *Open banking* (reference-only).
- Banco de México / CNBV — Ley Fintech 2018 (Art. 76) y circulares de Open Finance.
- UE — Directiva (UE) 2015/2366 (PSD2); Brasil BCB Res. Conjunta 1/2020 (Open Finance).
- Fiskil — *Open Finance Tracker* (LatAm status, 2026).
- Cross-ref: `dominio/fintech`, `dominio/pagamentos`, `dominio/embedded-finance`,
  `dominio/servicios-financieros`, `dominio/regtech`, `dominio/proteccion-de-datos`,
  `dominio/ciberseguridad`, `sustrato/mexico/banca-sistema-financiero`.
