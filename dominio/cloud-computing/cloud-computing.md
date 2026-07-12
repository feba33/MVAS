---
titulo: Cloud computing (IaaS/PaaS/SaaS, hyperscalers, IaC, FinOps)
capa: dominio
tema: cloud-computing
fuente: https://en.wikipedia.org/wiki/Cloud_computing
fuente2: https://aws.amazon.com/what-is-cloud-computing/
fecha: 2026-07-12
confianza: alta
tags: [cloud, iaas, paas, saas, finops, multi-cloud, hyperscalers, serverless, infraestructura-ti, ia-c]
english_keywords: [cloud computing, IaaS, PaaS, SaaS, hyperscaler, infrastructure as code (IaC), FinOps, multi-cloud, shared responsibility model]
---

# Cloud computing (IaaS/PaaS/SaaS, hyperscalers, IaC, FinOps)

## 📜 Cita
> "Cloud computing is the on-demand availability of computer system resources, especially data storage (cloud storage) and computing power, without direct active management by the user." — Wikipedia (Cloud computing)

## 📝 Conocimiento
- **Modelos de servicio:** **IaaS** (infra: VMs, almacenamiento, red — el cliente gestiona SO/apps), **PaaS** (plataforma para desarrollar/desplegar — gestiona runtime), **SaaS** (software terminado consumido vía web, p.ej. CRM/email). Modelos intermedios: FaaS/**serverless**, DaaS, CaC.
- **Modelos de despliegue:** **público** (multi-tenant, hyperscalers), **privado** (on-prem/virtualizado dedicado), **híbrido** (puente con conectividad/abstracción), **multi-cloud** (varios proveedores para evitar lock-in y resiliencia).
- **Hyperscalers:** **AWS** (líder ~30% cuota), **Microsoft Azure**, **Google Cloud (GCP)**, **Oracle Cloud**; ofrecen cientos de servicios gestionados.
- **Habililitadores:** **IaC** (Infrastructure as Code, p.ej. Terraform, desplegos repetibles/versionados), **contenedores/Orquestación (Kubernetes)**, redes definidas por software.
- **Economía:** paso de Capex a **Opex**; elasticidad (scale up/down); **FinOps** (práctica de optimizar costo cloud, cultura+metricas, Cloud Financial Management) cada vez más crítico por la facturación por consumo.
- **Seguridad — modelo de responsabilidad compartida:** el proveedor asegura infra/red física; el cliente asegura datos, identidad, configuración (ver `rol/ciso/`, `dominio/ciberseguridad-gobierno/`).
- **Tendencias:** serverless/edge, **soberanía de datos** (nubes soberanas, regiones locales), IA en la nube (GPU, modelos fundacionales como servicio — ver `dominio/ia-generativa/`).
- **Cross-ref:** `dominio/computacion/`, `dominio/iot/`, `dominio/automatizacion/`, `dominio/ia-generativa/`, `rol/cio/`, `rol/chief-digital-officer/`, `rol/enterprise-architect/`.

## 🔗 Referencia
- Wikipedia EN — Cloud computing: https://en.wikipedia.org/wiki/Cloud_computing
- AWS — What is cloud computing: https://aws.amazon.com/what-is-cloud-computing/
- FinOps Foundation: https://www.finops.org/
- Cross-ref: `dominio/computacion/`, `dominio/iot/`, `rol/cio/`, `rol/enterprise-architect/`.
