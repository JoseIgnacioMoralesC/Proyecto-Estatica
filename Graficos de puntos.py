import matplotlib.pyplot as plt
import numpy as np

# Carga en N (repetidos para varios puntos de datos)
Cargas = np.array([1.96, 3.91, 5.87, 7.82, 9.78])

# Tensiones en N (diferentes valores para cada carga). Descomentar segun sea necesario

#BD
Tensiones = np.array([2.46, 2.35, 2.54, 2.69, 2.64, 2.44, 2.59, 2.49, 2.59, 2.49,
                      5.18, 5.28, 4.99, 5.08, 4.89, 5.38, 5.09, 5.21, 4.94, 4.99,
                      7.19, 7.82, 7.63, 7.82, 7.57, 7.58, 7.82, 7.77, 7.14, 7.68,
                      10.51, 10.21, 10.17, 10.38, 10.27, 10.32, 10.07, 10.18, 10.18, 9.97,
                      12.27, 12.86, 12.70, 12.56, 13.00, 12.72, 12.52, 12.68, 13.10, 13.01
                      ])


Cargas_expandidas = np.repeat(Cargas, 10)

# Crear el gráfico de puntos
plt.scatter(Cargas_expandidas, Tensiones,color='blue', edgecolors='black', linewidths=1, s=30)

# Añadir etiquetas
plt.xlabel('Carga W (N)')
plt.ylabel('Tensión T (N)')
plt.grid()

# Mostrar el gráfico
plt.show()
