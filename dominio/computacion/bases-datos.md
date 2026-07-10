---
titulo: Bases de datos
capa: dominio
tema: computacion
fuente: https://en.wikipedia.org/wiki/Database
fuente2: https://en.wikipedia.org/wiki/NoSQL
fecha: 2026-07-10
confianza: alta
tags: [bases-datos, sql, nosql, distribuidas, cap, relacional]
english_keywords: [database, sql, nosql, distributed, cap-theorem, relational]
---

# Bases de datos

## 📝 Conocimiento
Una **base de datos** es una colección organizada de datos gestionada por un **DBMS**
(Database Management System) que media entre usuarios/aplicaciones y los datos — Wikipedia
([Database](https://en.wikipedia.org/wiki/Database)). El sistema = base de datos + DBMS +
aplicaciones asociadas.

### SQL / Relacional
Lenguaje **SQL** (Structured Query Language) para gestionar datos en un **RDBMS**; ideal para
datos estructurados con relaciones entre entidades — Wikipedia ([SQL](https://en.wikipedia.org/wiki/SQL)).
Modelo tabla (filas/columnas), esquema fijo, integridad referencial (PK/FK), ACID. Ej.:
PostgreSQL, MySQL, SQL Server, Oracle.

### NoSQL
Diseño que **almacena/recupera datos distinto a la tabla relacional**: usa una sola estructura
— clave-valor, columnas anchas, grafos o documentos — Wikipedia ([NoSQL](https://en.wikipedia.org/wiki/NoSQL)).
Sin esquema fijo → escala fácil a datasets grandes/no estructurados. Subtipos:
- **Documental** (JSON/BSON): MongoDB, Couchbase.
- **Clave-valor**: Redis, DynamoDB.
- **Columnar** (wide-column): Cassandra, HBase.
- **Grafo**: Neo4j, Neptune.
"No only SQL": suelen admitir lenguajes tipo-SQL o conviven en *polyglot persistence*
(varios motores a la vez).

### Distribuidas
Una **base de datos distribuida** reparte los datos en **diferentes ubicaciones físicas**
(misma sala o red de equipos), con sitios débilmente acoplados que no comparten componentes
— Wikipedia ([Distributed database](https://en.wikipedia.org/wiki/Distributed_database)).
Mecanismos: **sharding** (particionado por clave), **replicación** (réplicas para
disponibilidad/lectura), **consenso** (Raft/Paxos).

### Teorema CAP
En un almacén distribuido solo se pueden garantizar **a lo sumo 2 de 3**: **C**onsistencia
(toda lectura ve el último write), **D**isponibilidad (toda petición recibe respuesta),
**T**olerancia a partición (red particionada sigue operando) — Wikipedia
([CAP theorem](https://en.wikipedia.org/wiki/CAP_theorem)). Ante partición (inevitable en red),
hay que sacrificar C o A: sistemas CP (consistencia) vs AP (disponibilidad). NewSQL intenta
reconciliar escala de NoSQL con ACID relacional.

### Cuándo usar qué
| Necesidad | Motor |
|---|---|
| Transacciones, integridad, reporting | SQL (relacional) |
| Escala horizontal, datos no estructurados | NoSQL |
| Alta disponibilidad geo / sharding | Distribuida (NewSQL/Cassandra) |

## 🔗 Referencia
- [data-engineering](data-engineering.md) — pipelines y warehouses que las consumen.
- [arquitectura](arquitectura.md) · [estilos-arquitectura](estilos-arquitectura.md) — patrones que las alojan.
- Fuentes: Database, NoSQL, SQL, CAP theorem, Distributed database (Wikipedia, en) — reference-only.
