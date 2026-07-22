---
titulo: "Realidad aumentada y virtual (AR/VR/XR)"
capa: "dominio"
tema: "realidad-aumentada-virtual"
fuente: "https://en.wikipedia.org/wiki/Augmented_reality"
fecha: "2026-07-22"
confianza: "alta"
tags: ["AR", "VR", "XR", "spatial-computing", "headsets", "metaverso", "industrial"]
profundidad: 2
estado: "profundo"
---

# Realidad aumentada y virtual (AR/VR/XR)

## Definiciones y espectro

| Término | Definición | Ejemplos |
|---------|------------|----------|
| **VR (Realidad Virtual)** | Entorno 100% sintético, inmersivo, oculta mundo físico | Meta Quest, HTC Vive, Valve Index, PSVR2 |
| **AR (Realidad Aumentada)** | Superposición de contenido digital sobre visión del mundo real | Pokémon GO, Google Lens, HoloLens, Magic Leap |
| **MR (Realidad Mixta)** | AR con anclaje espacial y oclusión realista; interacción bidireccional | HoloLens 2, Varjo XR-4, Meta Quest 3 (passthrough) |
| **XR (Extended Reality)** | Paraguas: VR + AR + MR + tecnologías afines | — |
| **Spatial Computing** | Computación donde la interfaz es el espacio 3D; entrada: mirada, manos, voz | visionOS (Apple), Windows Mixed Reality, Android XR |

**Continuum de Milgram (1994)**: Realidad física ←→ AR ←→ MR ←→ VR (Virtualidad total).

## Hardware — Panorama 2025-2026

### Headsets de consumo (Consumer)
| Dispositivo | Tipo | Resolución/ojo | FOV | Tracking | SoC | Precio ~ | Posicionamiento |
|-------------|------|----------------|-----|----------|-----|----------|-----------------|
| **Meta Quest 3** | MR (passthrough color) | 2064×2208 | 110° | Inside-out 6DoF | Snapdragon XR2 Gen 2 | $499 | Masivo, ecosistema apps/juegos |
| **Meta Quest 3S** | MR | 1832×1920 | 96° | Inside-out | XR2 Gen 2 | $299 | Entrada de gama |
| **Apple Vision Pro** | Spatial Computer (MR) | 3660×3200 (micro-OLED) | ~100° | Eye/hand tracking preciso | M2 + R1 | $3,499 | Premium, productividad, ecosistema Apple |
| **Meta Quest Pro** | MR | 1800×1920 | 106° | Eye/face tracking + inside-out | XR2+ | $999 | Prosumers, enterprise |
| **HTC Vive XR Elite** | MR | 1920×1920 | 110° | Inside-out + eye tracking opc. | XR2 | $1,099 | Enterprise, PCVR |
| **PICO 4 Ultra** | MR | 2160×2160 | 105° | Inside-out + eye tracking | XR2 Gen 2 | $599 | Competidor Quest (ByteDance) |
| **PlayStation VR2** | VR | 2000×2040 (OLED) | 110° | Inside-out + eye tracking | PS5 | $549 | Consola, gaming AAA |

### Enterprise / Industrial
| Dispositivo | Tipo | Clave | Uso típico |
|-------------|------|-------|------------|
| **Microsoft HoloLens 2** | MR (see-through óptico) | Waveguide, eye/hand tracking, IP50 | Manufactura, salud, defensa (IVAS) |
| **Magic Leap 2** | MR | Óptica waveguide, 70° FOV, 500 nits | Salud, manufactura, entrenamiento |
| **Varjo XR-4 / XR-4 Focal Edition** | XR (video pass-through) | 4K×4K/ojo, LiDAR, eye tracking, foveated rendering | Simulación, diseño, ingeniería, defensa |
| **RealWear Navigator Z1 / 520** | AR (monocular, hands-free) | Voz, rugged IP66, Android | Campo, mantenimiento, inspección |
| **Vuzix M4000 / Ultralite** | AR (waveguide) | Ligero, see-through | Logística, salud, retail |

### Próximas generaciones (2025-2027)
- **Meta Orion (prototipo AR glasses)**: Waveguide SiC, 70° FOV, EMG wristband, <100g.
- **Apple Vision Pro 2 / "Vision Air"**: Más ligero, precio menor, chips M5/R2.
- **Samsung + Google (Project Moohan)**: Android XR, Snapdragon XR2+ Gen 2, 2025.
- **Snap Spectacles (5th gen)**: AR glasses para desarrolladores, waveguide, 46° FOV.
- **Xiaomi / OPPO / Vivo**: AR glasses ligeros (tethered a smartphone).

## Software y plataformas

| Plataforma | Ecosistema | SDK / Herramientas | App Store |
|------------|------------|---------------------|-----------|
| **Meta Horizon OS** | Quest, Horizon Worlds, Horizon Workrooms | Unity, Unreal, React Native (Meta XR SDK), WebXR | Meta Horizon Store |
| **visionOS (Apple)** | Vision Pro, iPhone/iPad/Mac (continuity) | SwiftUI, RealityKit, ARKit, Unity (PolySpatial) | App Store (visionOS) |
| **Android XR (Google/Samsung)** | Próximo (2025) | ARCore, Jetpack XR, Unity, Unreal, WebXR | Play Store |
| **Microsoft Mesh / Teams Immersive** | HoloLens, PC, Meta Quest | Unity, MRTK3, Azure Remote Rendering | Teams, Dynamics 365 Guides |
| **Snap Lens Studio** | Snapchat, Spectacles | TypeScript, WebGL, ML | Lens Explorer |
| **Niantic Lightship / 8th Wall** | WebAR, móvil | Unity, WebXR, VPS (Visual Positioning System) | Web, apps nativas |
| **OpenXR (Khronos)** | Estándar multiplataforma | C/C++, Unity, Unreal, Godot | Agnóstico |

## Casos de uso industriales (Enterprise XR)

### 1. Entrenamiento y simulación (Training)
- **VR**: Simuladores de vuelo, cirugía, manejo de materiales peligrosos, *soft skills* (hablar en público, DEI), respuesta a emergencias.
- **ROI**: -40% tiempo formación, +75% retención (PwC 2022), reducción riesgo/lesiones.
- **Ejemplos**: Strivr (Walmart, Verizon), Osso VR (cirugía), Talespin (soft skills), Boeing (ensamblaje).

### 2. Mantenimiento, reparación y operaciones (MRO) — AR/MR
- **Flujos de trabajo guiados**: Instrucciones paso a paso superpuestas (HoloLens, RealWear).
- **Asistencia remota** (*See-what-I-see*): Experto remoto anota en visión del técnico.
- **Gemelos digitales**: Superposición de datos IoT (temperatura, vibración) sobre activo físico.
- **Casos**: Mercedes-Benz (HoloLens en planta), DHL (vision picking +25% productividad), Siemens (AR para turbinas), Coca-Cola (mantenimiento).

### 3. Diseño, ingeniería y revisión de diseño (Design Review)
- **Colaboración inmersiva**: Equipos distribuidos revisan modelos 3D a escala 1:1 (NVIDIA Omniverse, Autodesk Workshop XR, Gravity Sketch, Arkio).
- **Prototipado virtual**: Eliminar maquetas físicas (automoción, aeroespacial, arquitectura).
- **Ejemplos**: Ford, BMW, Hyundai (VR design reviews), Zaha Hadid Architects (AR en obra).

### 4. Salud (Healthcare)
- **Cirugía**: Planificación preoperatoria VR (PrecisionOS, Surgical Theater), navegación AR intraoperatoria (HoloLens, Magic Leap).
- **Rehabilitación**: VR gamificada (ej. MindMaze, Penumbra).
- **Salud mental**: Terapia de exposición VR (PTSD, fobias, ansiedad) — FDA approved (AppliedVR RelieVRx).
- **Formación médica**: Anatomía 3D (Complete HeartX, HoloAnatomy), simulación pacientes virtuales.

### 5. Retail, marketing y comercio
- **Virtual try-on**: Gafas, maquillaje, relojes, ropa (ARKit/ARCore, 8th Wall, Snap).
- **Showrooms virtuales**: Coches (Volvo, Porsche), muebles (IKEA Place, Wayfair), inmobiliaria (Matterport + VR).
- **Experiencias de marca**: *Immersive commerce* (Nike, Gucci en Roblox/Fortnite/Horizon).

### 6. Manufactura y logística
- **Pick-by-vision** (DHL, DB Schenker): Gafas AR guían picking → +15-25% velocidad, -30% errores.
- **Ensamblaje asistido**: Proyección de plantillas, torque verification (LightGuide, ProjectionWorks).
- **Control de calidad**: AR superpone especificaciones vs. pieza real (PTC Vuforia, TeamViewer Frontline).

### 7. Defensa y seguridad pública
- **IVAS (Integrated Visual Augmentation System)** — Ejército EE.UU. / Microsoft HoloLens militar: navegación, identificación amigo/enemigo, sensores térmicos.
- **Entrenamiento táctico VR**: STE (Synthetic Training Environment), simuladores de vehículo/arma.
- **Bomberos / primera respuesta**: Navegación en humo (HoloLens + thermal), gemelos digitales de edificios.

## Mercado y métricas 2024-2026

| Métrica | Valor 2024 | Proyección 2028 | Fuente |
|---------|------------|-----------------|--------|
| **Mercado global XR** | $57B | $200B+ (CAGR ~35%) | IDC, Statista, PwC |
| **Headsets vendidos (acum.)** | ~35M (Quest >20M) | >100M | IDC, Canalys |
| **Enterprise XR share** | ~40% ingresos | >50% | ABI Research |
| **Gasto empresarial XR** | $18B | $58B | PwC |
| **Usuarios activos AR móvil** | >1.4B (ARCore/ARKit) | >2.5B | ARtillery Intelligence |

## Retos y barreras

| Barrera | Estado / Soluciones |
|---------|---------------------|
| **Ergonomía / peso** | Quest 3: 515g; Vision Pro: 600-650g; objetivo <150g (gafas AR) |
| **Fatiga visual / *motion sickness*** | Foveated rendering, 90-120Hz, low latency (<20ms MTP), *comfort settings* |
| **Autonomía** | 2-3h (standalone); *hot-swap batteries*, compute pucks, tethered |
| **Campo de visión (FOV)** | 90-110° (VR); 40-70° (AR waveguide); objetivo >100° AR |
| **Brillo / see-through** | Waveguide <1000 nits; micro-OLED + passthrough video (MR) |
| **Entrada natural** | Eye tracking + hand tracking + voz (Vision Pro, Quest 3, HoloLens 2) |
| **Ecosistema apps enterprise** | Creciente (ISVs: PTC, TeamViewer, Scope AR, Librestream, Taqtile) |
| **Seguridad / privacidad** | Datos biométricos (eye/hand/face), mapeo espacial; *on-device processing*, *differential privacy* |
| **Costo TCO enterprise** | Hardware + MDM + desarrollo contenido + formación; *device-as-a-service* (ArborXR, ManageXR, Scalefusion) |

## Estándares e interoperabilidad
- **OpenXR 1.1** (Khronos): API unificada VR/AR/MR — adoptado por Meta, Microsoft, Google, Valve, HTC, Varjo, Qualcomm.
- **glTF / USDZ / USD** — Formatos 3D interoperables (Metaverse Standards Forum, AOUSD).
- **WebXR (W3C)** — XR en navegador (Chrome, Edge, Safari visionOS).
- **IEEE 2888** — *Augmented Reality Learning Experience Model* (entrenamiento).
- **Metaverse Standards Forum** (200+ orgs): Interoperabilidad de identidad, pagos, activos 3D.

## Futuro: Spatial Computing + AI
- **Generative AI en XR**: Creación de mundos/avatares/assets por texto (Unity Muse, Roblox Assistant, Spline, Luma AI, Gaussian Splatting/NeRFs).
- **AI Agents en XR**: Asistentes contextuales que "ven" lo que el usuario ve (Gemini + Project Astra, Apple Intelligence + Vision Pro).
- **Neural interfaces**: EMG wristband (Meta/CTRL-labs), BCI no invasivo (Neurable, NextMind) → control sin manos.
- **5G/6G + Edge Compute**: *Split rendering* (headset ligero + GPU en edge/cloud), baja latencia, multi-usuario masivo.
- **Digital Twins a escala ciudad/país**: NVIDIA Earth-2, Google Immersive View, gemelos digitales industriales (Siemens, Bentley, Esri).

## Fuentes
- [Wikipedia — Augmented reality](https://en.wikipedia.org/wiki/Augmented_reality)
- [Wikipedia — Virtual reality](https://en.wikipedia.org/wiki/Virtual_reality)
- [Wikipedia — Mixed reality](https://en.wikipedia.org/wiki/Mixed_reality)
- [IDC — Worldwide AR/VR Headset Forecast 2024-2028](https://www.idc.com/)
- [PwC — Seeing is Believing (2022/2024)](https://www.pwc.com/seeingisbelieving)
- [Meta — Quest Developer Documentation](https://developer.oculus.com/)
- [Apple — visionOS Developer](https://developer.apple.com/visionos/)
- [Microsoft — HoloLens 2 / Mixed Reality Toolkit (MRTK3)](https://github.com/microsoft/MixedRealityToolkit)
- [Khronos — OpenXR](https://www.khronos.org/openxr/)
- [Metaverse Standards Forum](https://metaverse-standards.org/)
- [ABI Research — Enterprise AR/VR](https://www.abiresearch.com/)
- [ARtillery Intelligence — Market Reports](https://artilleryintelligence.com/)