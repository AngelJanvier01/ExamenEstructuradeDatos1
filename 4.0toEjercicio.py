# Angel Janvier Gonzalez Delgado
# 1er Examen Parcial - Laboratorio de Estructura de Datos

# 12 de Octubre del 2024

# Una compañía almacena la información relacionada con sus proveedores en los siguientes arreglos:

# Cada Pi es el nombre del proveedor i. Este arreglo está ordenado alfabéticamente.

# Cada Ci representa el nombre de la ciudad en la que reside el proveedor i.

# Cada a¡ es el número de artículos diferentes que provee el proveedor i.

# Escriba un programa que pueda llevar a cabo las siguientes transacciones:

#       a. Dado el nombre de un proveedor, informar el nombre de la ciudad en la que reside y el
#       número de artículos que provee.

#       b. Actualizar el nombre de la ciudad, en caso de que un proveedor cambie de domicilio. Los
#       datos serán el nombre del proveedor y el nombre de la ciudad a la cual se mudó.

#       c. Actualizar el número de artículos, manejados por un proveedor para el caso de que éste
#       aumente o disminuya. Los datos serán el nombre del proveedor y la cantidad en la que
#       aumenta (+) o disminuye (-) el total de artículos que provee.

#       d. La compañía incorpora a un nuevo proveedor. Actualizar los arreglos sin alterar el orden
#       de PROVEEDORES. Los datos serán el nombre del proveedor, el nombre de la ciudad y el
#       total de artículos que provee.

#       e. La compañía da de baja a un proveedor. Actualizar los arreglos. El dato será el nombre
#       del proveedor.

proveedores = ["Zegucom", "JanvierShop", "Abasteo"]
ciudades = ["Aguascalientes", "Zacatecas", "Guadalajara"]
articulos = [2000, 853, 648548541]

def obtener_datos_proveedor(nombre):
    
    if nombre in proveedores:
        
        index = proveedores.index(nombre)
        return ciudades[index], articulos[index]
    
    else:
        
        return "Proveedor no encontrado"

def actualizar_ciudad(nombre, nueva_ciudad):
    
    if nombre in proveedores:
        
        index = proveedores.index(nombre)
        ciudades[index] = nueva_ciudad
        print(f"Ciudad actualizada para {nombre}: {nueva_ciudad}")
        
    else:
        
        print("Proveedor no encontrado")

def actualizar_articulos(nombre, cantidad):
    
    if nombre in proveedores:
        
        index = proveedores.index(nombre)
        articulos[index] += cantidad
        print(f"Artículos actualizados para {nombre}. Ahora tiene {articulos[index]} artículos.")
        
    else:
        
        print("Proveedor no encontrado")

def agregar_proveedor(nombre, ciudad, articulos_nuevos):
    
    proveedores.append(nombre)
    ciudades.append(ciudad)
    articulos.append(articulos_nuevos)
    print(f"Proveedor {nombre} agregado con {articulos_nuevos} artículos en {ciudad}.")

def eliminar_proveedor(nombre):
    
    if nombre in proveedores:
        
        index = proveedores.index(nombre)
        del proveedores[index]
        del ciudades[index]
        del articulos[index]
        print(f"Proveedor {nombre} eliminado.")
        
    else:
        
        print("Proveedor no encontrado")


while True:                 # Programa Principal
    print("\nOpciones: ")
    print("     1. Obtener datos de un proveedor")
    print("     2. Actualizar ciudad de un proveedor")
    print("     3. Actualizar cantidad de artículos de un proveedor")
    print("     4. Agregar un nuevo proveedor")
    print("     5. Eliminar un proveedor")
    print("     6. Salir")
    print(" ")
    
    opcion = int(input("Elige una opción: "))
    
    if opcion == 1:
        
        nombre = input("Introduce el nombre del proveedor: ")
        resultado = obtener_datos_proveedor(nombre)
        
        if resultado != "Proveedor no encontrado":
            
            ciudad, cantidad_articulos = resultado
            print(f"Proveedor {nombre} está en {ciudad} y provee {cantidad_articulos} artículos.")
            
        else:
            
            print(resultado)
    
    elif opcion == 2:
        
        nombre = input("Introduce el nombre del proveedor: ")
        nueva_ciudad = input(f"Introduce la nueva ciudad para {nombre}: ")
        actualizar_ciudad(nombre, nueva_ciudad)
    
    elif opcion == 3:
        
        nombre = input("Introduce el nombre del proveedor: ")
        cantidad = int(input("Introduce la cantidad de artículos para actualizar (puede ser negativa para disminuir): "))
        actualizar_articulos(nombre, cantidad)
    
    elif opcion == 4:
        
        nombre = input("Introduce el nombre del nuevo proveedor: ")
        ciudad = input(f"Introduce la ciudad para {nombre}: ")
        cantidad_articulos = int(input(f"Introduce la cantidad de artículos que provee {nombre}: "))
        agregar_proveedor(nombre, ciudad, cantidad_articulos)
    
    elif opcion == 5:
        
        nombre = input("Introduce el nombre del proveedor a eliminar: ")
        eliminar_proveedor(nombre)
    
    elif opcion == 6:
        
        print("Saliendo del programa.")
        break
    