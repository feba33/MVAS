# MVAS

**Super wiki en capas de conocimiento**, de lo más general a lo más específico y granular.

El punto de este repositorio es ser una base de conocimiento por capas donde cada
carpeta contiene **subcarpetas** que se van llenando progresivamente a partir de
un esquema de taxonomía. Hermes (el asistente) es responsable de cuidarlo,
mantenerlo, optimizarlo y dar retrieval.

## Las 4 capas (de general → específico)

| Capa | Carpeta | Qué contiene |
|------|---------|--------------|
| **Sustrato** | `sustrato/` | Fundamento general por **país**: legislación, cultura, reglas, normatividad, noticias y mercados. Ej.: `sustrato/mexico/`, `sustrato/estados-unidos/`. |
| **Dominio** | `dominio/` | Material de referencia y conocimiento puntual por **dominio**: finanzas, computación, marketing, leyes, contabilidad, diseño, etc. |
| **Organización** | `organización/` | Lo específico de **empresas**: operaciones, decisiones, responsabilidades, artefactos creados, bases de conocimiento internas. |
| **Rol** | `rol/` | **Responsabilidades** y sets de capacidades por rol: ingeniero de software, ingeniero UI/UX, road lead, etc. |

Flujo de granularidad: `sustrato → dominio → organización → rol`
(lo más general del mundo → lo más específico de una persona/equipo).

## Para Hermes
Ver `GUIA-HERMES.md` — protocolo de inserción de nueva información,
navegación entre capas y retrieval. La taxonomía completa de subcarpetas
vive en `esquema.md` (lo provee el usuario).
