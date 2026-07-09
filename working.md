# MVAS — Working Log del Bucle de Enriquecimiento (investigación web)

> **ARCHIVO DE REANUDACIÓN.** Cualquier LLM puede leer este archivo y continuar el
> bucle sin contexto previo. Contiene el **prompt maestro**, el **plan**, la **cola
> de temas** y el **estado**. Para reanudar: lee TODO este archivo, busca el primer
> tema `pending` en la cola, ejecuta **UNA iteración** (investigar → ingerir →
> actualizar este archivo → commit), y deja el archivo actualizado para la siguiente.

## PROMPT MAESTRO (qué hacer)
Enriquecer MVAS con conocimiento real extraído de la web, **hasta que el usuario
digite `/stop`**. Cubrir tres capas siguiendo estas guías:

### Guías por capa
- **Sustrato:** legalidad, normas, marcos legales, derecho corporativo, noticias,
  etc. Sobre **México, EE.UU.** y otros países del hemisferio (o los que consideres
  relevantes).
- **Dominio:** libros y material académico, estrategias, herramientas, conocimiento,
  insights — **todo conocimiento valioso**.
- **Rol:** roles y capacidades comunes en el **sector tecnología**, en todos los
  departamentos y útiles en varios giros (consultoras, startups, producto, etc.).
  Haz **web scraping de descripciones de trabajo** y generaliza; también Reddit, o
  donde puedas. IE: *growth lead, product lead*. La idea: que un LLM pueda entrar a
  estas entidades y **operar efectivamente**.

### Reglas de ingest (MVAS)
- Aplica `protocolo-discriminamiento.md`: **infiere la entidad destino SIN que el
  usuario la diga**. En modo autónomo (bucle), si la certeza es baja, elige la más
  probable y márcala **INFERIDA** en el log; no pidas confirmación.
- **Raw = cita:** para fuentes web/scraping **NO** guardes el documento en `raw/`;
  cita la **URL en el frontmatter `fuente`** de la página. (Optimización aprobada por
  el usuario — ver `esquema.md` / `GUIA-HERMES.md`.)
- Crea la página en el nodo entidad: `<capa>/<entidad>/<slug>.md` con YAML frontmatter
  (`titulo`, `capa`, `tema`, `fuente:<url>`, `fecha`, `confianza`, `tags`).
- Resumen condensado (3-6 bullets) + contexto. Cross-refs con rutas relativas.
- Actualiza `<nodo>/index.md` y `<nodo>/log.md`. Si el nodo no existe, **créalo con
  su superstructura** (`raw/`, `index.md`, `log.md`, `README`) según `esquema.md` y
  añade entrada al `index.md` raíz.
- **DEDUPE:** si el tema/slug ya existe, OMITE o amplía; no dupliques.
- Sigue `GUIA-HERMES.md` y el skill `mvas-knowledge-base`.

### Pasos de UNA iteración
1. Entorno:
   ```
   export PATH=/opt/data/bin:$PATH HOME=/opt/data GH_CONFIG_DIR=/opt/data/.config/gh
   git config --global user.email "hermes@nousresearch.com" 2>/dev/null
   git config --global user.name "Hermes" 2>/dev/null
   gh auth setup-git 2>/dev/null || true
   cd /opt/data/MVAS 2>/dev/null || { gh auth setup-git; git clone https://github.com/feba33/MVAS.git /opt/data/MVAS; cd /opt/data/MVAS; }
   git pull --ff-only 2>/dev/null || true
   ```
2. Lee este `working.md`; elige el **primer tema `pending`** de la cola.
3. Investiga en la web (browser / curl / python): fuentes autorizadas (Wikipedia,
   Investopedia, docs oficiales, job boards, Reddit, libros/académico).
4. Condensa y escribe la(s) página(s) en el nodo inferido.
5. Actualiza `index.md`/`log.md` del nodo **+ este `working.md`** (marca `done`,
   añade al log, incrementa `iteración`).
6. `git add -A && git commit -m "mv: ingest <tema> en <entidad>" && git push`.
7. Termina. El scheduler vuelve a llamar para la siguiente iteración.

## ESTADO
- **Iteración actual:** 0
- **Última ejecución:** 2026-07-09 (creación del working.md)
- **Temas completados:** 0 / 41

## COLA DE TEMAS (pending / done)
### Sustrato
- [ ] Marco societario México — Ley General de Sociedades Mercantiles
- [ ] Régimen fiscal México — ISR, IVA, RESICO
- [ ] Derecho laboral México — LFT, outsourcing (Ley 50/2021)
- [ ] Protección de datos México — LFPDPPP
- [ ] Competencia económica México — COFECE
- [ ] Delaware General Corporation Law (EE.UU.)
- [ ] LLC / estructuras EE.UU.
- [ ] Impuestos federales EE.UU. — IRS
- [ ] Employment law EE.UU. — at-will, FLSA
- [ ] IP / Copyright / Patent EE.UU.
- [ ] Derecho corporativo Canadá / Brasil (hemisferio)
- [ ] Noticias recientes regulación fintech México/US
### Dominio
- [ ] Finanzas — instrumentos financieros (bonos, acciones, derivados)
- [ ] Finanzas — valoración (DCF, múltiplos)
- [ ] Finanzas — libros clave (The Intelligent Investor, Principles)
- [ ] Computación — paradigmas y lenguajes
- [ ] Computación — arquitectura de software / patrones
- [ ] Computación — DevOps / CI-CD / cloud
- [ ] Marketing — 4Ps, growth hacking, SEO/SEM
- [ ] Leyes — ramas del derecho / contratos
- [ ] Contabilidad — NIIF / US GAAP
- [ ] Diseño — Design Thinking / UX research
### Rol
- [ ] growth lead — responsabilidades y skills (job descriptions)
- [ ] product lead / product manager
- [ ] engineering manager
- [ ] data lead / data scientist
- [ ] UX/UI lead
- [ ] marketing lead
- [ ] finance lead / controller
- [ ] operations lead
- [ ] agile coach / scrum master

## LOG DE ITERACIONES
_(vacío hasta la iteración 1)_
