---
titulo: Seguros agrícolas
capa: dominio
tema: seguros-agricolas
fuente: https://en.wikipedia.org/wiki/Crop_insurance
fuente2: https://www.rma.usda.gov/Policy-and-Procedure/Standard-Reinsurance-Agreement
fecha: 2026-07-17
confianza: alta
tags: [seguros, agricultura, crop-insurance, seguros-agricolas, parametrico, fcip, gestion-de-riesgos-agricolas]
organizaciones: [USDA-RMA, FCIP, aseguradoras-agricolas, SADER]
responsabilidades: [gestion-de-riesgo-agricola, proteccion-de-medios-de-vida, subsidio-agropecuario]
profundidad: 2
estado: profundo
---

# Seguros agrícolas

Los **seguros agrícolas** (crop insurance) son pólizas que adquieren los productores
agropecuarios y que suelen estar **subvencionadas por el gobierno** para protegerlos
contra la pérdida de cosechas por desastres naturales (granizo, sequía, inundaciones)
o contra la pérdida de ingresos por caídas en los precios de los commodities
agrícolas.

## Modalidades
1. **Yield / crop insurance**: indemniza por debajo de un rendimiento garantizado.
2. **Revenue insurance**: cubre la caída de ingresos (rendimiento × precio).
3. **Paramétrico / index-based**: paga ante un índice (lluvia, temperatura,
   NDVI) sin ajuste de pérdida individual; clave en mercados emergentes y para
   pequeños productores.
4. **Seguro de ganado / pecuario**: contra mortandad y riesgos climáticos.

## El caso de EE.UU. (FCIP)
- El **Federal Crop Insurance Corporation (FCIP)**, administrado por **RMA**
  (USDA), es el programa más grande del mundo: el gobierno subsidia la prima y
  comparte riesgo con aseguradoras privadas vía el **Standard Reinsurance
  Agreement**.
- Cobertura para maíz, soya, trigo y cientos de cultivos; >80% de la tierra
  cultivable elegible está asegurada.

## En México y Canadá
- México: **Agroasemex** (reaseguradora de la nación) y esquemas de la **SADER**;
  históricamente baja penetración pero creciente interés paramétrico.
- Canadá: **AgriInsurance** (cost-shared federal-provincial), parte de
  *Business Risk Management* (BRM).

## Relevancia
- Estabiliza ingresos del productor, facilita crédito (colateral) y resiliencia
  climática; pieza clave de la **seguridad alimentaria**.

## Relación con otras capas
- vs `dominio/seguros`, `dominio/seguros-de-credito`, `dominio/sector-agroalimentario`.
- Sustrato: `sustrato/mexico/agricultura`, `sustrato/estados-unidos/agricultura`.
- Rol: `rol/underwriter`, `rol/head-of-underwriting`, `rol/risk-manager`.

## Fuentes
- Crop insurance (Wikipedia): <https://en.wikipedia.org/wiki/Crop_insurance>
- USDA RMA — Standard Reinsurance Agreement: <https://www.rma.usda.gov/Policy-and-Procedure/Standard-Reinsurance-Agreement>
