---
titulo: DevOps
capa: dominio
tema: devops
fuente: https://en.wikipedia.org/wiki/DevOps
fuente2: https://www.atlassian.com/devops
fecha: 2026-07-19
confianza: alta
tags: [devops, ci-cd, iac, entrega-continua, observabilidad, cultura, sre]
profundidad: 2
estado: profundo
---

# DevOps

**DevOps** es la integración y automatización del desarrollo de software y las
operaciones de TI. Abarca las tareas necesarias para el desarrollo de software y puede
acortar el tiempo de desarrollo y mejorar el ciclo de vida. Según Neal Ford, DevOps —
en particular vía *continuous delivery* — aplica el principio *"bring the pain forward"*:
enfrentar temprano las tareas difíciles, fomentar la automatización y detectar fallos
rápido.

## Prácticas centrales
- **CI/CD (Continuous Integration / Continuous Delivery)**: integración frecuente,
  pipelines automatizados de build→test→deploy.
- **IaC (Infrastructure as Code)**: infraestructura declarativa y versionada.
- **Observabilidad**: métricas, logs, trazas (distributed tracing).
- **Cultura**: colaboración dev/ops/negocio, responsabilidad compartida, *blameless
  postmortems*.
- **Automatización de pruebas y *release***: feature flags, despliegues canary/blue-green.

## Relación con disciplinas vecinas
- **SRE (Site Reliability Engineering)**: operaciones como problema de ingeniería, SLOs.
- **Platform Engineering**: construye la plataforma interna que habilita DevOps.
- **DevSecOps**: seguridad integrada en el pipeline.

## Beneficios y retos
- Más frecuencia de despliegue, menor *lead time*, recuperación más rápida.
- Curva de adopción cultural; necesidad de tooling y estándares.

## Cross-references
- Vs `dominio/plataforma-sre`, `dominio/ingenieria-de-plataforma`,
  `dominio/gestion-de-la-nube`, `dominio/testing-qa`, `dominio/computacion`,
  `rol/head-of-engineering-excellence`, `rol/head-of-platform-engineering`.
