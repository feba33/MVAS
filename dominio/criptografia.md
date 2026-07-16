---
titulo: Criptografía
capa: dominio
tema: criptografia
fuente: https://mycybersecuritypath.com/cybersecurity/cryptography-basics/
fuente2: https://destcert.com/resources/asymmetric-cryptography/
fecha: 2026-07-16
confianza: alta
tags: [criptografia, cifrado, pki, tls, post-cuantico, seguridad, hashing]
organizaciones: [nist]
rol: [security-engineer, head-of-security-operations, ciso]
profundidad: 2
estado: profundo
---

# Criptografía (Cryptography)

La **criptografía** es la base de la seguridad digital: resuelve tres
problemas —**confidencialidad** (solo el destinatario lee), **integridad**
(el mensaje no se alteró) y **autenticación** (el emisor es quien dice ser).
Sin criptografía, cualquiera en la red podría leer credenciales bancarios o
modificar datos en tránsito.

## Tipos principales
- **Cifrado simétrico:** una sola clave para cifrar y descifrar. Rápido,
  usado para datos en volumen. Estándar: **AES-256**. El problema es la
  **distribución de claves**.
- **Cifrado asimétrico (clave pública/privada):** par de claves; resuelve
  el reparto de claves. Estándares: **RSA** y **ECC** (curvas elípticas).
  Más lento; se usa para el handshake y firmas.
- **Hashing (resumen):** función unidireccional que genera una "huella"
  (SHA-256). Verifica integridad; no se reversible.
- **Firmas digitales:** prueban autoría e integridad usando clave privada.

## Infraestructura y protocolos
- **TLS/HTTPS:** handshake asimétrico para acordar una clave de sesión
  simétrica (AES), luego cifrado simétrico de todos los datos. Los
  **certificados** prueban la identidad del servidor.
- **PKI** (Public Key Infrastructure): emite, gestiona y revoca certificados
  (CA raíz, certificados intermedios).

## Criptografía post-cuántica (PQC)
Los computadores cuánticos romperían RSA/ECC. **NIST estandarizó
algoritmos resistentes a cuántica en 2024** (p.ej. CRYSTALS-Kyber,
Dilithium). Organizaciones con datos de larga vida (estado, salud, finanzas)
deben planificar migración ahora ("harvest now, decrypt later").

## Relevancia
Sostiene banca, mensajería (Signal), e.firma/SAT, blockchain y VPN.
Vincula con `dominio/ciberseguridad`, `dominio/seguridad-corporativa` y
`dominio/proteccion-de-datos` (privacy by design).
