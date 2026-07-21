---
titulo: "Meteorología"
capa: "dominio"
tema: "meteorologia"
fuente: "https://en.wikipedia.org/wiki/Meteorology"
fuente2: "https://www.wmo.int/"
fecha: "2026-07-21"
confianza: "alta"
tags: ["meteorología", "atmósfera", "clima", "pronóstico", "fenómenos-meteorológicos", "observación", "modelado-numérico", "alertas-tempranas"]
profundidad: 3
estado: "profundo"
rol: ["head-of-sustainability", "head-of-risk-analytics", "head-of-supply-chain", "head-of-operations", "head-of-rd"]
actividades: ["pronóstico-tiempo", "alertas-tempranas", "modelado-numérico", "observación-atmosférica", "climatología-operacional", "servicios-meteorológicos"]
organizaciones: ["wmo", "noaa", "ecmwf", "uk-met-office", "jma", "cma", "smn-argentina", "ideal-méxico", "smn-chile", "meteochile", "senamhi-peru", "insivumeh-guatemala"]
responsabilidades: ["predicción-tiempo", "alertas-peligrosas", "climatología", "investigación-atmosférica", "servicios-especializados"]
tareas: ["asimilación-datos", "modelado-numérico", "verificación-pronósticos", "productos-climáticos", "capacitación", "cooperación-internacional"]
---

# Meteorología: atmósfera, clima, pronóstico, fenómenos meteorológicos, observación

## Definición y alcance

**Meteorología** = ciencia de la **atmósfera terrestre**, sus fenómenos, procesos y leyes; aplicación para **pronóstico del tiempo** (horas-días), **climatología** (promedios, variabilidad, cambio climático), **alertas tempranas** y **servicios especializados** (aviación, marítima, energía, agricultura, salud, seguros, gestión emergencias, defensa, espacio).

**Ramas principales**:
- **Meteorología sinóptica/operacional** — análisis cartas, pronóstico determinista/probabilístico, nowcasting (0-6h), very-short-range (6-72h), medium-range (3-10d), extended-range (10-30d), sub-seasonal-to-seasonal (S2S, 2-8 semanas).
- **Meteorología dinámica** — ecuaciones primitivas, dinámica fluidos atmósfera, ondas (Rossby, gravedad, Kelvin), inestabilidad baroclínica, ciclogénesis, jet stream, bloqueos.
- **Meteorología física / microfísica nubes** — nucleación, crecimiento gotas/cristales, precipitación, radiación, turbulencia, capa límite, aerosoles-nubes.
- **Climatología** — promedios 30 años (normales OMM), variabilidad (ENSO, NAO, AO, MJO, PDO, AMO), extremos, tendencias, atribución, escenarios (CMIP6).
- **Meteorología aplicada/servicios** — aviación (METAR/TAF/SIGMET), marítima, agrícola (agrometeorología), energética (eólica, solar, hidro), salud (olas calor, calidad aire, polen), hidrometeorología (inundaciones, sequías), seguros (cat bonds, índices paramétricos), defensa, espacio (weather espacial).

## Atmósfera: composición, estructura, termodinámica

**Composición aire seco** (vol %): N₂ 78.08%, O₂ 20.95%, Ar 0.93%, CO₂ ~420 ppm (2024, +2.5 ppm/año), Ne, He, CH₄ ~1.9 ppm, N₂O ~336 ppb, H₂O variable (0-4%).

**Estructura vertical** (por temperatura):
| Capa | Altitud | Gradiente T | Características |
|------|---------|-------------|-----------------|
| **Troposfera** | 0-8/15 km (polos/ecuador) | -6.5°C/km (promedio) | 75-80% masa, vapor agua, fenómenos tiempo, capa límite planetaria (PBL 0.1-3 km) |
| **Estratosfera** | ~15-50 km | +T con altura (ozono UV) | Capa ozono (20-30 km), QBO (28-30 meses), vórtice polar |
| **Mesosfera** | ~50-85 km | -T con altura | Meteoros, nubes noctilucentes, onda gravedad |
| **Termosfera** | ~85-600 km | +T muy alto (radiación solar EUV) | Ionosfera (capas D/E/F), auroras, satélites LEO drag |
| **Exosfera** | >600 km | Transición espacio | Escape átomos ligeros |

**Termodinámica atmósfera**: primer principio (energía interna + trabajo = calor + trabajo), entalpía, entropía, temperatura potencial (θ), temperatura potencial equivalente (θₑ), estabilidad estática (N² = g/θ ∂θ/∂z), CAPE/CIN, índices inestabilidad (LI, K-index, TT, SWEAT, SCP).

**Ciclo hidrológico**: evaporación (océano 86%, tierra 14%), transporte vapor, condensación (nubes), precipitación, escorrentía, infiltración, recarga acuíferos, evapotranspiración. Balance hídrico global: evaporación ≈ precipitación ≈ 505,000 km³/año; atmósfera contiene ~12,900 km³ agua (tiempo residencia ~9 días).

## Observación atmosférica: sistemas globales integrados

**WMO Integrated Global Observing System (WIGOS)** — coordina redes superficie, alta atmósfera, espacio, oceánicas.

| Plataforma | Variables clave | Cobertura / Resolución | Ejemplos |
|------------|-----------------|------------------------|----------|
| **Superficie (SYNOP, METAR, buoys)** | T, Td, viento, P, precipitación, visibilidad, nubosidad, estado tiempo | ~11,000 estaciones tierra, 1,300 boyas (DBCP), 7,000 barcos (VOS) | ASOS/AWOS (US), SYNOP (global), RSMC buoys |
| **Radiosondas (upper-air)** | Perfil T, Td, viento, P hasta 30-35 km | ~900 estaciones 00/12Z (GUAN) + móviles | Vaisala RS41, Graw, Meteomodem |
| **Radares meteorológicos** | Reflectividad, velocidad Doppler, polarimétrico (Zdr, Φdp, ρhv) | Redes nacionales (NEXRAD WSR-88D, OPERA EU, CINRAD China, JMA, SINARAME MX, RMA AR, SMC Col) | WSR-88D dual-pol, C-band polarimétrico, gap-filling X-band |
| **Satélites geoestacionarios** | Imagen visible/IR/WV, AMV, SST, productos derivados (lluvia, nubes, aerosoles, viento) | Disco completo 5-15 min, 0.5-2 km | GOES-16/17/18/19 (ABI), Himawari-8/9 (AHI), Meteosat Third Gen (MTG-I FCI, MTG-S IRS), FY-4A/B (AGRI/GIIRS) |
| **Satélites polares / LEO** | Perfiles T/q (sondaje IR/MW), precipitación (MW), vientos scatterometría, ozono, aerosoles, nubes, superficie | Global, 2-4 pasadas/día, 10-50 km | JPSS/NOAA-20/21 (CrIS, ATMS, VIIRS), MetOp-SG (IASI-NG, 3MI, MWI, MWS, RO), FY-3 (MWTS, MWHS, GNOS), GPM (DPR, GMI), Sentinel-5P (TROPOMI), EarthCARE (ATLID, CPR, MSI), SWOT |
| **GNSS-RO / GNSS-PW** | Perfiles T/q (radioocultación), vapor precipitable total | Global, all-weather, alta vertical | COSMIC-2, MetOp-RO, GRAS, Spire, GeoOptics |
| **Lidar / Ceilómetro / Wind profiler** | Perfil aerosoles/nubes, techo nubes, viento vertical | Redes locales/regionales | MPLNET, EARLINET, CWINDE, NOAA Profiler Network |
| **Supercomputación / HPC** | Asimilación 4D-Var/EnVar/EnKF, ensemble forecasting, post-procesamiento | Exaescala (Frontier, Aurora, LUMI, Fugaku, EuroHPC, Tianhe-3, Sunway) | ECMWF (IFS/ENS), NCEP (GFS/GEFS), UKMO (UM/MOGREPS), CMA (CMA-GFS/GRAPES), JMA (GSM/GEPS), DWD (ICON/ICON-EU/ICON-D2), ECCC (GEM/GEPS) |

## Modelado numérico del tiempo (NWP)

**Ecuaciones primitivas** (forma hidrostática/no-hidrostática): momentum (3), continuidad, termodinámica (1ª ley), estado (gas ideal), humedad (conservación vapor/líquido/hielo). Discretización: malla horizontal (espectral, finite-volume, finite-difference, discontinuous Galerkin), vertical (sigma, híbrida, height-based), tiempo (semi-implícito, split-explicit, Runge-Kutta).

**Escalas y configuraciones típicas 2025**:
| Modelo | Centro | Resolución horizontal | Niveles verticales | Ensemble | Ciclos/día |
|--------|--------|----------------------|-------------------|----------|------------|
| **IFS / ENS** | ECMWF | 9 km (HRES) / 18 km (ENS) | 137 | 50+1 miembros (ENS) | 4 (00,06,12,18) |
| **GFS / GEFS** | NCEP | 13 km (GFS) / 25 km (GEFS) | 127 | 30+1 miembros (GEFS) | 4 |
| **UM / MOGREPS** | UK Met Office | 10 km (UK) / 20 km (Global) | 70 | 18+1 (MOGREPS-G) | 4 |
| **GSM / GEPS** | JMA | 13 km (GSM) / 20 km (GEPS) | 100 | 50+1 (GEPS) | 4 |
| **CMA-GFS / GRAPES** | CMA | 13 km / 25 km | 60 | 20+1 | 4 |
| **ICON / ICON-EU / ICON-D2** | DWD | 13 km (ICON) / 6.5 km (EU) / 2.1 km (D2) | 90 | 40+1 (ICON-EPS) | 4/8/8 |
| **ARPEGE / AROME** | Météo-France | 7.5 km (ARPEGE) / 1.3 km (AROME) | 90 | 25+1 (PEARP) | 4/8 |
| **GEM / GEPS** | ECCC | 15 km (GEM) / 2.5 km (RDPS) | 80 | 20+1 (GEPS) | 4 |
| **WRF / MPAS / COSMO / HARMONIE-AROME** | Comunitarios / Servicios nacionales | Convección-permitiendo (1-3 km) | 50-100 | Variables | Variables |

**Asimilación de datos (DA)**: 4D-Var (ECMWF, Met Office, NCEP), 3D-Var/3DEnVar (JMA, CMA, DWD), EnVar/EnKF (experimental/operacional híbrido), *all-sky* radiances, *all-surface* (tierra, mar, hielo), *hybrid 4DEnVar* (ECMWF 2024), *coupled DA* (atmósfera-océano-hielo).

**Post-procesamiento / calibrado**: *Model Output Statistics (MOS)*, *Ensemble Model Output Statistics (EMOS)*, *Non-homogeneous Gaussian Regression (NGR)*, *Isotonic Distributional Regression (IDR)*, *Machine Learning post-processing* (Random Forests, Gradient Boosting, Neural Nets, Diffusion Models), *bias correction* satélites/radares.

**Verificación**: *Continuous* (RMSE, MAE, correlation, anomaly correlation ACC), *Categorical* (POD, FAR, CSI, ETS, bias), *Probabilistic* (Brier Score, BSS, CRPS, ROC, reliability diagram, sharpness), *Spatial* (FSS, SAL, MODE, object-based), *Extreme* (quantile verification, extreme dependency score).

## Fenómenos meteorológicos clave

| Fenómeno | Escala | Mecanismo clave | Impacto |
|----------|--------|-----------------|---------|
| **Ciclón extratropical** | Sinóptica (1000-3000 km) | Inestabilidad baroclínica, vorticidad potencial, jet streak, conveyor belts | Viento, lluvia, nieve, oleaje, marejada |
| **Ciclón tropical / Huracán / Tifón** | Mesoescala (100-1000 km) | CISK / WISHE, ojo, pared ojo, lluvia extrema, marejada ciclónica | Viento destructivo, lluvia extrema, marejada, tornados |
| **Tormenta severa / Supercelda** | Mesoescala (10-100 km) | CAPE alto, shear vertical, helicidad, updraft rotatorio (mesociclon) | Granizo grande, tornado, viento rectilíneo (derecho), lluvia extrema |
| **Tornado** | Micro/meso (100m-2km) | Rear-flank downdraft, stretching vorticidad, LCL bajo, SRH alto | Viento extremo localizado, destrucción |
| **Lluvia extrema / Inundación flash** | Mesoescala | Entrenamiento ecos, PW alto, movimiento lento, orografía | Inundación repentina, deslaves, víctimas |
| **Ola de calor / Frío extremo** | Sinóptica-planetaria | Bloqueo (Omega block, Rex block), subsidencia, advección, retroalimentación suelo-atmósfera | Salud, energía, agricultura, incendios |
| **Sequía meteorológica / agrícola / hidrológica** | Estacional-interanual | Déficit precipitación, evaporación alta, retroalimentación suelo-humedidad, teleconexiones (ENSO, IOD) | Agua, agricultura, energía, ecosistemas, incendios |
| **Incendio forestal (weather)** | Mesoescala | Viento, baja humedad, T alta, inestabilidad (Haines Index), pirocumulonimbus | Combustión extrema, pyroCb, humo transcontinental |
| **Ciclón mediterráneo / Medicane** | Mesoescala | Baroclinicidad + convección, SST cálida, shear bajo | Viento, lluvia, marejada Mediterráneo |
| **Río atmosférico (AR)** | Sinóptica (2000+ km largo, 400-600 km ancho) | Transporte vapor meridiano, IVT >250 kg/m/s | Lluvia extrema costa oeste continentes, inundaciones, nieve montaña |
| **El Niño / La Niña (ENSO)** | Interanual (2-7 años) | Acoplamiento océano-atmósfera Pacífico tropical; teleconexiones globales | Sequías/lluvias globales, ciclones, pesca, salud, mercados |
| **Oscilación Madden-Julian (MJO)** | Sub-estacional (30-90 días) | Envelope convección este Pacífico/Índico propagación este; modula ciclones, monzones, ARs | Predicción S2S, ciclones, olas calor, inundaciones |

## Servicios meteorológicos especializados

| Sector | Productos clave | Estándares / Regulación |
|--------|-----------------|------------------------|
| **Aviación** | METAR, TAF, SIGMET, AIRMET, GAMET, VAA/VA (ceniza volcánica), SWX (space weather), OPMET, WAFS (WAFC London/Washington), IAVW | ICAO Annex 3, WMO No. 49 Vol II, ICAO Doc 8896 |
| **Marítimo** | NAVTEX, SafetyNET, HF/Inmarsat, GMDSS, Marine Forecast (HIGH SEAS, COASTAL), Ice charts, Wave/Ice forecasts | SOLAS, IMO, WMO Marine Meteorology, Polar Code |
| **Energía** | Pronóstico eólico (hub-height, ramp events), solar (GHI/DNI/DIF, cloud cover), hidro (precip, snowpack, inflow), demanda (T, humedad), *balancing market* | ENTSO-E, IEC 61400-12, WMO Energy Systems |
| **Agricultura** | Agromet advisories, pest/disease models (BLIGHT, RUST), irrigation scheduling (ETc, Kc), frost/freeze warnings, growing degree days, drought indices (SPI, SPEI, PDSI, EDI) | WMO Agrometeorology, FAO AquaCrop, National services |
| **Salud** | Heat-health warning systems (HHWS), air quality (PM2.5, O3, NO2, pollen, dust), UV index, cold spells, vector-borne disease climate suitability (dengue, malaria, chikungunya, Zika) | WHO/WMO Heat-Health, WMO GAW, ECDC, PAHO |
| **Hidrometeorología** | QPF (Quantitative Precipitation Forecast), flash flood guidance (FFG), flash flood watch/warning, river forecast (ensemble), dam safety, flash drought | WMO Flash Flood Guidance System (FFGS), HEPEX, NOAA NWS RFCs |
| **Seguros / Riesgo** | Cat bonds, parametric triggers (wind speed, rainfall, earthquake), loss models (RMS, AIR, EQECAT, CoreLogic), post-event verification (forensic meteorology) | ISO, IAIS, Lloyd's, Guy Carpenter, Aon, Willis Towers Watson |
| **Espacio (Space Weather)** | Solar flares (X-ray), CMEs, geomagnetic storms (Kp, Dst, G-scale), solar radiation storms (S-scale), radio blackouts (R-scale), GNSS scintillation, satellite drag, power grid GIC | NOAA SWPC, ESA SSA, ISES, WMO ISSS, ICAO SWX |

## Alertas tempranas y gestión riesgo

**Marco WMO Multi-Hazard Early Warning Systems (MHEWS)** — 4 pilares: (1) Conocimiento riesgo, (2) Monitoreo/alerta, (3) Comunicación/difusión, (4) Capacidad respuesta.

**Niveles alerta (ej. Europa Meteoalarm / WMO CAP)**:
- **Verde** — Sin riesgo.
- **Amarillo** — Peligro potencial; manténgase informado.
- **Naranja** — Peligro significativo; prepárese, tome precauciones.
- **Rojo** — Peligro extremo; actúe inmediatamente, siga instrucciones autoridades.

**Protocolos CAP (Common Alerting Protocol) v1.2** — estándar XML para alertas multi-hazard, multi-canal (sirena, SMS, app, TV, radio, web, redes sociales). *Alert Hub* (WMO), *FEMA IPAWS*, *EU-Alert*, *Google Public Alerts*, *Apple/Google Emergency Alerts*.

**Verificación alertas**: *Probability of Detection (POD)*, *False Alarm Ratio (FAR)*, *Critical Success Index (CSI)*, *Lead time* medio, *False Alarm Rate* por fenómeno/región.

## Cambio climático y meteorología

**Atribución extrema (Event Attribution)** — *probabilistic event attribution* (PEA): comparar mundo factual (con forzamiento antropogénico) vs contrafactual (preindustrial) usando ensembles modelos / observacionales; *Fraction of Attributable Risk (FAR)*, *Risk Ratio (RR)*. World Weather Attribution (WWA) protocolo rápido (días-semanas post-evento).

**Proyecciones CMIP6 / CORDEX / HighResMIP / DCPP** — SSP1-2.6, SSP2-4.5, SSP3-7.0, SSP5-8.5; downscaling dinámico/estadístico; *emergent constraints*; *large ensembles* (CESM-LE, MPI-GE, CanESM5-LE, ACCESS-LE, ACCESS-LE).

**Señales emergentes**: aumento intensidad precipitación extrema (Clausius-Clapeyron ~7%/°C), mayor proporción ciclones tropicales cat 4-5, desplazamiento polo-ward tracks, aumento frecuencia/intensidad olas calor, sequías compuestas (calor+sequía), incendios extremos, ralentización ciclones (mayor lluvia), expansión Hadley, jet stream más ondulado (debate), AMOC debilitamiento.

## Herramientas cuantitativas y IA/ML en meteorología

| Área | Herramientas / Métodos |
|------|------------------------|
| **Asimilación datos** | 4D-Var, 3DEnVar, EnKF, EnVar híbrido, *all-sky/all-surface*, *coupled DA*, *ML-based QC/bias correction* (CNN, autoencoders) |
| **Modelado NWP** | Espectral (IFS, GFS), FV (FV3, MPAS, ICON, FVM), DG (NICAM, DYNAMICO), *scale-aware physics*, *stochastic physics*, *scale-adaptive convection*, *ML parameterizations* (emuladores radiación, microfísica, radiación, PBL) |
| **Ensemble / Probabilístico** | Breeding vectors, SVs, ETKF, EnKF, EnVar, *initial condition perturbations*, *stochastic physics* (SPPT, SKEB, SHUM), *multi-model ensembles* (S2S, TIGGE, WMO WWRP) |
| **Post-procesamiento / Calibrado** | MOS, EMOS, NGR, IDR, QR, *distributional regression*, *Boosting (XGBoost, LightGBM, CatBoost)*, *Deep Learning* (QRNN, Normalizing Flows, Diffusion Models), *spatial post-processing* (Gaussian Random Fields, CNN) |
| **Verificación** | `harprex`, `METplus`, `scores`, `xverif`, `ensemble_verification`, `SAL`, `MODE`, `FSS`, `SpatialVx`, `properscoring` |
| **Nowcasting (0-6h)** | *Extrapolación* (optical flow, Lucas-Kanade, Deep Learning: RainNet, STEPS, PySTEPS, DGMR, NowcastNet), *data assimilation radar* (4D-Var, EnKF), *convection-permitting ensembles* |
| **Sub-seasonal to Seasonal (S2S)** | *Real-time forecasts* (ECMWF, NCEP, UKMO, JMA, CMA, ECCC, BoM, KMA, CNRM, CNES), *reforecasts* 20-30 años, *teleconnection indices* (MJO, ENSO, NAO, PNA, SAM), *statistical-dynamical hybrids* (ML on S2S output) |
| **IA/ML meteorología** | *WeatherBench 2* benchmark, *GraphCast* (DeepMind), *Pangu-Weather* (Huawei), *FourCastNet* (NVIDIA), *FuXi* (Fudan), *ClimaX* (Microsoft), *Aurora* (MSR), *AIFS* (ECMWF), *NeuralGCM* (Google), *ML for DA* (CNN QC, bias correction), *ML for parameterizations* (radiation, microphysics, convection, PBL), *ML post-processing*, *ML for extremes* (extreme event attribution, compound events) |
| **Computación** | HPC (CPU/GPU), *exascale*, *digital twins* (DestinE, Earth-2), *data lakes* (AWS Open Data, Google Cloud Public Datasets, Azure Planetary Computer, Copernicus Data Space, NOAA Big Data Program), *Zarr/Parquet/Cloud-Optimized GeoTIFF*, *STAC*, *xarray/dask/julia* |

## Cross-refs

- [[dominio/cambio-climatico]] — atribución, proyecciones, señales emergentes, adaptación
- [[dominio/cambio-climatico]] — extremos, olas calor, sequías, ciclones, incendios
- [[dominio/hidrologia]] / [[dominio/hidrometeorologia]] — QPF, inundaciones, sequías, nieve/hielo, gestión agua
- [[dominio/energia]] — pronóstico eólico/solar/hidro, balancing, ramp events, integración renovables
- [[dominio/agricultura]] / [[dominio/agrotech]] — agromet, plagas, riego, heladas, sequía, fenología
- [[dominio/salud-publica]] — olas calor, calidad aire, polen, UV, enfermedades vectoriales
- [[dominio/seguridad-publica]] / [[dominio/gestion-de-crisis]] — alertas tempranas, evacuaciones, gestión emergencias
- [[dominio/transporte]] / [[dominio/logistica]] — aviación, marítimo, carretero, ferroviario, interrupciones
- [[dominio/seguros]] / [[dominio/finanzas-climaticas]] — cat bonds, parametric insurance, loss models, forensic met
- [[dominio/ciencia-de-datos]] / [[dominio/ia-generativa]] — ML NWP, DA, post-processing, verification, nowcasting
- [[rol/head-of-sustainability]] — estrategia climática, resiliencia, TCFD, TNFD, SBTi
- [[rol/head-of-risk-analytics]] — riesgo meteorológico, cat modeling, stress testing climático
- [[rol/head-of-supply-chain]] — resiliencia logística, disrupciones clima, *supply chain weather intelligence*
- [[rol/head-of-operations]] — continuidad negocio, planificación operativa clima-dependiente
- [[rol/head-of-sustainability]] — estrategia NbS, TCFD, TNFD, SBTi
- [[rol/head-of-risk-analytics]] — riesgo meteorológico, cat modeling, stress testing climático
- [[rol/head-of-supply-chain]] — resiliencia logística, disrupciones clima, *supply chain weather intelligence*
- [[rol/head-of-operations]] — continuidad negocio, planificación operativa clima-dependiente
- [[sustrato/estados-unidos/ciencia-de-datos]] — NOAA, NASA, NSF, ONR, IOOS, Argo, PACE, SWOT
- [[sustrato/canada/ciencia]] — DFO, ONC, MEOPAR, ArcticNet, Canadian Argo