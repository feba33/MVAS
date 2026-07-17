---
titulo: Ciberseguridad educativa
capa: dominio
tema: protección de datos estudiantiles, seguridad de LMS e identidad educativa
fuente: https://en.wikipedia.org/wiki/Family_Educational_Rights_and_Privacy_Act
fuente2: https://en.wikipedia.org/wiki/Edtech
fecha: 2026-07-17
confianza: alta
tags: [ciberseguridad-educativa, edtech, ferpa, coppa, datos-estudiantiles, lms, proteccion-de-datos]
rol: [head-of-information-security, ciso, head-of-business-technology]
organizaciones: [usde, ferpa, coppa]
profundidad: 2
estado: profundo
---

# Ciberseguridad educativa

La **ciberseguridad educativa** protege los datos y sistemas de instituciones de
enseñanza (K-12, superior, y plataformas edtech). El activo crítico es la
**información de menores y estudiantes**, sujeta a regulación de privacidad
estricta.

## Marco regulatorio (EE.UU. como referencia)
- **FERPA (Family Educational Rights and Privacy Act, 1974):** ley federal que rige
  el acceso a expedientes educativos y la privacidad de datos de estudiantes en
  instituciones que reciben fondos federales.
- **COPPA (Children's Online Privacy Protection Act):** protege datos de menores de
  13 años en servicios en línea.
- En la UE, el **RGPD** (incluido el "derecho a la olvidanza" y la protección de
  menores) y directivas nacionales aplican a edtech.

## Superficie de ataque
- **LMS (Learning Management Systems):** Moodle, Canvas, Blackboard — objetivos de
  ransomware y filtración.
- **Identidad educativa:** SSO/Rosto, cuentas de estudiante, acceso de padres.
- **Edtech / proveedores:** terceros con acceso a datos; requieren DPA y evaluación
  de riesgo (ver `dominio/ciberseguridad-cadena-suministro`).

## Relación con otras capas
- Cruza con `dominio/proteccion-de-datos`, `dominio/educacion`, `dominio/edtech`.
- Para gobierno de IA en educación, ver `dominio/gobierno-de-ia`.

## Referencias
- FERPA — Wikipedia: https://en.wikipedia.org/wiki/Family_Educational_Rights_and_Privacy_Act
- Edtech — Wikipedia: https://en.wikipedia.org/wiki/Edtech
