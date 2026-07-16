---
titulo: Privacidad diferencial y tecnologías de privacidad (PETs)
capa: dominio
tema: computacion
fuente: https://en.wikipedia.org/wiki/Differential_privacy
fuente2: https://en.wikipedia.org/wiki/Federated_learning
fecha: 2026-07-16
confianza: alta
tags: [privacidad-diferencial, pets, federated-learning, homomorfico, anonymization, privacidad]
profundidad: 2
estado: profundo
---

# Privacidad diferencial y tecnologías de privacidad (PETs)

Las **tecnologías de privacidad (PETs)** protegen los datos personales mientras
se habilita su uso (analítica, IA, colaboración). Incluyen **privacidad
diferencial**, **aprendizaje federado**, **cifrado homomórfico** y técnicas de
anonimización. Son distintas de la mera "protección de datos" (cumplimiento
legal): son métodos técnicos de privacidad por diseño.

## Privacidad diferencial (Differential Privacy, DP)
- Marco **matemáticamente riguroso** para publicar información estadística de
  un dataset protegiendo a los individuos: comparte patrones agregados del grupo
  limitando lo que se filtra sobre personas específicas.
- Se logra inyectando **ruido calibrado** en los cómputos estadísticos.
- Parámetro ε (epsilon): controla el trade-off privacidad–utilidad.
- Usado por Apple, Google, censos (ej. US Census) y analítica de producto.

## Aprendizaje federado (Federated Learning)
- Técnica de ML donde múltiples entidades **entrenan un modelo colaborativamente**
  manteniendo los datos **descentralizados** (no se centralizan).
- Característica clave: **heterogeneidad de datos** (los datos de cada cliente
  no son i.i.d.). El modelo se envía a los clientes; solo se comparten
  gradientes/pesos, no datos crudos.

## Otras PETs
- **Cifrado homomórfico:** computar sobre datos cifrados sin descifrar.
- **Anonimización / k-anonimato / sintéticos:** reducir re-identificación.
- **Secure multi-party computation (MPC).**

## Implicaciones
- Habilidad clave para cumplir [dominio/proteccion-de-datos](dominio/proteccion-de-datos.md)
  y [dominio/criptografia](dominio/criptografia.md) en analítica e IA.
- Habilita colaboración de datos entre empresas / con reguladores sin exponer PII.

## Referencias cruzadas
- [dominio/proteccion-de-datos](dominio/proteccion-de-datos.md).
- [dominio/criptografia](dominio/criptografia.md).
- [dominio/ciencia-de-datos](dominio/ciencia-de-datos.md).
- [rol/head-of-information-security](rol/head-of-information-security.md).
