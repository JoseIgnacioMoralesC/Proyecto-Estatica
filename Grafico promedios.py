import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Valores de carga en N
cargas = np.array([1.96, 3.916, 5.87, 7.82, 9.78])

# Promedios de la tension experimental. 
tensiones = np.array([2.5394, 5.1028, 7.6010, 10.2252, 12.7429])

# Porcentaje de error del promedio
error = np.array([0.50, 0.37, 0.33, 0.56, 0.25])

# Ajuste de la regresión lineal
modelo = LinearRegression()
modelo.fit(cargas.reshape(-1, 1), tensiones)
y_pred = modelo.predict(cargas.reshape(-1, 1))

# Coeficiente de determinación R^2
r2 = r2_score(tensiones, y_pred)

# Coeficientes de la regresión
coeficiente = modelo.coef_[0]
intercepto = modelo.intercept_

# Crear el gráfico con intervalo de incertidumbre
plt.errorbar(cargas, tensiones, yerr=error, fmt='o', capsize=5)
plt.plot(cargas, y_pred, label=f'Regresión: T = {coeficiente:.2f}W + {intercepto:.2f}', marker='o', linestyle='-', color='blue', markersize = 2)
plt.xlabel('Carga W (N)')
plt.ylabel('Tensión T (N)')

# Agregar leyenda para R^2
plt.text(2.5, 11.8, f'$R^2$ = {r2:.2f}', ha='center', fontsize=11, bbox=dict(facecolor='white', alpha=0.5))

plt.legend()
plt.grid()
plt.show()
