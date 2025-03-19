import numpy as np
from scipy.optimize import linprog

# Coeficientes de la función objetivo (negados porque linprog minimiza por defecto)
c = [-300, -400]

# Coeficientes de las restricciones (matriz A)
A = [
    [3, 3],   # Coeficientes de la primera restricción
    [3, 6],   # Coeficientes de la segunda restricción
    [0, 0]   # Coeficientes de la tercera restricción
]

# Lados derechos de las restricciones (vector b)
b = [120, 180, 0]

# Límites de las variables (x1 >= 0, x2 >= 0)
bounds = [(0, None), (0, None)]

# Resolver el problema usando el método simplex
res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='simplex')

# Imprimir los resultados
if res.success:
    print("Solución óptima encontrada:")
    print(f"x1 = {res.x[0]}")
    print(f"x2 = {res.x[1]}")
    print(f"Valor máximo de z = {-res.fun}")  # Negamos el resultado porque minimizamos -z
else:
    print("No se encontró solución.")