# Registro de iot (log.md)

Registro cronológico **append-only** de la entidad `iot`.
Prefijo: `## [YYYY-MM-DD] <tipo> | <título>` (parseable: `grep "^## \[" log.md`).

## [2026-07-12] setup | Nodo wiki de iot
- Creada la superstructura recursiva de la entidad `iot` dentro de `dominio/`:
  `raw/`, `index.md`, `log.md` y `README.md`.
- Principio: toda la info de iot vive solo en esta carpeta.

## [2026-07-12] ingest | Internet de las Cosas (IoT) / IIoT
- Fuentes: Wikipedia (en) — Internet of things; Industrial internet of things — reference-only.
- Página: `iot.md`. Definición, arquitectura por capas (edge/conectividad/cloud/app), IIoT (Industry 4.0, gemelos digitales). Retos: seguridad (superficie de ataque), interoperabilidad, privacidad, latencia/edge. Cross-ref dominio/computacion, telecomunicaciones, automatizacion, manufactura, energia, rol/ciso.