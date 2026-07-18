---
titulo: Gestión de activos de TI (ITAM)
capa: dominio
tema: gestion-de-activos-de-ti
fuente: https://www.iso.org/standard/53898.html
fuente2: https://en.wikipedia.org/wiki/IT_asset_management
fecha: 2026-07-18
confianza: alta
tags: [ti, itam, inventario, licencias, cmdb, ciclo-de-vida, gobernanza-de-ti]
organizaciones: [ISO, ITIL, IAITAM]
---

# Gestión de activos de TI (ITAM)

La **gestión de activos de TI** (IT Asset Management) rastrea y optimiza el
ciclo de vida de hardware, software y licencias; base del gobierno de TI.
Hermano de `gobierno-de-ti.md` y `gestion-de-riesgos-it.md`.

## Alcance
- **Inventario**: hardware (endpoints, servidores, red) y software (instalado,
  suscrito, SaaS).
- **CMDB** (Configuration Management Database): relación de CIs (configuration
  items) con servicios; piedra angular de ITIL/ITSM.
- **Licencias y cumplimiento**: conteo de uso vs. derechos (SAM — Software
  Asset Management), auditorías de editores, ahorro por optimización.

## Ciclo de vida
- Adquisición → asignación → mantenimiento → retiro/descarte (con seguridad de
  datos y disposición de residuos electrónicos — ver `reciclaje.md`).

## Valor de negocio
- Reducción de costos (subutilización, renovaciones innecesarias), mitigación de
  riesgo de auditoría y soporte a la **seguridad** (superficie de ataque conocida).
- Integración con **FinOps** (nube) y gestión de la cadena de suministro.

## Referencias transversales
- `gobierno-de-ti.md`, `it-service-management.md`, `gestion-de-riesgos-it.md`
- `cloud-computing.md`, `reciclaje.md`, `seguridad-corporativa.md`
