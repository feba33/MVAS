---
titulo: NovaTech — empresa SaaS de ejemplo (organización)
capa: organización
tema: ejemplo-empresa
fuente: conocimiento general (reference-only)
fecha: 2026-07-09
confianza: alta
tags: [organizacion, empresa, ejemplo, saas]
english_keywords: [organizacion, empresa, ejemplo, saas]
---

# NovaTech — empresa SaaS de ejemplo

Entidad ficticia de demostración de la capa `organización`. Modela una startup SaaS
con su misión, estructura, producto, mercado, métricas y decisiones, siguiendo la
arquitectura LLM Wiki recursiva (todo aislado en `organización/ejemplo-empresa/`).

## 📝 Conocimiento

### Identidad y misión
- **Nombre:** NovaTech (entidad ficticia, con fines de demostración).
- **Tipo:** startup SaaS B2B.
- **Tamaño:** 50 empleados.
- **Sedes:** Ciudad de México (HQ) y Austin, Texas (EE.UU.).
- **Misión:** «Democratizar la automatización de procesos para PyMEs de habla hispana y
  EE.UU., reduciendo en 70% el tiempo de operación manual mediante flujos inteligentes».
- **Visión:** ser la plataforma de orquestación de workflows por defecto en LatAm para 2030.

### Estructura (org chart)
- **CEO** — Elena Vázquez (fundadora; visión y estrategia general).
  - **CTO** — Diego Ramírez (tecnología, arquitectura, seguridad). Reporta a la CEO.
    - **Engineering Manager** — lidera el equipo de ingeniería. → `rol/engineering-manager`
    - **Data Lead** — analítica y ML del producto. → `rol/data-lead`
    - Ingenieros de software / QA. → `rol/ingeniero-software`
  - **VP Sales** — Carlos Méndez (ventas enterprise + SMB, EE.UU. y México). → `dominio/ventas`
  - **VP Marketing** — Sofía Torres (marca, demand gen, contenido). → `dominio/marketing`
  - **Head of Product** — Ana López (descubrimiento, PMF, roadmap). → `dominio/producto`
  - **Finance Lead / Controller** — Roberto Cruz (FP&A, fundraising, control). → `rol/finance-lead`
  - **Head of People (RRHH)** — Lucía Fernández (cultura, contratación, compensación). → `dominio/recursos-humanos`

### Producto: NovaFlow
- Plataforma SaaS de automatización de workflows B2B para PyMEs.
- Capacidades: constructor de flujos no-code, integraciones vía APIs, analítica y motor de reglas.
- Modelo de negocio: suscripción mensual por asientos + tier enterprise.
- Stack: cloud multi-región (México/EE.UU.), cumplimiento SOC 2 en camino.

### Mercado
- Segmento: PyMEs (10–200 empleados) en México y EE.UU.
- Verticales: fintech, e-commerce y servicios profesionales.
- Contexto: opera bajo el marco de `sustrato/mexico/` y `sustrato/estados-unidos/`.

### Métricas clave
- **MRR / ARR:** ingreso recurrente mensual / anual.
- **Churn:** tasa de cancelación (objetivo < 3% mensual).
- **CAC / LTV:** costo de adquisición y valor de vida del cliente (objetivo LTV:CAC ≥ 3:1).
- **Pipeline:** oportunidades abiertas (ver `dominio/ventas`).
- **NPS:** satisfacción (objetivo > 40).
- **Burn rate / run-rate:** salud financiera (ver `rol/finance-lead`).

### Decisiones de ejemplo
1. **Expansión a EE.UU. (2025):** abrir oficina en Austin para acercarse a clientes
   enterprise y facilitar la ronda de financiamiento.
2. **Ronda Seed ($3M, 2025):** liderada con VC; uso de fondos en GTM y producto
   (ver `dominio/finanzas`).
3. **Fijación de precio por valor:** migrar de precio por asiento a tiers por volumen
   de ejecuciones.
4. **Contratación de CTO (2024):** decisión clave para escalar la arquitectura
   multi-tenant.

### Cómo un LLM opera esta entidad
- Lee `raw/` (inmutable) y genera/refina páginas con YAML frontmatter en
  `organización/ejemplo-empresa/`.
- Mantiene `index.md` y `log.md` (append-only) al ingerir conocimiento.
- Cruza referencias con `rol/*` (quién ejecuta) y `dominio/*` (cómo se hace).
- Al responder, prioriza métricas y decisiones validadas; marca `confianza` según la fuente.

## 🔗 Referencia
- `rol/engineering-manager/engineering-manager.md` — líder de ingeniería que reporta al CTO de NovaTech.
- `rol/data-lead/data-lead.md` — Data Lead responsable de analítica y ML del producto.
- `rol/finance-lead/finance-lead.md` — Finance Lead / Controller encargado de FP&A y fundraising.
- `dominio/producto/producto.md` — base de conocimiento de producto aplicada a NovaFlow.
- `dominio/ventas/ventas.md` — metodología y funnel usados por el VP Sales.
- `dominio/marketing/` — estrategia de marca y demand gen del VP Marketing.
- `dominio/recursos-humanos/recursos-humanos.md` — gestión de personas a cargo del Head of People.
- `dominio/finanzas/private-equity-vc.md` — rondas de financiamiento (Seed) de NovaTech.
- `sustrato/mexico/` — contexto México donde opera la sede HQ.
- `sustrato/estados-unidos/` — contexto EE.UU. donde opera la oficina de Austin.
