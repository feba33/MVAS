# Registro de crowdfunding (log.md)

Registro cronológico **append-only** de la entidad `crowdfunding`.
Prefijo: `## [YYYY-MM-DD] <tipo> | <título>` (parseable: `grep "^## \[" log.md`).

## [2026-07-12] setup | Nodo wiki de crowdfunding
- Creada la superstructura recursiva de la entidad `crowdfunding` dentro de `dominio/`:
  `raw/`, `index.md`, `log.md` y `README.md`.
- Principio: toda la info de crowdfunding vive solo en esta carpeta.

## [2026-07-12] ingest | Crowdfunding (financiamiento colectivo)
- Fuentes: Wikipedia (en) — Crowdfunding; Equity crowdfunding — reference-only.
- Página: `crowdfunding.md`. Tipos donation/reward, equity (Reg CF/JOBS Act 2012), debt p2p, inmobiliario; >US$34B global 2015. Retos fracaso, fraude, protección inversionista. Cross-ref dominio/finanzas, capital-riesgo, fintech, rol/chief-investment-officer, sustrato/estados-unidos/sec-valores.