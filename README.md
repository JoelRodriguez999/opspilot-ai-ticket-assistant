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

## Autor

Joel Rodríguez  
GitHub: [JoelRodriguez999](https://github.com/JoelRodriguez999)
