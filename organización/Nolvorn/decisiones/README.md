---
titulo: Nolvorn — Decisiones
capa: organización
tema: cronología de decisiones de Nolvorn
fuente: chat Telegram Nolvorn (Hermes)
fecha: 2026-07-19
confianza: alta
tags: [nolvorn, decisiones, cronología]
organizaciones: [nolvorn]
responsabilidades: [hermes-nolvorn]
profundidad: 2
estado: profundo
---

# Decisiones (Nolvorn)

Cronología de decisiones tomadas en Nolvorn. Cada entrada nueva es una página
con fecha y contexto. Orden cronológico descendente.

## 2026-07-19 — Arquitectura de conocimiento y operación con Hermes
- Se define al chat Telegram Nolvorn como capa de comunicación síncrona;
  Hermes captura pasivamente insights, action items, to-dos y updates.
- Plane.so self-hosted (`plane.mvaslabs.cloud`, workspace `nolvorn`, proyecto
  `General`/NOLVO) como sistema de tickets; Hermes redacta tickets y recordatorios.
- Cronjob diario 12 AM CDMX entrega resumen de tickets abiertos al grupo, agrupado
  por miembro.
- Shared Drive "nolvorn" como knowledge base (sistema PARA); se establece bucle
  bidireccional Drive↔MVAS con regla de NO escritura sin autorización.
- Se crea entidad Nolvorn en MVAS (`organización/Nolvorn/`) con subcarpetas
  responsabilidades / protocolos / decisiones / conocimiento / kb-drive.
