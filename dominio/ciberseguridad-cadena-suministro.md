---
titulo: Ciberseguridad de la cadena de suministro
capa: dominio
tema: ciberseguridad-cadena-suministro
fuente: https://fossa.com/blog/sbom-requirements-cra-cyber-resilience-act/
fuente2: https://www.cisa.gov/sbom
fecha: 2026-07-16
confianza: alta
tags: [ciberseguridad, cadena-de-suministro, sbom, terceros, devsecops, regulacion]
---

# Ciberseguridad de la cadena de suministro (Supply-Chain Security)

La **ciberseguridad de la cadena de suministro** protege el software y hardware
que una organización consume de terceros — proveedores, librerías de código
abierto, integradores y 4th-party — contra compromisos que luego se propagan al
cliente (ataques *software supply chain* como SolarWinds, Log4Shell, xz).

## Conceptos clave
- **SBOM (Software Bill of Materials):** inventario de componentes y dependencias
  de un producto de software; habilita respuesta rápida ante vulnerabilidades.
- **SCA (Software Composition Analysis):** escaneo de dependencias para CVEs y
  licencias.
- **Riesgo de terceros / 4th-party:** el riesgo del proveedor del proveedor.
- **Procedencia (provenance) y firmas:** garantizar integridad y autoría.

## Marco regulatorio y normativo
- **EE.UU. — EO 14028 (May 2021):** exige SBOM y prácticas de desarrollo seguro
  en el gobierno federal; impulso de *zero trust* y estándares NIST.
- **UE — Cyber Resilience Act (CRA, 2024):** exige SBOM de nivel superior a las
  autoridades de vigilancia del mercado como parte de la documentación técnica de
  productos digitales; el código abierto tiene exenciones específicas.
- **Estándares:** SLSA (Supply-chain Levels for Software Artifacts), OpenSSF,
  NIST SSDF (SP 800-218).

## Práctica
- Generación de SBOM en CI/CD, escaneo continuo (SCA/SCST), políticas de
  *dependency admission*, firma de artefactos y monitoreo de anomalías en
  dependencias.

## Diferenciación
- Es un subconjunto de la ciberseguridad general centrado en **orígenes y
  dependencias**, a diferencia de la seguridad perimetral corporativa.

## Relación con el modelo MVAS
- Ver `dominio/ciberseguridad`, `dominio/ciberdefensa`, `dominio/seguridad-corporativa`,
  `dominio/devsecops` (rol) y `dominio/cadena-suministro`.
