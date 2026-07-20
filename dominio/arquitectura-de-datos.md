---
titulo: Arquitectura de datos
capa: dominio
tema: arquitectura-de-datos
fuente: https://en.wikipedia.org/wiki/Data_architecture
fuente2: https://www.dama.org/
fecha: 2026-07-19
confianza: alta
tags: [arquitectura-de-datos, datos, gobierno-de-datos, data-lake, data-warehouse]
profundidad: 2
estado: profundo
---

# Arquitectura de datos

## Definición
Disciplina que define cómo se recopilan, almacenan, integran, gobiernan y entregan
los datos en una organización. Conecta requisitos de negocio con modelos lógicos/físicos
y plataformas técnicas.

## Componentes y patrones
- **Modelado:** relacional, dimensional (esquemas estrella), grafos, datos anidados.
- **Almacenamiento:** data warehouses (OLAP), data lakes (brutos), lakehouse
  (transaccional + analítico), múltiples motores.
- **Integración:** ETL/ELT, CDC, streaming (Kafka), orquestación (Airflow/Dagster).
- **Gobierno:** linaje, catálogo, calidad, seguridad/PDM (integra `dominio/gobierno-de-datos`).

## Roles relacionados
- Data architect (diseño), data engineer (implementación), `rol/head-of-data-strategy`
  (estrategia), `rol/head-of-data-governance` (políticas).

## Estándares
- DAMA-DMBOK, TOGAF (data architecture), Zachman. Nubes: zonas (raw/curated/serving).

## Referencias cruzadas
- `dominio/gobierno-de-datos`, `dominio/ingenieria-de-datos`, `dominio/arquitectura-de-soluciones`,
  `dominio/analitica-de-negocio`, `rol/head-of-data-strategy`.
