---
titulo: Nolvorn — Protocolos
capa: organización
tema: procesos y formas de operar en Nolvorn
fuente: chat Telegram Nolvorn (Hermes) + README del Drive
fecha: 2026-07-19
confianza: alta
tags: [nolvorn, protocolos, procesos, para, autorización]
organizaciones: [nolvorn]
responsabilidades: [hermes-nolvorn]
profundidad: 2
estado: profundo
---

# Protocolos (Nolvorn)

Procesos y formas de operar. Evolucionan con la operación; cada página documenta
un protocolo y su historia de cambios.

## Protocolo de organización del Drive (sistema PARA)
Del README del Shared Drive "nolvorn". Regla de decisión aplicada en orden cada
vez que un documento necesita hogar:

1. ¿Atado a un engagement de cliente con fecha de fin? → **Projects** (`/{Client}`)
2. ¿Responsabilidad continua sin fecha de fin? → **Areas**
3. ¿Material de referencia que se consulta pero rara vez se edita? → **Resources**
4. ¿Terminado/cerrado? → **Archive**

Profundidad máxima: 2 niveles (excepto subcarpetas por cliente en Projects/Archive).
Styling: plain, minimal, sin decoración.

## Protocolo de autorización para escritura en Drive
Hermes NUNCA escribe/comparte/borra en el Drive sin autorización explícita previa.
Flujo: detecta mejora → la propone en el chat → escala plan y necesidades →
espera aprobación → ejecuta. (Regla del skill `google-workspace`: confirmar antes
de cualquier mutación.)

## Protocolo de ingest Drive → MVAS
1. Leer `README` y `nolvorn_master_context_v1` como fuentes de verdad de identidad.
2. Reflejar estructura PARA en `kb-drive/` (índice de carpetas/doc IDs).
3. Sintetizar contenido relevante en `conocimiento/`, `responsabilidades/`,
   `decisiones/` según corresponda (frontmatter transversal para filtrado QMD).
4. Actualizar `index.md` raíz + `log.md` raíz de MVAS y commitear.

## Protocolo de comunicación síncrona (este chat)
El chat Nolvorn es la capa de comunicación síncrona y directa. Hermes captura
insights, action items, to-dos y updates de forma pasiva; produce resúmenes y
tickets bajo demanda.
