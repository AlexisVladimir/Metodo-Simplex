# Datos de entrada
c = [-3, -5]  # Coeficientes de la función objetivo
A = [
    [1, 0],   # Coeficientes de la primera restricción
    [0, 2],   # Coeficientes de la segunda restricción
    [3, 2]   # Coeficientes de la tercera restricción
]
d = [
    [1, 0, 0],  # Coeficientes de las variables de holgura (primera restricción)
    [0, 1, 0],  # Coeficientes de las variables de holgura (segunda restricción)
    [0, 0, 1]   # Coeficientes de las variables de holgura (tercera restricción)
]
b = [4, 12, 18]  # Lados derechos de las restricciones

# Construir la matriz simplex
matrixsimplex = []

# Fila de la función objetivo
fila_objetivo = c + [0] * len(d[0]) + [0]
matrixsimplex.append(fila_objetivo)

# Filas de las restricciones
for i in range(len(A)):
    fila = A[i] + d[i] + [b[i]]
    matrixsimplex.append(fila)

# Función para mostrar la matriz
def mostrar_matriz(matriz):
    for fila in matriz:
        print([f"{x:.2f}" for x in fila])

# Método simplex
iteracion = 1
while True:
    print(f"\n--- Iteración {iteracion} ---")
    print("Matriz simplex:")
    mostrar_matriz(matrixsimplex)

    # Paso 1: Identificar la columna pivote
    columna_pivote = -1
    min_valor = 0
    for j in range(len(matrixsimplex[0]) - 1):  # Ignorar la última columna (b)
        if matrixsimplex[0][j] < min_valor:
            min_valor = matrixsimplex[0][j]
            columna_pivote = j

    if columna_pivote == -1:
        print("\nNo hay coeficientes negativos en la función objetivo. Solución óptima encontrada.")
        break

    print("Columna pivote:", columna_pivote)

    # Paso 2: Identificar la fila pivote
    fila_pivote = -1
    min_razon = float('inf')
    for i in range(1, len(matrixsimplex)):  # Ignorar la fila de la función objetivo
        coeficiente = matrixsimplex[i][columna_pivote]
        if coeficiente > 0:
            razon = matrixsimplex[i][-1] / coeficiente
            if razon < min_razon:
                min_razon = razon
                fila_pivote = i

    if fila_pivote == -1:
        print("\nNo se encontró una fila pivote válida. El problema puede ser no acotado.")
        break

    print("Fila pivote:", fila_pivote)

    # Paso 3: Realizar la operación de pivoteo
    # Hacer que el coeficiente pivote sea 1
    pivote = matrixsimplex[fila_pivote][columna_pivote]
    for j in range(len(matrixsimplex[fila_pivote])):
        matrixsimplex[fila_pivote][j] /= pivote

    # Hacer que los demás coeficientes en la columna pivote sean 0
    for i in range(len(matrixsimplex)):
        if i != fila_pivote:
            factor = matrixsimplex[i][columna_pivote]
            for j in range(len(matrixsimplex[i])):
                matrixsimplex[i][j] -= factor * matrixsimplex[fila_pivote][j]

    iteracion += 1

# Mostrar la solución óptima
print("\n--- Solución óptima ---")
print("Matriz simplex final:")
mostrar_matriz(matrixsimplex)

# Extraer la solución
solucion = [0] * (len(matrixsimplex[0]) - 1)
for i in range(1, len(matrixsimplex)):
    for j in range(len(matrixsimplex[i]) - 1):
        if matrixsimplex[i][j] == 1:
            solucion[j] = matrixsimplex[i][-1]
            break

print("Solución óptima:")
for i, valor in enumerate(solucion):
    print(f"x{i+1} = {valor:.2f}")
print("Valor óptimo de la función objetivo:", matrixsimplex[0][-1])