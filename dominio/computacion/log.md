# Registro de computacion (log.md)

Registro cronológico **append-only** de la entidad `computacion`.
Prefijo: `## [YYYY-MM-DD] <tipo> | <título>` (parseable: `grep "^## \[" log.md`).

## [2026-07-09] setup | Nodo wiki de computacion
- Creada la superstructura recursiva de la entidad `computacion` dentro de `dominio/`:
  `raw/`, `index.md`, `log.md` y `README.md`.
- Demuestra el principio: toda la info de computacion vive solo en esta carpeta.

## [2026-07-09] ingest | Paradigmas de Programación
- Fuente: Wikipedia (en) — reference-only.
- Página: `paradigmas.md`. Imperativo (procedural, OOP) vs declarativo (funcional, lógico); multiparadigma.

## [2026-07-09] ingest | Arquitectura de Software
- Fuente: Wikipedia (en) — reference-only.
- Página: `arquitectura.md`. Estructuras para razonar el sistema; 'todo es trade-off'; modelo C4; NFR.

## [2026-07-09] ingest | DevOps
- Fuente: Wikipedia (en) — reference-only.
- Página: `devops.md`. Automatización dev+ops; propiedades: ownership compartido, automatización, feedback rápido; CI/CD y cloud.

## [2026-07-09] ingest | Ciberseguridad
- Fuente: Wikipedia (en) — reference-only.
- Página: `ciberseguridad.md`. Tríada CIA (confidencialidad, integridad, disponibilidad); amenazas; frameworks NIST; seguridad física y digital.

## [2026-07-09] ingest | Ingeniería de Datos
- Fuente: conocimiento general — reference-only.
- Página: `data-engineering.md`. Pipelines; ETL vs ELT; data warehouses/lakes; dbt; Spark.

## [2026-07-09] ingest | Ingeniería de Machine Learning
- Fuente: conocimiento general — reference-only.
- Página: `ml-engineering.md`. Entrenamiento/serving; MLOps; feature store; ciclo de vida del modelo.

## [2026-07-09] ingest | Testing y QA
- Fuente: Wikipedia (en) — reference-only.
- Página: `testing-qa.md`. Niveles unit/integration/e2e; test pyramid; TDD; automatización y QA.

## [2026-07-10] ingest | Estilos arquitectónicos de software
- Fuente: Wikipedia (en) — Microservices, Event-driven architecture — reference-only.
- Página: `estilos-arquitectura.md`. Monolito modular, SOA, microservicios (servicios poco
  acoplados, protocolos ligeros, despliegue/escala independiente), event-driven (EDA:
  producción/detección de eventos, tolerancia a fallos), serverless; tabla de trade-offs.

## [2026-07-10] ingest | Bases de datos
- Fuente: Wikipedia (en) — Database, NoSQL, SQL, CAP theorem, Distributed database — reference-only.
- Página: `bases-datos.md`. SQL relacional (RDBMS, ACID); NoSQL (documental/clave-valor/
  columnar/grafo, sin esquema, polyglot); distribuidas (sharding, replicación, consenso);
  teorema CAP (CP vs AP); NewSQL.

## [2026-07-10] ingest | Ingeniería de Plataforma + SRE
- Fuente: Splunk, Gart Solutions, SwitchtoDevOps, OpenSpace, Urolime (2026) — reference-only.
- Página: `plataforma-sre.md`. DevOps (cultura/automatización) vs SRE (SLI/SLO/error budget,
  confiabilidad, origen Google 2003) vs Ingeniería de Plataforma (IDP, golden paths, DX);
  tabla comparativa; cross-ref a devops, estilos-arquitectura, bases-datos.

## [2026-07-10] ingest | Frontend — Frameworks y rendimiento
- Fuente: Midrocket, DEV.to, Coderio, Pharos Production (2026) — reference-only.
- Página: `frontend.md`. React/Vue/Svelte/Angular/Astro/Next.js; meta-frameworks; bundle size,
  hidratación parcial/islands, Core Web Vitals, SSR/SSG vs CSR; tabla de decisión por contexto;
  cross-ref a arquitectura, estilos-arquitectura, testing-qa, plataforma-sre.

## [2026-07-11] ingest | Apple demanda a OpenAI por robo de secretos comerciales
- Fuente: El Financiero (sección tech, 2026-07-10) — reference-only (URL en frontmatter, sin raw/).
- Página: `apple-openai-secretos-comerciales.md`. Apple acusa a OpenAI de alentar a exempleados a compartir información, componentes, planos y materiales de futuros productos; señala al jefe de hardware de OpenAI.
- Discernimiento: dominio/computacion (certeza alta, ángulo tecnológico/IA+hardware) + cross-ref dominio/leyes (propiedad-intelectual / trade secrets).
