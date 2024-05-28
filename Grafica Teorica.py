import matplotlib.pyplot as plt

# Valores específicos de masa W (en kg)
cargas_Wkg = [0.2, 0.4, 0.6, 0.8, 1]

# Valores de carga en N (newtons)
cargas_WN = [9.77744 * w for w in cargas_Wkg]

# Valores teoricos de tensión para cada carga W. 
tensionesCF_Teor = [1.3 * W for W in cargas_WN]


# Crear el gráfico. 
plt.plot(cargas_WN, tensionesCF_Teor, marker='o', linestyle='-', color='green', label = 'T = 1.3W')


# Bucle para colocar los valores en las curvas.
for i, tension in enumerate(tensionesCF_Teor):
    # Formatear el valor de tensión con coma para la separación decimal
    tension_formateada = "{:0.3f}".format(tension).replace('.', ',')

    # Colocar el texto en el gráfico
    offset = 0.1
    plt.text(cargas_WN[i]+offset, tension, tension_formateada, ha='left', va='top')

# Etiquetas y título. Descomentar segun sea necesario
plt.xlabel('Carga W (N)')
plt.ylabel('Tensión T (N)')
plt.legend()


# Muestra el gráfico
plt.grid()
plt.show()
