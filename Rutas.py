import networkx as nx
import matplotlib.pyplot as plt

# Esta función lee un archivo de texto con información sobre rutas y crea un grafo con esos datos.
def crear_grafo_desde_archivo(nombre_archivo):
    grafo = nx.Graph() # Crea un grafo no dirigido.
    with open(nombre_archivo, 'r') as archivo: # Abre el archivo de rutas.
        for linea in archivo: # Itera sobre cada línea en el archivo.
            partes = linea.strip().split(',') # Divide la línea en partes separadas por comas.
            origen = partes[0].strip('" ') # Limpia y extrae la estación de origen.
            destino = partes[1].strip('" ') # Limpia y extrae la estación de destino.
            costo = int(partes[2].strip())  # Limpia y convierte el costo a entero.
            grafo.add_edge(origen, destino, weight=costo)
            grafo.add_edge(destino, origen, weight=costo)  # Agregar ruta simétrica
    return grafo # Retorna el grafo construido.

# Define la ruta al archivo de texto y crea el grafo a partir de este archivo.
nombre_archivo = 'Rutas.txt'
grafo = crear_grafo_desde_archivo(nombre_archivo)

# Imprime información básica del grafo para verificación.
print("Nodos del grafo:")
print(grafo.nodes())
print("Bordes del grafo:")
print(grafo.edges(data=True))

# Esta función utiliza el algoritmo de Dijkstra para encontrar la ruta más corta y su costo.
def dijkstra_rutas(grafo, origen):
    # Devuelve las rutas más cortas y sus costos desde el origen a todos los demás nodos en el grafo
    return nx.single_source_dijkstra(grafo, source=origen, weight='weight')

# Puedes cambiar esto por el punto de origen que desees
origen = 'Pueblo Paleta'
rutas, costos = dijkstra_rutas(grafo, origen)

print(f"Desde el origen '{origen}', las rutas más cortas a otros nodos son:")
for destino, ruta in rutas.items():
    print(f"{origen} -> {destino}: {ruta} con un costo de {costos[destino]}")


# Pide al usuario introducir la estación de origen.
def pedir_estacion_origen():
    return input("Por favor, introduce el nombre de la estación de origen: ")

# Pide al usuario elegir una acción a realizar.
def pedir_accion():
    print("\nOpciones:")
    print("1. Mostrar rutas más cortas desde la estación de origen.")
    print("2. Mostrar gráfico de rutas.")
    print("3. Salir.")
    return input("Elige una opción (1, 2 o 3): ")

# Función que dibuja el grafo con las rutas y costos utilizando matplotlib.
def mostrar_grafo(grafo, origen, rutas):
    pos = nx.spring_layout(grafo)  # Posición de los nodos en el grafo
    nx.draw(grafo, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue') # Dibuja los nodos, las aristas y etiquetas de nodos.
    
    # Dibujar todas las aristas del grafo
    nx.draw_networkx_edges(grafo, pos, edgelist=grafo.edges(), edge_color='gray')
    
    # Etiquetar las aristas con sus pesos
    edge_labels = dict([((u, v,), d['weight']) for u, v, d in grafo.edges(data=True)])
    nx.draw_networkx_edge_labels(grafo, pos, edge_labels=edge_labels)

    # Dibujar las rutas más cortas en rojo
    for destino, ruta in rutas.items():
        if destino != origen:
            if isinstance(ruta, list) and len(ruta) > 1:  # Verificar que ruta es una lista y tiene más de un nodo
                path_edges = list(zip(ruta[:-1], ruta[1:]))
                nx.draw_networkx_edges(grafo, pos, edgelist=path_edges, edge_color='red', width=2)

    plt.title(f'Rutas desde {origen}')
    plt.show()

# Esta es la función principal que inicia el flujo del programa
def iniciar_programa(grafo):
    while True:
        origen = pedir_estacion_origen()
        rutas, costos = dijkstra_rutas(grafo, origen)

        accion = pedir_accion()
        if accion == '1':
            print(f"\nDesde el origen '{origen}', las rutas más cortas a otros nodos son:")
            for destino, costo in costos.items():
                if destino != origen:  # Evitamos imprimir la ruta al mismo origen
                    print(f"{origen} -> {destino}: {costo} con una ruta de {rutas[destino]}")
        elif accion == '2':
            mostrar_grafo(grafo, origen, rutas)
        elif accion == '3':
            print("Saliendo del programa.")
            break  # Romper el bucle para salir del programa
        else:
            print("Opción no válida. Por favor, introduce 1 o 2.")

# Ahora, en lugar de definir 'origen' y llamar a dijkstra_rutas y mostrar_grafo directamente,
# llamamos a iniciar_programa para que maneje el flujo en base a las elecciones del usuario

# Ejecutamos el programa
nombre_archivo = 'Rutas.txt'
grafo = crear_grafo_desde_archivo(nombre_archivo)
iniciar_programa(grafo)
