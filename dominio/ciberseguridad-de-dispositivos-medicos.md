---
titulo: Ciberseguridad de dispositivos médicos (medical device security)
capa: dominio
tema: ciberseguridad-de-dispositivos-medicos
fuente: https://en.wikipedia.org/wiki/Medical_device
fuente2: https://www.fda.gov/medical-devices/cybersecurity
fecha: 2026-07-19
confianza: alta
tags: [dispositivos-medicos, ciberseguridad, FDA, HIPAA, salud-digital, IoMT, IEC-62443]
rol: []
actividades: []
organizaciones: [FDA, COFEPRIS, Health Canada, IEC, NIST]
responsabilidades: []
tareas: []
profundidad: 2
estado: profundo
---

# Ciberseguridad de dispositivos médicos

Un **dispositivo médico** es cualquier instrumento, aparato o software
destinado a un fin médico (diagnóstico, tratamiento, monitorización). Por su
potencial de daño, los gobiernos exigen demostrar **seguridad y eficacia**
antes de autorizar su comercialización; a mayor riesgo del dispositivo, mayor
exigencia de pruebas. La **ciberseguridad** de estos dispositivos es la
disciplina que protege su funcionamiento y los datos de paciente contra
accesos no autorizados, manipulación y ransomwares.

## Superficie de riesgo
- **Dispositivos conectados (IoMT):** bombas de infusión, marcapasos/desfibriladores
  implantables, monitores, imagenología (CT/MR), sistemas de historia clínica.
- **Red hospitalaria:** el dispositivo es un nodo más; una vulnerabilidad puede
  ser puerta a todo el hospital (ransomware tipo WannaCry 2017 afectó NHS).
- **Datos de salud:** sujetos a **HIPAA** (EE.UU.), GDPR/LEPDP (UE/MX),
  Health Canada.

## Marco regulatorio
- **FDA (EE.UU.):** guías de *premarket* (incluye SBOM, diseño seguro) y
  *postmarket* (gestión de vulnerabilidades, avisos de seguridad). Reautoriza
  con requisitos de ciberseguridad desde 2023.
- **IEC 62443 / 80001:** estándares de seguridad de sistemas de tecnología
  médica en red.
- **COFEPRIS / Health Canada:** autoridades de registro con criterios de
  ciberseguridad en evolución.
- Cruza con **salud digital**, **dispositivos médicos** (regulatorio) y
  **ciberseguridad de la información** (HIPAA/DLP).
