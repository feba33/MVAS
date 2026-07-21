---
titulo: "Epidemiología"
capa: "dominio"
tema: "epidemiologia"
fuente: "https://en.wikipedia.org/wiki/Epidemiology"
fuente2: "https://www.cdc.gov/epidemiology/"
fecha: "2026-07-21"
confianza: "alta"
tags: ["epidemiología", "salud-pública", "vigilancia", "estudios-observacionales", "determinantes-salud", "prevención"]
profundidad: 3
estado: "profundo"
rol: ["head-of-medical-affairs", "head-of-clinical-data-management", "head-of-rd", "head-of-regulatory-affairs"]
actividades: ["vigilancia-epidemiológica", "investigación-brotes", "diseño-estudios", "análisis-riesgo", "políticas-basadas-evidencia"]
organizaciones: ["who", "cdc", "epi", "iac", "society-epidemiologic-research", "iea"]
responsabilidades: ["distribución-enfermedades", "determinantes", "prevención", "control", "evaluación-intervenciones"]
tareas: ["diseño-cohorte", "caso-control", "ensayos-pragmáticos", "meta-análisis", "modelado-enfermedades"]
---

# Epidemiología: distribución de enfermedades, determinantes, vigilancia, estudios (cohorte/caso-control), vs salud-pública/medicina/salud

## Definición y alcance

**Epidemiología** = estudio de la **distribución** y **determinantes** de estados/eventos relacionados con la salud en poblaciones específicas, y **aplicación** de este conocimiento para control de problemas de salud (Last, 1988; Porta, 2014).

**Tres pilares**:
1. **Distribución**: ¿Quién? ¿Dónde? ¿Cuándo? (persona, lugar, tiempo)
2. **Determinantes**: causas, factores de riesgo/protección, mecanismos causales
3. **Aplicación**: prevención, control, políticas, evaluación intervenciones

**Diferencia clave vs medicina clínica**: unidad de análisis = **población** (no individuo); objetivo = **prevención primaria/secundaria/terciaria** a nivel poblacional.

## Medidas de frecuencia y asociación

### Frecuencia
| Medida | Fórmula | Uso |
|--------|---------|-----|
| **Prevalencia** (puntual/período) | Casos existentes / Población en riesgo | Carga enfermedad, planificación servicios |
| **Incidencia** (acumulada/tasa) | Casos nuevos / Población en riesgo (tiempo) | Riesgo desarrollar enfermedad, etiología |
| **Mortalidad** | Defunciones causa específica / Población | Impacto letalidad, tendencias temporales |
| **Años de vida perdidos (AVPP)** | Σ (esperanza vida - edad muerte) | Carga prematura, priorización |

### Asociación / efecto
| Diseño | Medida | Interpretación |
|--------|--------|----------------|
| **Cohorte** | Riesgo relativo (RR), Rate Ratio (IRR), Hazard Ratio (HR) | RR > 1 = factor riesgo; RR < 1 = protector |
| **Caso-control** | Odds Ratio (OR) ≈ RR si enfermedad rara | OR = (a×d)/(b×c) en tabla 2×2 |
| **Transversal** | Prevalence Ratio (PR), OR | Asociación simultánea exposición-enfermedad |
| **ECA / Pragmático** | Risk Difference (RD), NNT, HR | Efecto causal intervención |

**Ajuste confusión**: estratificación (Mantel-Haenszel), regresión multivariable (logística, Cox, Poisson), propensity score (matching, IPTW, estratificación), G-methods (g-computation, IPTW, TMLE).

## Diseños de estudio observacionales

### 1. Cohorte (longitudinal, prospectiva/retrospectiva)
- **Población base** → clasificación exposición basal → seguimiento → detección desenlaces.
- **Ventajas**: temporalidad clara, múltiples desenlaces, incidencia, sesgo recuerdo mínimo.
- **Retos**: pérdida seguimiento (attrition bias), costo/tiempo, cambios exposición/confusores tiempo-dependientes.
- **Ejemplos**: Framingham Heart Study (1948-), Nurses' Health Study (1976-), UK Biobank (500k), EPIC, Mexican Teachers' Cohort.

### 2. Caso-control
- **Casos** (enfermos) vs **Controles** (no enfermos) → exposición retrospectiva.
- **Ventajas**: eficiente enfermedades raras, latencia larga, múltiples exposiciones.
- **Retos**: sesgo selección (controles representativos población base), sesgo recuerdo, no permite incidencia directa.
- **Anidados**: casos-controles dentro de cohorte definida (eficiente, acceso muestras basales).

### 3. Transversal (prevalencia)
- Exposición y desenlace medidos **simultáneamente**.
- **Uso**: prevalencia, hipótesis generadoras, carga enfermedad, factores asociados (no causalidad).
- **Sesgo**: supervivencia (prevalencia = incidencia × duración), temporalidad ambigua.

### 4. Serie de tiempo / ecológicos
- Unidad análisis = **grupo/población** (no individuo).
- **Riesgo**: falacia ecológica (asociación grupo ≠ individuo).
- **Uso**: tendencias seculares, evaluación intervenciones poblacionales (ej. vacunación, fortificación, políticas tabaco).

### 5. Ensayos pragmáticos / híbridos
- **Pragmáticos**: condiciones reales, criterios inclusión amplios, desenlaces relevantes pacientes (PRECIS-2).
- **Híbridos tipo 1/2/3** (Curran et al.): efectividad + implementación simultánea.

## Vigilancia epidemiológica

**Definición** (CDC/OMS): recolección, análisis, interpretación **continua, sistemática** de datos salud → diseminación oportuna → acción.

| Tipo | Características | Ejemplos |
|------|-----------------|----------|
| **Pasiva** | Notificación rutinaria proveedores/laboratorios | Enfermedades de notificación obligatoria (ENO) |
| **Activa** | Búsqueda proactiva casos (personal campo, revisión registros) | Eradicación polio, vigilancia influenza grave |
| **Centínea** | Sitios representativos reportan todos casos | Red Global Vigilancia Influenza (GISRS), Dengue |
| **Sindrómica** | Datos pre-diagnóstico (urgencias, farmacias, ausentismo) | Detección temprana brotes, olas calor, bioterrorismo |
| **Basada en eventos** | Minería web/noticias/redes (EIOS, HealthMap, ProMED) | Alerta temprana enfermedades emergentes |

**Indicadores calidad**: sensibilidad, representatividad, oportunidad, simplicidad, flexibilidad, aceptabilidad, valor predictivo positivo.

## Investigacion de brotes (Outbreak Investigation)

**Pasos CDC (10 pasos)**:
1. Preparación (equipo, recursos, autoridad legal)
2. Confirmar existencia brote (exceso casos vs baseline)
3. Verificar diagnóstico (clínico, lab, definición caso)
4. Construir definición caso (clínico + tiempo + lugar + persona)
5. Encontrar casos sistemáticamente (búsqueda activa)
6. Descripción datos (curva epidémica, mapa spot, tabla persona)
7. Generar hipótesis (patrón transmisión, vehículo)
8. Evaluar hipótesis (estudio analítico: cohorte/caso-control)
9. Implementar control/prevención (inmediato + largo plazo)
10. Comunicar hallazgos (informe, publicación, lecciones aprendidas)

**Herramientas**: Epi Info, R (epitools, surveillance, OutbreakTools), Go.Data (OMS), DHIS2.

## Modelado matemático de enfermedades infecciosas

| Modelo | Ecuación base | Parámetros clave | Uso |
|--------|---------------|------------------|-----|
| **SIR** (Kermack-McKendrick 1927) | dS/dt = -βSI/N; dI/dt = βSI/N - γI; dR/dt = γI | R₀ = β/γ; umbral inmunidad colectiva = 1-1/R₀ | Dinámica transmisión, tamaño epidemia final |
| **SEIR** | + Expuestos (E): dE/dt = βSI/N - σE | Período latencia 1/σ | Enfermedades con incubación (COVID, sarampión) |
| **Meta-población** | Acoplamiento patches (movilidad, transporte) | Matriz movilidad, R₀ local | Espacial, internacional (Global Epidemic and Mobility Model) |
| **Basados en agentes (ABM)** | Individuos heterogéneos, contactos, comportamiento | Redes contacto, adherencia intervenciones | Intervenciones no farmacológicas (cierres, mascarillas) |
| **Nowcasting / forecasting** | Modelos estadísticos (ARIMA, ETS, Rt estimation EpiEstim) | Serie temporal casos, movilidad, variantes | Pronóstico corto plazo, evaluación intervenciones |

**R₀ vs Rt**: R₀ = número reproductivo básico (población totalmente susceptible); Rt = efectivo tiempo t (inmunidad, intervenciones, comportamiento).

## Epidemiología de enfermedades no transmisibles (ENT)

**Factores riesgo modificables** (GBD 2019): hipertensión, tabaquismo, glucosa alta, PM2.5, obesidad, alcohol, dieta baja frutas/verduras, inactividad física, colesterol LDL, riñón.

**Enfoque vida entera (life-course)**: exposoma (exposiciones acumuladas prenatal→vejez), programación fetal (Barker hypothesis), acumulación riesgo, ventanas críticas.

**Prevención**:
- **Primaria**: reducción exposición (impuestos tabaco/azúcar, reformulación alimentos, entornos activos, aire limpio).
- **Secundaria**: tamizaje basado evidencia (mama, cervix, colon, pulmón alto riesgo, HTA, glucosa, lípidos) — criterios Wilson-Jungner.
- **Terciaria**: rehabilitación, manejo enfermedad crónica, cuidados paliativos.

## Inferencia causal en epidemiología

**Contrafactuales (Rubin Causal Model)**: Y(1) vs Y(0) — efecto causal = Y(1) - Y(0) para mismo individuo (fundamental problem of causal inference).

**Criterios Bradford Hill** (1965) — guía, no checklist:
1. Fuerza asociación
2. Consistencia (replicabilidad)
3. Especificidad
4. Temporalidad (necesaria)
5. Gradiente dosis-respuesta
6. Plausibilidad biológica
7. Coherencia
8. Experimentación (ECA, experimentos naturales)
9. Analogía

**Métodos modernos**:
- **Variable instrumental (IV)**: aleatoriedad natural (ej. polimorfismos genéticos — *Mendelian Randomization*), políticas (edad elegibilidad, distancia hospital).
- **Diseños cuasi-experimentales**: discontinuidad regresión (RDD), diferencias-en-diferencias (DiD), control sintético, series temporales interrumpidas (ITS).
- **G-methods**: g-computation, IPTW marginal structural models, g-estimation — confusión tiempo-dependiente.
- **Targeted Maximum Likelihood Estimation (TMLE)**: doble robustez, eficiente, machine learning (Super Learner).

## Epidemiología genética / molecular

- **Epidemiología molecular**: biomarcadores exposición/susceptibilidad/efecto (adductos ADN, metabolitos, omics).
- **Mendelian Randomization (MR)**: variantes genéticas como IV para exposición (ej. *ALDH2* alcohol, *PCSK9* LDL-C, *FTO* obesidad) → inferencia causal sin confusión/retro-causalidad.
- **GWAS + MR + colocalización** → dianas terapéuticas validadas genéticamente (éxito 2-3x mayor en fases clínicas).

## Evaluación de intervenciones y políticas

| Diseño | Cuándo usar | Ejemplo |
|--------|-------------|---------|
| **ECA cluster** | Intervención nivel grupo, factible aleatorización | Vacunación escuelas, agua/saneamiento comunidades |
| **Stepped wedge** | Ético/práctico todos reciben intervención eventualmente | Despliegue progresivo programa salud |
| **DiD** | Política implementada en algunas áreas/tiempos | Impuesto bebidas azucaradas (México 2014, UK 2018) |
| **RDD** | Corte arbitrario elegibilidad | Programa transferencias condicionadas (PROGRESA/Oportunidades) |
| **Control sintético** | Una unidad tratada, muchas control | Reforma salud Massachusetts (Romneycare) vs EE.UU. |
| **Real-world evidence (RWE)** | Datos rutinas (EHR, claims, registros) + métodos causales | Vigilancia post-comercialización fármacos, efectividad comparativa |

## Cross-refs

- [[dominio/salud-publica]] — prevención, promoción, sistemas salud, políticas
- [[dominio/economia-de-la-salud]] — CEA, CUA, HTA, QALY, DALY, threshold
- [[dominio/biostadistica]] — inferencia, modelado, meta-análisis, Bayesian
- [[dominio/ciencia-de-datos]] — ML epidemiológico, predicción riesgo, fenotipado digital
- [[dominio/gestion-de-la-calidad]] — vigilancia calidad, indicadores, auditoría
- [[rol/head-of-medical-affairs]] — estrategia evidencia, KOLs, medical affairs
- [[rol/head-of-clinical-data-management]] — datos ensayos, EDC, calidad
- [[rol/head-of-rd]] — pipeline I+D, epidemiología translacional
- [[rol/head-of-regulatory-affairs]] — evidencia regulatoria, RWE, post-marketing
- [[sustrato/mexico/salud]] — Secretaría Salud, IMSS, Cofepris, vigilancia
- [[sustrato/estados-unidos/salud]] — CDC, FDA, CMS, NIH, vigilancia
- [[sustrato/canada/salud]] — PHAC, Health Canada, provincias, CADTH