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
