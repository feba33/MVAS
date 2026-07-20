---
titulo: Seguros paramétricos / Parametric Insurance
capa: dominio
tema: seguros-parametricos
fuente: https://en.wikipedia.org/wiki/Parametric_insurance
fecha: 2026-07-20
confianza: alta
tags: [seguros-parametricos, parametric-insurance, indice, clima, catastrofe, iot, agricultura]
profundidad: 3
estado: profundo
---

# Seguros paramétricos / Parametric Insurance

El **seguro paramétrico** es un producto no tradicional que paga un monto pre-especificado cuando ocurre un **evento disparador (trigger)**, en lugar de indemnizar el daño real. Los disparadores dependen del producto: ambientales (velocidad de viento, lluvia, temperatura), o de negocio (tráfico peatonal, etc.).

## Ejemplos reales
- **CCRIF** (Caribe) y **African Risk Capacity (ARC)**: cobertura paramétrica climática/cat para gobiernos.
- **Quintana Roo (México)**: protección paramétrica de arrecifes de coral (trigger por huracán).

## Ventajas
Pago rápido (días, no meses), menor disputa de ajuste, útil para catástrofes y para agricultura/clima. Requiere datos confiables (satélites, IoT, estaciones). Converge con [dominio/seguros], [dominio/seguros-agricolas] y [dominio/seguros-de-catastrofe].

## Relaciones
- Seguros: [dominio/seguros], [dominio/seguros-agricolas].
- Riesgo: [rol/head-of-catastrophe-risk], [rol/head-of-credit-risk].
