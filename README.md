## Estudiante
Joel Antonio Jaquez López
## Carné
23369

# Hoja de Trabajo No. 9 - Algoritmo de Dijkstra y Grafos

Este proyecto es una implementación en Python del algoritmo de Dijkstra para encontrar la ruta más corta en un grafo que representa un sistema de rutas de transporte.

## Descripción

El programa utiliza la biblioteca `networkx` para crear y manipular grafos y `matplotlib` para visualizarlos. Las rutas se leen desde un archivo de texto `Rutas.txt`, que contiene las estaciones de origen y destino junto con los costos de viaje entre ellas. El algoritmo de Dijkstra se utiliza para calcular la ruta más corta y el costo mínimo desde una estación de origen especificada hasta todas las demás estaciones en el grafo.

## Funciones

- `crear_grafo_desde_archivo`: Lee el archivo de rutas y construye el grafo.
- `dijkstra_rutas`: Calcula las rutas más cortas desde una estación de origen hasta todas las demás estaciones utilizando el algoritmo de Dijkstra.
- `mostrar_grafo`: Visualiza el grafo utilizando `matplotlib`, destacando las rutas más cortas.
- `pedir_estacion_origen`: Pide al usuario que ingrese la estación de origen.
- `pedir_accion`: Pide al usuario que elija entre mostrar las rutas más cortas, visualizar el grafo o salir del programa.
- `iniciar_programa`: Controla el flujo principal del programa, permitiendo al usuario hacer varias búsquedas y visualizaciones antes de decidir salir.

## Uso

Para ejecutar el programa, simplemente ejecute el script `main.py` con Python:

```bash
python main.

