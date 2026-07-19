---
titulo: Head of Incident Response
capa: rol
tema: ciberseguridad
fuente: https://en.wikipedia.org/wiki/Computer_security_incident_management
fuente2: https://www.nist.gov/cyberframework
fecha: 2026-07-19
confianza: alta
tags: [incident-response, csirt, respuesta-a-incidentes, runbooks, crisis, post-mortem, seguridad]
rol: [head-of-incident-response]
actividades: [respuesta-a-incidentes, crisis-management]
organizaciones: [nist, sans-institute]
responsabilidades: [respuesta-a-incidentes, csirt, gestion-de-crisis]
tareas: [contencion, erradicacion, recuperacion, post-mortem]
profundidad: 2
estado: profundo
---

# Head of Incident Response

El **Head of Incident Response** dirige la capacidad de **respuesta a incidentes de
seguridad** de la organización: la detección, contención, erradicación y recuperación ante
brechas, malware, ransomwares y abusos. Lidera el **CSIRT** (Computer Security Incident
Response Team) y coordina la respuesta con negocio, legal, comunicaciones y autoridades.

## Responsabilidades
- **Detección y triage:** clasificación de alertas (SOC, EDR, SIEM), priorización (CVSS,
  impacto/likelihood).
- **Contención, erradicación, recuperación:** ejecución de runbooks, aislamiento,
  restauración desde backups inmutables.
- **Crisis management:** war room, comunicación de incidentes, notificaciones
  regulatorias (brechas de datos: GDPR/Art.33, Ley 21.719 CL, reguladores sectoriales).
- **Post-mortem / lessons learned:** análisis sin culpa, mejoras de controles.
- **Planificación:** simulacros (tabletop), playbooks, ejercicios rojos/azules.

## Reporta y se relaciona
Reporta al CISO / Head of Platform Security o CIO. Colabora con `rol/head-of-platform-security`,
`rol/head-of-it-security`, `rol/head-of-information-security` y `rol/compliance-officer`.
Se diferencia de `rol/head-of-business-resilience` (BCP/DR de continuidad) por el foco en
seguridad activa.

## Marco de referencia
**NIST SP 800-61** (Computer Security Incident Handling Guide), SANS PICERL
(Preparation, Identification, Containment, Eradication, Recovery, Lessons Learned),
MITRE ATT&CK para detección.

## Relación con otras capas
- De `dominio/ciberseguridad` y `dominio/seguridad-de-la-informacion-empresarial`.
- Vincula con `rol/head-of-platform-security`, `rol/head-of-it-security`, `rol/head-of-business-resilience`.
