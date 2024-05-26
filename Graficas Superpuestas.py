import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

#Valores de cada cara en N.
cargas = np.array([1.96, 3.91, 5.87, 7.82, 9.78])

# Valores teoricos de tension para cada carga en N
tensiones_Teor = np.array([2.54, 5.08, 7.63, 10.17, 12.71])

# Promedios experimentales de la tension para cada carga en N. 
tensiones_Exp = np.array([2.5394, 5.1028, 7.6010, 10.2252, 12.7429])

# Ajuste de la regresión lineal
modelo = LinearRegression()
modelo.fit(cargas.reshape(-1, 1), tensiones_Exp)
y_pred = modelo.predict(cargas.reshape(-1, 1))

# Coeficiente de determinación R^2
r2 = r2_score(tensiones_Exp, y_pred)

# Coeficientes de la regresión
coeficiente = modelo.coef_[0]
intercepto = modelo.intercept_

# Crear el gráfico teorico. 
plt.plot(cargas, tensiones_Teor, marker='o', linestyle='-', color='green', label='Datos Teoricos. Ecuación: T=1.3W')
plt.plot(cargas, y_pred, label=f'Datos Expermientales. Ecuación: T = {coeficiente:.2f}W + {intercepto:.2f}', marker='o', linestyle='-', color='blue', alpha=0.6)
plt.xlabel('Carga W (N)')
plt.ylabel('Tensión T (N)')

# Agregar leyenda para R^2
plt.text(2.5, 11, f'$R^2$ = {r2:.2f}', ha='center', fontsize=11, bbox=dict(facecolor='white', alpha=0.5))

plt.legend()
plt.grid()
plt.show()
    

