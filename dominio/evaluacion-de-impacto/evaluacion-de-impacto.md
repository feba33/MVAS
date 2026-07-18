---
titulo: Evaluación de impacto (Impact Evaluation)
capa: dominio
tema: evaluacion-de-impacto
fuente: https://en.wikipedia.org/wiki/Impact_evaluation
fecha: 2026-07-18
confianza: alta
tags: [evaluacion-de-impacto, impact-evaluation, contrafactual, metodos, politicas-publicas, medicion, analitica]
rol: []
actividades: []
organizaciones: [banco-mundial, j-pal, oecd, 3ie]
responsabilidades: []
tareas: []
profundidad: 2
estado: profundo
---

# Evaluación de impacto (Impact Evaluation)

La **evaluación de impacto** determina en qué medida una intervención es
*causalmente responsable* de los resultados observados (intencionados o no).
A diferencia del monitoreo de resultados (¿se alcanzaron las metas?), busca
responder: ¿cómo habrían cambiado los resultados si la intervención no se
hubiera realizado? Requiere **análisis contrafactual** — comparar lo que
pasó con lo que habría pasado en su ausencia.

## Métodos
- **Experimental (ensayos controlados aleatorizados, RCT):** asignación
  aleatoria a tratamiento/control; estándar de oro para causalidad.
- **Cuasi-experimental:** *difference-in-differences* (dif-en-dif), *matching*,
  *instrumental variables*, *regression discontinuity*.
- **Evaluación de proceso y teoría de cambio:** complementa la causalidad con
  mecanismos.

## Aplicaciones
- Políticas públicas (educación, salud, protección social) — ver
  `dominio/politica-publica`.
- Programas sociales, intervenciones de desarrollo, inversión de impacto.
- Decisiones empresariales (A/B testing es su contraparte comercial) — ver
  `dominio/analitica-negocio` y `dominio/analitica-predictiva`.

## Instituciones de referencia
Banco Mundial (DIME), J-PAL, 3ie, OECD.

## Relación con otras capas
- Cruza con `dominio/analitica-negocio`, `dominio/politica-publica` y
  `dominio/inteligencia-de-mercado`; operada por analistas de
  `rol/data-scientist` y `rol/economist`.
