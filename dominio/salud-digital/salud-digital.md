---
titulo: Salud digital (Digital Health)
capa: dominio
tema: salud-digital
fuente: https://en.wikipedia.org/wiki/Digital_health
fuente2: https://www.hl7.org/fhir/
fecha: 2026-07-18
confianza: alta
tags: [salud-digital, digital-health, telemedicina, wearables, ehr, fhir, hl7, ia-salud, regulacion-salud]
rol: []
actividades: []
organizaciones: [fda, health-canada, cofepris, hl7, oms]
responsabilidades: []
tareas: []
profundidad: 2
estado: profundo
---

# Salud digital (Digital Health)

La **salud digital** es una disciplina que usa tecnologías de información y
comunicación (TIC) para mejorar la eficiencia de la atención y personalizarla.
Abarca programas de cuidado digital, dispositivos conectados y el cruce con
salud pública y sociedad; se solapa con informática médica y *health informatics*.

## Componentes
- **Telemedicina / telehealth:** consulta remota, telemonitoreo, teleradiología
  (ver `dominio/telemedicina`).
- **Wearables y apps de salud:** seguimiento de signos vitales, fitness,
  gestión de crónicos.
- **Historia clínica electrónica (EHR):** núcleo de la digitalización.
- **Interoperabilidad:** estándares **HL7** y **FHIR** (Fast Healthcare
  Interoperability Resources) para el intercambio de registros electrónicos
  entre sistemas dispares.
- **IA en salud:** diagnóstico asistido, triaje, NLP clínico (ver `dominio/ia-generativa`).

## Marco regulatorio y ético
- EE.UU.: FDA *Digital Health* regula dispositivos/apps de salud; HIPAA para
  privacidad; Medicare/Medicaid cubren telehealth.
- México: **COFEPRIS** regula servicios y dispositivos; Ley General de Salud.
- Canadá: Health Canada; licencias médicas a nivel provincial.
- **Bioética:** consentimiento informado remoto y equidad digital son dilemas
  activos (ver `dominio/bioetica`).

## Riesgos
- Brecha digital y acceso desigual.
- Privacidad y ciberseguridad de datos de salud (ver
  `dominio/ciberseguridad-de-la-informacion`).
- Calidad de la relación médico-paciente a distancia.

## Relación con otras capas
- Operada por `rol/head-of-medical-affairs`, `rol/head-of-clinical-affairs` y
  `dominio/telecomunicaciones` (conectividad); cruza con `dominio/sanidad` y
  `dominio/medicina-regenerativa`.
