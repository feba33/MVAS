---
titulo: Gobierno de datos (data governance)
capa: dominio
tema: gobierno-de-datos
fuente: https://en.wikipedia.org/wiki/Data_governance
fuente2: https://www.dama.org/cpages/body-of-knowledge
fecha: 2026-07-12
confianza: alta
tags: [gobierno-de-datos, data-governance, dama, dcam, calidad-datos, linaje, catalogo-datos, data-steward, privacidad-by-design]
english_keywords: [data governance, DAMA DMBOK, DCAM, data quality, data lineage, data catalog, data steward, privacy by design, data mesh]
---

# Gobierno de datos (data governance)

## 📝 Conocimiento

### Definición
El **gobierno de datos** es el conjunto de políticas, procesos, roles y estándares que
aseguran que los datos sean **precisos, accesibles, seguros y utilizables** como activo.
Es la "capa de gobierno" sobre la gestión de datos operativa.

### Marcos de referencia
- **DAMA-DMBOK (Data Management Body of Knowledge):** el *DAMA Wheel* con 11 áreas
  (calidad, arquitectura, metadata, integración, seguridad, etc.).
- **DCAM (EDMC):** madurez de capacidades de gestión de datos.
- **COBIT / ISO 38500** para alineación con gobierno TI.

### Pilares
1. **Calidad de datos (DQ):** exactitud, completitud, frescura, unicidad; perfiles y
   reglas de validación.
2. **Linaje (lineage):** trazabilidad origen→transformación→consumo.
3. **Catálogo y diccionario:** descubrimiento y significado (business glossary).
4. **Seguridad y privacidad:** clasificación, acceso por rol, **privacy by design**
   (LGPD/GDPR/PIPEDA).
5. **Arquitectura y metadata:** modelos, estándares, interoperabilidad.

### Roles
**CDO** (Chief Data Officer) lidera; **data stewards** (área) y **data owners** aplican
políticas; DPO velan por privacidad; arquitectos de datos definen estándares. Ver
`rol/chief-data-officer/`.

### Patrones modernos
**Data mesh** (dominios como productores de datos, *data products*), *Data contracts*,
gobernanza federada, y automatización con metadata activa / *data catalogs*.

### Relevancia de negocio
Baja calidad de datos corrompe IA, reportes y decisiones; el gobierno habilita
analítica confiable, cumplimiento y monetización de datos. Base de `dominio/analitica-negocio`
y de la confianza en `dominio/ia-generativa`.

## 🔗 Referencia
- `rol/chief-data-officer/chief-data-officer.md` — liderazgo del gobierno de datos.
- `dominio/analitica-negocio/analitica-negocio.md` — BI sobre datos gobernados.
- `dominio/etica-ia/etica-ia.md` — privacidad y sesgo en datos de entrenamiento.
- `dominio/ciberseguridad-gobierno/iso-27001.md` — seguridad de la información.
