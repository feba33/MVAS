---
titulo: Gestión de la nube
capa: dominio
tema: gestion-de-la-nube
fuente: https://en.wikipedia.org/wiki/Cloud_computing
fuente2: https://www.finops.org/
fecha: 2026-07-19
confianza: alta
tags: [nube, cloud, finops, multi-cloud, gobernanza, saas, costos, arquitectura]
profundidad: 2
estado: profundo
---

# Gestión de la nube

La **gestión de la nube** (cloud management) es la disciplina de gobernar, operar y
optimizar los recursos de cómputo entregados como servicio. La ISO define *cloud
computing* como un paradigma que permite acceso de red a un **pool escalable y elástico
de recursos físicos o virtuales compartibles, con aprovisionamiento y administración
autoservicio bajo demanda** ("la nube").

## Modelos de servicio
- **IaaS / PaaS / SaaS**: de infraestructura a software como servicio.
- **FaaS / Serverless**: cómputo por eventos.
- **Multi-cloud / hybrid cloud**: combinación de nubes públicas y privadas para evitar
  lock-in y cumplir residencia de datos.

## Dimensiones de gestión
- **FinOps (Cloud Financial Operations)**: disciplina para gestionar el costo de la nube
  de forma colaborativa entre ingeniería, finanzas y negocio; principios: accountability
  de unidades de negocio, modelado de uso, descuentos (reserved/committed use),
  *showback/chargeback*.
- **Gobernanza de cloud**: identidad y acceso (IAM), políticas, *landing zones*,
  *guardrails* (prevención de exfiltración/costos), cumplimiento regulatorio.
- **Operaciones**: observabilidad, automatización (IaC), *sprawl* de SaaS e inventario.
- **Resiliencia**: multi-región, recuperación ante desastres, arquitecturas well-architected.

## Actores y rol
- Cloud Centers of Excellence (CCoE), plataformas internas (*platform engineering*).
- Relación con `dominio/computacion` (arquitectura), `dominio/devops`,
  `dominio/seguridad-de-la-informacion`, `rol/head-of-platform-engineering`,
  `rol/head-of-cloud` (cuando existe).

## Riesgos
- *Egress costs*, facturación por uso impredecible, *shadow IT* (SaaS no autorizado),
  dependencia de un proveedor (lock-in), residencia/soberanía de datos.

## Cross-references
- Vs `dominio/computacion`, `dominio/devops`, `dominio/arquitectura-nube`,
  `dominio/seguridad-de-la-informacion`, `dominio/regulacion-de-datos`,
  `dominio/ciberseguridad-de-la-informacion-en-la-nube`.
