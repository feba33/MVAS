---
titulo: Ciberseguridad OT/ICS industrial (Purdue, ISA/IEC 62443, NERC CIP)
capa: dominio
tema: ciberseguridad
fuente: https://en.wikipedia.org/wiki/Industrial_control_system
fecha: 2026-07-19
confianza: alta
tags: [ciberseguridad, ot, ics, scada, isa-62443, nerc-cip, industria]
rol: []
actividades: []
organizaciones: [isa, nerC, cisa, industrias]
responsabilidades: []
tareas: []
profundidad: 2
estado: profundo
---

# Ciberseguridad OT/ICS industrial (Purdue, ISA/IEC 62443, NERC CIP)

## Definición
La ciberseguridad de sistemas de control industrial (ICS — Industrial Control Systems) protege los entornos **OT** (Operational Technology) que gobiernan procesos físicos: SCADA, DCS, PLC, RTU. Difiere de IT porque prioriza **disponibilidad y seguridad física** sobre confidencialidad.

## Arquitectura de referencia
- **Purdue Enterprise Reference Architecture (PERA)**: modelo de 6 niveles que separa niveles de control (0-1), supervisión (2-3) y enterprise (4-5). La segmentación entre IT y OT es el primer control.
- **ISA/IEC 62443**: estándar de seguridad de sistemas de control; introduce zonas/conduits, *security levels* (SL) y el modelo de *defense-in-depth*.

## Marco regulatorio (Norteamérica)
- **EE.UU.**: **NERC CIP** (Critical Infrastructure Protection) obligatorio para el sector eléctrico; guía de **CISA** (IC3, CPG). TSA también emite directivas para pipelines/ferrocarriles.
- **Canadá**: alineado con NERC CIP (hydro/transmisión); guía de CCCS (Centre for Cyber Security).
- **México**: CENACE/CRE en energía; CSIRT México en incidentes.

## Amenazas y controles
Riesgos: ransomware a PLC, manipulación de proceso, acceso remoto no gestionado. Controles: gestión de accesos, monitorización de red OT, parcheo controlado, respuesta a incidentes (ver head-of-incident-response).

## Referencias
- Industrial control system (Wikipedia EN) — https://en.wikipedia.org/wiki/Industrial_control_system
- ISA/IEC 62443 — https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443
- NERC CIP — https://www.nerc.com/pa/Stand/Pages/Critical-Infrastructure-Protection.aspx
