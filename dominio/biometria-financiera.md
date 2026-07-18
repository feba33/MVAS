---
titulo: Biometría financiera
capa: dominio
tema: biometria-financiera
fuente: https://gdpr-info.eu/issues/biometric-data/
fuente2: https://www.kyc360.com/resources/biometric-authentication/
fecha: 2026-07-18
confianza: alta
tags: [biometria, kyc, autenticacion, identidad-digital, fraude, privacidad]
profundidad: 2
estado: profundo
---

# Biometría financiera

## Definición
Uso de rasgos biológicos (huella, rostro, voz, iris) para **autenticación** e
**identidad** en servicios financieros: onboarding **KYC**, autorización de pagos y
detección de fraude. Es un subcampo de `dominio/biometria` aplicado a finanzas.

## Aplicaciones
- **KYC biométrico / eKYC:** verificación de identidad remota (véase
  `dominio/pld-uif`, `dominio/regtech`).
- **Autenticación en pagos y banca móvil** (FaceID, huella).
- **Detección de fraude** por comportamiento biométrico (behavioral biometrics).

## Riesgos y regulación
- **Datos biométricos = categoría especial** bajo GDPR (Art. 9) y muchas leyes
  (LFPDPPP en MX, PIPEDA en CA): consentimiento explícito, prohibiciones en algunas
  jurisdicciones (bans locales en EE.UU.).
- Riesgo de robo de plantillas (no se puede "resetear" una huella).
- Converge con `dominio/proteccion-de-datos` y `dominio/fintech`.

## Fuentes
- GDPR — Biometric data (gdpr-info.eu).
- KYC360 / regulatory resources (kyc360.com).
