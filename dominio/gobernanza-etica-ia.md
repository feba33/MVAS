---
titulo: Gobernanza ética de la IA
capa: dominio
tema: gobernanza-etica-ia
fuente: https://en.wikipedia.org/wiki/Ethics_of_artificial_intelligence
fuente2: https://en.wikipedia.org/wiki/Artificial_Intelligence_Act
fecha: 2026-07-17
confianza: alta
tags: [ai-governance, ai-ethics, model-risk, human-in-the-loop, eu-ai-act, nist-ai-rmf, auditabilidad]
rol: []
actividades: []
organizaciones: []
responsabilidades: []
tareas: []
profundidad: 2
estado: profundo
---

# Gobernanza ética de la IA

## 📝 Conocimiento

### Definición
La **gobernanza ética de la IA** es el conjunto de procesos, comités y controles que aseguran que los sistemas de IA sean seguros, justos, auditables y alineados con valores y normas. Puente entre la ética de la IA (principios) y el gobierno de IA (riesgo/operación): traduce principios a decisiones operativas y cumplimiento regulatorio.

### Componentes
- **Comité de ética / AI Review Board:** revisión de casos de uso de alto riesgo, dilemas y excepciones.
- **Model risk management:** evaluación de sesgo, robustez, explicabilidad, monitoreo de deriva (drift).
- **Human-in-the-loop / human-on-the-loop:** supervisión humana según el riesgo.
- **Auditabilidad:** registros, trazabilidad de decisiones, documentación (model cards, datasheets).
- **Evaluación y red teaming:** pruebas de seguridad y comportamiento antes del despliegue.
- **Gestión del ciclo de vida:** desde el entrenamiento hasta el retiro (vs `dominio/gobierno-de-ia.md`).

### Marco normativo de referencia
- **EU AI Act (en vigor 1 ago 2024, aplicación gradual 6–36 meses):** clasificación por riesgo (inaceptable/alto/bajo/mínimo); obligaciones para IA de alto riesgo.
- **NIST AI Risk Management Framework (AI RMF):** marco voluntario (GOVERN/MAP/MEASURE/MANAGE).
- **ISO/IEC 42001:** sistema de gestión de IA.
- **OECD AI Principles**, **UNESCO** (ética de la IA).

### Actores
- **Chief AI Officer / Head of AI** (dueño de la estrategia), **Legal/Compliance**, **Risk**, **Producto**.
- **Reguladores:** agencias de protección de datos, autoridades sectoriales.

### Riesgos y dilemas
- **Sesgo y equidad:** discriminación en scoring/crédito/justicia.
- **Opacidad:** modelos no explicables en decisiones de alto impacto.
- **Desalineación:** comportamiento no previsto (agentes autónomos — `dominio/agentes-ia.md`).
- ** vs `dominio/etica-ia` y `dominio/gobierno-de-ia`:** ética = principios/filosofía; gobierno = operación/riesgo; gobernanza ética = cómo se institucionalizan los principios en la org.

### Cross-refs
- `dominio/etica-ia.md` · `dominio/gobierno-de-ia.md` · `dominio/agentes-ia.md`
- `rol/chief-ai-officer.md` · `rol/head-of-ai.md` · `dominio/proteccion-de-datos.md`
