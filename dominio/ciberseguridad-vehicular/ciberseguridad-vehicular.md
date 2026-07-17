---
titulo: Ciberseguridad vehicular
capa: dominio
tema: ciberseguridad-vehicular
fuente: https://en.wikipedia.org/wiki/Automotive_security
fuente2: https://www.iso.org/standard/77382.html
fecha: 2026-07-17
confianza: alta
tags: [ciberseguridad, automotriz, vehicular, iso-sae-21434, un-r155, ecu, v2x, ciberseguridad-ot]
organizaciones: [UNECE-WP29, ISO, SAE, NHTSA, fabricantes-OEM]
responsabilidades: [seguridad-de-producto, ciberseguridad-de-producto, cumplimiento-regulatorio]
profundidad: 2
estado: profundo
---

# Ciberseguridad vehicular

La **ciberseguridad vehicular** (automotive security) es la rama de la seguridad
informática centrada en los riesgos cibernéticos del contexto automotriz. El
creciente número de **ECUs** (unidades de control electrónico) en los vehículos y la
implantación de múltiples medios de comunicación remota e inalámbica hacia/desde el
vehículo hicieron necesaria una rama de ciberseguridad dedicada a las amenazas
asociadas al automóvil. No debe confundirse con la **seguridad automotriz** (safety).

## Superficie de ataque
- **ECUs / buses CAN**: inyección de mensajes, spoofing.
- **Conectividad**: infotainment, cellular, Wi-Fi, Bluetooth, keyless entry.
- **V2X** (vehicle-to-everything): comunicación con infraestructura, otros
  vehículos, peatones.
- **OBD-II / actualizaciones OTA**: vectores de compromiso del firmware.

## Estándares y regulación
- **ISO/SAE 21434** (2021): estándar de ingeniería de ciberseguridad para la
  carretera; ciclo de vida del producto.
- **UN R155** (UNECE WP.29): reglamento que exige un **CSMS** (Cyber Security
  Management System) para la homologación; **UN R156** cubre actualizaciones de
  software (SUMS).
- **NHTSA** (EE.UU.) emite guías; la **NIST CSF** aplicable.

## Relevancia
- Vehículos autónomos y conectados amplían la superficie; un compromiso puede
  afectar seguridad física (recall remoto). Crítico para OEMs y Tier-1.

## Relación con otras capas
- vs `dominio/ciberseguridad-ot` (ICS/SCADA), `dominio/ciberseguridad`,
  `dominio/electromovilidad`, `dominio/automatizacion-procesos`.
- Sustrato: `sustrato/estados-unidos/industria-manufacturera`,
  `sustrato/mexico/industria-automotriz`.
- Rol: `rol/security-architect`, `rol/head-of-security-operations`,
  `rol/head-of-engineering`.

## Fuentes
- Automotive security (Wikipedia): <https://en.wikipedia.org/wiki/Automotive_security>
- ISO/SAE 21434: <https://www.iso.org/standard/77382.html>
