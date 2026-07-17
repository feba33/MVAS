---
titulo: Ciberseguridad de la información
capa: dominio
tema: ciberseguridad-de-la-informacion
fuente: https://www.nist.gov/cyberframework
fuente2: https://www.nist.gov/cybersecurity
fecha: 2026-07-17
confianza: alta
tags: [infosec, cia, vulnerabilidades, GRC, NIST, seguridad-de-la-informacion]
organizaciones: [NIST, ISO, MITRE, (ISC)2]
rol: [head-of-information-security, ciso, security-analyst, head-of-risk-and-compliance]
profundidad: 2
estado: profundo
---

# Ciberseguridad de la información

La **ciberseguridad de la información** (InfoSec) protege la confidencialidad, integridad y
disponibilidad de la información (el **modelo CIA**), abarcando datos, sistemas y personas,
independientemente de la amenaza (ciber o física).

## Fundamentos
- **Tríada CIA:** Confidentiality (acceso solo autorizado), Integrity (precisión/integridad),
  Availability (acceso cuando se necesita).
- **Gestión de vulnerabilidades:** descubrimiento, priorización (CVSS), remediación y
  verificación continua; apoyada en el **NVD** (National Vulnerability Database, NIST).
- **Gobierno, Riesgo y Cumplimiento (GRC):** marcos que alinean seguridad con el negocio y la
  normativa (ISO 27001, NIST CSF 2.0, SOC 2, PCI-DSS).
- **Defensa por capas / Zero Trust:** verificación continua, mínima confianza, microsegmentación.

## Disciplinas
Gestión de identidades (IAM), cifrado, gestión de parches, respuesta a incidentes (CSIRT),
seguridad de aplicaciones (AppSec), seguridad de datos y continuidad (ver
`dominio/seguridad-corporativa`). El **MITRE ATT&CK** es la matriz de tácticas/telemetría
de adversario.

## Diferenciación
Distinto de `dominio/ciberseguridad` (disciplina amplia: redes, SOC, threat intel) y
`dominio/seguridad-corporativa` (física/crisis); InfoSec se centra en **protección de la
información y su gobierno**. Las certificaciones clave: CISSP, CISM, CISA.

## Relación
Cruza con `dominio/proteccion-de-datos` (privacidad/GDPR), `dominio/ciberseguridad-ot`
(ICS/OT) y `rol/head-of-information-security`.
