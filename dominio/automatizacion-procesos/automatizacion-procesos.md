---
titulo: Automatización de procesos
capa: dominio
tema: automatizacion-procesos
fuente: https://www.deloitte.com/us/en/what-we-do/capabilities/applied-artificial-intelligence/articles/ai-agents-in-collaborative-automation.html
fuente2: https://www.gartner.com/en/information-technology/glossary/hyperautomation
fecha: 2026-07-17
confianza: alta
tags: [automatizacion, RPA, BPM, hyperautomation, IA-agentes, procesos, eficiencia]
organizaciones: [Deloitte, Gartner, UiPath, AutomationEdge]
rol: [head-of-operations, chief-operating-officer, head-of-continuous-improvement]
profundidad: 2
estado: profundo
---

# Automatización de procesos

La **automatización de procesos** aplica tecnología para ejecutar tareas de un flujo de
trabajo con mínima intervención humana, mejorando velocidad, calidad y costo. Evoluciona
desde la automatización de reglas hacia la **hiperautomatización** y los **agentes de IA**.

## Enfoques
- **BPA (Business Process Automation):** orquestación de workflows de extremo a extremo
  sobre BPMN; integra sistemas mediante APIs y middleware.
- **RPA (Robotic Process Automation):** robots de software que imitan clics/teclas en la
  capa de presentación para tareas repetitivas (conciliación, onboarding, data entry).
- **BPM (Business Process Management):** disciplina de modelado, ejecución y mejora
  continua de procesos (notación BPMN 2.0).
- **Hiperautomatización:** combinación de RPA + IA + process mining + low-code para
  automatizar procesos complejos de principio a fin (término acuñado por Gartner).
- **Agentes de IA / agentic automation:** sistemas que razonan, planifican y ejecutan
  acciones multicanal con supervisión humana (Deloitte: "AI agents redefining BPA").

## Componentes tecnolónicos
ETL/integración, OCR/IDP (document AI), NLP/conversational AI, machine learning para
excepciones, orquestadores (control room), y **process mining** para descubrir
cuellos de botella.

## Beneficios y riesgos
- Beneficios: reducción de errores, ciclos más cortos, liberar talento para trabajo de valor,
  cumplimiento auditable.
- Riesgos: deuda técnica de bots frágiles, gobernanza, excepciones no previstas, impacto
  laboral y sesgos en modelos. Requiere **CoE de automatización** y gestión del cambio.

## Relación con otros nodos
Complementa `dominio/automatizacion` (RPA general), `dominio/operaciones`,
`dominio/gestion-del-cambio` y `rol/head-of-continuous-improvement` (OpEx).
