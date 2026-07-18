---
titulo: Ciberseguridad de identidad (IAM, MFA, zero trust, cuentas privilegiadas)
capa: dominio
tema: ciberseguridad-de-identidad
fuente: https://en.wikipedia.org/wiki/Identity_management
fuente2: https://www.nist.gov/itl/applied-cybersecurity/nice/resources/glossary
fecha: 2026-07-18
confianza: alta
tags: [ciberseguridad, identidad, iam, mfa, zero-trust, privilegios, gestion-de-identidad]
english_keywords: [identity security, IAM, MFA, zero trust, PAM, privileged access]
---

# Ciberseguridad de identidad (IAM, MFA, zero trust, cuentas privilegiadas)

## 📝 Conocimiento

### Definición
- Disciplina de seguridad centrada en **gestionar, proteger y verificar identidades**
  (humanas y de máquina/servicio) y sus accesos. Es el núcleo del modelo **Zero Trust**
  ("never trust, always verify"): la identidad es el nuevo perímetro.

### Componentes
- **IAM (Identity & Access Management):** autenticación, autorización, provisioning/
  deprovisioning, directorio (AD/Entra ID), SSO.
- **MFA / 2FA:** factor de conocimiento + posesión + inherencia; mitiga credenciales
  filtradas. FIDO2/passkeys reducen phishing.
- **PAM (Privileged Access Management):** controla cuentas con privilegios elevados
  (admin, root, service accounts) — objetivo principal de atacantes (movimiento lateral).
- **IGA (Identity Governance & Administration):** ciclo de vida, certificaciones de
  acceso, segregación de funciones (SoD), compliance (SOX, GDPR).

### Riesgos y controles
- **Credential theft / phishing / lateral movement:** el 80%+ de brechas involucran
  identidades comprometidas.
- **Postura:** principio de mínimo privilegio, JIT (just-in-time) access, vaulting de
  secretos, monitorización de sesiones, detección de anomalías por UEBA.

## 🔗 Relaciones
- **vs dominio/seguridad-de-aplicaciones:** identidad habilita el acceso; AppSec protege
  el código. Complementarios en SDLC.
- **vs dominio/proteccion-de-datos:** el control de acceso es el primer muro de la
  privacidad.
- **vs rol/head-of-platform-security:** las plataformas implementan IAM/Zero Trust.

## 📚 Fuentes
- Wikipedia — Identity management.
- NIST — NICE cybersecurity glossary / identity concepts.
- Reference-only: se citan URLs; no se copió contenido íntegro.
