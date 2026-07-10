---
titulo: Estilos arquitectónicos de software
capa: dominio
tema: computacion
fuente: https://en.wikipedia.org/wiki/Microservices
fuente2: https://en.wikipedia.org/wiki/Event-driven_architecture
fecha: 2026-07-10
confianza: alta
tags: [arquitectura, microservicios, event-driven, serverless, soa, estilos]
english_keywords: [architecture, microservices, event-driven, serverless, soa, software-styles]
---

# Estilos arquitectónicos de software

## 📝 Conocimiento
Los **estilos (o patrones) arquitectónicos** definen cómo se organiza un sistema en
componentes y cómo se comunican. La elección es, como toda decisión de arquitectura
([arquitectura](arquitectura.md)), un *trade-off*: no hay "mejor", solo adecuado al contexto.

### Monolito modular
Una sola unidad de despliegue dividida internamente en módulos bien delimitados
(límites claros, dependencias dirigidas). Simplicidad operativa; el desafío es evitar
el acoplamiento accidental. Punto de partida recomendado antes de distribuir.

### SOA (Arquitectura Orientada a Servicios)
Servicios reutilizables expuestos vía un bus de mensajería (ESB); énfasis en
interoperabilidad empresarial y contratos de servicio.

### Microservicios
Patrón que organiza la aplicación en una colección de **servicios poco acoplados y de
grano fino** que se comunican por **protocolos ligeros** (HTTP/REST, gRPC, mensajería)
— Wikipedia ([Microservices](https://en.wikipedia.org/wiki/Microservices)). Permite a los
equipos **desarrollar, desplegar y escalar servicios de forma independiente**, mejorando
modularidad, escalabilidad y adaptabilidad. A cambio introduce complejidad: sistemas
distribuidos, comunicación inter-servicio, consistencia y observabilidad — más difícil de
arrancar que un monolito.

### Event-driven (EDA)
Paradigma centrado en la **producción y detección de eventos**. Los componentes reaccionan
a eventos (pub/sub, event streaming con Kafka/Pulsar) en lugar de llamadas síncronas. Alta
**tolerancia a fallos, rendimiento y escalabilidad**, ideal para cargas complejas y dinámicas
— Wikipedia ([Event-driven architecture](https://en.wikipedia.org/wiki/Event-driven_architecture)).
Coste: complejidad e inherente dificultad para probar y trazar el flujo.

### Serverless
FaaS + servicios gestionados (ej. AWS Lambda); el proveedor gestiona escalado y servidores.
Pago por uso; *cold-start* y acoplamiento al proveedor como contras.

### Tabla de trade-offs
| Estilo | Acoplamiento | Escala | Complejidad op. | Mejor para |
|---|---|---|---|---|
| Monolito modular | alto interno | vertical | baja | MVPs, equipos pequeños |
| Microservicios | bajo | horizontal | alta | dominios grandes, muchos equipos |
| Event-driven | muy bajo (asínc.) | alta | alta | flujos reactivos, alta concurrencia |
| Serverless | n/a (efímero) | automática | media | cargas esporádicas, eventos |

## 🔗 Referencia
- [arquitectura](arquitectura.md) — base conceptual de arquitectura de software.
- [devops](devops.md) — CI/CD y despliegue de servicios.
- Fuentes: Microservices (Wikipedia, en) · Event-driven architecture (Wikipedia, en) — reference-only.
