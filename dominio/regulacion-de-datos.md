---
titulo: Regulación de datos
capa: dominio
tema: regulacion-de-datos
fuente: https://en.wikipedia.org/wiki/General_Data_Protection_Regulation
fuente2: https://en.wikipedia.org/wiki/Personal_Information_Protection_and Electronic_Documents_Act
fecha: 2026-07-19
confianza: alta
tags: [regulacion, datos, privacidad, gdpr, pipeda, flujos-transfronterizos, gobernanza-de-datos]
profundidad: 2
estado: profundo
---

# Regulación de datos

La **regulación de datos** abarca el conjunto de normas que gobiernan la recolección,
uso, almacenamiento, transferencia y eliminación de datos — en particular los datos
personales — así como la soberanía y gobernanza de los datos en general. Es una capa
jurídico-regulatoria distinta de la protección de datos puntual: incluye flujos
transfronterizos, localización de datos, portabilidad e interoperabilidad.

## Marcos fundamentales
- **GDPR (General Data Protection Regulation)**: reglamento de la Unión Europea sobre
  privacidad de la información en la UE y el EEE; entró en vigor en 2018, sustituye a la
  Directiva 95/46/CE. Objetivos: reforzar el control y los derechos de las personas sobre
  su información personal y simplificar la regulación para el negocio internacional.
  Regula también la **transferencia de datos personales fuera de la UE/EEE** (cláusulas
  estándar, decisiones de adecuación).
- **PIPEDA (Canadá)**: *Personal Information Protection and Electronic Documents Act*,
  ley canadiense de privacidad de datos que rige cómo las organizaciones del sector
  privado recolectan, usan y divulgan información personal en el curso de negocios
  comerciales; vigente desde el 13 de abril de 2000 para fomentar la confianza del
  consumidor en el comercio electrónico y demostrar "adecuación" ante la UE.
- **APPI (Japón)**, **LGPD (Brasil)**, **Ley Fintech / datos personales (México)**,
  **CCPA/CPRA (EE.UU.)**: regímenes equivalentes con enfoques distintos
  (opt-in vs opt-out, derecho al olvido, portabilidad).

## Temas centrales
- **Flujos transfronterizos**: restricciones y mecanismos de transferencia internacional
  (adecuación, BCRs, cláusulas contractuales).
- **Localización de datos (data residency)**: requisitos de almacenamiento en territorio
  nacional (sectores financieros, salud, gobierno).
- **Portabilidad e interoperabilidad**: derecho a mover datos entre proveedores.
- **Gobernanza de datos empresarial**: data catalog, linaje, calidad, compliance por
  diseño; conecta con `rol/head-of-data-governance` y `dominio/ciencia-de-datos`.
- **Datos no personales / datos abiertos**: open data gubernamental, datos de investigación.

## Riesgos y cumplimiento
- Multas severas (hasta 4% de facturación global en GDPR, 20M€).
- Conflictos de jurisdicción (nube multinacional, acceso gubernamental).
- Tensiones entre innovación (IA, big data) y derechos fundamentales.

## Cross-references
- Vs `dominio/proteccion-de-datos`, `dominio/ciencia-de-datos`,
  `dominio/gestion-de-la-nube`, `rol/head-of-data-privacy`,
  `rol/head-of-data-governance`, `sustrato/*/proteccion-datos`.
