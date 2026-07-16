---
titulo: Gestión de la cadena de suministro (SCM operativo)
capa: dominio
tema: operaciones
fuente: https://www.mckinsey.com/capabilities/operations/our-insights/taking-the-pulse-of-shifting-supply-chains
fuente2: https://www.gartner.com/en/supply-chain/topics/supply-chain-planning
fecha: 2026-07-16
confianza: media
tags: [cadena-de-suministro, scm, planificacion, sourcing, make, entrega, s&op, resiliencia, operaciones]
profundidad: 2
estado: profundo
rol: [supply-chain-manager, head-of-supply-chain-planning, head-of-manufacturing]
organizaciones: [ascm, mckinsey, gartner]
---

# Gestión de la cadena de suministro (SCM operativo)

La **gestión de la cadena de suministro (SCM)** es la dirección de los flujos de
producto, información y dinero desde la materia prima hasta el consumidor final.
Operativamente se descompone en las fases clásicas **planificar (plan), abastecer
(source/sourcing), hacer (make), entregar (deliver) y retornar (return)** — el modelo
SCOR de APICS/ASCM. Su objetivo: servicio al cliente, costo total y capital
invertido óptimos, con **resiliencia** ante shocks.

## Fases operativas

| Fase | Qué abarca |
|---|---|
| **Plan** | Pronóstico, S&OP/IBP, plan maestro, equilibrio oferta-demanda |
| **Source** | Sourcing estratégico, proveedores, P2P, gestión de categorías |
| **Make** | Programación de producción, manufactura, calidad, WIP |
| **Deliver** | Almacenamiento, transporte, última milla, gestión de pedidos |
| **Return** | Logística inversa, devoluciones, reparación, reciclaje |

## Planificación integrada (S&OP / IBP)

- **Sales & Operations Planning (S&OP)**: proceso mensual de alineación comercial-
  operaciones-finanzas sobre un plan único.
- **Integrated Business Planning (IBP)**: S&OP extendido con finanzas y escenarios.
- Vincula con `dominio/cadena-suministro.md` (macro cadena) y
  `dominio/cadena-de-valor.md` (Porter).

## Resiliencia y riesgo

- Post-COVID y tensiones geopolíticas, la prioridad pasó de *lean/costo* a
  **resiliencia**: dual sourcing, nearshoring, inventario estratégico, visibilidad
  (McKinsey: "shifting supply chains").
- **Visibility** y **control tower** como capacidades centrales.
- Riesgo de proveedor, riesgo país y ciberseguridad de la cadena
  (`dominio/ciberseguridad-cadena-suministro.md`).

## Tecnología habilitadora

- **ERP** (SAP/Oracle), **WMS/TMS**, **APS** (planificación avanzada),
  **control tower**, **IoT** y **IA** para pronóstico y control.
- Digital twin de la cadena para escenarios.

## KPIs típicos

- Service level / fill rate, OTIF, rotación de inventario, cash-to-cash cycle,
  costo de la cadena como % de ventas, días de inventario.

## Relación con otras capas

- `dominio/cadena-suministro.md`, `dominio/cadena-de-valor.md`, `dominio/compras.md`
- `dominio/almacenamiento.md`, `dominio/logistica-inversa.md`, `dominio/manufactura.md`
- `dominio/investigacion-operaciones.md` (optimización de la cadena)

## Referencias

- McKinsey Operations: "Taking the pulse of shifting supply chains" (resiliencia).
- Gartner: Supply Chain Planning (topic) / Supply Chain Resilience.
- ASCM (APICS): modelo SCOR.
