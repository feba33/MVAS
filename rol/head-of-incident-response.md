---
titulo: Head of Incident Response
capa: rol
tema: head-of-incident-response
fuente: https://en.wikipedia.org/wiki/Incident_management
fuente2: https://www.nist.gov/cyberframework
fecha: 2026-07-15
confianza: alta
tags: [head-of-incident-response, incident-response, csirt, ir, breach, containment, forense, ciberseguridad]
profundidad: 2
estado: profundo
rol: [head-of-incident-response, ciso, security-analyst, head-of-threat-intelligence, chief-compliance-officer]
actividades: [respuesta-a-incidentes, gestion-de-crisis, forense, comunicacion-de-crisis, cumplimiento]
organizaciones: [csirt, soc, empresa, reguladores, forense]
responsabilidades: [liderar-ir, containment, post-mortem, mejora-de-controles, notificacion]
tareas: [plan-de-respuesta, simulacros, triaje, coordinacion-con-forense, reporte-regulador]
---

# Head of Incident Response

El **Head of Incident Response** lidera la capacidad de la organización para **identificar, analizar y corregir incidentes** que amenazan operaciones, servicios o funciones —especialmente ciberincidentes. Un incidente es un evento que puede causar pérdida o interrupción; se gestiona vía un *Incident Response Team (IRT)*, *Incident Management Team (IMT)* o *Incident Command System (ICS)*. Sin gestión efectiva, un incidente puede interrumpir operaciones, seguridad de la información, sistemas TI, empleados o clientes. El rol es el puente entre la detección (SOC/threat intel) y la recuperación, e incluye la fase forense (ver `dominio/forense-digital`, `dominio/ciberseguridad`).

## Responsabilidades clave

- **Liderazgo del CSIRT/IR:** gobierno del equipo, *runbooks*, escalado y coordinación con SOC (ver `rol/security-analyst`, `rol/head-of-threat-intelligence`).
- **Fases (NIST SP 800-61):** *preparation, detection&analysis, containment/eradication/recovery, post-incident*.
- **Contención y erradicación:** aislar sistemas, detener la amenaza, restaurar con evidencia.
- **Comunicación de crisis:** coordinar con `dominio/gestion-de-crisis`, legales y *stakeholders*.
- **Notificación regulatoria:** plazos de brecha (GDPR 72h, LFPDPPP, LGPD, CCPA) (ver `dominio/proteccion-de-datos`).
- **Post-mortem:** *blameless RCA*, mejoras de control, *tabletop exercises*.

## Habilidades y toolkit

- **Frameworks:** NIST CSF/SP 800-61, MITRE ATT&CK, ISO/IEC 27035.
- **Plataformas:** SOAR, case management, *threat intel* feeds.
- **Forense:** adquisición y cadena de custodia (ver `dominio/forense-digital`).
- **Soft skills:** toma de decisiones bajo presión, comunicación ejecutiva.

## Relevancia para el negocio (MVAS)

- **Resiliencia:** reduce MTTR y alcance del daño; protege ingresos y continuidad (ver `dominio/gestion-del-riesgo`, `dominio/continuidad`).
- **Cumplimiento y legal:** evita multas por notificación tardía y respalda defensa (ver `dominio/cumplimiento-regulacion`).
- **Confianza:** protege reputación y datos de clientes (ver `dominio/proteccion-de-datos`).
- **Ciberseguros:** las aseguradoras exigen programas maduros de IR (ver `dominio/seguros`).
- **Paridad con pares:** distinto de `ciso` (estrategia) y `security-analyst` (ejecución de monitoreo); lidera la respuesta.

## Riesgos y tendencias

- **Ransomware y extorsión:** presión de pago vs recuperación e información.
- **Cadena de suministro:** incidentes de terceros requieren IR coordinado (ver `dominio/cadena-de-suministro`).
- **IA en IR:** automatización de triaje y *autonomous response*.
- **Regencia:** expectativas crecientes de reguladores y clientes sobre tiempos de respuesta.

## Conexiones

- `dominio/ciberseguridad` — SOC, detección, zero trust.
- `dominio/forense-digital` — evidencia y análisis post-breach.
- `dominio/gestion-de-crisis` — comunicación y coordinación.
- `dominio/proteccion-de-datos` — notificación de brechas.
- `rol/ciso`, `rol/security-analyst`, `rol/head-of-threat-intelligence` — ecosistema de seguridad.
- `dominio/continuidad` — recuperación de negocio.

## Referencias

- [Incident management — Wikipedia](https://en.wikipedia.org/wiki/Incident_management)
- [NIST SP 800-61 — Computer Security Incident Handling](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-61r2.pdf)
- [ISO/IEC 27035 — Information security incident management](https://www.iso.org/standard/44424.html)
- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)
- [MITRE ATT&CK](https://attack.mitre.org)
