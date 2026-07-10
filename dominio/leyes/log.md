# Registro de leyes (log.md)

Registro cronológico **append-only** de la entidad `leyes`.
Prefijo: `## [YYYY-MM-DD] <tipo> | <título>` (parseable: `grep "^## \[" log.md`).

## [2026-07-09] setup | Nodo wiki de leyes
- Creada la superstructura recursiva de la entidad `leyes` dentro de `dominio/`:
  `raw/`, `index.md`, `log.md` y `README.md`.
- Demuestra el principio: toda la info de leyes vive solo en esta carpeta.

## [2026-07-09] ingest | Ramas del Derecho
- Fuente: conocimiento general + Wikipedia 'List of areas of law' — reference-only.
- Página: `ramas-derecho.md`. Derecho constitucional, civil, penal, mercantil, laboral, administrativo, fiscal, internacional, procesal.

## [2026-07-09] ingest | Derecho de Contratos
- Fuente: Wikipedia EN 'Contract' (https://en.wikipedia.org/wiki/Contract).
- Página: `derecho-contratos.md`. Elementos esenciales, tipos, formación (common law vs. civil), incumplimiento (breach) y remedios (damages, specific performance, rescission).

## [2026-07-09] ingest | Propiedad Intelectual (profundización)
- Fuente: Wikipedia EN 'Intellectual property' (https://en.wikipedia.org/wiki/Intellectual_property).
- Página: `propiedad-intelectual.md`. Marcas, patentes, copyright, trade secrets; relación con el régimen de EE. UU. (Copyright Office, USPTO, Lanham Act, DTSA).

## [2026-07-10] ingest | Derecho Societario y Gobierno Corporativo
- Fuentes: TYP Advisers (2023), RMS Abogados (2025) — reference-only.
- Página: `derecho-societario.md`. Contrato de sociedad, civil vs mercantil, persona jurídica/responsabilidad limitada, levantamiento del velo; tipos LGSM (SA/SAPI/SAS/SRL); órganos (asamblea/consejo/comisario); gobierno corporativo.

## [2026-07-10] ingest | Derecho Laboral (México, LFT — profundización)
- Fuentes: Lledías Abogados (2025), Cámara de Diputados LFT (vigente 14-05-2026) — reference-only.
- Página: `derecho-laboral.md`. Relación laboral, jornada/salario/PTU, IMSS/INFONAVIT, rescisión, reforma outsourcing 2021 + REPSE, justicia laboral, reforma jornada 2026.

## [2026-07-10] ingest | Cumplimiento y Regulación (compliance)
- Fuentes: ISO 37301:2021, Audit Advisor (2025) — reference-only.
- Página: `cumplimiento-regulacion.md`. Compliance como disciplina transversal; ISO 37301 (CMS certificable, PDCA); enfoque basado en riesgo; DOJ/UK Bribery Act; vs ISO 37001.
