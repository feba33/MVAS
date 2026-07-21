---
titulo: "Ecología"
capa: "dominio"
tema: "ecologia"
fuente: "https://en.wikipedia.org/wiki/Ecology"
fuente2: "https://www.esa.org/"
fecha: "2026-07-21"
confianza: "alta"
tags: ["ecología", "ecosistemas", "biodiversidad", "poblaciones", "comunidades", "redes-tróficas", "sucesión", "biogeoquímica", "conservación"]
profundidad: 3
estado: "profundo"
rol: ["head-of-sustainability", "head-of-rd", "head-of-regulatory-affairs", "head-of-environmental-health-safety"]
actividades: ["investigación-ecológica", "monitoreo-biodiversidad", "restauración-ecológica", "evaluación-impacto", "servicios-ecosistémicos"]
organizaciones: ["esa", "inba", "ipbes", "iucn", "gbif", "lter", "nebona", "cbd"]
responsabilidades: ["conservación-biodiversidad", "restauración-ecosistemas", "evaluación-impacto-ambiental", "servicios-ecosistémicos", "cambio-global"]
tareas: ["muestreo-campo", "análisis-datos-ecológicos", "modelado-distribución-especies", "planificación-conservación", "comunicación-ciencia"]
---

# Ecología: ecosistemas, biodiversidad, poblaciones, comunidades, sucesión, biogeoquímica

## Definición y niveles de organización

**Ecología** = estudio científico de las interacciones entre **organismos** y su **ambiente** (biótico + abiótico), determinando distribución, abundancia, diversidad y funcionamiento de la vida en la Tierra.

**Niveles jerárquicos** (cada nivel emerge del anterior):
1. **Organismo** — fisiología, comportamiento, historia de vida, adaptación (autecología).
2. **Población** — grupo individuos misma especie, mismo lugar/tiempo; dinámica, estructura, genética (poblacional).
3. **Comunidad** — ensamblaje poblaciones especies interactuando (simpatría); estructura, diversidad, redes tróficas, interacciones (sinecología).
4. **Ecosistema** — comunidad + ambiente abiótico (flujo energía, ciclos materia); funcionamiento, servicios.
5. **Paisaje / Paisaje marino** — mosaico ecosistemas heterogéneo; conectividad, fragmentación, metapoblaciones.
6. **Bioma** — unidades globales clima-vegetación (bosque tropical, desierto, tundra, pradera, bosque templado, boreal, mediterráneo, sabana).
7. **Biosfera** — suma todos los ecosistemas; sistema Tierra acoplado (clima, biogeoquímica, vida).

## Ecología de poblaciones: dinámica, estructura, regulación

**Variables estado**: *N* (tamaño), *λ* (tasa crecimiento finito), *r* (tasa intrínseca), *K* (capacidad carga), estructura edad/tamaño/etapa, sexo, dispersión.

**Modelos crecimiento**:
- **Exponencial**: *dN/dt = rN* → *N(t) = N₀eʳᵗ*; *r = b - d* (natalidad - mortalidad); irrealista largo plazo.
- **Logístico**: *dN/dt = rN(1 - N/K)*; *r* máximo densidad baja, *K* equilibrio recursos; *sigmoide*.
- **Estructurados** (matriz Leslie/Lefkovitch, modelos integrodiferenciales): clases edad/etapa/tamaño; *λ* = valor propio dominante; *elasticidades/sensibilidades* (perturbación *λ* vs parámetros vitales).

**Regulación densidad-dependiente vs independiente**:
- **DD**: competencia (explotación/interferencia), depredación, parasitismo, enfermedad, estrés social, alelopatía; *regulan* alrededor *K*.
- **DI**: clima extremo, catástrofes, perturbaciones abióticas; *fluctúan* poblaciones sin regular.

**Metapoblaciones** (Levins, Hanski): parches hábitat conectados dispersión; *p* fracción ocupados; *dp/dt = cp(1-p) - ep*; persistencia si *c/e > 1* (colonización > extinción); *rescate demográfico/genético*.

**Ciclos vitales / Estrategias *r/K* / *fast-slow* continuum** (Pianka, Stearns): *r-seleccionadas* (alta fecundidad, desarrollo rápido, vida corta, dispersión alta, *r* max) ↔ *K-seleccionadas* (baja fecundidad, desarrollo lento, vida larga, cuidado parental, eficiencia competencia). *Continuum fast-slow* (Pianka 1970, Reznick 1992): eje historia vida (longevidad, edad madurez, tamaño camada, tamaño adulto, iteroparidad/semelparidad).

**Genética poblacional / Ecología evolutiva**: deriva, flujo génico, selección natural, adaptación local, *gene-environment interaction*, *phenotypic plasticity*, *reaction norms*, *local adaptation* (reciprocal transplants, common gardens), *evolutionary rescue*.

## Ecología de comunidades: ensamblaje, diversidad, interacciones, redes

**Ensamblaje comunidades** (filters):
1. **Regional pool** — historia biogeográfica, especiación, extinción, dispersión.
2. **Filtro abiótico** — clima, suelo, disturbio → *environmental filtering* (rasgos funcionales convergentes).
3. **Filtro biótico** — interacciones (competencia, facilitación, depredación, mutualismo) → *limiting similarity* (rasgos divergentes coexistencia).
4. **Estocástico / neutral** — deriva ecológica, prioridad llegada, *Hubbell's neutral theory*.

**Diversidad** (Whittaker, Jost, Chao):
- **α** (local) — riqueza *S*, Shannon *H'*, Simpson *D*, Hill numbers *qD* (q=0 riqueza, q=1 exp(H'), q=2 1/D).
- **β** (rotación / anidamiento) — *β = γ/α* (Whittaker), *βsor* (Sørensen), *βsim* (turnover), *βsne* (nestedness); Baselga partition.
- **γ** (regional) — pool total.
- **Filogenética / Funcional** — *Faith's PD*, *MPD*, *MNTD*, *FRic*, *FEve*, *FDiv*, *FDis*; *SES* (standardized effect size) vs nulo.

**Interacciones especies** (matriz *A* comunidad):
| Tipo | Efecto sp1 | Efecto sp2 | Ejemplos |
|------|------------|------------|----------|
| **Competencia** (-/-) | - | - | Recursos, espacio, interferencia, aparente (compartido depredador) |
| **Depredación / Herbivoría / Parasitismo** (+/-) | + | - | Funcional respuesta (Holling I/II/III), numérica, cascada trófica |
| **Mutualismo** (+/+) | + | + | Polinización, dispersión semillas, micorrizas, rizobios, limpieza |
| **Comensalismo** (+/0) | + | 0 | Epífitas, forésia, inquilinismo |
| **Amensalismo** (-/0) | - | 0 | Alelopatía, pisoteo, sombra |
| **Facultativo vs Obligado** | | | Especialización, dependencia |

**Redes tróficas / ecológicas**:
- **Nodos** = especies / grupos funcionales / *trophic species*; **Enlaces** = quién come a quién / interactúa.
- **Propiedades**: *connectance (C = L/S²)*, *link density*, *trophic level* (basal=1, herbivores=2, carnívoros=3+), *omnivory*, *path length*, *clustering*, *modularity*, *nestedness* (mutualistas), *degree distribution* (power-law?).
- **Estabilidad** (May 1972): *σ√(SC) < 1* (inestabilidad aleatoria); realistas: estructura trófica, omnivoría débil, *weak interactions stabilize* (McCann 2000), *trophic cascades*, *alternative stable states*, *hysteresis*.
- **Cascadas tróficas** (top-down): lobo → ciervo → vegetación (Yellowstone); otaria → erizo → kelp (Pacífico Norte).
- **Ingenieros ecosistémicos** (Jones et al. 1994): castor, coral, elefante, lombriz, *Spartina*; modifican hábitat → afectan muchas especies.

**Sucesión ecológica** (Clements vs Gleason):
- **Primaria** (sustrato nuevo: lava, glacial, dunas, minas) → **Secundaria** (disturbio retiene suelo/banco semillas).
- **Facilitación** (pioneras mejoran condiciones) → **Tolerancia** → **Inhibición** (competencia late-successional).
- **Estado climax** vs **estados alternativos** (histeresis, puntos inflexión); *shifting baselines*.

**Biogeografía insular / de hábitats fragmentados** (MacArthur & Wilson 1967): *S = cAᶻ* (especies-área); *inmigración* ↓ con aislamiento, *extinción* ↓ con área; *rescue effect*; *SLOSS* (Single Large or Several Small); *corredores ecológicos*, *stepping stones*, *matrix permeability*.

## Funcionamiento ecosistémico: energía, materia, servicios

**Flujo energía** (Lindeman 1942): *Producción primaria bruta (GPP)* → *Respiración autótrofa (Ra)* → *NPP = GPP - Ra* → *Consumo herbívoros* → *Producción secundaria* → *Respiración heterótrofa (Rh)* → *NEP = NPP - Rh* (sumidero/fuente carbono). *Eficiencia transferencia trófica* ~10% (Lindeman); *Longitud cadena trófica* limitada energía.

**Ciclos biogeoquímicos** (acoplados C-N-P-S-Fe-Si-H₂O):
- **Carbono**: fotosíntesis (120 PgC/año), respiración, océano (bomba solubilidad + biológica), sedimentación, combustibles fósiles (perturbación antrópica +40% atm CO₂ desde 1750).
- **Nitrógeno**: fijación biológica (100-200 TgN/año), deposición atmosférica, fertilización Haber-Bosch (120 TgN/año), desnitrificación, lixiviación (eutrofización), N₂O (GEI potente).
- **Fósforo**: intemperización roca (lento, limitante largo plazo), sedimentación, minerales, sin reservorio atmosférico; eutrofización lagos/costeros.
- **Azufre**: DMS (clima), deposición ácida, ciclos redox sedimentos.
- **Hierro**: limitante HNLC (High Nutrient Low Chlorophyll); polvo atmosférico, fuentes hidrotermales, sedimentos.

**Servicios ecosistémicos** (MEA 2005, IPBES, TEEB, SEEA-EA):
| Categoría | Ejemplos | Valoración |
|-----------|----------|------------|
| **Provisión** | Alimento, agua, fibra, combustible, medicinas, recursos genéticos | Mercado / costo reposición |
| **Regulación** | Clima (secuestro C), calidad aire/agua, polinización, control plagas/enfermedades, protección costera, erosión, inundaciones | Costo evitado, daño evitado, sustituto |
| **Cultural** | Recreación, turismo, espiritual, estético, educativo, identidad, sentido lugar | Preferencia revelada, contingent valuation |
| **Soporte** | Formación suelo, ciclado nutrientes, producción primaria, hábitat, diversidad genética | Base otras categorías |

**Economía ecológica / Capital natural** — *Natural Capital Protocol*, *SEEA-EA* (UN), *TNFD* (naturaleza), *SBTN* (science-based targets nature), *biodiversity credits*, *nature-based solutions (NbS)*, *payment for ecosystem services (PES)*, *debby-for-nature swaps*.

## Cambio global y ecología: respuestas, adaptación, puntos inflexión

**Drivers** (IPBES 2019): (1) Cambio uso suelo/océano, (2) Explotación directa, (3) Cambio climático, (4) Contaminación, (5) Especies invasoras.

**Respuestas especies**: (1) **Desplazamiento rango** (polos/altitud; *velocity of climate change* ~km/década), (2) **Cambio fenología** (avance primavera, desincronización trófica *mismatch*), (3) **Cambio morfología/fisiología** (tamaño cuerpo *Bergmann*, *Allen's rule*, plasticidad), (4) **Adaptación genética** (selección contemporánea, *evolutionary rescue*), (5) **Extinción** (deuda extinción, *extinction debt*).

**Puntos inflexión ecosistémicos** (Lenton et al. 2008, 2019):
- Amazon dieback → sabana
- Pérdida arrecifes coralinos (>99% 2°C)
- Deshielo permafrost → metano/hidratos
- Colapso AMOC
- Pérdida hielo marino Ártico / Groenlandia / Antártida Occidental
- Boreal forest dieback / shift
- Expansión desiertos / desertificación
- *Cascading tipping points* (interacciones)

**Ecología de la restauración** (SER Standards): *recovery wheel* (atributos: ausencia amenazas, condiciones físicas, composición especies, estructura, función, intercambio paisaje). *Rewilding* (trófico, pasivo, activo), *assisted migration / gene flow*, *synthetic biology* (gene drives invasoras, *de-extinction* debate).

**Ecología urbana / ciudades**: *urban heat island*, *novel ecosystems*, *green infrastructure* (techos verdes, corredores, *sponge cities*), *biodiversity-friendly design*, *ecosystem services valuation* ciudades.

**One Health / EcoHealth / Planetary Health** — interdependencia salud humana, animal, ecosistémica; *zoonosis emergence* (deforestación, comercio vida silvestre, intensificación ganadera, cambio climático), *antimicrobial resistance* ambiente, *microbiome* suelo/humano.

## Herramientas cuantitativas y tecnológicas

| Área | Métodos / Herramientas |
|------|------------------------|
| **Muestreo / Monitoreo** | Transectos, cuadrantes, *capture-recapture* (Cormack-Jolly-Seber, robust design), *occupancy models* (MacKenzie), *distance sampling*, *camera traps* (CT), *acoustic monitoring* (ARU, BirdNET, BatDetect), *eDNA* (metabarcoding, qPCR), *citizen science* (iNaturalist, eBird, GBIF), *drones/LiDAR/photogrammetry*, *satélite* (Sentinel, Landsat, Planet, GEDI, BIOMASS, FLEX). |
| **Análisis datos** | *R* (vegan, lme4, glmmTMB, brms, INLA, spdep, sf, stars, terra, raster, tidyverse), *Python* (scikit-learn, xgboost, pytorch, jax, geopandas, rasterio, xarray, dask), *Julia* (Turing, DifferentialEquations, EcologicalNetworks), *Bayes* (Stan, NIMBLE, JAGS), *Spatiotemporal* (INLA, GP, Kriging, MAXENT, BIOMOD2, sdm, ENMeval). |
| **Modelado** | *SDM/ENM* (MaxEnt, GLM, GAM, RF, BRT, GBM, GLMNet, ensemble BIOMOD2), *Dynamic vegetation models* (LPJ-GUESS, LPJmL, ED2, FATES, ORCHIDEE, JULES), *Dynamic global vegetation models (DGVMs)*, *Ecosystem models* (Ecopath/Ecosim, Atlantis, MIZER, MADING, MICE), *Metapopulation* (RAMAS, Metapop), *Individual-based models (IBM/ABM)* (NetLogo, Repast, HexSim, RangeShifter). |
| **Redes / Estabilidad** | *bipartite*, *igraph*, *NetIndices*, *EconMult*, *cheddar*, *FoodWebs*, *Network3D*, *randomization curves*, *loop analysis*, *qualitative modeling*. |
| **Filogenia / Rasgos** | *ape*, *phytools*, *geiger*, *picante*, *phylolm*, *phylopath*, *RRphylo*, *TR8*, *TRY*, *BIEN*, *GBIF*, *Open Tree of Life*, *FishBase*, *BirdLife*, *IUCN Red List API*. |
| **Datos abiertos / Infraestructura** | GBIF, OBIS, iDigBio, NEON, LTER,ILTER, ICOS, FLUXNET, GEO BON, EBVs (Essential Biodiversity Variables), ESSs (Essential Ecosystem Service Variables), *FAIR principles*, *Darwin Core*, *Ecological Metadata Language (EML)*, *DataONE*, *Dryad*, *Zenodo*, *Zenodo*, *Figshare*. |

## Cross-refs

- [[dominio/conservacion]] — planificación sistemática, áreas protegidas, corredores, rewilding,Species Recovery
- [[dominio/biodiversidad]] — diversidad genética/especie/ecosistema, hotspots, EDGE species
- [[dominio/cambio-climatico]] — desplazamientos, fenología, adaptación, puntos inflexión, refugios climáticos
- [[dominio/cambio-climatico]] — impactos, vulnerabilidad, adaptación ecosistemas
- [[dominio/ciencia-ambiental]] — ciclos biogeoquímicos, contaminación, eutrofización, acidificación
- [[dominio/ecologia-marina]] / [[dominio/oceanografia]] — ecología pelágica/bentónica, arrecifes, pesquerías, carbono azul
- [[dominio/ecologia-urbana]] — ciudades, infraestructura verde, salud urbana
- [[dominio/agrotecnia]] / [[dominio/agrotech]] — agroecología, policultivos, servicios ecosistémicos agrícolas
- [[dominio/economia-ecologica]] — valoración, PES, capital natural, contabilidad ecosistémica (SEEA-EA)
- [[dominio/biogeografia]] — patrones espaciales, endemismo, especiación, extinción
- [[rol/head-of-sustainability]] — estrategia naturaleza, TNFD, SBTN, NbS, reporte ESG
- [[rol/head-of-rd]] — I+D base ecológica, bioinspiración, bioprospección
- [[rol/head-of-regulatory-affairs]] — EIA, permisos, compensación biodiversidad, *biodiversity net gain*
- [[rol/head-of-environmental-health-safety]] — monitoreo ecológico, cumplimiento, gestión residuos/químicos
- [[sustrato/mexico/medio-ambiente]] / [[sustrato/estados-unidos/medio-ambiente]] / [[sustrato/canada/medio-ambiente]] — políticas nacionales, áreas protegidas, leyes especies en riesgo