---
titulo: Blockchain empresarial
capa: dominio
tema: blockchain-empresarial
fuente: https://en.wikipedia.org/wiki/Blockchain
fuente2: https://www.hyperledger.org/
fecha: 2026-07-17
confianza: alta
tags: [blockchain, enterprise-blockchain, hyperledger, rwa, supply-chain-traceability, smart-contracts, consorcios]
rol: []
actividades: []
organizaciones: []
responsabilidades: []
tareas: []
profundidad: 2
estado: profundo
---

# Blockchain empresarial

## 📝 Conocimiento

### Definición
El **blockchain empresarial** (o permisionado) aplica registros distribuidos (DLT) a procesos B2B: consorcios de empresas comparten un libro inmutable y auditado sin una autoridad central. A diferencia de las criptomonedas públicas, suele ser **permissioned** (participantes conocidos, control de acceso) y enfocado en eficiencia, trazabilidad y confianza entre contrapartes.

### Componentes
- **Ledger distribuido:** copia sincronizada entre nodos; consenso (PBFT, Raft, BFT) en vez de proof-of-work.
- **Contratos inteligentes:** lógica de negocio ejecutable (ej. liberación de pago al cumplir condición).
- **Identidad y permisos:** gestión de identidades de organizaciones (CA, MSP).
- **Tokens / RWA:** representación on-chain de activos reales (bonos, commodities, facturas).
- **Interoperabilidad:** puentes y estándares para conectar redes.

### Plataformas y ecosistema
- **Hyperledger (Linux Foundation):** Fabric, Besu, Sawtooth — marcos permisionados empresariales.
- **R3 Corda:** financiero/legal (consorcios bancarios).
- **Quorum / Enterprise Ethereum:** derivados de Ethereum para uso corporativo.
- **Consorcios:** redes de industria (trade finance, logística, alimentaria).

### Casos de uso
- **Trazabilidad de cadena de suministro:** procedencia de alimentos, minerales, fármacos (auditabilidad ESG/COFEPRIS/FDA).
- **Trade finance:** cartas de crédito, conocimientos de embarque electrónicos, reducción de papel.
- **RWA / tokenización:** bonos, facturas, comodities; liquidación más rápida.
- **Identidad verificable:** credenciales corporativas, KYC compartido (vs `dominio/proteccion-de-datos.md`).
- **Logística:** tracking multi-parte sin reconciliación manual.

### Riesgos y consideraciones
- **Gobernanza:** quién administra la red, costos de operación de nodos.
- **Privacidad:** datos sensibles requieren canales privados / zero-knowledge.
- **Regulatorio:** valores tokenizados tocan a SEC/CNBV; AML/KYC aplica.
- **Hype vs. valor:** no todo necesita DLT; a veces una BD compartida basta.
- ** vs `dominio/blockchain`:** este nodo es la adopción empresarial/B2B; el de dominio cubre la tecnología base y web3.

### Cross-refs
- `dominio/blockchain.md` · `dominio/deep-tech.md` · `dominio/cadena-suministro.md`
- `dominio/fintech.md` · `dominio/regtech.md`
