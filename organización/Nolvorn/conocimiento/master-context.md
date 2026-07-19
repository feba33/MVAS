---
titulo: Nolvorn — Master Context (síntesis v1.3)
capa: organización
tema: identidad canónica, servicios, pricing, mercados, roadmap y moats de Nolvorn
fuente: google-drive://nolvorn/Resources/Org/Master Context (v1.3, 2026-07-19)
fuente2: https://nolvorn.com
fecha: 2026-07-19
confianza: alta
tags: [nolvorn, master-context, identidad, servicios, pricing, roadmap, moats]
organizaciones: [nolvorn]
responsabilidades: [hermes-nolvorn]
profundidad: 2
estado: profundo
---

# Nolvorn — Master Context (síntesis v1.3)

Síntesis de `nolvorn_master_context` v1.3 (Julio 2026, 804 líneas) del Shared
Drive "nolvorn". Es la fuente de identidad canónica para LLM handoff. Cuando
algo aquí entre en conflicto con una instrucción explícita y más reciente de
Fernando en la sesión actual, gana Fernando. (Styling: plain, minimal.)

## Qué es Nolvorn
Firma boutique de Software & Technology Partners, fundada y liderada por Fernando
Balderas (ingeniero full-stack con experiencia Fortune 500 en PayPal y The Home
Depot Global Technology Center). Opera como equipo pequeño senior-led. Entrega
proyectos de software AI-augmented, engagements de advisory e ingeniería integrada
a mid-market en México y EE.UU. Es el motor de cash-flow y vehículo de credibilidad
del portafolio de Fernando.

Posicionamiento (una frase): Nolvorn cierra la brecha de ejecución para
organizaciones donde la restricción no es capacidad, es concretar — combinando
conocimiento técnico de primer nivel e innovación continua con pricing accesible
y financiable, y entrega rápida y continua.

La brecha que ocupa: entre freelancers de $5k (sin credibilidad ni estructura de
responsabilidad) y consultoras enterprise de $500k (lentas, caras, junior-heavy).
En Tamaulipas y NE México esa brecha está desocupada.

## Identidad y marca
- Nombre: Nolvorn (trademark pendiente de registro).
- Taglines: "Software & Technology Partners" (interno) / "Enterprise Engineering
  at Speed" (sitio).
- Website: nolvorn.com. Fundada 2026. HQ: Tampico, Tamaulipas, México.
- Mercados: México (primario), EE.UU. (secundario, remoto-only).
- Idiomas: Español (MX, /es/), Inglés (EE.UU., async).
- Entidad legal: opera como PFAE bajo Fernando Balderas. Incorporación S.A.S.
  se dispara cuando: entra socio, hay cláusula de responsabilidad en contrato, o
  facturación excede ~80–100k MXN/mo.
- Color primario: #0F8A6E (Nolvorn Green). Tipografía: Orelega One (display,
  -5% tracking) + Afacad (body/UI). Ver `brand-system.md`.
- Personalidad: Precise, Quiet, Authoritative, Trustworthy, Modern with retro
  sensibility. Referencia estética: Oliver Wyman meets early Macintosh / Palo Alto.
- Nunca debe percibirse como "cheap" (mediocre). "Accesible y financiable" no es
  "barato".

## Qué NO es Nolvorn
No es staffing agency (sin colocación de headcount), no dev shop (sin hourly
billing ni equipos junior-heavy), no AI product company (AI es metodología de
entrega, no producto), no large consultancy (sin overhead/burocracia), no
freelancer operation (estructura firma, liability framework, outcome ownership).

## Fundador y Principal
- Fernando Balderas, 24, Mexicano, Tampico. Principal & Lead Architect.
- Experiencia: PayPal México (via TCS, 2022–2024), The Home Depot GTC (SWE I,
  Jul 2024–presente). Competencias: full-stack, cloud (GCP), AI-augmented
  delivery, system architecture, REST API, DevOps básico.
- Educación: B.Eng Computer Systems (97/100), M.Eng Software (90/100), MBA +
  Finance minor en curso (TecMilenio 2026–2028, 10 hrs/sem).
- THD y MBA son "protected commitments" — nunca sacrificados. Capacidad Nolvorn:
  ~20 hrs/semana.

## Equipo (cambio material v1.3)
Nolvorn es un equipo de 3 (al cierre de v1.3): Fernando (Principal & Lead
Architect) + 2 miembros de delivery (SRE1-level / recién egresados).
- Estructura: project rev-share — compensados por proyectos entregados, no
  salariados ni con equity.
- Responsabilidad actual: sostienen 100% de operación diaria y ejecución de
  deliverables mientras Fernando construye la capa de sistema (MVAS,
  documentación, infraestructura de experiencia de cliente).
- Estado cliente-facing: aún no; integración gradual y deliberada, con meta de
  que cada uno eventualmente posea un proyecto end-to-end.
- Modelo de entrega: senior-led, team-executed. Fernando sigue siendo arquitecto
  y dueño final de accountability en cada engagement.
- Cambio vs modelo previo: "Principal-led always — no handoff to juniors" quedó
  retirado como constraint operativo (describía realidad solo-operador, no un
  moat deliberado). El copy de marketing que aún dice "no overhead, no juniors,
  no handoff" es posicionamiento retórico contra large-firm bloat, no promesa
  operativa literal.

## Core differentiators (moat actual)
- Top-tier knowledge + continuous innovation (AI-native applied).
- Client-friendly pricing con opciones de financiamiento (sin leer como descuento).
- Fast, continuous delivery (semanal, no phase-gated).
- No overhead (AI-native, sin markup de agencia).
- Outcome ownership (responsabilidad contractual a deliverables, no horas).
- Senior-led, team-extended.
- Full-stack end-to-end (design, build, deploy, document).
- AI orchestration depth (agent workflows, enterprise AI experience real).
- Fortune 500 pedigree a precio SMB (PayPal + THD, 1.6B txns/anño).

## Tech stack
Forgejo (VCS/CI en Hostinger VPS) · Plane.so (issue tracking) · n8n
(orchestration) · OpenObserve (monitoring) · Cloudflare Pages (frontend) ·
Railway (backend) · Supabase/Neon (DB) · GCP (cloud primario) · Figma (design) ·
Notion + Google Drive (docs/PM) · Claude/Cursor (AI delivery) · Telegram +
WhatsApp (client comms).

## Servicios (4 tiers + productized)
01 Advisory — architecture review, tech audits, fractional CTO. Retainer.
   MX 15–25k MXN/mo · EE.UU. $500–1,250/mo.
02 Project Delivery — fixed-fee scoped builds (migrations, integrations, MVPs).
   MX 20–80k MXN fixed · EE.UU. $750–4,000+ USD fixed.
03 Integrated Engineering (renombrado desde "Embedded") — backlog execution,
   platform admin, staff augmentation, technical oversight. Async-first.
   MX 20–35k MXN/mo · EE.UU. $1,000–1,750/mo.
04 Transformation — multi-month legacy modernization. Opportunistic.
   MX 150k+ · EE.UU. $50k+ USD.

Productized Offers (sin sales call; trojan horse a engagement mayor):
- Tech Audit Sprint — 3-day review + reporte. 8,500 MXN / $800 USD.
- Legacy API Migration — Starter — 1 endpoint a REST moderno, 2 semanas.
  18,000 MXN / $1,800 USD.
- AI Workflow Audit — 2-day audit de 1 proceso. 12,000 MXN / $1,200 USD.
- MVP in 30 Days — live en 30 días. 45,000 MXN / $4,500 USD.

## Target markets (3 ICPs)
Primario — MX Industrial/Regional: compañía regional en petrochemical, maritime,
logistics, manufacturing. Revenue $5–200M USD. Geo: Tampico, Altamira, Reynosa,
Matamoros, Monterrey, Veracruz. IT low-medium. Decision maker: Owner/GM/Ops/IT
Director, a menudo no-técnico, compra por confianza. Pain: bottleneck operativo
solucionable por software. Budget $15–100k MXN/engagement; retainer 15–25k/mo.
Compra por referral/introducción personal.

Secundario — US Remote/Async: B2B SaaS startup ($1–20M ARR) o mid-market
($20–100M ARR). Decision maker: CTO/VP Eng/Founder-CTO, técnico. Pain: capacity
gap. Budget $5–50k USD/project; Integrated Eng $1–1.75k/mo. Channel: Contra,
Gun.io, Lemon.io, LinkedIn outbound. Edge: AI-native, CST tz, Fortune 500,
fixed-fee, financing, 40–60% cost vs US.

Terciario — Nearshoring foreign companies en MX: fabricantes recién llegados a
Tamaulipas/NE México. Mayor LTV. Retainer potential $30–150k MXN/engagement.

## Market context
- MX tech consulting CAGR 12.80% (segmento de consultoría de más rápido
  crecimiento en México).
- Tamaulipas FDI $20B+ activo, 146 proyectos confirmados, 6.3% crecimiento
  industrial (3er nacional, 2025).
- Industrias clave: Petrochemical/oil&gas, Maritime/port logistics, Automotive
  (192 empresas: Eaton, Magna, Valeo), Aerospace, Electrical/electronic.
- Señal global: 40% de enterprise buyers buscan activamente alternativas a Big
  Four.

## Competitive position
Compite en la brecha freelancers↔enterprise. En Tamaulipas está desocupada.
Big Four/Accenture (threat low, min $100k+, 6–18mo), regional dev shops (medium,
sin strategy/AI/F500), freelancers/Upwork (low, sin firm/liability), nearshore
staffing (medium US, venden headcount no outcomes), world-class indies (high
teórico, pero vertical+relación compiten más rápido).

## Pricing & payment
Filosofía: precio por output, no por hora. Written scope antes de cada
engagement. Liability capped al contract value. No trabajo sin signed scope +
first payment. Regla dura: el precio NO es negociable; el scope sí. Si el cliente
presiona en precio → reducir scope, nunca precio. Ninguna opción de
financiamiento/installment cambia el precio total (nunca es descuento).

Estructuras: Full upfront (small/short) · 50/50 (default fixed-scope) ·
Milestone 30/40/30 (medium-large) · Success-based (outcome/KPI, selectivo) ·
Final-deliverable/post-delivery (high-trust only) · Revenue share % of sales
(capped, time-limited, B2C) · Interest-free installments self-administered (0%,
trusted clients) · Third-party financing BNPL (Stripe, paga Nolvorn full, cliente
repaa al proveedor) · Retainer-credit/prepaid pool (lump sum a par, drawdown) ·
Milestone + success kicker híbrido (5–10% extra en métrica post-launch).

## Sales methodology
Sin deck, sin pitch: conversación de 30 min sobre el problema real. Público:
Audit, Define, Build, Transfer. Interno: 01 Discovery (4 preguntas: qué sistema,
qué falla, qué has intentado, qué es éxito) · 02 Proposal 48hrs (written scope
1-pager: problem, solution, deliverables, timeline, fixed price, liability cap,
payment) · 03 Negotiation (scope flexible, precio no) · 04 Close (signed + first
payment) · 05 Delivery (weekly check-in, scope change = mini-proposal) ·
06 Completion (deliver + docs + 30-day support + testimonial + 2 intros).

## GTM strategy
Two-speed engine: MX (relationship-first, slow cycle) y US (portfolio-first, fast
cycle) simultáneos sin canibalización. MX beachhead Tampico/Altamira, zero travel,
credential anchor "el ingeniero de PayPal/THD trabaja para ti a fracción de
costo". US platform-first (Contra/Gun.io, 3 portfolio entries mínimo), first
message = interview. Marketing channels por prioridad: case studies en sitio →
LinkedIn de Fernando (1–2x/sem EN+ES) → platform profiles → website → referral
program → technical content (12–18mo).

## Clients & portfolio
- AMarin (amarine.com.mx): Tampico PPE company. Binary blob→GCS migration.
  CLI script (18,000 MXN) + REST service (55,000 MXN). Proposal entregada Jun 2026.
  Primer engagement documentado.
- Second use case: confirmado que existe, no documentado individualmente aún.
- Claim público vs documentado: nolvorn.com dice "15+ Projects, 4 Industries" —
  preciso bajo portfolio policy (agrega toda la carrera de Fernando, no solo
  Nolvorn-branded). Actualmente 2 use cases Nolvorn-specific; case study
  production es backlog item, no gap urgente.
- Portfolio policy: todo el work previo de Fernando (THD, PayPal, pre-Nolvorn
  freelance) es válido para el portafolio Nolvorn, enmarcado como principal-led.

## Growth roadmap
Phase 0 — Foundation (ahora→Aug 2026): equipo de 3 operando; nolvorn.com live
bilingüe con case study AMarin; LinkedIn optimizado; 1 US platform profile;
Tech Audit Sprint live; 1 cliente MX adicional; paperwork automatizado vía MVAS
(ver MVAS Operating Architecture doc). Exit: infraestructura completa + 1 cliente
MX activo más allá de AMarine + ambos use cases documentados.
Phase 1 — Traction (Sep 2026→Q2 2027): 2 clientes MX (1 retainer), 1 US engagement
completado 5-star, ≥1 team member client-facing, billing combinado $120k MXN/mo
equivalente sostenido. Exit revisado: ya NO gated a hire decision (el equipo ya
existe en rev-share; admin se automatiza). Ahora: $120k/mo sostenido + ≥1 member
operando proyecto end-to-end.
Phase 2 — Scale (Q3 2027→2028): Farm liquidity ($50–100k USD, Sep 2027) deploy
según thesis; rev-share members evaluados para senior partner (equity-adjacent);
vertical specialization declarada (Nolvorn = industrial tech firm de NE México);
US direct outbound; $1M USD transformation contract realista H1 2028.

## Moats
Current: geographic arbitrage (Tampico + F500 creds) · price-credibility gap ·
AI delivery speed (2–6 semanas) · Fortune 500 credentials (permanentes) ·
senior-led team-extended · client-friendly pricing con financing.
Being built (12–24mo): vertical expertise industrial/maritime · case study library
(10 = el compounding asset más agudo; gap actual 2 vs 15+ claimed) · productized IP
· AI orchestration depth · team capability (2 members → independent ownership).
Long-term (2028+): vertical SaaS product (petro/maritime) · partner network ·
brand authority (Fernando voz definitiva industrial tech NE México).

## Entity boundaries (Nolvorn vs Pinnd)
Separadas en brand, finances, operations, legal. Nolvorn: active fees (retainers,
fixed fees); Pinnd: equity appreciation only. Nolvorn cliente paga Nolvorn; Pinnd
es co-founder equity partnership. Nolvorn una firma entity; Pinnd nueva S.A.S. por
venture. Fernando: Nolvorn principal entregando/vendiendo; Pinnd equity partner
buildiendo productos. Talent: Nolvorn rev-share delivery team (desde Phase 0);
Pinnd OSS contributors informales. Portfolio cross-use: Pinnd outcomes MAY aparecer
en Nolvorn portfolio; Nolvorn brand NO aparece en Pinnd ventures.

## Operating rules (hard)
- Written scope antes de cada engagement.
- Liability capped al contract value.
- No trabajo sin signed scope + first payment.
- Precio no negociable; scope sí; financing cambia timing no total.
- Rev-share delivery partners pueden operar antes de revenue thresholds si hay
  talento confiable (ya no gated a Phase 1).
- No equity en Nolvorn antes de Phase 2 (inalterado, aplica pese a crecimiento
  rev-share).
- Todo proyecto completado → case study inmediato. Gap activo: 2 documentados vs
  15+ claimed.
- Fernando sigue siendo client relationship owner y final accountability holder;
  team members se vuelven client-facing gradualmente.

## Context hierarchy (para LLM)
1. Instrucción explícita en sesión actual de Fernando · 2. Master Context ·
3. Brand System v1.0 · 4. Fernando personal context brief · 5. General knowledge.
