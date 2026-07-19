---
titulo: Inteligencia artificial generativa
capa: dominio
tema: computacion
fuente: https://www.copyright.gov/ai/
fuente2: https://link.springer.com/article/10.1007/s44163-025-00379-6
fecha: 2026-07-19
confianza: alta
tags: [ia-generativa, llm, rag, agentes, gobierno-de-modelos, copyright, entrenamiento, multimodal]
rol: []
actividades: []
organizaciones: [us-copyright-office, eu-ai-act, nist-ai-rmf]
responsabilidades: []
tareas: []
profundidad: 2
estado: profundo
---

# Inteligencia artificial generativa

La **IA generativa** (genAI) es la subdisciplina de la inteligencia artificial que produce
contenido novedoso — texto, imagen, audio, video, código — a partir de modelos
probabilísticos entrenados sobre grandes corpus. Los **modelos de lenguaje grandes (LLMs)**
son su núcleo (arquitecturas Transformer, decenas a miles de millones de parámetros).

## Arquitecturas y patrones
- **LLMs base / instruct:** pre-entrenamiento auto-supervisado + fine-tuning supervisado y
  RLHF (aprendizaje por refuerzo con retroalimentación humana) para alineación.
- **RAG** (Retrieval-Augmented Generation): inyecta conocimiento organizacional actualizado
  vía búsqueda en una base de datos/vector store; reduce alucinaciones y ancla respuestas en
  fuentes. Requiere **gobernanza de datos** (calidad, linaje, derechos de acceso).
- **Agentes:** sistemas que planifican, usan herramientas (APIs, código) y ejecutan
  tareas de forma autónoma en bucles de razonamiento-acción.
- **Multimodal:** combina texto, visión y audio en un mismo modelo.

## Gobierno y riesgos
- **Gobernanza de modelos:** evaluación (eval), monitoreo de deriva, red teaming,
  human-in-the-loop, trazabilidad. Alineado con el **NIST AI RMF** y el **EU AI Act**.
- **Privacidad y datos:** entrenamiento y contexto pueden filtrar PII; requiere
  anonimización, límites de retención.
- **Alucinaciones / exactitud:** validación de salidas en contextos de alto riesgo.
- **Seguridad:** prompt injection, exfiltración de datos, abuso (deepfakes, malware).

## Derecho de autor y entrenamiento
El uso de **obras protegidas para entrenar modelos** es el principal foco de litigio
(EE.UU., UE, Japón, Brasil). La *U.S. Copyright Office* publicó reportes (2023-2025)
analizando el alcance del copyright en obras generadas por IA y el uso de material
protegido en entrenamiento; se debaten transparencia obligatoria y compensación a
titulares. Régimen varía: Japón permisivo, UE con excepción de minería de texto y datos
(sujeta a opt-out), EE.UU. bajo doctrina de *fair use* en litigio.

## Relación con otras capas
- De `dominio/computacion` (aprendizaje-automatico, ciencia-de-datos-empresarial).
- Gobierno: `dominio/gobernanza-etica-ia`, `rol/head-of-ai-strategy`, `rol/head-of-ai-product`.
- Riesgo: `rol/head-of-model-risk`, `dominio/ciberseguridad`.
