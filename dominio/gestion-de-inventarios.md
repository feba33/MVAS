---
titulo: Gestión de inventarios
capa: dominio
tema: gestion-de-inventarios
fuente: https://en.wikipedia.org/wiki/Inventory_management
fuente2: https://nventory.io/blog/inventory-management-methods-compared
fecha: 2026-07-18
confianza: alta
tags: [gestion-inventarios, eoq, jit, mrp, abc, safety-stock, wms, cadena-suministro, almacenamiento]
profundidad: 2
estado: profundo
---

# Gestión de inventarios

La **gestión de inventarios (inventory management)** planifica, controla y
optimiza las existencias de materia prima, trabajo en proceso y producto
terminado para equilibrar **servicio al cliente** y **costo de mantener
stock**. Impacta directamente el working capital y la continuidad operativa.

## Métodos y técnicas
- **EOQ (Economic Order Quantity)**: calcula la cantidad de pedido que minimiza
  el costo total (ordenar + mantener) para demanda estable.
- **JIT (Just-in-Time)**: se recibe inventario solo cuando se necesita;
  reduce almacenamiento pero exige proveedores confiables.
- **MRP (Material Requirements Planning)**: calcula necesidades de
  materiales a partir del plan maestro de producción.
- **ABC Analysis**: clasifica SKUs por impacto en ingresos (A=alto control,
  B=medio, C=bajo) para priorizar esfuerzo.
- **Safety stock (stock de seguridad)**: buffer contra variabilidad de demanda
  y lead time.
- **FIFO / LIFO / FEFO**: políticas de rotación (FEFO = primer a expirar).
- **DDMRP** (Demand-Driven MRP): buffers en puntos de desacoplo para cadenas
  complejas.

## Reorden y KPIs
- **Reorder point (ROP)**, **lead time**, **nivel de servicio**, **días de
  inventario**, **turnover / rotación**, **stockout rate**, **obsolescencia**.
- Conteo cíclico (cycle counting) para precisión sin paros.

## Tecnología
- **WMS (Warehouse Management System)**, integración ERP, códigos de barras /
  RFID, serialización y lotes para trazabilidad.
- Visibilidad en tiempo real y pronóstico de demanda (S&OP/IBP).

## Diferenciación
- vs `dominio/almacenamiento` (operación física de bodega): aquí el foco es el
  nivel óptimo de stock.
- vs `dominio/cadena-de-valor` / `dominio/logistica`: el inventario es un
  subproceso.

## Relación con otras capas MVAS
- Conecta con `dominio/almacenamiento`, `dominio/cadena-de-valor`,
  `dominio/logistica`, `dominio/gestion-de-la-cadena-de-suministro`. A nivel
  rol: `rol/supply-chain-manager`, `rol/head-of-supply-chain-planning`,
  `rol/operations-manager`, `rol/head-of-manufacturing`.
