# Angel Janvier Gonzalez Delgado
# 1er Examen Parcial - Laboratorio de Estructura de Datos

# 12 de Octubre del 2024

# El departamento de personal de una escuela tiene registros del nombre, sexo y edad de cada uno de los profesores adscritos ahí.
#  Escriba un programa que calcule e imprima los siguientes datos:

#           a) Edad promedio del grupo de profesores.
#           b) Nombre del profesor más joven del grupo.
#           e) Nombre del profesor de más edad.
#           d) Número de profesoras con edad mayor al promedio.
#           e) Número de profesores con edad menor al promedio.

profesores = [
    
    {"nombre": "Carlos Humberto Espino Salinas", "sexo": "M", "edad": 25},
    {"nombre": "Jorge Alejandro Morgan Benita", "sexo": "M", "edad": 45},
    {"nombre": "Julieta G. Rodriguez Ruiz", "sexo": "F", "edad": 26},
    {"nombre": "Oscar Armando Veruete Macias", "sexo": "M", "edad": 38},
    
]

def calcular_datos_profesores(profesores):
    
    total_edades = sum([prof['edad'] for prof in profesores])
    promedio = total_edades / len(profesores)
    
    
    prof_joven = min(profesores, key=lambda x: x['edad'])
    prof_mayor = max(profesores, key=lambda x: x['edad'])
    
    
    profesoras_mayor_promedio = len([prof for prof in profesores if prof['sexo'] == 'F' and prof['edad'] > promedio])
    profesores_menor_promedio = len([prof for prof in profesores if prof['sexo'] == 'M' and prof['edad'] < promedio])
    
    return promedio, prof_joven, prof_mayor, profesoras_mayor_promedio, profesores_menor_promedio

promedio, joven, mayor, f_mayor, m_menor = calcular_datos_profesores(profesores)

print(f"Edad promedio: {promedio}")
print(f"Profesor más joven: {joven['nombre']}")
print(f"Profesor de mayor edad: {mayor['nombre']}")
print(f"Profesoras con edad mayor al promedio: {f_mayor}")
print(f"Profesores con edad menor al promedio: {m_menor}")

# este programa no se explica su funcionamiento es claro