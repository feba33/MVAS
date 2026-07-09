# GUÍA PARA HERMES — Repositorio MVAS

MVAS es un **super wiki en capas de conocimiento**, de lo más general a lo más
específico y granular. Mi trabajo con este repo es **cuidarlo, mantenerlo,
optimizarlo y dar retrieval**.

## Modelo de capas (general → específico)
1. **sustrato/** — Fundamento por país: legislación, cultura, reglas,
   normatividad, noticias y mercados. Subcarpetas por país
   (p.ej. `sustrato/mexico/`, `sustrato/estados-unidos/`).
2. **dominio/** — Referencia y conocimiento puntual por dominio: finanzas,
   computación, marketing, leyes, contabilidad, diseño, etc.
3. **organización/** — Lo específico de empresas: operaciones, decisiones,
   responsabilidades, artefactos creados, bases de conocimiento internas.
4. **rol/** — Responsabilidades y sets de capacidades por rol: ingeniero de
   software, ingeniero UI/UX, road lead, etc.

## Protocolo de inserción de nueva información
Cuando el usuario adjunte información nueva y pida *"actualiza MVAS/MWAS/MUBAS"*
(el nombre varía en pronunciación, pero siempre es este repo):

1. Lee esta guía y `esquema.md` (la taxonomía que el usuario provee).
2. **Clasifica por capa** según la granularidad de la info:
   - ¿Es de un país (leyes, cultura, mercado)? → `sustrato/<pais>/`
   - ¿Es conocimiento de un dominio? → `dominio/<dominio>/`
   - ¿Es de una empresa específica? → `organización/<empresa>/`
   - ¿Es responsabilidad/capacidad de un rol? → `rol/<rol>/`
3. Crea o actualiza el archivo markdown correspondiente dentro de la subcarpeta.
4. Incluye **metadatos** al inicio de cada entrada:
   `fuente`, `fecha`, `tema`, `nivel de confianza`.
5. Si la subcarpeta no existe, créala siguiendo `esquema.md`.
6. **Deduplica** y mantén consistencia con lo ya existente.

## Navegación y retrieval
- Empezar en `sustrato/` (general) y taladrar hacia `rol/` / `organización/`
  (específico).
- Usar `git grep` o búsqueda de archivos para localizar entradas.
- Para responder consultas: leer de `organización/` + `rol/` y respaldar con
  `dominio/` + `sustrato/`.

## Mantenimiento periódico
- Revisar `sustrato/` para limpiar duplicados y obsoletos.
- Mantener `esquema.md` como fuente de verdad de la taxonomía.
- Verificar que `rol/` y `organización/` siguen alineados con la realidad.

## Referencia técnica
- Repo: https://github.com/feba33/MVAS (privado)
- Clone local: `/opt/data/MVAS`
- Autenticación `gh` como `feba33`; al usar gh exportar
  `PATH=/opt/data/bin:$PATH`, `HOME=/opt/data`, `GH_CONFIG_DIR=/opt/data/.config/gh`.
