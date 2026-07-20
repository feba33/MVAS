---
titulo: Ciberseguridad cloud-native
capa: dominio
tema: ciberseguridad cloud-native (containers, Kubernetes, service mesh, eBPF, Zero Trust)
fuente: https://en.wikipedia.org/wiki/Cloud_native
fuente2: https://www.cncf.io
fecha: 2026-07-20
confianza: alta
tags: [dominio, ciberseguridad, cloud-native, kubernetes, contenedores, zero-trust]
organizaciones: [cncf, nist]
profundidad: 2
estado: profundo
---

# Ciberseguridad cloud-native

## Resumen
La **ciberseguridad cloud-native** protege aplicaciones construidas sobre arquitecturas nativas de nube: **contenedores**, **microservicios**, **orquestación (Kubernetes)**, **service mesh** e infraestructura inmutable. Se aleja de la protección de perímetro estático hacia defensa por carga de trabajo y *identity-aware*.

## Componentes y controles
- **Contenedores**: *image scanning*, firma de imágenes, *admission control*, *runtime security* (eBPF, Falco).
- **Kubernetes**: *RBAC*, *network policies* (microsegmentación), *secrets management*, *pod security standards*, *policy-as-code* (OPA/Gatekeeper).
- **Service mesh** (Istio/Linkerd): mTLS, autorización por servicio.
- **Zero Trust** en cloud: identidad, *least privilege*, *workload identity*.
- **Supply chain**: SBOM, firmado (Sigstore), SLSA; `ciberseguridad-de-la-cadena-de-suministro`.

## Frameworks
- **NIST SP 800-190** (application container security), **CIS Kubernetes Benchmark**.
- **CNCF** (Cloud Native Computing Foundation) define el ecosistema y buenas prácticas.

## Relaciones
- Vincula con `dominio/ciberseguridad`, `dominio/ciberseguridad-de-redes`, `dominio/seguridad-de-aplicaciones`, `dominio/gestion-de-la-nube`, `rol/head-of-cloud-architecture`.
