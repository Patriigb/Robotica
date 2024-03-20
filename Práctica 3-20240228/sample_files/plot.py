import matplotlib.pyplot as plt
import sys

"""
    This script is used to plot the results of a robot's movements
    arg1: log file to plot
    arg2: plot file
"""

# Leer el archivo y extraer los datos
timestamps = []
x_coords = []
y_coords = []

with open(sys.argv[1], 'r') as file:
    for line in file:
        parts = line.split()
        timestamps.append(float(parts[0]))
        x_coords.append(float(parts[1]))
        y_coords.append(float(parts[2]))

# Trazar el recorrido
plt.figure(figsize=(8, 6))
plt.plot(x_coords, y_coords, marker='o', linestyle='-')
plt.title('Recorrido del Robot')
plt.xlabel('Coordenada X')
plt.ylabel('Coordenada Y')
plt.grid(True)

# Hacer que las escalas de los ejes X e Y sean iguales
plt.axis('equal')

# Guardar el gráfico en un archivo
plot_file = sys.argv[2] 
plt.savefig(plot_file)  # Cambia el nombre del archivo según lo desees