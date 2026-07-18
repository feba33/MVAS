---
titulo: Redes 5G y móviles
capa: dominio
tema: redes-5g-moviles
fuente: https://en.wikipedia.org/wiki/5G
fuente2: https://en.wikipedia.org/wiki/Network_slicing
fecha: 2026-07-18
confianza: alta
tags: [5g, telecomunicaciones, redes-moviles, espectro, edge-computing, network-slicing]
organizaciones: [3GPP, ITU, FCC, operadores-moviles]
---

# Redes 5G y móviles

Quinta generación de redes celulares (estándar **3GPP Release 15+**, IMT-2020 de la
ITU), con latencia ultrabaja, alta densidad de dispositivos y *network slicing*.
Complementa `telecomunicaciones.md`, `telecomunicaciones-corporativas.md` y
`sustrato/estados-unidos/telecomunicaciones-5g.md`.

## Bandas (espectro)
- **FR1 (sub-6 GHz)**: 600 MHz–6 GHz; cobertura y capacidad (incluye C-band 3.5 GHz).
- **FR2 (mmWave, 24–39 GHz)**: capacidad extrema, alcance corto; requiere densificación.

## Arquitectura y tecnologías
- **NR (New Radio)**: aire interfaz 5G; OFDM flexible, massive MIMO, beamforming.
- **Network slicing**: redes lógicas virtuales sobre una infraestructura física, cada
  una con SLA (ej. slice de misión crítica, IoT masivo, eMBB).
- **Edge computing (MEC)**: procesamiento cerca del usuario para bajar latencia.
- **NSA vs SA**: Non-Standalone (apoya en 4G core) vs Standalone (core 5G nativo).

## Casos de uso
- **eMBB** (banda ancha móvil mejorado), **URLLC** (ultra-low latency, industrias),
  **mMTC** (IoT masivo, sensores).
- Habilita industria 4.0, vehículos conectados (V2X), *fixed wireless access* (BEAD),
  y prepara **5G-Advanced / 6G**.

## Despliegue y regulación
- Subastas de espectro (FCC en EE.UU., IFT en México, CRTC/Industry Canada).
- **Open RAN** (desagregación) y seguridad de la cadena de suministro (restricciones
  a proveedores) son temas de política industrial y `ciberseguridad`.

## Referencias
- `telecomunicaciones.md`, `telecomunicaciones-corporativas.md`, `ciberseguridad.md`
- `sustrato/estados-unidos/telecomunicaciones-5g.md`
