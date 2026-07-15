---
titulo: Forense digital
capa: dominio
tema: forense-digital
fuente: https://en.wikipedia.org/wiki/Computer_forensics
fuente2: https://www.nist.gov/itl/ssd/software-quality-group/computer-forensics-tool-testing-program-cftt
fecha: 2026-07-15
confianza: alta
tags: [forense-digital, digital-forensics, evidencia-digital, incident-response, cadena-de-custodia, ciberseguridad, e-discovery]
profundidad: 2
estado: profundo
rol: [head-of-incident-response, security-analyst, legal-counsel, chief-compliance-officer, ciso]
actividades: [respuesta-a-incidentes, investigacion, litigio, cumplimiento, auditoria]
organizaciones: [nist, fbi, interpol, iso, empresa]
responsabilidades: [preservacion-evidencia, cadena-de-custodia, debida-diligencia, reportes-legales]
tareas: [adquisicion-evidencia, analisis-forense, redaccion-informe, testigo-pericial]
---

# Forense digital

La **forense digital** (digital forensics / computer forensics) es la rama de la ciencia forense que se ocupa de la identificación, preservación, recuperación, análisis y presentación de hechos y opiniones sobre información contenida en medios digitales, de manera *forensically sound* (que preserve la integridad). Aunque se asocia sobre todo a la investigación de ciberdelitos, también se usa en litigios civiles (e-discovery), arbitrajes laborales, investigaciones internas de fraude y compliance. Comparte técnicas con la recuperación de datos, pero añade controles para generar una **cadena de custodia** legalmente admisible. La evidencia forense digital es aceptada como fiable en sistemas judiciales de EE.UU. y Europa.

## Fases del proceso (modelo estándar)

1. **Identificación:** determinar medios y sistemas relevantes (dispositivos, logs, nubes, memoria).
2. **Preservación / adquisición:** crear una copia bit a bit (imagen forense) con *hashing* (MD5/SHA-256) para garantizar inmutabilidad; trabajar sobre la copia, no el original.
3. **Análisis:** recuperar archivos borrados, reconstruir líneas de tiempo, correlacionar eventos, extraer metadatos, detectar anti-forensia (wiping, steganography, cifrado).
4. **Documentación y presentación:** informe pericial, cadena de custodia, y — en su caso — testimonio experto.

## Marcos y estándares

- **NIST** (Computer Forensics Tool Testing, CFTT; SP 800-101 para móviles) y **ISO/IEC 27037** (identificación/preservación de evidencia digital).
- **SWGDE / IOCE** guías de calidad; **RFC 3227** (guía de recolección de evidencia).
- **LOCARD / guías de INTERPOL** y manuales del **FBI** (Digital Evidence). En México, la evidencia digital se rige por el **Código Nacional de Procedimientos Penales (CNPP)** y pericias del **UNAC**/laboratorios de la Fiscalía; en Brasil, por la **Lei 13.964/2019** y la ABIN/PF.

## Subdisciplinas

- **Computer/mobile forensics:** discos, memoria RAM, smartphones (iOS/Android extraction).
- **Network forensics:** captura de tráfico, análisis de intrusiones y *pivot* de atacantes.
- **Memory forensics:** análisis de RAM (volatility) para malware en memoria.
- **Cloud/multimedia forensics:** entornos SaaS, imágenes/video (autenticidad).
- **e-discovery / forense legal:** revisión de correos y documentos en litigio (FRCP Rule 26/37, reglas locales).

## Relevancia para el negocio (MVAS)

- **Respuesta a incidentes:** forense digital es la fase post-breach del IR (ver `dominio/ciberseguridad` y `rol/head-of-incident-response`); determina alcance, vector y responsabilidad.
- **Fraude y compliance:** investigaciones internas de desviación de fondos, cohecho y conflictos de interés; soporte a **SOX**, anticorrupción (FCPA/UKBA) y **PLD/AML**.
- **Litigio y M&A:** e-discovery en disputas comerciales, diligence técnica y leaks de IP (ver `dominio/propiedad-intelectual`).
- **Protección de datos:** en brechas de privacidad (RGPD/LFPDPPP/LGPD), la forense acredita qué datos fueron expuestos y cuándo (ver `dominio/proteccion-de-datos`).
- **Cadena de custodia:** métodos débiles invalidan la evidencia; formación de `legal-counsel` y `chief-compliance-officer` es crítica.

## Riesgos y tendencias

- **Cifrado y anti-forensia** dificultan el análisis; la *cloud* y los dispositivos móviles fragmentan la evidencia.
- **IA generativa** habilita deepfakes y falsificación de evidencia multimedia → forense de autenticidad en auge.
- **Privacidad vs investigación:** tensiones con normativas de datos personales y derechos de los empleados.
- **Mercado:** proveedores (FTK, EnCase, Axiom, Autopsy open-source) y servicios gestionados (MDR/forensic retainer).

## Conexiones

- `dominio/ciberseguridad` — SOC, zero trust, detección (previa a la forense).
- `dominio/ciberdefensa` — amenazas patrocinadas por estados.
- `dominio/gestion-de-crisis` — comms y coordinación durante la crisis.
- `dominio/propiedad-intelectual` — protección de secretos comerciales en filtraciones.
- `rol/head-of-incident-response` — lidera el CSIRT y la fase forense.
- `dominio/proteccion-de-datos` — notificación de brechas y acreditación de impacto.

## Referencias

- [Computer forensics — Wikipedia](https://en.wikipedia.org/wiki/Computer_forensics)
- [NIST Computer Forensics Tool Testing (CFTT)](https://www.nist.gov/itl/ssd/software-quality-group/computer-forensics-tool-testing-program-cftt)
- [ISO/IEC 27037 — digital evidence](https://www.iso.org/standard/44381.html)
- [SWGDE digital evidence guidelines](https://www.swgde.org)
- [FBI — Digital Evidence](https://www.fbi.gov/services/laboratory)
