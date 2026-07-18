---
titulo: Ciberseguridad OT
capa: dominio
tema: ciberseguridad-de-ot
fuente: https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series
fuente2: https://www.nerc.com/pa/Stand/Reliable%20Grid%20Initiative%20(NERC%20CIP)/Pages/default.aspx
fecha: 2026-07-18
confianza: alta
tags: [ciberseguridad, ot, ics, scada, 62443, nerc-cip, industrias]
profundidad: 2
estado: profundo
---

# Ciberseguridad OT (Tecnología Operacional)

## Definición
La ciberseguridad **OT** protege los sistemas de control industrial (**ICS/SCADA**) que
supervisan y controlan procesos físicos: plantas eléctricas, agua, petróleo,
manufactura, transporte. A diferencia de IT, la disponibilidad y seguridad física
priman sobre la confidencialidad.

## Estándares y marcos
- **ISA/IEC 62443:** serie de estándares para seguridad de sistemas de control
  industrial (zonas/conduits, defensa en profundidad, gestión de riesgos).
- **NERC CIP:** normas obligatorias de ciberseguridad para el **grid eléctrico** de
  Norteamérica (EE.UU./Canadá).
- **NIST SP 800-82:** guía de seguridad ICS.

## Diferencias vs IT
- Ciclo de vida de décadas; dispositivos legacy sin parches.
- Consecuencias físicas (seguridad humana, medio ambiente).
- Convergencia IT/OT vía IIoT aumenta la superficie de ataque.

## Relación con otras capas
- Profundiza `dominio/ciberseguridad-industrial` y converge con
  `dominio/ciberdefensa`, `dominio/ciberseguridad-cloud`.
- Apoya `sustrato/*/energia`, `dominio/manufactura`.

## Fuentes
- ISA — ISA/IEC 62443 series (isa.org).
- NERC — CIP Standards (nerc.com).
