---
titulo: Observabilidade (software)
capa: dominio
tema: observabilidade
fuente: https://opentelemetry.io
fuente2: https://en.wikipedia.org/wiki/Observability
fecha: 2026-07-15
confianza: alta
tags: [observabilidade, opentelemetry, monitoring, apm, slo, metrics, logs, traces, devops]
english_keywords: [observability, OpenTelemetry, monitoring, APM, SLO, SLI, metrics, logs, traces, MELT, distributed tracing]
profundidad: 2
estado: profundo
---

# Observabilidade (software)

## 📝 Conocimiento
- **Definición:** medida de qué tan bien pueden **inferirse los estados internos** de
  un sistema a partir de sus **salidas externas** (métricas, logs, trazas). Nace de la
  teoría de control (observabilidad/controllabilidad como duales) y se aplica a sistemas
  distribuidos modernos. (Wikipedia — *Observability*)
- **Los tres pilares (MELT):** **Metrics** (contadores/gauges/histogramas, p.ej.
  latencia, throughput), **Events/Logs** (registros estructurados), y **Traces**
  (trazas distribuidas que siguen una petición a través de microservicios). Algunos
  añaden **Profiles** como cuarto pilar.
- **OpenTelemetry (CNCF):** estándar **vendor-neutral** y de código abierto para
  generar, recolectar y exportar telemetría (traces/metrics/logs). Es la columna
  vertebral de la observabilidad moderna: un solo instrumentación, múltiples backends
  (Datadog, New Relic, Grafana, Jaeger, Prometheus). (opentelemetry.io)
- **APM (Application Performance Monitoring):** prácticas/herramientas para monitorear
  el rendimiento y la experiencia del usuario en producción, sobre la telemetría.
- **SLO / SLI / Error Budget:** **SLI** = indicador de nivel de servicio (p.ej. %
  de requests exitosos); **SLO** = objetivo acordado; **Error Budget** = margen de
  fallo tolerable que financia velocidad de despliegue. Conecta con `dominio/computacion`
  (SRE/plataforma).
- **De "¿está arriba?" a "¿está correcto?":** la observabilidad moderna correlaciona
  síntomas (alertas) con causa raíz vía trazas y *flame graphs*; habilita *debugging*
  en producción sin reproducir localmente.
- **Observabilidade de agentes de IA:** MELT extendido a **llamadas a herramientas**,
  costos de token, deriva de modelo y alucinaciones — ver `dominio/agentes-ia`
  (AgentOps). También es base del monitoreo de seguridad (SOC) en `dominio/ciberseguridad`.
- **Riesgos/retos:** volumen de datos y costo, *cardinalidad*, *alert fatigue*, y la
  necesidad de trazas *end-to-end* en arquitecturas event-driven / serverless.

## 🔗 Referencia
- OpenTelemetry — opentelemetry.io (CNCF, reference-only).
- Wikipedia — *Observability* (reference-only).
- Google SRE Book — *Monitoring Distributed Systems* (sre.google).
- Cross-ref: `dominio/computacion`, `dominio/agentes-ia`, `dominio/ciberseguridad`,
  `dominio/ciberdefensa`.
