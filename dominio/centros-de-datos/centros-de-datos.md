---
titulo: Centros de datos (Data Centers)
capa: dominio
tema: centros-de-datos
fuente: https://en.wikipedia.org/wiki/Data_center
fuente2: https://uptimeinstitute.com/tiers
fecha: 2026-07-14
confianza: alta
tags: [centros-de-datos, data-center, infraestructura-ti, tier, colocation, hiperscala, sostenibilidad]
english_keywords: [data center, Tier classification, colocation, hyperscale, Uptime Institute]
---

# Centros de datos (Data Centers)

## 📝 Conocimiento
- **Definición:** instalación física (sala, edificio o recinto) que aloja sistemas de TI (servidores, almacenamiento, red) para **procesar, almacenar y transmitir** datos. La *Energy Independence and Security Act* de 2007 (EE.UU.) la define como facilidad con equipo electrónico para procesar/almacenar/transmitir información digital, con control ambiental.
- **Componentes clave:** energía (UPS, PDU, generadores), refrigeración (CRAC/CRAH, free cooling, líquida), racks/cabinas, red (switches, cruces), capa física (seguridad, supresión de incendios).
- **Estándares Tier (Uptime Institute):** 4 niveles (I–IV) según redundancia y disponibilidad de la infraestructura; certificación de diseño/construcción/operaciones. (Uptime dejó de publicar % de uptime en 2009; el Tier mide topología, no un SLA contractual.)
- **Modelos de entrega:** empresa propia (enterprise), **colocation** (espacio/energía alquilados), **hiperscala** (propietarios masivos: AWS, Google, Meta, Microsoft), y **edge** (cerca del usuario para baja latencia).
- **Sostenibilidad:** consumo eléctrico masivo; métrica **PUE** (Power Usage Effectiveness), energías renovables, reutilización de calor, normas (EU PED/EPBD). Impacta `dominio/energia` y `dominio/cloud-computing`.
- **Relevancia MVAS:** la decisión de ubicación (costo de energía, latencia, riesgo, regulación de datos) y el CAPEX/OPEX definen la estrategia TI; intersecta `dominio/ciberseguridad-gobierno`. Complementa `dominio/cloud-computing`, `dominio/infraestructura` y `dominio/energia`.

## 🔗 Referencia
- Wikipedia EN — Data center: https://en.wikipedia.org/wiki/Data_center
- Uptime Institute — Tier Classification: https://uptimeinstitute.com/tiers
- Cross-ref: `dominio/cloud-computing`, `dominio/infraestructura`, `dominio/energia`, `dominio/ciberseguridad-gobierno`.
