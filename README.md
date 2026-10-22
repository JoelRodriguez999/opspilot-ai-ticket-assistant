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

## Menú de uso

Al ejecutar el programa se muestran tres opciones:

1. Crear ticket: solicita los datos, calcula la prioridad y guarda el incidente.
2. Consultar historial: muestra los tickets guardados en el archivo JSON.
3. Buscar ticket por ID: solicita el identificador y muestra el ticket encontrado.
4. Salir: finaliza el programa.

Las opciones inválidas se rechazan y se vuelve a solicitar una opción.
Después de crear un ticket o consultar el historial, se muestra nuevamente el menú.

Se verificó la creación de un tercer ticket desde el menú,
la conservación de los dos anteriores, la consulta del historial
y la salida del programa.

## Identificación y fecha de los tickets

Cada nuevo ticket incluye:

- `id`: identificador generado mediante UUID4.
- `fecha_creacion`: fecha y hora en formato ISO 8601, con la zona horaria del equipo.

Estos campos se guardan en el archivo JSON y se muestran al consultar
el historial. Los tickets anteriores siguen siendo compatibles,
aunque no contienen identificador ni fecha de creación.

Se verificó la creación y consulta de un ticket con los nuevos campos,
conservando los tres registros anteriores.

## Búsqueda por ID

Permite consultar un ticket mediante su identificador completo.
Si no existe una coincidencia, muestra un mensaje y regresa al menú.

Los registros antiguos sin ID se omiten durante la búsqueda y siguen
disponibles en la consulta del historial.

Se comprobó la búsqueda de un ticket existente y de un identificador
inexistente, sin errores al recorrer los registros antiguos.

## Autor

Joel Rodríguez  
GitHub: [JoelRodriguez999](https://github.com/JoelRodriguez999)
