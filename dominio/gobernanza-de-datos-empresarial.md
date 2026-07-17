---
titulo: Gobernanza de datos empresarial
capa: dominio
tema: gobernanza-de-datos-empresarial
fuente: https://www.damadmbok.org/copy-of-about-dama-dmbok
fuente2: https://atlan.com/dama-dmbok-framework/
fecha: 2026-07-17
confianza: alta
tags: [gobernanza-datos, dama, dmbok, data-stewardship, data-quality, lineage, catalogo, data-products]
rol: []
actividades: []
organizaciones: [dama-international]
responsabilidades: []
tareas: []
profundidad: 2
estado: profundo
---

# Gobernanza de datos empresarial

La **gobernanza de datos empresarial (Enterprise Data Governance)** es la disciplina
que asegura que los datos se gestionen como **activo estratégico** confiable, seguro
y utilizable en toda la organización. Responde a la pregunta operativa "¿podemos
confiar en este dato?" mediante políticas, roles, estándares y controles.

## Marco de referencia: DAMA-DMBOK
DAMA International publica el **Data Management Body of Knowledge (DMBOK)**, cuyo
corazón son **11 áreas de conocimiento**:
1. **Data Governance** (políticas, roles, estándares; subyace a todas las demás).
2. Data Architecture · 3. Data Modeling & Design · 4. Data Storage & Operations ·
5. Data Security · 6. Data Integration & Interoperability · 7. Document & Content
Management · 8. **Data Quality** · 9. **Data Warehousing & Business Intelligence** ·
10. **Metadata Management** · 11. **Data Stewardship**.

## Componentes operativos
- **Data stewardship:** stewardship por dominio (business/technical stewards) que
  ejecuta las políticas día a día y resuelve conflictos de ownership.
- **Data quality:** perfiles, reglas, scorecards (completitud, exactitud,
  consistencia, puntualidad, unicidad, validez).
- **Data lineage:** trazabilidad campo a campo (origen → transformación → destino).
- **Catálogo de datos:** inventario descubierto, glosario de negocio, buscabilidad.
- **Data products:** conjuntos de datos empaquetados con SLA, dueño y contrato.
- **Metadata activa:** gobierno "en movimiento" (clasificación, masking automático).

## Diferenciación
- **vs `dominio/gobierno-de-datos`** (concepto amplio/estatal): aquí el foco es la
  ejecución empresarial (stewardship, catálogo, data products).
- **vs `dominio/proteccion-de-datos`**: la gobernanza abarca calidad y uso, no solo
  privacidad/regulatorio (aunque se solapan en clasificación y acceso).
- **vs `rol/head-of-data-platform`**: plataforma entrega los pipelines; gobernanza
  fija las reglas y el ownership.

## Relevancia para el usuario
- Habilita **analítica fiable, IA/ML de confianza, reportes regulatorios y
  interoperabilidad**; sin gobernanza, los dashboards contradictorios erosionan
  decisiones.
- Conecta con `dominio/analitica-negocio`, `dominio/ciencia-de-datos`,
  `dominio/proteccion-de-datos`, `dominio/arquitectura-empresarial`.

## Referencia
- DAMA-DMBOK (damadmbok.org, reference-only).
- Atlan — *DAMA DMBOK Framework Guide 2026* (atlan.com, reference-only).
- Cross-ref: `dominio/gobierno-de-datos`, `dominio/proteccion-de-datos`,
  `dominio/analitica-negocio`, `rol/head-of-data-platform`.
