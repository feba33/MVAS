---
titulo: Frontend — Frameworks y optimización de rendimiento
capa: dominio
tema: computacion
fuente: https://midrocket.com/en/guides/best-frontend-frameworks/
fuente2: https://dev.to/_d7eb1c1703182e3ce1782/react-vs-vue-vs-svelte-choosing-the-right-frontend-framework-in-2026-24fk
fecha: 2026-07-10
confianza: alta
tags: [frontend, react, vue, svelte, angular, astro, nextjs, rendimiento, spa, ssr, metaframework]
english_keywords: [frontend, React, Vue, Svelte, Angular, Astro, Next.js, SSR, SSG, performance, hydration, meta-framework]
---

# Frontend — Frameworks y optimización de rendimiento

## 📝 Conocimiento
El ecosistema frontend evoluciona rápido; en 2026 cinco frameworks dominan el mercado
profesional: **React, Vue, Astro, Next.js y Svelte**. La elección correcta depende del
contexto (tipo de proyecto, equipo y requisitos), no de la popularidad.

### Frameworks principales (2026)
- **React** — estándar de industria (JSX, componentes). Ecosistema enorme (React Router,
  Zustand, TanStack Query), mayor base de talento. React 19 trajo Server Components y
  Server Actions estables, difuminando cliente/servidor. No incluye routing/SSR/data
  fetching solo: requiere un *meta-framework* (Next.js, Remix).
- **Vue** — equilibrio entre potencia y simplicidad. Options API (suave) o Composition API.
  TypeScript decente (v3+). Meta-framework: **Nuxt**.
- **Svelte / SvelteKit** — compila a JS sin runtime virtual DOM (~2KB gz); excelente
  rendimiento y DX. Ecosistema pequeño pero creciente.
- **Angular** — completo y opinado (TypeScript nativo, RxJS); fuerte en enterprise.
- **Astro** — *peak performance* con cero JS por defecto (islas de islas / islands
  architecture); ideal para contenido/marketing.

### Meta-frameworks
Next.js (React listo para producción: SSR/SSG, App Router, RSC), Nuxt (Vue), SvelteKit,
Remix. Resuelven routing, SSR/SSG, data fetching e hidratación que el framework base
solo no cubre.

### Rendimiento (core)
- **Tamaño de bundle**: React+ReactDOM ~40KB gz, Vue ~23KB gz, Svelte ~2KB gz (sin runtime).
- **Hidratación parcial / islands**: solo el JS necesario en la interacción.
- **Core Web Vitals**: LCP (carga), INP (interactividad), CLS (estabilidad visual).
- **SSR/SSG vs CSR**: render en servidor mejora TTI y SEO; SSG para contenido estático.
- **Code-splitting, lazy loading, tree-shaking** y caching para reducir JS enviado.

### Tabla de decisión
| Framework | Curva | Bundle | Rendimiento | Ecosistema | Mejor para |
|---|---|---|---|---|---|
| React | moderada (JSX/hooks) | grande | bueno | enorme | equipos grandes, enterprise, empleabilidad |
| Vue | suave/moderada | medio | bueno | grande | equipos que buscan DX equilibrada |
| Svelte | suave | pequeño | excelente | pequeño | rendimiento crítico, apps pequeñas |
| Angular | empinada | grande | bueno | enterprise | apps corporativas grandes |
| Astro | suave | mínimo | excelente | medio | contenido/marketing, sitios estáticos |

## 🔗 Referencia
- [arquitectura](arquitectura.md) — decisiones de estructura que el frontend consume.
- [estilos-arquitectura](estilos-arquitectura.md) — SPAs y micro-frontends sobre microservicios.
- [testing-qa](testing-qa.md) — testing de componentes UI (unit/e2e).
- [plataforma-sre](plataforma-sre.md) — CI/CD y observabilidad del despliegue frontend.
- Fuentes: Midrocket (Best frontend frameworks 2026), DEV.to (React vs Vue vs Svelte 2026),
  Coderio (guide 2026), Pharos Production (comparison 2026) — reference-only.
