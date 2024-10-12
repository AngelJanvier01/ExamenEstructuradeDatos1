# Angel Janvier Gonzalez Delgado
# 1er Examen Parcial - Laboratorio de Estructura de Datos

# 12 de Octubre del 2024

# Dado un arreglo unidimensional de números enteros, ordenados crecientemente, escriba un
# programa que elimine todos los elementos repetidos. Considere que, de haber valores repetidos,
# éstos se encontrarán en posiciones consecutivas del arreglo.

def eliminar_repetidos(arr):
    
    return list(set(arr))

arreglo = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 7, 8, 8, 8, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13,]
print(eliminar_repetidos(arreglo))

# def eliminar_repetidos(arr) define una función llamada 
# eliminar_repetidos que toma un argumento, arr, que es una lista de números enteros.


# return list(set(arr)) devuelve una nueva lista que se crea 
# al convertir la lista de entrada arr a un set (eliminando los elementos duplicados),
# y luego convertir el set de nuevo a una lista.