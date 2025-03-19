# Método Simplex

Este proyecto implementa el método Simplex para resolver problemas de programación lineal. Contiene dos scripts principales:

1. **`simplex.py`**: Implementación manual del método Simplex para resolver un problema de programación lineal.
2. **`simplex2.py`**: Uso de la librería `scipy.optimize` para resolver un problema de programación lineal utilizando el método Simplex.

---

## Descripción del Proyecto

El método Simplex es un algoritmo ampliamente utilizado para resolver problemas de optimización lineal. Este proyecto muestra dos enfoques diferentes para implementar este método:

1. **Implementación manual (`simplex.py`)**: Se construye la matriz Simplex paso a paso y se realizan iteraciones para encontrar la solución óptima.
2. **Uso de librerías (`simplex2.py`)**: Se utiliza la función `linprog` de la librería `scipy.optimize` para resolver el problema de manera más eficiente.

---

## Requisitos

Para ejecutar este proyecto, necesitas tener instalado Python 3.x y las siguientes librerías:

- `numpy`
- `scipy`

Puedes instalar las dependencias necesarias ejecutando:

```bash
pip install numpy scipy
```
## Uso

### `simplex.py`

Este script resuelve un problema de programación lineal utilizando una implementación manual del método Simplex. El problema está definido por los siguientes datos:

- **Función objetivo**: Maximizar z=3x1+5x2z=3x1​+5x2​.
    
- **Restricciones**:
    
    - x1≤4x1​≤4
        
    - 2x2≤122x2​≤12
        
    - 3x1+2x2≤183x1​+2x2​≤18
        

Para ejecutar el script, simplemente corre:
```bash
python3 simplex.py
```

El script mostrará la matriz Simplex en cada iteración y la solución óptima al final.

### `simplex2.py`

Este script resuelve un problema de programación lineal utilizando la función `linprog` de la librería `scipy.optimize`. El problema está definido por los siguientes datos:

- **Función objetivo**: Maximizar z=300x1+400x2z=300x1​+400x2​.
    
- **Restricciones**:
	 -  3x1​+3x2​≤120
        
    - 3x1+6x2≤1803x1​+6x2​≤180
        
    - x1,x2≥0x1​,x2​≥0
        

Para ejecutar el script, corre:

```bash
python3 simplex2.py
```

El script mostrará la solución óptima y el valor máximo de la función objetivo.

---

## Estructura del Código
### `simplex.py`

1. **Datos de entrada**:
    
    - Coeficientes de la función objetivo (`c`).
        
    - Coeficientes de las restricciones (`A`).
        
    - Coeficientes de las variables de holgura (`d`).
        
    - Lados derechos de las restricciones (`b`).
        
2. **Matriz Simplex**:
    
    - Se construye la matriz Simplex a partir de los datos de entrada.
        
3. **Iteraciones**:
    
    - Se realizan iteraciones para encontrar la solución óptima.
        
    - En cada iteración, se identifica la columna y fila pivote, y se realiza la operación de pivoteo.
        
4. **Solución óptima**:
    
    - Se extrae la solución óptima de la matriz Simplex final.
        

### `simplex2.py`

1. **Datos de entrada**:
    
    - Coeficientes de la función objetivo (`c`).
        
    - Coeficientes de las restricciones (`A`).
        
    - Lados derechos de las restricciones (`b`).
        
    - Límites de las variables (`bounds`).
        
2. **Resolución**:
    
    - Se utiliza la función `linprog` de `scipy.optimize` para resolver el problema.
        
3. **Resultados**:
    
    - Se imprime la solución óptima y el valor máximo de la función objetivo.
        

---
## Resultados

Ambos scripts proporcionan la solución óptima para los problemas de programación lineal definidos. La implementación manual (`simplex.py`) es útil para comprender el funcionamiento interno del método Simplex, mientras que el uso de librerías (`simplex2.py`) es más eficiente y adecuado para problemas más grandes.

