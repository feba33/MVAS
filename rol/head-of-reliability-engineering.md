---
titulo: Head of Reliability Engineering
capa: rol
tema: head-of-reliability-engineering
fuente: https://sre.google/sre-book/table-of-contents/
fecha: 2026-07-19
confianza: alta
tags: [rol, head-of-reliability-engineering, sre, slo, sli, error-budget, incidentes, post-mortem]
rol: [head-of-reliability-engineering]
responsabilidades: [slo-sli, error-budgets, incident-response, post-mortem, observabilidad]
profundidad: 2
estado: profundo
---

# Head of Reliability Engineering

El **Head of Reliability Engineering** lidera la organización de **Site Reliability Engineering (SRE)**: garantiza que los sistemas de software sean confiables, escalables y eficientes en producción, equilibrando velocidad de entrega y estabilidad.

## Responsabilidades
- **SLO/SLI y error budgets:** definir objetivos de nivel de servicio, indicadores y presupuestos de error que gobiernen la tolerancia a fallos.
- **Incidentes:** liderar respuesta, runbooks, war-room, y coordinación con desarrollo/operaciones. vs `rol/head-of-incident-response`.
- **Post-mortem:** cultura de revisión sin culpa (blameless), acciones correctivas. vs `rol/head-of-incident-response`.
- **Observabilidad:** métricas, logs, tracing; capacidad y performance.
- **Automatización:** reducir toil, infraestructura como código, CI/CD, on-call engineering.

## Reportes y relación
- Reporta a VP Engineering / CTO. Colabora estrechamente con `head-of-platform-engineering`, desarrollo de producto y operaciones.
- Diferencia vs `rol/head-of-platform-engineering` (plataforma interna como producto) y `rol/head-of-engineering` (宽阔 org de ingeniería).

## Habilidades
- SRE/cloud (GCP/AWS/Azure), Kubernetes, Prometheus/Grafana, tracing, scripting (Python/Go).
- Cultura de confiabilidad, gestión de crisis, datos/SLI.

## Referencias
- Google SRE Book (sre.google) para principios de SRE, SLO/error budgets.
- CNCF, Prometheus, OpenTelemetry para observabilidad.
