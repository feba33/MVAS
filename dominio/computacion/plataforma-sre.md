---
titulo: Plataforma / DevOps / SRE (Ingeniería de Plataforma y Confiabilidad)
capa: dominio
tema: computacion
fuente: https://www.splunk.com/en_us/blog/learn/sre-vs-devops-vs-platform-engineering.html
fuente2: https://gartsolutions.com/platform-engineering-vs-devops/
fecha: 2026-07-10
confianza: alta
tags: [platform-engineering, sre, devops, idp, slo, error-budget, confiabilidad, internal-developer-platform]
english_keywords: [platform engineering, site reliability engineering, SRE, DevOps, internal developer platform, SLI, SLO, error budget]
---

# Plataforma / DevOps / SRE (Ingeniería de Plataforma y Confiabilidad)

## 📝 Conocimiento
Tres disciplinas relacionadas pero con foco distinto que, en 2026, conviven en la
misma organización de ingeniería. No se reemplazan entre sí; se complementan.

### DevOps (forma de trabajar)
No es un cargo ni una herramienta, sino un **cambio cultural** que rompe silos entre
desarrollo y operaciones mediante automatización del pipeline de entrega. Prácticas
centrales: CI/CD, Infraestructura como Código (IaC), automatización-first, ownership
compartido. (Ver [devops](devops.md).) El problema: a escala, los equipos "DevOps"
devinieron cuellos de botella — fenómeno conocido como *DevOps fatigue* — porque cada
squad reinventaba su propio camino a producción.

### SRE — Site Reliability Engineering
Aplica **principios de ingeniería de software a problemas de operaciones**. Nació en
Google (2003) para manejar sistemas a gran escala. Foco: confiabilidad, respuesta a
incidentes y mantener SLAs. Herramientas de gobierno de confiabilidad:
- **SLI** (Service Level Indicator): métrica observada (latencia, disponibilidad, tasa de error).
- **SLO** (Service Level Objective): objetivo acordado (p. ej. 99.9% disponibilidad).
- **Error budget**: la fracción de falla permitida (100% − SLO); equilibra velocidad de
  features vs. confiabilidad. Si se agota el presupuesto, se frena el lanzamiento.
- Responsabilidades: monitoreo, respuesta a emergencias, change management, eficiencia/rendimiento.

### Ingeniería de Plataforma (Platform Engineering)
Construye y mantiene una **Internal Developer Platform (IDP)** que abstrae la complejidad
de la infraestructura para que los desarrolladores se auto-sirvan (self-service). Foco:
**developer experience (DX)** y productividad. Surge como evolución de DevOps para
terminar con la carga cognitiva ("construyes y operas") sobre los devs. Conceptos clave:
- **Golden paths**: caminos opinados y soportados (plantillas, scaffolders) del código a
  producción, sin obligar a dominar Kubernetes/Terraform.
- **Plataforma como producto**: el equipo de plataforma trata a los devs internos como
  clientes, con catálogo de servicios y portal (p. ej. Backstage).

### Tabla comparativa
| Disciplina | Naturaleza | Foco | Métrica reina | Analogía |
|---|---|---|---|---|
| DevOps | Cultura/proceso | Automatizar entrega | Lead time de despliegue | "construye las carreteras y el tráfico" |
| SRE | Práctica de ingeniería | Confiabilidad/uptime | SLO / error budget | "asegura que el tráfico fluya y repara accidentes" |
| Platform Eng. | Equipo/producto | DX y productividad | Adopción de la IDP, lead time | "crea el GPS para que el dev navegue solo" |

### Relación con otras capas de computación
La plataforma se apoya en [estilos-arquitectura](estilos-arquitectura.md) (microservicios,
event-driven) y [bases-datos](bases-datos.md) (réplicas, sharding para escalar); el SRE
necesita observabilidad sobre todo ello. Los roles afines viven en `rol/` (ver
`rol/engineering-manager`, `rol/cto`).

## 🔗 Referencia
- [devops](devops.md) — base cultural de automatización y CI/CD.
- [estilos-arquitectura](estilos-arquitectura.md) — microservicios/EDA que la plataforma orquesta.
- [bases-datos](bases-datos.md) — escalabilidad distribuida que SRE monitoriza.
- Fuentes: Splunk (SRE vs DevOps vs Platform Eng.), Gart Solutions (The Full Breakdown, 2026),
  SwitchtoDevOps (carreras 2026), OpenSpace Services, Urolime — reference-only.
