---
titulo: Ciberseguridad de aplicaciones (AppSec)
capa: dominio
tema: application-security
fuente: https://owasp.org/Top10/
fuente2: https://owasp.org/www-community/attacks/
fecha: 2026-07-18
confianza: alta
tags: [ciberseguridad, appsec, owasp, sast, dast, devsecops, sdlc-seguro, threat-modeling]
profundidad: 2
estado: profundo
---

# Ciberseguridad de aplicaciones (AppSec)

## Definición
La ciberseguridad de aplicaciones protege el software en todas las fases del ciclo de vida (SDLC) — desde el diseño hasta la operación — frente a vulnerabilidades de código y configuración. Es una disciplina dentro de la ciberseguridad que se centra en la **capa aplicación**, a diferencia de la red o el endpoints.

## Prácticas centrales
- **SDLC seguro (Secure SDLC):** requisitos de seguridad en diseño, modelado de amenazas, revisión de código, pruebas de seguridad.
- **SAST (Static Application Security Testing):** análisis estático del código fuente para detectar bugs/vulnerabilidades sin ejecutarlo.
- **DAST (Dynamic Application Security Testing):** pruebas en tiempo de ejecución contra la app en funcionamiento.
- **IAST/SCA:** análisis interactivo y escaneo de componentes de terceros (software supply chain, log4j-type).
- **Threat modeling:** identificar amenazas por diseño (STRIDE, PASTA).
- **OWASP Top 10:** catálogo de riesgos web críticos (inyección, autenticación rota, SSRF, etc.).

## DevSecOps
Integra controles de seguridad en CI/CD: escaneo automatizado en el pipeline, *shift-left*, gates de seguridad, y *security as code*. Relacionado con `dominio/ciberseguridad-de-la-informacion.md` y `dominio/ciberseguridad-cloud.md`.

## Roles y organización
- `rol/security-engineer.md`, `rol/devsecops-engineer.md`, y `rol/head-of-application-security.md` lideran la función.
- Frameworks: NIST SSDF (Secure Software Development Framework), BSIMM, SAMM.

## Referencias cruzadas
- `dominio/ciberseguridad.md`, `dominio/ciberseguridad-de-la-informacion.md`
- `rol/head-of-application-security.md`, `rol/security-architect.md`
