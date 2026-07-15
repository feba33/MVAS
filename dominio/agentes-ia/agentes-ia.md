---
titulo: Agentes de IA (Agentic AI)
capa: dominio
tema: agentes-ia
fuente: https://www.ibm.com/new/product-blog/powering-the-future-of-autonomous-it-operations-agentic-ai-ready-ibm-infrastructure
fuente2: https://modelcontextprotocol.io
fecha: 2026-07-15
confianza: alta
tags: [agentes-ia, agentic-ai, llm, mcp, automatizacion, orchestration, enterprise-ai]
english_keywords: [AI agents, agentic AI, LLM agents, Model Context Protocol, MCP, agent orchestration, tool use, AgentOps, enterprise AI]
profundidad: 2
estado: profundo
---

# Agentes de IA (Agentic AI)

## 📝 Conocimiento
- **Definición:** los **agentes de IA** (en el contexto de la IA generativa) son una
  clase de agentes inteligentes que **persiguen objetivos, usan herramientas y
  ejecutan acciones** con grados variables de autonomía, operando dentro de objetivos,
  restricciones y herramientas definidas por humanos. (Wikipedia — *AI agent*)
- **Patrón de operación:** el LLM "piensa" y las **herramientas** traducen ese
  razonamiento en acciones (recuperar datos o ejecutar comandos) contra sistemas
  empresariales y externos. Un agente combina planificación, uso de herramientas,
  memoria y bucle de retroalimentación.
- **Model Context Protocol (MCP):** estándar (Anthropic, 2024) que conecta sistemas
  de agentes con herramientas, datos y prompts de forma **normalizada**. Los **MCP
  servers** son la superficie de integración empresarial: exponen herramientas,
  recursos y *prompts* dentro de límites auditables. Es la base de interoperabilidad
  en el "agente empresarial". (modelcontextprotocol.io; IBM)
- **Agent Development Lifecycle (ADLC):** extensión de DevSecOps para agentes
  probabilísticos (IBM, *Architecting Secure Enterprise AI Agents with MCP*, verificado
  por Anthropic, 2025). Fases: Plan → Build → Test/Release → Deploy → Monitor →
  Operate, con bucles de experimentación (evals en build-time) y optimización en
  runtime. Prioriza *evaluation-first*, orquestación de *prompts*/herramientas,
  *guardrailed testing*, y observabilidad en runtime.
- **Seguridad por capas:** identidad del agente, herramientas de mínimo privilegio,
  ejecución en *sandbox*, y un **MCP Gateway** que centraliza autenticación,
  políticas, *rate-limits* y auditoría. *Kill-switches*, métricas de deriva/alucinación
  y catálogos gobernados. Relación con `dominio/ciberseguridad`.
- **Cuándo (no) usar agentes:** favorecer la solución más simple; los agentes
  brillan en tareas multi-paso complejas: soporte al cliente, procesos intensivos en
  documentos, y augmentación de trabajo de conocimiento. El *AgentOps* mueve de
  "¿está arriba?" a "¿está correcto?" (MELT: *metrics, events, logs, traces*).
- **Observabilidad del agente:** trazas de llamadas a herramientas, costos de token,
  y evaluaciones continuas — ver `dominio/observabilidade`. Converge con
  `dominio/computacion` (ingeniería de plataforma/SRE) y `dominio/ciencia-de-datos`.
- **Riesgos:** alucinaciones, acciones no autorizadas, *prompt injection*, dependencia
  de herramientas externas, y gobernanza de datos. Necesita *human-in-the-loop* en
  decisiones de alto impacto.

## 🔗 Referencia
- IBM — *Powering the future of autonomous IT operations: Agentic AI-ready IBM
  infrastructure* (2025) y *Architecting Secure Enterprise AI Agents with MCP*.
- Model Context Protocol — modelcontextprotocol.io (estándar, Anthropic).
- Wikipedia — *AI agent* (reference-only).
- Cross-ref: `dominio/computacion`, `dominio/observabilidade`, `dominio/ciberseguridad`,
  `dominio/ciencia-de-datos`, `dominio/regtech`.
