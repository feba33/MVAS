# Registro de mexico (log.md)

Registro cronológico **append-only** de la entidad `mexico`.
Prefijo: `## [YYYY-MM-DD] <tipo> | <título>` (parseable: `grep "^## \[" log.md`).

## [2026-07-09] setup | Nodo wiki de mexico
- Creada la superstructura recursiva de la entidad `mexico` dentro de `sustrato/`:
  `raw/`, `index.md`, `log.md` y `README.md`.
- Demuestra el principio: toda la info de mexico vive solo en esta carpeta.

## [2026-07-09] ingest | La CDMX y los nuevos partidos
- Fuente: El Financiero (opinión, R. Guerra). Más partidos: ¿erosionan o amplían el voto opositor?

## [2026-07-09] ingest | Roxana Guzmán y el fracaso de las primeras horas
- Fuente: El Financiero (opinión). Caso periodista evidencia urgencia de protocolos/tecnología de búsqueda.

## [2026-07-09] ingest | ¿Dónde está Rocha Moya?
- Fuente: El Financiero (opinión, R. Riva Palacio). Rocha Moya resguardado en Sinaloa bajo vigilancia del Ejército.

## [2026-07-09] ingest | El triste legado de la crisis climática para la salud infantil
- Fuente: El Financiero (opinión). Clima/contaminación dañan salud infantil y elevan gasto público.

## [2026-07-09] ingest | ¿Y AMLO no le preguntó a Rocha por Ismael 'N'?
- Fuente: El Financiero (opinión, S. Camarena). Caso Zambada-Cuén y entramado político-narco en Sinaloa.

## [2026-07-09] ingest | Ley General de Sociedades Mercantiles (LGSM)
- Fuente: Cámara de Diputados (texto vigente) + CICDE (digest de 7 tipos).
- Página: `lgsm.md`. Cubre los 7 tipos sociales, última reforma (DOF 20-10-2023) y SAS (art. 260, montos DOF 26-12-2025).
- Cross-ref: `dominio/leyes/` y `dominio/finanzas/`.

## [2026-07-09] ingest | Código de Comercio (CCom)
- Fuente: Cámara de Diputados (texto vigente) + Gobierno.com.mx (guía histórica).
- Página: `codigo-de-comercio.md`. Actos de comercio, contratos mercantiles, títulos de crédito, quiebras; reforma DOF 14-11-2025.
- Cross-ref: `lgsm.md` y `dominio/leyes/`.

## [2026-07-09] ingest | LFPDPPP 2025 (protección de datos)
- Fuente: Hogan Lovells (análisis 25-03-2025) + Cámara de Diputados (texto DOF).
- Página: `lfpdpdp.md`. Nueva ley publicada DOF 20-03-2025, vigencia 21-03-2025, abroga la de 2010; INAI disuelto y transferido a la Secretaría Anticorrupción y Buen Gobierno; refuerza derechos ARCO+ y eleva obligaciones de responsables/encargados. Reference-only.

## [2026-07-09] ingest | Regulación de IA en México
- Fuente: CeCo (22-01-2025, cuadro de iniciativas 2023-2025) + Mobile Time (03-10-2025, Marco Normativo del Senado).
- Página: `regulacion-ia.md`. México aún sin ley de IA vigente; múltiples iniciativas con enfoque por riesgo (estilo UE); propuesta de 3 niveles (reforma const., Ley General de IA, armonización de 17 leyes). Confianza media (estatus de iniciativas cambia).

## [2026-07-09] lint | Curación: baja de 5 notas de bajo valor (filtro de relevancia)
- Removidas de `sustrato/mexico/` 5 opinión político-criminales sin ángulo legal-corporativo-técnico (cdmx-nuevos-partidos, roxana-guzman-fracaso-primeras-horas, donde-esta-rocha-moya, crisis-climatica-salud-infantil, amlo-rocha-ismael-n): no pasan el filtro de relevancia (`protocolo-discriminamiento.md`).
- `index.md` de nodo y raíz actualizados. Fuentes eran reference-only (sin `raw/`).

## [2026-07-09] ingest | Régimen Fiscal de México (ISR, IVA, RESICO)
- Fuente: SAT + icopyme/calculadoraIVA/contpaqi (reference-only).
- Página: `regimen-fiscal.md`. ISR e IVA son los impuestos federales principales; RESICO (arts. 113-E a 113-J ISR, desde 2022) simplifica cumplimiento para PF (ingresos ≤$3.5M) y PM (≤$35M, ≤30 trabajadores) con retención 1.25%.

## [2026-07-09] ingest | Competencia Económica en México (LFCE / COFECE)
- Fuente: Cámara de Diputados (texto LFCE, DOF 23-05-2014, última reforma 14-11-2025) — reference-only.
- Página: `cofece.md`. COFECE es el órgano autónomo constitucional que aplica la LFCE: prácticas monopólicas, concentraciones y competencia.

## [2026-07-09] ingest | Ley Federal del Trabajo (LFT)
- Fuente: Wikipedia ES (artículo *Ley Federal del Trabajo (México)*) + conocimiento general — reference-only.
- Página: `lft.md`. Marco laboral (art. 123 Constitucional, vigente desde 1970); jornada (8/7/7.5 h), salario mínimo (CONASAMI), reforma de subcontratación 2021 (outsourcing prohibido en lo sustantivo), PTU (10 % utilidades) y tipos de contrato.

## [2026-07-09] ingest | PROFECO y CONDUSEF
- Fuente: conocimiento general (reference-only).
- Página: `profeco-condusef.md`. PROFECO protege al consumidor (LFPC, registro de contratos, conciliación/arbitraje); CONDUSEF protege al usuario de servicios financieros (Buró de Entidades Financieras, SHCP).

## [2026-07-09] ingest | Prevención de Lavado de Dinero / UIF
- Fuente: conocimiento general (reference-only).
- Página: `pld-uif.md`. Ley Antilavado (LFPIORPI) y UIF (SHCP): sujetos obligados, KYC, avisos de operaciones relevantes y sanciones.
## [2026-07-10] ingest | Comercio exterior México (T-MEC/USMCA, IMMEX, aduana)
- Fuente: Wikipedia (en) — United States–Mexico–Canada Agreement (reference-only).
- Página: `comercio-exterior.md`. México: 14+ TLC; USMCA vigente 1 jul 2020 (sustituye NAFTA); reglas de origen auto 75% regional / 40-45% laboral; IMMEX (importación temporal); PROSEC/draw-back; SE y SAT. Cross-ref controles-exportacion EE.UU.

## [2026-07-11] ingest | Sector energético de México (electricidad, hidrocarburos, renovables)
- Fuentes: Wikipedia ES — Energía eléctrica en México; Petróleos Mexicanos (reference-only).
- Página: `energia.md`. Marco constitucional (propiedad federal); CFE controla electricidad (~90.543 MW, 36,9% limpia 2024); SENER/CRE/CENACE; PEMEX (1938, expropiación), CNH/ASEA; reforma energética 2013; retos de producción y renovables.

## [2026-07-11] ingest | Sistema financiero y banca de México
- Fuentes: Banco de México (banxico.org.mx), CNBV (gob.mx/cnbv) — reference-only.
- Página: `banca-sistema-financiero.md`. Banxico (banco central, política monetaria), CNBV (supervisión), banca múltiple (BBVA, Santander, Banorte, Citibanamex, HSBC), banca de desarrollo (NAFIN, Bancomext, Banobras), Sofipos/ITF/fintech (Nu, Mercado Pago, Klar), SPEI/CoDi; Ley de Instituciones de Crédito.

## [2026-07-11] ingest | Sistema de pensiones de México (AFORE / CONSAR / SAR)
- Fuente: Wikipedia (en, Afore) + CONSAR (gob.mx) — reference-only.
- Página: `pensiones-afore.md`. AFORE administran cuentas individuales de retiro; CONSAR (SHCP) las regula; SAR desde 1997 (sustituye reparto); aportaciones trabajador+patrón+gobierno vía SIEFOREs; AUM ~MX$8.3 billones (23.8% PIB) y >70% cobertura formal (Consar 2025). Cross-ref regimen-fiscal, banca-sistema-financiero, dominio/finanzas.

## [2026-07-11] ingest | Telecomunicaciones en México (IFT→CRT, LMTR 2025)
- Fuentes: Ríosferrer (análisis LMTR 2025), IFT (comunicado banda ancha fija) — reference-only.
- Página: `telecomunicaciones.md`. Reforma constitucional 2024 elimina el IFT; Ley en Materia de Telecomunicaciones y Radiodifusión (LMTR) aprobada 01-07-2025 abroga la LFTR 2014; CRT sustituye al IFT como órgano desconcentrado de la ATDT (5 comisionados); espectro, concesiones, conectividad; crecimiento de banda ancha fija vía fibra. Cross-ref regulacion-ia, dominio/telecomunicaciones.

## [2026-07-11] ingest | Inversión Extranjera Directa en México (LIE, IMMEX)
- Fuentes: SNICE/Secretaría de Economía (programa IMMEX), American Industries Group, Wikipedia (Maquiladora) — reference-only.
- Página: `inversion-extranjera.md`. Marco LIE (sectores reservados al Estado/mexicanos, RNIE); IMMEX (importación temporal sin IGI/IVA, ≥60% exportación, certificación IVA/IEPS); IED >USD$40B al 3T2025 (manufactura ~37%); ~6,500 establecimientos IMMEX, >3M empleos; modalidad Shelter (arranque 3-6 meses). Cross-ref comercio-exterior, sector-manufacturero, regimen-fiscal.

## [2026-07-11] ingest | Sector manufacturero de México (maquiladora)
- Fuentes: American Industries Group (maquiladora 2026), Wikipedia (Maquiladora) — reference-only.
- Página: `sector-manufacturero.md`. Maquila: importa-ensambla-exporta bajo IMMEX; >USD$300B exportados 2024, ~6,800 ops; ~48% empleo fronterizo; salario ~$4.5-5/h; acceso USMCA libre de arancel, 3-5 días a EE.UU.; clústeres (auto, aeroespacial, médica, electrónica). Cross-ref inversion-extranjera, comercio-exterior, energia.

## [2026-07-12] ingest | SAT — Servicio de Administración Tributaria (sustrato/mexico)
- Fuentes: Wikipedia ES (Servicio de Administración Tributaria) + SAT oficial + gobierno.com.mx (CFDI 4.0/e.firma) — reference-only.
- Página: `sat.md`. Órgano desconcentrado de la SHCP (Ley del SAT, 1997); máxima autoridad fiscal; administra RFC, CFF, CFDI 4.0 (e.firma, CIEC, Buzón Tributario, Mi Contabilidad); recauda ISR/IVA/IEPS/aranceles y cuotas IMSS-ISSSTE; carga tributaria baja (~13-14% PIB). Complementa `regimen-fiscal.md`.

## [2026-07-12] ingest | Pemex niega fracking en la Huasteca Potosina (sustrato/mexico)
- Fuente: El Financiero (2026-07-11) — reference-only (URL en frontmatter, sin raw/).
- Página: `pemex-fracking-huasteca.md`. Pemex desmiente que un permiso de explosivos en San Antonio, SLP, implique fracking en la Huasteca Potosina; reitera su postura frente a la polémica ambiental/social de la región.
- Discernimiento: sustrato/mexico (energía/hidrocarburos) + cross-ref energia.md. Certeza alta.
- Gate de relevancia: el ítem tiene ángulo de sector energético (Pemex, hidrocarburos, fracking) → ingerido. Los otros 4 ítems del scrape (mundial deportes, fuga Cereso Hermosillo, tiroteo en velorio Michoacán, operativos de seguridad Uruapan) se filtraron por gate de relevancia (coyuntura deportiva/criminal/seguridad sin ángulo legal-corporativo-técnico).

## [2026-07-12] ingest | Educación en México (SEP, sistema educativo, educación superior)
- Fuentes: Wikipedia (en) — Education in Mexico; Scholaro (Mexico Education System); SEP — reference-only.
- Página: `educacion.md`. SEP (1921, Vasconcelos) fija política/curriculo; educación básica (preescolar 1 año obligatorio + primaria 1-6 + secundaria 7-9 obligatoria) y media superior (bachillerato 10-12); superior (UNAM, IPN, UAM, TecNM, ITESM, ANUIES; licenciatura/maestría/doctorado/TSU). Reformas 2013 (eval. docente) y 2019 (roll-back). ~36M estudiantes; ~3% PIB; retos equidad/calidad (PISA). Cross-ref dominio/educacion, lft (docente), regimen-fiscal (gasto).

## [2026-07-12] ingest | Medio ambiente México (SEMARNAT, LGEEPA, cambio climático, ESG)
- Fuentes: SEMARNAT (gob.mx); Wikipedia (en) — Environmental issues in Mexico — reference-only.
- Página: `medio-ambiente.md`. SEMARNAT (2000) es autoridad federal; PROFEPA/CONANP/CONAFOR. LGEEPA (1988) es ley mãe; NOM-EMA. Ley General de Cambio Climático (2012) + NDC; Ley de Transición Energética; Ley General de Economía Circular (2023). Criterios ESG (GRI/SASB). Retos: deforestación, escasez hídrica, contaminación. Cross-ref sustrato/mexico/energia, dominio/sostenibilidad, dominio/agua, dominio/mineria, dominio/agronegocios.

## [2026-07-12] ingest | Seguridad social México (IMSS, ISSSTE, regímenes)
- Fuentes: Wikipedia (es) — IMSS; Gob.mx IMSS; Wikipedia (es) — ISSSTE — reference-only.
- Página: `seguridad-social.md`. Art. 123 Constitución (Apartados A/B). IMSS (LSS 1943) cubre sector privado: enfermedad/maternidad, riesgos de trabajo, invalidez/vida, retiro (SAR/AFORE 1997), guarderías. ISSSTE (Ley 2007) sector público federal; regímenes especiales ISSFAM/PEMEX/CFE/SB. INSABI (2019) descontinuado 2023 → IMSS-Bienestar. Financiamiento por cuotas obrero-patronales. Cross-ref sustrato/mexico/pensiones-afore, sustrato/mexico/sat, sustrato/mexico/lft, dominio/salud, rol/head-of-people.

## [2026-07-12] ingest | Transporte e infraestructura México (SICT)
- Fuentes: Wikipedia (en) — Secretariat of Infrastructure, Communications and Transportation; gob.mx/sct — reference-only.
- Página: `transporte.md`. SICT (antes SCT) regula carreteras/puertos/aeropuertos/ferrocarriles; red carretera ~377k km; APIs (Manzanillo, Lázaro Cárdenas, Veracruz); CPKC conecta CA-US-MX; AICM/AIFA; ~28 cruces fronterizos. Certeza alta. Cross-ref comercio-exterior, sector-manufacturero, dominio/transporte, dominio/logistica.
