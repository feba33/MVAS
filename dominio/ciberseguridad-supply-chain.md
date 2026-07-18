---
titulo: Ciberseguridad de la cadena de suministro
capa: dominio
tema: ciberseguridad-supply-chain
fuente: https://www.cisa.gov/supply-chain-security
fuente2: https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act
fecha: 2026-07-18
confianza: media
tags: [ciberseguridad-supply-chain, sbom, sca, eo-14028, eu-cra, tisax, terceros, riesgo-proveedores, devsecops]
profundidad: 2
estado: profundo
---

# Ciberseguridad de la cadena de suministro

La **ciberseguridad de la cadena de suministro** protege la integridad,
confidencialidad y disponibilidad de los productos y servicios frente a
compromisos introducidos por proveedores, software de terceros y componentes
integrados. Los ataques **supply-chain** (SolarWinds, Log4Shell, XZ) demostraron
que un proveedor comprometido afecta a miles de clientes a la vez.

## Superficie de riesgo
- **Software de terceros / dependencias open-source** (transitive deps).
- **Proveedores de servicios gestionados (MSP/MSSP)** y cloud subcontratado.
- **Componentes de hardware** y firmware en la manufactura.
- **Proveedores con acceso a redes/OT** (4.ª línea de defensa).

## Controles y estándares
- **SBOM (Software Bill of Materials)**: inventario de componentes de software
  para rastrear vulnerabilidades (EO 14028 lo exige a agencias federales EE.UU.).
- **SCA (Software Composition Analysis)**: escaneo continuo de dependencias.
- **EU Cyber Resilience Act (CRA, 2024)**: requisitos de seguridad para
  productos con elementos digitales en la UE (vulnerabilidades, parches).
- **TISAX** (automotriz, basado en ISO 27001) para proveedores de la industria
  automotriz alemana/EU.
- **SLSA** (Supply-chain Levels for Software Artifacts) y firmas de artefactos.

## Marco de gestión
- Due diligence de ciber-riesgo en proveedores; cláusulas contractuales de
  seguridad; monitoreo continuo; respuesta a incidentes coordinada.
- Alineado con NIST CSF 2.0 (GOV/ID/PROTEC/DETECT/RESP/RECOVER) y los
  principios de zero trust.

## Diferenciación
- vs `dominio/ciberseguridad` (general): se enfoca en terceros y componentes.
- vs `dominio/seguridad-corporativa` (física/crisis): es cibernética.
- vs `dominio/ciberseguridad-ot` (ICS/SCADA): el supply-chain abarca IT y OT.

## Relación con otras capas MVAS
- Conecta con `dominio/ciberseguridad`, `dominio/ciberseguridad-cloud`,
  `dominio/seguridad-corporativa`, `dominio/auditoria-interna`. A nivel rol:
  `rol/chief-information-security-officer`, `rol/security-engineer`,
  `rol/supply-chain-manager`, `rol/head-of-risk-and-compliance`.
