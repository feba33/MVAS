---
titulo: Ciberseguridad de endpoints
capa: dominio
tema: ciberseguridad
fuente: https://www.cisa.gov/ (Cybersecurity & Infrastructure Security Agency, US)
fuente2: https://attack.mitre.org/ (MITRE ATT&CK)
fecha: 2026-07-19
confianza: alta
tags: [ciberseguridad, endpoints, edr, dominio]
organizaciones: [cisa, mitre, gobierno-de-eeuu]
profundidad: 2
estado: profundo
---

# Ciberseguridad de endpoints (Endpoint Security)

La **seguridad de endpoints** protege dispositivos finales (laptops, móviles,
servidores, IoT) contra amenazas. Es la capa más expuesta de la red corporativa y
el vector inicial en la mayoría de las intrusiones (phishing, malware, ransomware).

## Componentes
- **Antivirus / antimalware** tradicional (firma + heurística).
- **EDR (Endpoint Detection & Response)**: telemetría continua, detección de
  comportamiento, cacería de amenazas y respuesta automatizada.
- **MDM / UEM** (Mobile Device Management): políticas en dispositivos móviles.
- **Hardening**: deshabilitar servicios innecesarios, parches, control de aplicaciones.
- **Cifrado de disco** (BitLocker, FileVault) y **DLP** en endpoints.

## Frameworks de referencia
- **MITRE ATT&CK** (matriz Enterprise): técnica de adversarios por etapa.
- **NIST 800-53 / CSF 2.0**, **CIS Controls** (Control 7: protección de endpoints).
- **CISA** (EE.UU.) publica guías de *endpoint detection* y respuesta a ransomware.

## Operación
- Telemetría centralizada en un **SOC**; integración con SIEM/XDR.
- **Zero Trust**: identidad + postura del dispositivo antes de conceder acceso.

## Relación con otras capas
- vs `dominio/ciberseguridad` (general), `dominio/ciberseguridad-de-aplicaciones`,
  `dominio/ciberseguridad-de-la-informacion`, `dominio/ciberseguridad-cloud`.
- Converge con `rol/head-of-application-security`, `rol/head-of-platform-security`.

## Referencias
- CISA: Endpoint Security guidance.
- MITRE ATT&CK Enterprise.
- NIST SP 800-53 Rev.5.
