---
titulo: Logística de medios
capa: dominio
tema: logistica-de-medios
fuente: https://www.iab.com/guidelines/campaign-trafficking-and-delivery-quality-guidelines/
fuente2: https://en.wikipedia.org/wiki/Ad_trafficking
fecha: 2026-07-17
confianza: media
tags: [medios, publicidad, ad-operations, trafficking, distribucion-contenido, adtech]
organizaciones: [IAB, Google Ad Manager, The Trade Desk, Mediaocean]
rol: [head-of-operations, head-of-revenue-operations, marketing-manager]
profundidad: 2
estado: profundo
---

# Logística de medios

La **logística de medios** (media logistics / ad operations) es la cadena de suministro de
la publicidad y el contenido: cómo las campañas y los activos se trafican, verifican,
distribuyen y miden a través de canales y plataformas, del anunciante a la pantalla del
usuario.

## Componentes
- **Ad trafficking:** configuración técnica de campañas (tags, píxeles, audiencias, pacing,
  frequency capping) en servidores de publicidad (Google Ad Manager, Xandr, FreeWheel)
  según las *Campaign Trafficking and Delivery Quality Guidelines* de la IAB.
- **Verificación y QA:** pre-visualización, comprobación de creative, brand safety y
  visibilidad.
- **Distribución de contenido:** ingestión, transcodificación y entrega CDN para video/
  streaming (ver `dominio/medios-comunicacion`, `dominio/entretenimiento`).
- **Medición y reconciliación:** impresiones/served, billing, tercerización de reportes.

## Actores y sistemas
Ad servers, SSP/DSP (programática), OMS (order management systems, p. ej. Mediaocean),
verificadores (DoubleVerify, IAS) y data providers. La automatización (programática/header
bidding) desplazó el trafficking manual hacia operaciones de plataforma.

## Retos
Fragmentación de sistemas, privacidad (cookies de terceros/Post-3P), fraude (ad fraud),
sincronización cross-channel y reconciliación financiera.

## Diferenciación
Distinto de `dominio/publicidad` (estrategia/creatividad/media mix) y
`dominio/medios-comunicacion` (industria editorial). Este nodo es la **operación técnica
de entrega de campañas y contenido**.

## Relación
Cruza con `dominio/marketing-digital`, `dominio/comercio-electronico` y
`rol/head-of-revenue-operations`.
