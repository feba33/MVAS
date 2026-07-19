---
titulo: Seguros de salud
capa: dominio
tema: seguros
fuente: https://www.healthcare.gov/choose-a-plan/plan-types/
fuente2: https://en.wikipedia.org/wiki/Health_insurance
fecha: 2026-07-19
confianza: alta
tags: [seguros-de-salud, health-insurance, managed-care, hmo, ppo, pagadores, aca, medicare]
rol: []
actividades: []
organizaciones: [healthcare-gov, cms, aca]
responsabilidades: []
tareas: []
profundidad: 2
estado: profundo
---

# Seguros de salud

El **seguro de salud** es el contrato por el cual una aseguradora (pagador) cubre el riesgo
de gastos médicos del asegurado a cambio de una prima. En mercados maduros conviven el
**seguro privado** y el **público** (single-payer o social).

## Tipos de planes (managed care)
- **HMO** (Health Maintenance Organization): red cerrada, cuidado primario (PCP) como
  "gatekeeper", referencia para especialistas; primas y copagos bajos; sin cobertura
  fuera de red salvo emergencia.
- **PPO** (Preferred Provider Organization): libertad de proveedor, redes preferidas con
  menor costo compartido; no requiere referencia.
- **EPO / POS:** variantes de red exclusiva y punto de servicio (referencia requerida).

## Categorías de metal (Mercado ACA)
Bronze (~60% costo cubierto), Silver (~70%), Gold (~80%), Platinum (~90%), más
Catastrófico (jóvenes/sanos). Prima vs. deducible/out-of-pocket trade-off.

## Actores y mercado
- **Pagadores** (insurers): UnitedHealthcare, Elevance, Cigna, Humana, Kaiser Permanente,
  y públicos (Medicare/Medicaid en EE.UU.).
- **Proveedores:** hospitales, médicos, farmacias integrados en red.
- **Administradores de terceros (TPA)** y PBMs (gestión de beneficios farmacéuticos).

## Marco regulatorio (EE.UU.)
- **Affordable Care Act (ACA / Obamacare):** Mercado de seguros, obligación de cobertura
  esencial, prohibición de preexistencias, subsidios por ingresos.
- **Medicare** (65+ y discapacidad) y **Medicaid** (bajos ingresos) administrados por CMS.
- **Insureds**: community rating, garantías de emisión.

## Relación con otras capas
- De `dominio/seguros` (rama de personas) y `dominio/seguros-de-vida`.
- Vincula con `sustrato/estados-unidos/seguridad-social` (Medicare/Medicaid) y
  `sustrato/mexico/seguridad-social` (IMSS/ISSSTE) y `sustrato/canada/salud` (universal).
- Riesgo: `dominio/seguros` (suscripción, reservas), `rol/head-of-financial-risk`.
