---
titulo: Ciberseguridad de datos
capa: dominio
tema: ciberseguridad-de-datos
fuente: https://en.wikipedia.org/wiki/Data_security
fuente2: https://csrc.nist.gov/ (NIST SP 800-53)
fecha: 2026-07-20
confianza: alta
tags: [ciberseguridad, data-security, cifrado, dlp, clasificacion]
rol: [ciso, head-of-security-architecture, head-of-data-strategy]
actividades: [proteccion-de-datos, cifrado, prevencion-de-perdida]
organizaciones: [nist, iso, cisa]
responsabilidades: [seguridad-de-datos, gobierno-de-datos]
tareas: []
profundidad: 2
estado: profundo
---

# Ciberseguridad de datos

La **ciberseguridad de datos** protege la confidencialidad, integridad y disponibilidad de
los datos en reposo, en tránsito y en uso. Complementa (no sustituye) la protección legal de
datos personales.

## Controles principales
- **Cifrado:** simétrico/asimétrico, en reposo y en tránsito; gestión de claves (KMS/HSM).
- **DLP (Data Loss Prevention):** clasificación y bloqueo de exfiltración.
- **Clasificación y etiquetado:** sensibilidad (público/confidencial/secreto).
- **Control de acceso:** mínimo privilegio, ABAC/RBAC, tokenización, enmascaramiento.

## Marcos
- **NIST SP 800-53 / 800-171**, **ISO/IEC 27001**, **CIS Controls**.
- Integra con gobierno de datos y gestión de identidades.

## Riesgos
Fugas, ransomware, errores de configuración en la nube, y pérdida de claves. La exfiltración
es el vector de mayor impacto tras el acceso inicial.

## Cross-refs
- `dominio/proteccion-de-datos-personales`, `dominio/ciberseguridad-de-identidad`,
  `dominio/seguridad-de-la-informacion`, `dominio/gobierno-de-datos`,
  `rol/head-of-vulnerability-management`, `rol/ciso`.
