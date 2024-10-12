# Angel Janvier Gonzalez Delgado
# 1er Examen Parcial - Laboratorio de Estructura de Datos

# 12 de Octubre del 2024

# Sean A(M x N) YB(N) arreglos de dos y una dimensión, respectivamente. Escribe. un programa
# que asigne valores a B, a partir de A, teniendo en cuenta los siguientes criterios:

# Si 𝑖  es impar, se realiza una suma simple de los elementos de la fila correspondiente
# Si 𝑖 es par, se multiplica el elemento actual de la fila 𝑖 con los correspondientes de la fila anterior (𝑖 − 1) y se suman esos productos.

def calcular_b(a):
    
    m, n = len(a), len(a[0])
    
    b = []
    
    for i in range(m):
        
        if i % 2 == 0:
            
            b_i = sum(a[i][j] for j in range(n))
            
        else:
            
            b_i = sum(a[i][j] * a[i-1][j] for j in range(n))
            
        b.append(b_i)
        
    return b


A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ]

print(calcular_b(A))

# es una función llamada calcular_b que toma una matriz bidimensional (2D array) a como entrada 
# y devuelve una matriz unidimensional b según los criterios especificados. Los criterios son que
# si el índice de fila i es par, debe sumar los elementos de la fila correspondiente. Si el índice
# de fila i es impar, debe multiplicar el elemento actual de la fila i con los correspondientes
# de la fila anterior (i - 1) y luego sumar esos productos.