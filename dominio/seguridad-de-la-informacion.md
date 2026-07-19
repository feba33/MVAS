---
titulo: Seguridad de la información
capa: dominio
tema: ciberseguridad
fuente: https://en.wikipedia.org/wiki/Information_security
fuente2: https://www.iso.org/isoiec-27001-information-security.html
fecha: 2026-07-19
confianza: alta
tags: [seguridad-informacion, cia, confidencialidad, integridad, disponibilidad, controles]
rol: []
actividades: []
organizaciones: [iso, nist]
responsabilidades: []
tareas: []
profundidad: 2
estado: profundo
---

# Seguridad de la información

## Definición
Disciplina que protege la información —en cualquier forma— para preservar su
**confidencialidad, integridad y disponibilidad (triada CIA)**, además de
autenticidad, trazabilidad y no repudio. Es más amplia que la ciberseguridad (que
cubre activos digitales/conectados).

## Triada CIA y objetivos
- **Confidencialidad**: solo quien debe accede (cifrado, control de acceso, mínimo
  privilegio).
- **Integridad**: sin alteración no autorizada (hashes, firmas, controles de cambio).
- **Disponibilidad**: acceso oportuno (resiliencia, backups, redundancia).

## Marcos y controles (NA)
- **ISO/IEC 27001**: ISMS certificable; Anexo A con 93 controles (2022).
- **NIST SP 800-53 / CSF 2.0**: controles e identificación de riesgos.
- **ISO/IEC 27002**: guía de controles; **27701**: privacidad (PII).
- Clasificación de la información (pública/restringida/confidencial/secreta) y
  *data loss prevention* (DLP), *rights management*.

## Gestión de riesgos
Identificar → valorar → tratar (mitigar/transferir/aceptar) → monitorear. Converge
con `gestion-de-riesgos` (ISO 31000) y `ciberseguridad-gobierno` (ISO 27001/27002).

## Relación con otros nodos
Base de `ciberseguridad`, `ciberseguridad-gobierno`, `ciberseguridad-para-ot-y-ics`,
`privacidad`/`lpdp` y `seguridad-nacional`. Alimenta roles de CISO y
`head-of-regulatory-affairs` (datos).

## Referencias
- Information security (Wikipedia EN) — https://en.wikipedia.org/wiki/Information_security
- ISO/IEC 27001 — https://www.iso.org/isoiec-27001-information-security.html
- NIST CSF 2.0 — https://www.nist.gov/cyberframework
