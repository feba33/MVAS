---
titulo: "Tecnología espacial / Space Tech"
capa: "dominio"
tema: "tecnologia-espacial"
fuente: "https://en.wikipedia.org/wiki/Space_technology"
fecha: "2026-07-22"
confianza: "alta"
tags: ["espacio", "satelites", "launch", "LEO", "observacion-tierra", "comunicaciones", "navegacion", "mineria-espacial", "NewSpace"]
profundidad: 2
estado: "profundo"
---

# Tecnología espacial / Space Tech

## Definición y alcance

**Space Tech** abarca el diseño, fabricación, lanzamiento y operación de **vehículos y sistemas espaciales**, así como los **servicios y aplicaciones** derivados de la infraestructura orbital. Incluye:

- **Segmento espacial**: satélites, naves, estaciones, *payloads*, *rovers*, *landers*.
- **Segmento de lanzamiento**: cohetes (expendables, reutilizables), *spaceports*, logística de lanzamiento.
- **Segmento terrestre**: estaciones de control (TT&C), *gateways* de datos, centros de procesamiento.
- **Servicios *downstream***: observación de la Tierra (EO), comunicaciones (satcom), navegación (GNSS/PNT), *space situational awareness* (SSA), *in-orbit servicing* (IOS), manufactura orbital, minería.

## Evolución: Old Space → New Space

| Dimensión | **Old Space** (1957-2000s) | **New Space** (2000s-presente) |
|-----------|----------------------------|--------------------------------|
| **Actores** | Agencias gubernamentales (NASA, Roscosmos, ESA, CNSA, ISRO, JAXA) + *prime contractors* (Boeing, Lockheed, Airbus, Thales) | **Empresas privadas** (SpaceX, Blue Origin, Rocket Lab, Planet, Spire, OneWeb, Starlink, Astranis, Varda, Axiom, Sierra Space, Relativity, Firefly, ABL, Isar, PLD Space, iSpace, Astroscale, +1000 startups) |
| **Financiación** | Presupuestos públicos, *cost-plus contracts* | **Capital riesgo (VC)**, *public markets* (SPACs, IPOs), *fixed-price contracts* (NASA CLPS, CRS, HLS, Commercial LEO Destinations) |
| **Filosofía** | Fiabilidad extrema, ciclos 10-15 años, *heritage* | **Iteración rápida**, *fail fast*, COTS, reutilización, *vertical integration*, *software-defined* |
| **Cadena de valor** | Vertical, *single-source*, *government-as-customer* | **Ecosistema multi-cliente**, *platforms*, *rideshare*, *hosted payloads*, *data-as-a-service* |
| **Costo a órbita** | $10,000-50,000/kg (expendable) | **$1,500-3,000/kg** (Falcon 9 reutilizado); target Starship <$100/kg |

## Segmentos de mercado y megatendencias 2025-2030

### 1. Satélites y constelaciones

| Categoría | Altitud | Latencia | Casos de uso | Ejemplos 2025 |
|-----------|---------|----------|--------------|---------------|
| **GEO** (35,786 km) | Geoestacionario | ~600 ms | TV, *broadcast*, *backhaul*, meteorología (GOES, Meteosat, Himawari), *high-throughput* (HTS) | ViaSat-3, Jupiter-3, Eutelsat Konnect, Inmarsat GX |
| **MEO** (8,000-20,000 km) | Media | ~100-150 ms | Navegación (GPS, Galileo, GLONASS, BeiDou, NavIC, QZSS), *O3b mPOWER* (SES) | GPS IIIF, Galileo 2nd Gen, O3b mPOWER (11 sat) |
| **LEO** (<2,000 km) | Baja | **20-50 ms** | **Broadband global (Starlink, OneWeb, Kuiper, Guowang)**, EO alta revisita, IoT, SSA | **Starlink ~6,000 sat** (Gen2/V2 Mini, *direct-to-cell*), OneWeb 634, Kuiper (proto 2023, *deployment 2025+*), Guowang (China, 13,000 plan), Telesat Lightspeed |
| **VLEO** (<450 km) | Muy baja | <10 ms | EO ultra-alta resolución (<10 cm), *quantum comms*, *debris mitigation* (arrastre natural) | Albedo Space (10 cm), Skeyeon, ESA *Skimsat*, DARPA *Ouija* |

**Megaconstelaciones LEO** — transforman conectividad global:
- **Starlink (SpaceX)**: >4M usuarios (2024), *direct-to-cell* (T-Mobile, Rogers, Optus, Entel, Salt, One NZ), *Starshield* (gobierno).
- **Project Kuiper (Amazon)**: $10B+ inversión, 3,236 sat planificados, lanzamiento masivo 2025-2029 (ULA Vulcan, Ariane 6, New Glenn, Falcon 9).
- **OneWeb (Eutelsat)**: 634 sat operativos, *enterprise/aviation/maritime/gov*, fusión Eutelsat 2023.
- **Guowang / GW (China)**: 13,000 sat planificados (LEO + MEO), *China Satellite Network Group*.
- **Telesat Lightspeed**: 198 sat (LEO), *government/enterprise*, financiación Canadá.
- **Rivada Space Networks**: *outer-space spectrum* (Ka/Ku/V), *laser inter-satellite links* (optical mesh).

### 2. Observación de la Tierra (Earth Observation / EO)

| Tipo | Resolución | Revisita | Proveedores clave 2025 |
|------|------------|----------|------------------------|
| **Electro-óptico (EO) panchromático/multiespectral** | **<30 cm** (max comercial: 25-30 cm EE.UU.; 50 cm resto) | Diaria (constelaciones) | **Maxar** (WorldView Legion 6 sat, 30 cm), **Airbus** (Pléiades Neo 30 cm), **Satellogic** (constelación 40+ sat, 1m, alta frecuencia), **Planet** (Dove ~200 sat, 3-5m; Pelican 30 cm; SkySat 50 cm), **BlackSky** (Gen-3 35 cm, revisita horaria), **ICEYE** (SAR), **Capella Space** (SAR), **Ursa Space** (SAR analytics), **Synspective** (SAR), **PIXEL** (hyperspectral), **Orbital Sidekick** (hyperspectral GHG) |
| **Radar de apertura sintética (SAR)** | 25 cm - 5 m | Todo tiempo, noche, nubes | ICEYE (constelación 30+), Capella (acquisition on demand), Synspective (StriX), Umbra (0.25 m), PredaSAR |
| **Hiperspectral / Termal / GHG** | 30 m - 10 m | Metano, CO2, minerales, vegetación | **GHGSat** (metano 25m), **Carbon Mapper** (Planet/JPL), **PRISMA** (ASI), **EnMAP** (DLR), **TRISHNA** (CNES/ISRO 2025), **SBG** (NASA 2027) |
| **Radiooccultación / GNSS-RO** | Perfiles atmósfera | Clima, espacio | **Spire** (100+ sat), **GeoOptics**, **PlanetiQ** |

**Tendencias EO**: *Analysis-ready data (ARD)*, *cloud-native* (AWS Ground Station, Azure Orbital, Google Earth Engine), *AI/ML on-board* (filtrado nubes, detección cambios, *tip-and-cue* SAR→EO), *tasking API* (programación en minutos), *data fusion* (EO+SAR+AIS+RF).

### 3. Comunicaciones y Navegación (Satcom / GNSS)

- **5G NTN (Non-Terrestrial Networks)** — 3GPP Rel-17/18/19: *direct-to-device* (smartphones estándar), IoT-NTN, *satellite-to-cell*; Starlink *Direct-to-Cell*, AST SpaceMobile (BlueBird), Lynk Global, Omnispace, Skylo.
- **Óptica inter-satélite (OISL / lasercom)** — *SpaceX Starlink v1.5/v2* (laser mesh), *Tesat* (ESA EDRS), *Mynaric*, *BridgeComm*, *Xona* (PNT LEO), *Kinéis* (IoT), *SDA Tranche 1/2* (DoD mesh).
- **GNSS modernización** — GPS III/IIIF (L1C, L2C, L5, M-code), Galileo 2nd Gen (E1/E5/E6, *HAS* high accuracy), BeiDou-3 (global, RNSS), QZSS (Japón), NavIC (India), *LEO PNT* (Xona, TrustPoint, Geespace) → **cm-level** posicionamiento.

### 4. Lanzamiento (Launch)

| Vehículo | Carga LEO (kg) | Reutilización | Estado 2025 | Precio / kg |
|----------|----------------|---------------|-------------|-------------|
| **Falcon 9** (SpaceX) | 22,800 | 1ª etapa (20+ vuelos) | Operacional (cadencia >100/año) | ~$2,700 |
| **Falcon Heavy** | 63,800 | 2 laterales + central (parcial) | Operacional | ~$1,500 |
| **Starship / Super Heavy** (SpaceX) | **150,000+** (expendable) / **100,000+** (reutilizable) | **Totalmente reutilizable** | **Orbital flight tests (IFT-4/5/6 2024-25)**, objetivo orbital 2025 | **Target <$100/kg** |
| **New Glenn** (Blue Origin) | 45,000 | 1ª etapa (aterrizaje barco) | Primer lanzamiento 2024/25 | ~$2,000 target |
| **Vulcan Centaur** (ULA) | 27,200 | Motor BE-4 (reutilización futura *SMART*) | Certificación USSF 2024, operativo 2025 | ~$3,500 |
| **Ariane 6** (Arianespace) | 21,650 (A64) | Expendable | Inaugural 2024, ramp-up 2025 | ~$4,000 |
| **H3** (JAXA/MHI) | 6,500-4,000 | Expendable | Operacional 2024 | ~$5,000 |
| **Electron** (Rocket Lab) | 300 | 1ª etapa (helicóptero/barco - en desarrollo) | Operacional (cadencia ~mensual) | ~$25,000 (dedicado) |
| **Neutron** (Rocket Lab) | 13,000 | 1ª etapa (aterrizaje) | Primer vuelo 2025 | ~$3,000 target |
| **Terran R** (Relativity) | 23,500 | Totalmente reutilizable (impresión 3D) | Desarrollo, objetivo 2026 | ~$2,000 target |
| **New Line-1 / Zhuque-3 / Hyperbola-3** (China comercial) | 10,000-20,000 | 1ª etapa reutilizable | Vuelos prueba 2024-25 | Competitivo |
| **ArianeNext / Themis / Prometheus** (ESA) | — | Reutilizable LOX/CH4 | Demostradores 2025-2030 | Target €1M/launch |

**Rideshare / SmallSat launch**: SpaceX *Transporter* (misiones mensuales, $6,000/kg), Rocket Lab, Exolaunch, ISILaunch, Spaceflight Inc., *SSO* (Arianespace), *D-Orbit* (ION *space tug*), *Momentus* (Vigoride), *Epic Aerospace* (Chimera).

### 5. Aplicaciones emergentes *in-orbit*

| Categoría | Descripción | Empresas / Misiones clave |
|-----------|-------------|---------------------------|
| **In-Orbit Servicing (IOS) / Life Extension** | Repostaje, reparación, reubicación, *de-orbit*, inspección | **Northrop Grumman MEV-1/2** (GEO life extension), **Orbit Fab** (RAPID tanker, *fuel ports* RAFTI), **Astroscale** (ELSA-d, LEXI, *Life Extension In-orbit Servicer*), **DARPA RSGS** (NSSL), **Maxar SPACE Infrastructure** (OSAM-1/SPIDER), **ClearSpace** (ClearSpace-1 ESA 2026), **Obruta** (refueling) |
| **Active Debris Removal (ADR)** | Captura y desorbitado basura espacial | **Astroscale** (ELSA-d, ADRAS-J JAXA), **ClearSpace** (ClearSpace-1), **Rogue Space Systems**, **Tethers Unlimited** (terminator tape), **LeoLabs** (tracking) |
| **In-Orbit Manufacturing / Assembly** | Manufactura aditiva, ensamblaje estructuras grandes, *fiber optics* (ZBLAN), farmacéuticos, semiconductores | **Varda Space** (reentry capsules W-1/W-2, pharma), **Space Forge** (ForgeStar, materiales alta pureza), **Redwire** (Archinaut/OSAM-2, *Industrial Crystallization*), **Made In Space** (Archinaut, *Ceramic Manufacturing*), **ThinkOrbital** (soldadura electrónica) |
| **Orbital Data Centers / Edge Compute** | Procesamiento *in-situ* (EO, RF, *AI inference*), *low-latency* servicios | **Lumen Orbit**, **OrbitsEdge**, **HPE** (Spaceborne Computer-2 ISS), **Microsoft Azure Orbital**, **AWS Snowcone** (ISS), **Kleo Connect** (optical inter-sat) |
| **Space-Based Solar Power (SBSP)** | Energía solar orbital → microondas/laser → Tierra | **ESA SOLARIS**, **UK Space Energy Initiative**, **Caltech SSPP** (MAPLE demo 2023), **China** (2028 demo), **Virtus Solis**, **Space Solar** (UK) |
| **Lunar / Cislunar Economy** | *CLPS* (NASA), *Artemis*, *ILRS* (China/Rusia), ISRU, *lunar comms/nav* (LunaNet), *surface power*, *cargo delivery* | **Intuitive Machines** (IM-1 Odysseus 2024, IM-2/3), **Astrobotic** (Peregrine, Griffin), **Firefly** (Blue Ghost), **ispace** (Hakuto-R M1/M2), **Ispace EU/US**, **Astrolab** (FLEX rover), **Venturi Astrolab**, **Lockheed Martin** (Lunar Mobility Vehicle), **Nokia** (LTE/4G Moon), **ESA Moonlight** (comms/nav) |

## Economía y financiación

| Métrica | 2023 | 2024 (est.) | Tendencia |
|---------|------|-------------|-----------|
| **Economía espacial global** (Space Foundation / BryceTech) | **$570B** | ~$600B+ | Crecimiento 6-8% anual |
| **Inversión VC en space** (BryceTech / Space Capital) | $12.5B (2023, -40% vs 2022) | ~$10-12B (estabilización) | *Mega-rounds* selectivos (Starship, Kuiper, Varda, Astroscale, Relativity); *Series A/B* activas en *downstream* (EO analytics, satcom, software) |
| **Contratación pública (NASA DoD ESA)** | NASA $25B+; DoD $30B+ (Space Force); ESA €7B | Creciente (SDA, NSSL, CLPS, Artemis, IRIS²) | *Fixed-price*, *milestone-based*, *Other Transaction Authority (OTA)* |
| **Mercado público (SPACs/IPOs)** | 2021 pico (~20 SPACs); 2022-24 sequía | Reapertura selectiva (2025+) | *Pure-play* downstream (Planet, Spire, BlackSky, Rocket Lab, Redwire, Astra — la mayoría *de-SPAC* bajo presión) |

## Regulación y gobernanza emergente

| Tema | Estado 2025 |
|------|-------------|
| **Tráfico orbital / STM (Space Traffic Management)** | *Non-binding* UN COPUOS *Guidelines for Long-term Sustainability (LTS)* 2021; **EE.UU. Space Policy Directive-3 (SPD-3)** → **Office of Space Commerce (OSC)** *Traffic Coordination System for Space (TraCSS)* (operacional 2025); **UE** *Space Traffic Management* propuesta 2024; **China** *Space Debris Mitigation* regulations; **LeoLabs/Slingshot/ExoAnalytic** tracking comercial |
| **Espectro / Frecuencias** | **WRC-23/27** (UIT): asignaciones *mega-constellations* (Ku/Ka/V/Q/E-band), *non-geostationary* (NGSO) *coordination* (Art. 9/11 RR), *5G/6G vs. satcom* coexistence |
| **Responsabilidad / Seguros** | *Liability Convention* 1972 (Estado lanzador responsable); mercado seguros *hardening* (prima ↑, capacidad ↓) tras anomalías (Vega-C, Ariane 6, Starship); *parametric insurance* emergente |
| **Propiedad recursos / Minería** | **EE.UU. Commercial Space Launch Competitiveness Act 2015** (Art. 51302: *property rights* recursos asteroides/luna); **Luxemburgo** (2017), **UAE** (2020), **Japón** (2021) leyes similares; **Moon Agreement **similares**; **Tratado de la Luna 1979** (no ratificado por potencias) |
| **Protección planetaria** | **COSPAR Planetary Protection Policy** (categorías I-V); NASA *PDS* (Planetary Protection Directive) actualizada 2024 (Marte *Special Regions*, retorno muestras MSR) |

## Riesgos y retos críticos

| Riesgo | Impacto | Mitigación |
|--------|---------|------------|
| **Kessler Syndrome** (cascada colisiones) | Pérdida acceso LEO, destrucción activos ($1T+ en riesgo) | ADR obligatorio, *post-mission disposal* (PMD) <5 años (FCC 2022), *design for demise*, *collision avoidance* automatizado (AI/ML), *space traffic coordination* |
| **Dependencia lanzamiento único** (Starship / Falcon 9) | *Single point of failure* para occidente | New Glenn, Vulcan, Ariane 6, Neutron, Terran R, *European launcher challenge* (ESA), *commercial cargo/crew* redundancia |
| **Ciberseguridad / RF interference** | *Jamming/spoofing* GNSS (Ucrania, Oriente Medio), *hacking* satelites (Viasat KA-SAT 2022), *laser dazzling* | *Encryption*, *frequency hopping*, *lasercom* (inmune a RF), *zero-trust architecture*, *ground segment hardening* |
| **Brecha talento STEM** | 100k+ vacantes globales aeroespacial/software/IA | *Apprenticeships*, *universities partnerships* (Purdue, MIT, Stanford, TUM, ISAE, TU Delft), *talent visas* |
| **Incertidumbre regulatoria** (espectro, escombros, responsabilidad, minería) | Retrasa inversión, *chilling effect* | *Industry consortia* (GSOA, SIA, Eurospace, SDA), *engagement* temprano con *OSC, FCC, ITU, UN COPUOS* |

## Fuentes
- [Wikipedia — Space technology](https://en.wikipedia.org/wiki/Space_technology)
- [Space Foundation — The Space Report 2024](https://www.spacefoundation.org/space_report/)
- [BryceTech — Space Investment Quarterly / Start-up Space](https://brycetech.com/reports)
- [Space Capital — Quarterly Investment Report](https://spacecap.com/insights/)
- [ESA — Space Economy Report 2024](https://www.esa.int/About_Us/Corporate_news/ESA_publishes_Space_Economy_Report_2024)
- [NASA — Commercial Space](https://www.nasa.gov/commercial-space/)
- [Space Force / SDA — Proliferated Warfighter Space Architecture](https://www.sda.mil/)
- [FCC — Space Bureau / Satellite Division](https://www.fcc.gov/satellites)
- [UNOOSA / COPUOS — LTS Guidelines, BBNJ, STM](https://www.unoosa.org/oosa/en/ourwork/copuos/index.html)
- [ESA — Space Safety / Clean Space / Space Debris](https://www.esa.int/Safety_Security)
- [LeoLabs / Slingshot Aerospace / ExoAnalytic — Space Domain Awareness](https://leolabs.space/)
- [Seradata / Space Launch Report / Next Spaceflight — Launch database](https://nextspaceflight.com/)
- [Satellite Dashboard — UCS / ESA / Bryce](https://www.ucsusa.org/resources/satellite-database)