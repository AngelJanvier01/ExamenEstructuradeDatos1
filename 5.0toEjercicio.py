# Angel Janvier Gonzalez Delgado
# 1er Examen Parcial - Laboratorio de Estructura de Datos

# 12 de Octubre del 2024

# En una escuela por cada alumno se tienen los siguientes datos:
#           • Nombre
#           • Matrícula
#           • Número de semestres cursados
#           • Calificación promedio por semestre

# Escriba un programa que, dada la información de N alumnos, pueda realizarsiguientes operaciones:
#           a) Listar nombre y matrícula de estudiantes con promedios generales mayores o iguales a 8.
#           b) Actualizar los campos que correspondan cuando un estudiante ha concluido un semestre.
#           e) Listar nombre y matrícula de estudiantes que hayan obtenido 9 o más de calificación en todos los semestres cursados hasta el momento.

alumnos = [
    {"nombre": "Pedro Martinez", "matricula": "123", "semestres": 4, "promedio": 9},
    {"nombre": "Jose Garcia", "matricula": "456", "semestres": 3, "promedio": 8.5},
    {"nombre": "Pancha Lopez", "matricula": "789", "semestres": 5, "promedio": 7.9},
    {"nombre": "Luis Perez", "matricula": "234", "semestres": 6, "promedio": 9.2},
    {"nombre": "Maria Hernandez", "matricula": "567", "semestres": 2, "promedio": 8.1},
    {"nombre": "Andrea Gutierrez", "matricula": "890", "semestres": 7, "promedio": 6.5},
    {"nombre": "Juan Gonzalez", "matricula": "345", "semestres": 1, "promedio": 7.0},
    {"nombre": "Sofia Ramirez", "matricula": "678", "semestres": 4, "promedio": 8.9},
    {"nombre": "Roberto Jimenez", "matricula": "901", "semestres": 2, "promedio": 6.8},
    {"nombre": "Carmen Torres", "matricula": "112", "semestres": 5, "promedio": 9.8},
    {"nombre": "Pablo Vargas", "matricula": "223", "semestres": 6, "promedio": 7.2},
    {"nombre": "Lucia Castillo", "matricula": "334", "semestres": 3, "promedio": 8.3},
    {"nombre": "Raul Mendoza", "matricula": "445", "semestres": 5, "promedio": 9.1}
]

def listar_alumnos_promedio(alumnos, min_promedio):
    
    return [alumno for alumno in alumnos if alumno["promedio"] >= min_promedio]

def actualizar_semestres(alumno_nombre):
    
    for alumno in alumnos:
        
        if alumno['nombre'] == alumno_nombre:
            
            alumno['semestres'] += 1
            print(f"Semestres actualizados para {alumno_nombre}: {alumno['semestres']}")

def listar_alumnos_promedio_9(alumnos):
    
    return [alumno for alumno in alumnos if alumno["promedio"] >= 9]

while True:
    
    print("\nOpciones:")
    print("1. Listar alumnos con promedio mayor o igual a un valor")
    print("2. Actualizar número de semestres de un alumno")
    print("3. Listar alumnos con promedio mayor o igual a 9")
    print("4. Salir")

    opcion = int(input("Elige una opción: "))
    
    if opcion == 1:
        
        min_promedio = float(input("Introduce el promedio mínimo: "))
        alumnos_listados = listar_alumnos_promedio(alumnos, min_promedio)
        print(f"Alumnos con promedio mayor o igual a {min_promedio}:")
        
        for alumno in alumnos_listados:
            
            print(f"Nombre: {alumno['nombre']}, Matrícula: {alumno['matricula']}, Promedio: {alumno['promedio']}")
    
    elif opcion == 2:
        
        nombre_alumno = input("Introduce el nombre del alumno para actualizar semestres: ")
        actualizar_semestres(nombre_alumno)
        
    
    elif opcion == 3:
        
        alumnos_listados = listar_alumnos_promedio_9(alumnos)
        print("Alumnos con promedio mayor o igual a 9:")
        
        for alumno in alumnos_listados:
            
            print(f"Nombre: {alumno['nombre']}, Matrícula: {alumno['matricula']}, Promedio: {alumno['promedio']}")
    
    elif opcion == 4:
        
        print("Saliendo del programa.")
        break
    
