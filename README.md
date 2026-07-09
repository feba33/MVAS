# MWAS

Base de conocimiento en capas con pipeline de **cuidado → mantenimiento → optimización → retrieval**.

## Arquitectura (capas)

| Capa | Carpeta | Función |
|------|---------|----------|
| Sustrato | `sustrato/` | Fuentes **crudas**: documentos, notas, datos originales. El suelo del conocimiento. |
| Dominio | `dominio/` | Conocimiento de **dominio** ya refinado: conceptos, reglas y materia específica. |
| Organización | `organización/` | Estructura, taxonomía, índices y metadatos que preparan el conocimiento para la recuperación. |
| Rol | `rol/` | **Perspectiva/persona**: cómo se entrega y adapta el conocimiento según quien lo consulta. |

Flujo: `sustrato → dominio → organización → rol`.

## Cómo cuidar y mantener
- **Ingesta:** todo entra crudo en `sustrato/`. No mezclar Dominio hasta refinar.
- **Refinamiento:** derivar de `sustrato/` a `dominio/` lo ya validado.
- **Organización:** etiquetar, indexar y deduplicar en `organización/`.
- **Servicio:** preparar vistas/adaptaciones por rol en `rol/`.

## Optimización y retrieval
- Mantener metadatos consistentes (fuente, fecha, tema).
- Indexar `organización/` para búsqueda y (opcional) embeddings.
- El retrieval lee de `organización/` + `rol/` según la consulta.

## Mantenimiento periódico
- Revisar `sustrato/` para limpiar duplicados y obsoletos.
- Actualizar índices en `organización/`.
- Verificar que `rol/` sigue alineado con quien consulta.
