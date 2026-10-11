# OpsPilot: AI-Assisted IT Incident Triage

OpsPilot es un proyecto de laboratorio orientado a la clasificación y análisis inicial de incidentes de tecnología mediante Python e inteligencia artificial.

## Problema

Las mesas de servicio reciben incidentes con información incompleta, diferentes niveles de prioridad y descripciones poco estructuradas. Esto puede retrasar el diagnóstico y el escalamiento.

## Objetivo inicial

Construir una aplicación capaz de:

- Recibir la descripción de un incidente.
- Organizar la información del ticket.
- Sugerir una categoría.
- Identificar información faltante.
- Recomendar preguntas iniciales de diagnóstico.
- Generar una respuesta estructurada para el usuario.

## Estado

Prototipo de consola funcional, basado en reglas. Todavía no incorpora IA.

## Funcionalidades actuales

- Registro de incidentes.
- Validación de descripciones vacías.
- Validación de impacto y urgencia.
- Normalización de opciones a minúsculas.
- Cálculo de prioridad mediante una matriz de nueve combinaciones.
- Presentación del ticket con su prioridad y estado.

## Ejecución en Windows

Desde la carpeta del proyecto, con el entorno virtual ya creado:

```powershell
.\.venv\Scripts\python.exe main.py
```
## Estructura del proyecto

- `main.py`: coordina el registro y muestra el ticket.
- `priority.py`: calcula la prioridad según impacto y urgencia.
- `validators.py`: solicita y valida la descripción, el impacto y la urgencia.
- `storage.py`: carga el historial y guarda nuevos tickets en un archivo JSON.

El programa funciona mediante reglas y todavía no incorpora IA.

## Comprobaciones realizadas

- Las nueve combinaciones de impacto y urgencia devuelven la prioridad esperada.
- El registro de incidentes funciona después de separar el código en módulos.

## Almacenamiento local

Los tickets se guardan en `tickets.json`, en la carpeta del proyecto.
El archivo se crea al guardar el primer ticket y cada nuevo registro
se añade al historial existente.

El historial permanece disponible después de cerrar el programa.
`tickets.json` está excluido de Git mediante `.gitignore`.

Se comprobó el guardado de dos tickets en ejecuciones distintas,
conservando ambos registros y sus prioridades.

## Autor

Joel Rodríguez  
GitHub: [JoelRodriguez999](https://github.com/JoelRodriguez999)
