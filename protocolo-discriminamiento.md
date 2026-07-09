# Protocolo de Discernimiento / Enrutamiento (capa de inferencia)

Capa del pipeline que decide **a qué entidad/nodo va cada input**, SIN que el
usuario tenga que especificarlo. Es el "filtro inteligente" entre la fuente
cruda (`raw/`) y la escritura en el wiki.

## Cuándo se ejecuta
Inmediatamente después de recibir la fuente en `raw/` y **ANTES** de escribir
cualquier página del wiki.

## Pasos
1. **Analizar el input (raw):** leer la fuente y extraer entidades, dominios,
   países, empresas, roles y conceptos mencionados — keywords, nombres propios,
   contexto, tono.
2. **Buscar en la taxonomía:** consultar `esquema.md`, `index.md` y los nodos
   existentes para mapear lo extraído a entidades conocidas. Ej.:
   - "Banco de México" + "inflación" → `dominio/finanzas/` (cross-ref `sustrato/mexico/`)
   - "Ley del ISSSTE" → `sustrato/mexico/` + `dominio/leyes/`
   - "Sprint del equipo de diseño" → `dominio/diseno/` y/o `rol/ingeniero-uiux/`
3. **Inferir el nodo destino:** elegir la entidad (y capa) más probable. Si toca
   varias, definir la predominante y las secundarias (para cross-refs).
4. **Evaluar certeza:**
   - **Certeza ALTA** → proceder al ingest en ese nodo. Hermes menciona al
     usuario el destino inferido (transparencia), sin pedir confirmación.
   - **Certeza BAJA / ambiguo / multi-entidad sin predominante** →
     **PEDIR CONFIRMACIÓN** al usuario (aclarar las candidatas) **ANTES** de
     escribir. No escribir a ciegas.

## Filtro de relevancia (antes de escribir)
Además de inferir el nodo, evaluar: **¿esta pieza cambia una decisión, un supuesto
o una acción posible del usuario?**
- **Sí** → califica para ingesta.
- **No** (noticia real pero sin efecto sobre decisiones: nota política, crónica
  criminal, coyuntura sin marco normativo) → **NO ingerir**, aunque la fuente sea
  legítima.

Por capa: *Sustrato* = marcos normativos/mercados que condicionan operar en un país;
*Dominio* = conocimiento reutilizable de una disciplina; *Rol* = capacidades y
responsabilidades operativas. Coyuntura política/criminal sin ángulo
legal-corporativo-técnico no aplica a ninguna capa.

## Regla de oro
> El usuario NO debe especificar la entidad. Hermes la infiere. Solo pregunta
> cuando no hay nivel de certeza suficiente (usar la herramienta `clarify`).

## Si el usuario SÍ especifica
Hermes valida la entidad dicha contra la taxonomía (`esquema.md`). Si existe,
la usa; si no, propone crearla (con su superstructura) o pide confirmación.

## Nota de optimización
Si la fuente es web/URL (p.ej. scrape de El Financiero), el ingest **solo cita la URL**
en el frontmatter `fuente` y NO crea archivo en `raw/` (ver GUIA-HERMES.md,
sección de optimización). `raw/` queda para documentos que el usuario aporta localmente.

## Ejemplos
- Input: "Nota sobre la tasa de interés del Banco de México 2026"
  → inferencia: `dominio/finanzas/` (+ cross-ref `sustrato/mexico/`). Certeza alta → procede.
- Input: "Documento de la reunión del equipo de diseño"
  → candidatas: `dominio/diseno/`, `rol/ingeniero-uiux/`, o una empresa en
    `organización/`. Certeza baja → pregunta al usuario a cuál va.
