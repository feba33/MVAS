---
titulo: Arquitectura empresarial
capa: dominio
tema: arquitectura-empresarial
fuente: https://capstera.com/knowledge-hub/articles/enterprise-architecture-frameworks
fuente2: https://standarity.com/blog/enterprise-architecture-frameworks-compared
fecha: 2026-07-17
confianza: alta
tags: [arquitectura-empresarial, togaf, zachman, bizbok, capability-mapping, estrategia-ti, gobernanza]
organizaciones: [The Open Group, Business Architecture Guild, Gartner]
responsabilidades: [alineacion-estrategia-ti, planificacion-arquitectura, gobernanza-ti]
profundidad: 2
estado: profundo
---

# Arquitectura empresarial

La **arquitectura empresarial (EA)** es la práctica de describir, planear y gobernar cómo se
ajustan y evolucionan los **capability map**, la información, las aplicaciones y la tecnología
de una organización para apoyar la estrategia. Da un vocabulario compartido y puntos de vista
(viewpoints) para que estrategia, inversión en TI y entrega apunten en la misma dirección.

## Frameworks dominantes
- **TOGAF** (The Open Group): método y framework basado en el **ADM** (Architecture Development
  Method), un ciclo repetible para desarrollar arquitectura. El más adoptado en empresas
  comerciales. Incluye **ArchiMate** como lenguaje de modelado.
- **Zachman Framework**: **taxonomía/ontología** 6×6 (qué, cómo, dónde, quién, cuándo, por qué ×
  planificador, propietario, diseñador, implementador…). Dice *qué* documentar, no *cómo*.
- **BIZBOK** (Business Architecture Guild): blueprint del dominio de **arquitectura de negocio**
  — mapas de capacidades, organización por valor, iniciativas estratégicas.
- **FEAF** (gobierno federal EE.UU.), **DoDAF** (defensa/aeroespacial), y el enfoque
  **business-outcome** de Gartner (agilidad sobre capas prescritas).

## Dominios típicos
1. **Arquitectura de negocio** (capacidades, valor, procesos)
2. **Arquitectura de información / datos**
3. **Arquitectura de aplicaciones**
4. **Arquitectura tecnológica** (infra, red, seguridad)

## Práctica
- **Capability mapping**: árbol de capacidades para priorizar inversión y detectar redundancia.
- Evaluar madurez y disposición al cambio antes de comprometer frameworks complejos.
- Combinar frameworks (p.ej. TOGAF + ArchiMate + BIZBOK) según contexto.

## Relación con otras capas
- vs `dominio/enterprise-architect` (rol), `dominio/gobierno-de-ti`, `dominio/estrategia`,
  `dominio/metodologias-agiles`.
- Relevante para `rol/enterprise-architect`, `rol/chief-architect` implícito, `rol/cto`.

## Fuentes
- Enterprise Architecture Frameworks (Capstera): <https://capstera.com/knowledge-hub/articles/enterprise-architecture-frameworks>
- TOGAF vs Zachman (Standarity): <https://standarity.com/blog/enterprise-architecture-frameworks-compared>
