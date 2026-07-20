---
titulo: Ciberseguridad de redes
capa: dominio
tema: ciberseguridad de redes (firewalls, IDS/IPS, segmentación, zero trust)
fuente: https://en.wikipedia.org/wiki/Network_security
fuente2: https://csrc.nist.gov/glossary/term/zero_trust
fecha: 2026-07-20
confianza: alta
tags: [dominio, ciberseguridad, redes, firewall, zero-trust, ids-ips]
organizaciones: [nist, cisa]
profundidad: 2
estado: profundo
---

# Ciberseguridad de redes

## Resumen
La **ciberseguridad de redes** protege la integridad, confidencialidad y disponibilidad de los datos en tránsito y la infraestructura de red. Combina controles perimetrales tradicionales y el paradigma moderno de **Zero Trust** ("nunca confíes, siempre verifica").

## Controles y arquitectura
- **Firewalls** (L3-L7, *next-generation firewall* NGFW, *stateful*): filtrado por reglas y aplicación.
- **IDS/IPS** (detección/prevención de intrusión): firmas y comportamiento (Snort, Suricata).
- **Segmentación de red / VLAN / microsegmentación**: limita movimiento lateral.
- **VPN / cifrado** (IPsec, TLS), **NAC** (control de acceso a la red).
- **Zero Trust**: autenticación continua, *least privilege*, *microsegmentación*, *policy engine* (NIST SP 800-207).

## Operación
- **NOC/SOC**: monitoreo (SIEM, *traffic analysis*).
- **Hardening** de dispositivos de red (routers, switches), gestión de vulnerabilidades.
- Detección de anomalías, *threat intelligence*.

## Relación con otros dominios
- Complementa `seguridad-de-la-informacion`, `ciberseguridad`, `ciberseguridad-de-endpoints`, `ciberseguridad-cloud-native`.
- Marco: NIST CSF, ISO/IEC 27001 (controles de red A.8.20-8.24).

## Relaciones
- Vincula con `dominio/seguridad-de-la-informacion`, `dominio/ciberseguridad`, `dominio/ciberseguridad-de-endpoints`, `rol/head-of-network-security`, `rol/head-of-security-architecture`.
