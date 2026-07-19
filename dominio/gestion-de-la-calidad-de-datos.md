---
titulo: Gestión de la calidad de datos
capa: dominio
tema: gestion-de-la-calidad-de-datos
fuente: https://en.wikipedia.org/wiki/Data_quality
fuente2: https://www.dama.org/
fecha: 2026-07-19
confianza: alta
tags: [calidad-de-datos, data-quality, gobierno-de-datos, observability, dq]
---

# Gestión de la calidad de datos (Data Quality Management)

## Concepto
Disciplina que asegura que los datos sean **fit-for-purpose**: correctos, completos, consistentes, oportunos, válidos y únicos. Diferente de *gobierno de datos* (políticas/ownership) — la DQ es la ejecución de controles de calidad.

## Dimensiones de calidad (DAMA / ISO 25012)
Precisión, completitud, consistencia, puntualidad (timeliness), validez, unicidad, integridad, trazabilidad (lineage). Se miden con **DQ scorecards** por dominio/dataset.

## Actividades y herramientas
- **Perfilado (profiling)**: descubrir anomalías/distribuciones.
- **Reglas y validación**: constraints, matching/dedupe, referencial integrity.
- **Data observability**: monitoreo de calidad en pipelines (freshness, volumen, esquema) — categía emergente (Monte Carlo, Bigeye, Soda).
- **Remediación**: limpieza, enriquecimiento, master data management (MDM).

## Modelo operativo
Se integra con `dominio/gobierno-de-datos` (DAMA-DMBOK, DCAM): stewards de datos, SLAs de calidad, embed en pipelines de `dominio/ciencia-de-datos` y `dominio/arquitectura-de-datos` (lakehouse).

## Impacto
Malos datos cuestan a las empresas ~15-25% de ingresos (est. IBM/Gartner); afectan ML (garbage in/garbage out), reporting regulatorio y decisiones.

## Referencias
- DAMA-DMBOK (Data Management Body of Knowledge); ISO/IEC 25012.
- Wikipedia: Data quality.
