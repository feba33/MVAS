---
titulo: Ciberseguridad de nube
capa: dominio
tema: ciberseguridad-cloud
fuente: https://en.wikipedia.org/wiki/Cloud_computing_security
fuente2: https://cloudsecurityalliance.org/research/cloud-controls-matrix
fecha: 2026-07-17
confianza: alta
tags: [cloud-security, cspm, iam, shared-responsibility, multicloud, devsecops, csa]
rol: []
actividades: []
organizaciones: []
responsabilidades: []
tareas: []
profundidad: 2
estado: profundo
---

# Ciberseguridad de nube

## 📝 Conocimiento

### Definición
La **ciberseguridad de nube** protege datos, aplicaciones, servicios e infraestructura en entornos cloud (IaaS/PaaS/SaaS). Es subcampo de la seguridad de la información y de la ciberseguridad, con particularidades por el modelo de responsabilidad compartida y la naturaleza efímera/distribuida de la nube.

### Modelo de responsabilidad compartida
- **Proveedor (CSP):** seguridad de la *infraestructura física y del servicio* (hypervisor, red física, disponibilidad).
- **Cliente:** seguridad de *lo que despliega* — configuración, IAM, datos, aplicación, sistema operativo (en IaaS), y uso de SaaS.
- Falta de configuración (S3 abierto, credenciales expuestas) es la causa #1 de brechas cloud.

### Componentes y controles
- **IAM:** identidad, MFA, privilegios mínimos, rotación de secretos (vs `dominio/proteccion-de-datos.md`).
- **CSPM (Cloud Security Posture Management):** detecta malconfiguración y desviaciones de cumplimiento continuamente.
- **CWPP / protección de cargas:** runtime, contenedores, serverless.
- **CNAPP:** convergencia de CSPM+CWPP+red.
- **Cifrado:** en reposo y en tránsito; gestión de claves (KMS, BYOK).
- **Red:** security groups, microsegmentación, WAF, protección de API.
- **CloudTrail/logging:** auditoría y detección.

### Frameworks
- **Cloud Security Alliance — Cloud Controls Matrix (CCM):** catálogo de controles.
- **NIST SP 800-53 / 800-210 (AC en cloud)**; **ISO/IEC 27017/27018** (cloud/PII).
- **CIS Benchmarks** para configuración de CSPs.

### Riesgos
- **Multicloud:** inconsistencia de controles y visibilidad fragmentada.
- **Shadow IT / shadow data:** almacenes no gobernados.
- **IAM excesivo:** credenciales de servicio con alcance amplio (vs `dominio/ciberseguridad.md`).
- **Supply chain:** dependencia de imágenes/contenedores de terceros (vs `dominio/ciberseguridad-cadena-suministro.md`).

### Cross-refs
- `dominio/ciberseguridad.md` · `dominio/ciberseguridad-de-la-informacion.md` · `dominio/devsecops` (rol)
- `dominio/cloud-computing.md` · `dominio/seguridad-corporativa.md`
