---
titulo: Ciberseguridad de la cadena de suministro
capa: dominio
tema: ciberseguridad-de-la-cadena-de-suministro
fuente: https://en.wikipedia.org/wiki/Supply_chain_attack
fuente2: https://www.cisa.gov/sbom
fecha: 2026-07-20
confianza: alta
tags: [ciberseguridad, cadena-de-suministro, sbom, software-supply-chain, terceros, slsa, cisa]
profundidad: 2
estado: profundo
---

# Ciberseguridad de la cadena de suministro

La **ciberseguridad de la cadena de suministro** protege el flujo de hardware,
software y servicios desde proveedores hasta el cliente final. Los ataques
(*supply chain attacks*) comprometen un eslabón confiable para alcanzar a muchos
destinatarios —ej. SolarWinds (2020) y Log4Shell (2021).

## Vectores principales
- **Software supply chain:** dependencias open-source, CI/CD, firmas de código,
  actualizaciones firmadas, registros de imágenes.
- **Hardware/componentes:** chips y dispositivos adulterados, proveedores de
  manufactura.
- **Terceros / proveedores (TPRM):** acceso remoto, MSPs, SaaS, consultores.

## Marcos y controles
- **SBOM (Software Bill of Materials):** inventario de componentes para responder
  a vulnerabilidades (CISA, EO 14028).
- **SLSA** (Supply-chain Levels for Software Artifacts): provenance y integridad.
- **EO 14028** (US): mejora de la ciberseguridad y cadena de suministro de software.
- NIST SP 800-161 (supply chain risk management), ISO/IEC 27036.
- **Zero trust** extendido a proveedores; escaneo de dependencias (SCA).

## Práctica
- Vetting de proveedores, contratos con cláusulas de seguridad, monitoreo continuo,
  respuesta a incidentes coordinada.
- vs `dominio/ciberseguridad`, `dominio/gestion-de-la-cadena-de-suministro`,
  `rol/head-of-vendor-risk`.

## Referencias
- Wikipedia EN: Supply chain attack.
- CISA.gov (SBOM) y NIST SP 800-161.
