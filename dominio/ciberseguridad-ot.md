---
titulo: Ciberseguridad OT / industrial
capa: dominio
tema: ciberseguridad-ot
fuente: https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443
fuente2: https://en.wikipedia.org/wiki/Operational_technology
fecha: 2026-07-15
confianza: alta
tags: [ciberseguridad-ot, ics, scada, isa-iec-62443, nerc-cip, seguridad-industrial, it-ot, ics-scada]
profundidad: 2
estado: profundo
rol: [head-of-infrastructure, security-architect, ciso, plant-manager, head-of-manufacturing]
actividades: [seguridad-ot, monitoreo-de-ics, gestion-de-vulnerabilidades]
organizaciones: [isa, nerc, cisa, iec, nist]
responsabilidades: [proteccion-de-activos-industriales, continuidad-de-operacion]
tareas: [segmentacion-it-ot, evaluacion-de-riesgo-ot, respuesta-a-incidentes]
---

# Ciberseguridad OT / industrial

La **ciberseguridad OT (Operational Technology)** protege los **sistemas de control industrial (ICS)** — SCADA, PLC, DCS, RTU — que monitorean y controlan procesos físicos en plantas, redes eléctricas, agua, transporte y manufactura. Es una disciplina distinta de la `dominio/ciberseguridad` de TI: prioriza **disponibilidad y seguridad física** sobre confidencialidad, y los activos tienen ciclos de vida de décadas.

## Conceptos y arquitectura

- **OT vs TI:** la OT controla el mundo físico (válvulas, motores); la TI procesa datos. La convergencia IT/OT (IIoT, Industria 4.0) amplía la superficie de ataque.
- **ICS / SCADA:** Supervisory Control and Data Acquisition supervisa activos distribuidos; PLC ejecuta lógica en campo.
- **Purdue Model:** jerarquía de niveles (empresa → sitio → control → campo) usada para segmentación.
- **Amenazas:** ransomware a plantas, sabotaje (Stuxnet, Colonial Pipeline, ataques a agua), espionaje industrial.

## Estándares y regulación

- **ISA/IEC 62443:** familia de estándares para seguridad de ICS — zonas/conduits, modelo de madurez (CMMC-like), roles.
- **NERC CIP:** normas obligatorias en EE. UU./Canadá para la **red eléctrica** (Bulk Electric System); incumplimiento = multas.
- **NIST CSF / NIST 800-82:** guía de control industrial; CISA (EE. UU.) emite alertas y directivas.
- **Canadá:** el *Critical Cyber Systems Protection Act* y reguladores provinciales (ver `sustrato/canada/seguridad-nacional`).
- **México:** el **CERT-MX** y la Estrategia Nacional de Ciberseguridad; sectores críticos bajo la CNS (ver `sustrato/mexico/seguridad-publica`).

## Prácticas

- **Segmentación IT/OT** y *air gapping* donde sea posible.
- **Visibilidad:** inventario de activos OT, detección de anomalías (no firmas de TI).
- **Gestión de vulnerabilidades** con ventanas de mantenimiento (no parches arbitrarios).
- **Respuesta a incidentes** con enfoque en continuidad física.

## Relevancia para el negocio (MVAS)

- **Continuidad operativa:** un incidente OT paraliza producción y puede causar daño físico (ver `dominio/gestion-de-crisis`, `dominio/continuidad-del-negocio`).
- **Seguridad de la cadena:** ataques a proveedores críticos (ver `dominio/cadena-suministro`).
- **Cumplimiento:** NERC CIP y regulaciones de infraestructura crítica elevan el riesgo de multas (ver `dominio/cumplimiento-regulacion`).
- **Rol:** el `rol/head-of-infrastructure` y `rol/security-architect` deben gobernar la convergencia IT/OT.

## Conexiones

- `dominio/ciberseguridad` — seguridad de TI (complementaria).
- `dominio/forense-digital` — evidencia tras incidente.
- `dominio/seguridad-y-salud-ocupacional` — seguridad física de personas.
- `dominio/infraestructura` — activos críticos.
- `dominio/energia-distribuida` — DER y grid edge expuestos.

## Referencias

- [ISA — ISA/IEC 62443](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443)
- [NERC — Critical Infrastructure Protection (CIP)](https://www.nerc.com/pa/Stand/Pages/Critical-Infrastructure-Protection.aspx)
- [NIST — Guide to ICS Security (SP 800-82)](https://csrc.nist.gov/pubs/sp/800-82/r3/final)
