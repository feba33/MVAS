---
titulo: Transporte / movilidad
capa: dominio
tema: transporte
fuente: https://en.wikipedia.org/wiki/Transport
fuente2: https://www.itf-oecd.org/
fecha: 2026-07-11
confianza: alta
tags: [transporte, movilidad, logistica, aviacion, regulacion, infraestructura]
english_keywords: [transportation, mobility, logistics, aviation, freight, infrastructure, regulation]
---

# Transporte / movilidad

## 📝 Conocimiento

### Definición
El **transporte** es el movimiento de personas y mercancías entre lugares. Como dominio
abarca los **modos**, la **logística**, la **movilidad urbana** y la **regulación** de la
infraestructura. Es el sistema circulatorio de la economía y conecta a `dominio/logistica`.

### Modos
- **Carretera:** automóvil, camión, autobús; dominante en última milla.
- **Ferroviario:** carga pesada y pasajeros de alta capacidad.
- **Aéreo:** aviación comercial y carga; más rápido, más costoso.
- **Marítimo/fluvial:** contenedores, graneles; backbone del comercio global.
- **Tubería:** fluidos y energía (véase `dominio/energia`).

### Logística y cadena
Programación de rutas, intermodalidad, centros de distribución y **última milla**
(conecta con `dominio/logistica`). KPIs: costo por ton-km, OTIF, utilización.

### Movilidad urbana
Transporte público, micromovilidad, MaaS (Mobility-as-a-Service), y congestión. Las
ciudades buscan descarbonizar el transporte.

### Regulación
Agencias (DOT/FAA en EE.UU., SCT/AFAC en México, TC en Canadá), seguridad, estándares de
emisión y derechos de pasajero. Modos a menudo son servicios públicos regulados.

### Tendencias 2025-2026
- **Electrificación** (VE) y combustibles alternativos.
- **Autonomía** (AVs) en carga y last-mile.
- **Digitalización:** gemelos digitales de tráfico, pricing dinámico.
- **Sostenibilidad:** cero emisiones, movilidad compartida.

## 🔗 Referencia
- `dominio/logistica/gestion-cadena-suministro.md` — el transporte es el eslabón "Deliver".
- `dominio/logistica/ultima-milla.md` — entrega final al consumidor.
- `dominio/energia/energia.md` — combustibles y electrificación del transporte.
- `rol/coo.md` — el COO orquesta la distribución física.
