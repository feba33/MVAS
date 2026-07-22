---
titulo: "Economía del comportamiento"
capa: "dominio"
tema: "economia-del-comportamiento"
fuente: "https://en.wikipedia.org/wiki/Behavioral_economics"
fecha: "2026-07-22"
confianza: "alta"
tags: ["economia", "psicologia", "sesgos", "nudges", "arquitectura-eleccion", "prospect-theory"]
profundidad: 2
estado: "profundo"
---

# Economía del comportamiento / Behavioral Economics

## Definición

La **economía del comportamiento** integra conocimientos de la psicología cognitiva y social en modelos económicos para explicar decisiones que se desvían de la racionalidad clásica (*Homo economicus*). Estudia cómo **sesgos cognitivos**, **heurísticas**, **emociones** y **contexto** afectan elecciones de consumo, ahorro, inversión, salud, trabajo y política pública.

## Conceptos centrales

### 1. Racionalidad acotada (Bounded rationality) — Herbert Simon
- Los agentes tienen **información incompleta**, **capacidad cognitiva limitada** y **tiempo escaso**.
- Decisiones por **satisficing** (umbral de aceptabilidad) no maximización.

### 2. Teoría de la perspectiva (Prospect Theory) — Kahneman & Tversky (1979)
| Dimensión | Predicción | Evidencia |
|-----------|------------|-----------|
| **Valor** | Función en forma de S: cóncava en ganancias, convexa en pérdidas | Aversión a la pérdida (λ ≈ 2.25) |
| **Ponderación de probabilidades** | Sobrepondera prob. bajas, subpondera altas | Efecto certeza, efecto posibilidad |
| **Punto de referencia** | Dependiente del *status quo* o expectativa | *Endowment effect*, *status quo bias* |

### 3. Sesgos cognitivos principales
| Sesgo | Descripción | Aplicación |
|-------|-------------|------------|
| **Anclaje** | Dependencia excesiva de información inicial | Precios de referencia, negociación |
| **Disponibilidad** | Juicio por facilidad de recuerdo | Percepción de riesgo (terrorismo vs. accidente auto) |
| **Representatividad** | Juzgar por estereotipo/prototipo | Estereotipos, *base rate neglect* |
| **Exceso de confianza** | Sobreestimación de precisión propia | Trading, emprendimiento, planificación |
| **Presente (present bias)** | Preferencia fuerte por recompensas inmediatas | Ahorro, salud, adicciones |
| **Aversión a la pérdida** | Pérdidas duelen ~2x más que ganancias equivalentes | Seguros, *framing*, *default options* |
| **Efecto dotación (endowment)** | Valorar más lo que se posee | *Willingness to accept* > *willingness to pay* |
| **Contabilidad mental** | Categorizar dinero en "cuentas" no fungibles | Presupuesto, regalos vs. salario |

### 4. Heurísticas de decisión
- **Heurística de reconocimiento**: Si reconoces uno de dos objetos, inferir que tiene mayor valor.
- **Take-the-best**: Usar la pista más válida discriminatoria; ignorar el resto.
- **Fast-and-frugal trees**: Árboles de decisión simples para clasificación rápida (Gigerenzer).

## Nudge Theory y Arquitectura de la Elección (Thaler & Sunstein, 2008)

**Nudge** = intervención que altera comportamiento **sin prohibir opciones ni cambiar incentivos económicos significativos**, preservando libertad de elección (*libertarian paternalism*).

### Principios de diseño (EAST / MINDSPACE)
| Marco | Componentes |
|-------|-------------|
| **EAST** (BIT UK) | Easy, Attractive, Social, Timely |
| **MINDSPACE** | Messenger, Incentives, Norms, Defaults, Salience, Priming, Affect, Commitment, Ego |

### Herramientas (toolkit)
| Herramienta | Ejemplo |
|-------------|---------|
| **Default options** (opción por defecto) | Inscripción automática en pensiones (opt-out) → +30-50% participación |
| **Simplificación** | Formularios FAFSA simplificados → + matriculación universitaria |
| **Normas sociales** | "9 de 10 vecinos pagan impuestos a tiempo" → + cumplimiento |
| **Salience / Framing** | Etiquetas calóricas en menús; *loss framing* ("pierde $X si no actúas") |
| **Commitment devices** | Cuentas de ahorro con penalización por retiro anticipado (SEED, Commitment Savings) |
| **Feedback en tiempo real** | Medidores de energía en hogares → -5-15% consumo |
| **Pre-commitment** | Planes de ahorro "Save More Tomorrow" (Thaler & Benartzi) → + tasas ahorro |

## Aplicaciones por dominio

### Política pública (Gobiernos)
| País / Unidad | Intervención destacada | Resultado |
|---------------|------------------------|-----------|
| **UK — Behavioural Insights Team (BIT, "Nudge Unit")** (2010-) | Defaults pensiones, cartas impuestos, donación órganos | £100M+ ahorro/año; replicado en 30+ países |
| **EE.UU. — SBST (Social and Behavioral Sciences Team, Obama 2015)** | FAFSA, *Servicemembers Civil Relief Act*, prescripción opioides | Mejoras medibles en 15+ programas |
| **OECD — Behavioural Insights Network** | Guías metodológicas, repositorio casos | Estandarización, ética |
| **México — CONEVAL / SHCP** | *Nudges* en declaraciones fiscales, programas sociales | Pilotos en SAT, Bienestar |
| **Canadá — Impact and Innovation Unit (PCo)** | Vacunación, impuestos, beneficios | RCT en CRA, ESDC |

### Finanzas y ahorro
- **Save More Tomorrow (SMarT)**: Aumentar contribución 401(k) con cada subida salarial → tasas de ahorro del 3.5% al 13.6% en 40 meses.
- **Default en fondos *target-date*** → reducción error de asignación de activos.
- **Apps fintech** (Acorns, Qapital): *round-ups*, *rules-based saving*, *gamification*.

### Salud
- **Recordatorios SMS** → + adherencia medicación, citas médicas.
- **Defaults en donación de órganos** (opt-out: España, Austria, Bélgica) → tasas >90% vs. <15% opt-in.
- **Etiquetado nutricional** (semáforo, *traffic light*) → elecciones más saludables.

### Energía y medio ambiente
- **Opower / Oracle Utilities**: Informes comparativos de consumo vs. vecinos eficientes → -2% consumo agregado (RCT masivos).
- **Precios dinámicos + feedback** → desplazamiento de carga (*demand response*).

### Marketing y consumo
- *Decoy effect* (asymmetric dominance): Tercera opción hace atractiva la *target*.
- *Scarcity* ("Solo 3 habitaciones"), *social proof* ("12 personas viendo"), *anchoring* (precio tachado).
- *Subscription defaults* (renewal automático) → retención.

## Ética y límites

| Preocupación | Respuesta / Salvaguarda |
|--------------|-------------------------|
| **Manipulación** (ocultar opciones, *dark patterns*) | Transparencia: *nudges* deben ser visibles,易 opt-out |
| **Paternalismo** (¿quién define "mejor"?) | Deliberación democrática, *sunset clauses*, revisión independiente |
| **Equidad** (efectos diferenciados por SES, educación) | *Distributional analysis* obligatorio; *targeted nudges* vs. universales |
| **Efectos no deseados** (crowding-out motivación intrínseca) | Pilotos RCT, monitoreo continuo, *pre-registration* |
| **Privacidad** (datos conductuales masivos) | *Data minimization*, *purpose limitation*, consentimiento informado |

## Instituciones y red global
- **Behavioural Insights Team (BIT)** — UK, EE.UU., Australia, Singapur, Francia.
- **OECD Behavioural Insights Unit** — Red 30+ países, guías metodológicas.
- **World Bank — eMBeD (Mind, Behavior, and Development Unit)** — Aplicación en desarrollo.
- **UN Behavioural Science Group** — ODS, cambio climático, salud global.
- **Academia**: *Behavioral Science & Policy Association (BSPA)*, *Society for Judgment and Decision Making (SJDM)*, *Journal of Behavioral Economics*.

## Métricas de evaluación (RCT gold standard)
- **ITT (Intent-to-Treat)** vs. **TOT (Treatment-on-Treated)**.
- **Effect size** (Cohen's d), *lift* porcentual, *cost-effectiveness* ($/outcome).
- **External validity** — replicación en contextos/poblaciones distintas.
- **Ethical review** — IRB / *Ethics Advisory Board* (BIT, SBST, OECD).

## Referencias clave
- Kahneman, D. (2011). *Thinking, Fast and Slow*. Farrar, Straus and Giroux.
- Thaler, R.H. & Sunstein, C.R. (2008). *Nudge: Improving Decisions About Health, Wealth, and Happiness*. Yale UP.
- Tversky, A. & Kahneman, D. (1974). "Judgment under Uncertainty: Heuristics and Biases". *Science* 185(4157).
- Thaler, R.H. & Benartzi, S. (2004). "Save More Tomorrow™". *J. Political Economy* 112(S1).
- Halpern, D. (2015). *Inside the Nudge Unit*. WH Allen.
- OECD (2019). *Behavioural Insights and Public Policy: Lessons from Around the World*.
- [Wikipedia — Behavioral economics](https://en.wikipedia.org/wiki/Behavioral_economics)
- [BIT — Publications](https://www.bi.team/publications/)
- [OECD — Behavioural Insights](https://www.oecd.org/gov/regulatory-policy/behavioural-insights.htm)