import random

# 1) Crear una lista con las notas de 10 estudiantes.
# • Mostrar la lista completa.
# • Calcular y mostrar el promedio.
# • Indicar la nota más alta y la más baja.

notas_de_estudiantes = [5.0, 4.5, 3.0, 2.5, 4.0, 7.2, 6.5, 8.0, 9.5, 10.0]
promedio = sum(notas_de_estudiantes) / len(notas_de_estudiantes)
nota_mas_alta = max(notas_de_estudiantes)
nota_mas_baja = min(notas_de_estudiantes)

print(f"Las notas de los estudiantes son: {notas_de_estudiantes}")
print(f"El el promedio de notas es: {promedio:.2f}")
print(f"La nota mas alta es: {nota_mas_alta}")
print(f"La nota mas baja es: {nota_mas_baja}")


# 2) Pedir al usuario que cargue 5 productos en una lista.
# • Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
# • Preguntar al usuario qué producto desea eliminar y actualizar la lista.

productos = []

for producto in range(5):
    producto = input("Ingrese un producto: ")
    productos.append(producto)

productos.sort()

print(f"Los productos cargados son: {productos}")

producto_a_eliminar = input("Desea eliminar un producto? ingrese el producto a eliminar, si quiere continuar con todos ingrese no: ")

if producto_a_eliminar.lower() == "no":
    mensaje = "Se guardaron los productos que ingreso"
    print(mensaje)
else:
    if producto_a_eliminar in productos:
        productos.remove(producto_a_eliminar)
        print(f"Producto '{producto_a_eliminar}' eliminado. Productos restantes: {productos}")
    else:
        print("No se encontro el producto.")

while True:
    producto_a_eliminar = input("Desea eliminar un producto? Ingrese el producto a eliminar, si quiere continuar con todos ingrese no: ")
    if producto_a_eliminar.lower() == "no":
        print("Se guardaron los productos que ingreso.")
        break
    elif producto_a_eliminar in productos:
        productos.remove(producto_a_eliminar)
        print(f"Producto '{producto_a_eliminar}' eliminado. Productos restantes: {productos}")
        break
    else:
        print("No se encontro el producto. Intente nuevamente o escriba 'no' para salir.")


# 3) Generar una lista con 15 números enteros al azar entre 1 y 100.
# • Crear una lista con los pares y otra con los impares.
# • Mostrar cuántos números tiene cada lista.

numeros_al_azar = [random.randint(1,100) for _ in range(15)]
numeros_pares = []
numeros_impares = []

for numero in numeros_al_azar:
    if numero % 2 == 0:
        numeros_pares.append(numero)
    elif numero % 2 == 1:
        numeros_impares.append(numero)

print(f"Cantidad de numeros pares: {len(numeros_pares)}")
print(f"Cantidad de numeros impares: {len(numeros_impares)}")


# 4) Dada una lista con valores repetidos:
# datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
# • Crear una nueva lista sin elementos repetidos.
# • Mostrar el resultado.

datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]

datos_sin_repetir = []

for dato in datos:
    if dato not in datos_sin_repetir:
        datos_sin_repetir.append(dato)

print(f"La nueva lista de datos es: {datos_sin_repetir}")

# 5) Crear una lista con los nombres de 8 estudiantes presentes en clase.
# • Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
# • Mostrar la lista final actualizada.

estudiantes_presentes = ["Jose", "Marcos", "Maria", "Daniela", "Alejandro", "Leonel", "Matias", "Juan"]

while True:
    opcion = input("Agregar alumno: 1\nEliminar alumno: 2\nDejar la lista sin cambios: 0\nIngrese una opcion: ")
    if not opcion.isdigit():
        print("Por favor, ingrese solo 1, 2 o 0.")
        continue
    agregar_o_eliminar_estudiante = int(opcion)

    if agregar_o_eliminar_estudiante == 1:
        agregar = input("Ingrese el nombre del estudiante: ")
        estudiantes_presentes.append(agregar)
    elif agregar_o_eliminar_estudiante == 2:
        while True:
            eliminar = input("Ingrese el nombre del estudiante a eliminar (o escriba 'cancelar' para volver): ")
            if eliminar == "cancelar":
                break
            if eliminar in estudiantes_presentes:
                estudiantes_presentes.remove(eliminar)
                break
            else:
                print("No se encontro el estudiante, intente nuevamente.")
    elif agregar_o_eliminar_estudiante == 0:
        print(f"La lista de estudiantes presentes es: {estudiantes_presentes}")
        break


# 6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el último pasa a ser el primero).

numeros = [1, 2, 3 ,4 ,5 ,6 ,7]
print(f"Lista de numeros: {numeros}")

ultimo_numero = numeros[-1]

for numero in range(len(numeros) -1, 0, -1):
    numeros[numero] = numeros[numero - 1]

numeros[0] = ultimo_numero

print(f"Lista rotada hacia la derecha: {numeros}")


# 7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una semana.
# • Calcular el promedio de las mínimas y el de las máximas.
# • Mostrar en qué día se registró la mayor amplitud térmica.

temperaturas = [
    [22, 21, 25, 21, 14, 18, 17],
    [14, 16, 17, 12, 10, 8, 8]
]

dias_de_la_semana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

promedio_minimas = sum(temperaturas[0]) / len(temperaturas[0])
promedio_maximas = sum(temperaturas[1]) / len(temperaturas[1])
mayor_amplitud = None
dia_de_mayor_amplitud = None

for i in range(len(temperaturas[0])):
    amplitud = abs(temperaturas[0][i] - temperaturas[1][i])
    if (mayor_amplitud is None) or (amplitud > mayor_amplitud):
        mayor_amplitud = amplitud
        dia_de_mayor_amplitud = i



print(f"Promedio de temperaturas minimas: {promedio_minimas:.1f}")
print(f"Promedio de temperaturas maximas: {promedio_maximas:.1f}")
print(f"La mayor amplitud termica fue de: {mayor_amplitud} el dia {dias_de_la_semana[dia_de_mayor_amplitud]}")


# 8) Crear una matriz con las notas de 5 estudiantes en 3 materias.
# • Mostrar el promedio de cada estudiante.
# • Mostrar el promedio de cada materia.

notas = [
    [3, 8, 6, 2, 9],
    [6, 8 ,4, 1, 10],
    [5, 7, 6, 4, 8]
]

for estudiante in range(len(notas[0])):
    suma = 0
    for materia in range (len(notas)):
        suma += notas[materia][estudiante]
    promedio = suma / len(notas)
    print(f"El promedio del estudiante es {estudiante + 1} es {promedio:.2f}")

for materia in range(len(notas)):
    suma = 0
    for estudiante in range(len(notas[0])):
        suma += notas[materia][estudiante]
        promedio = suma / len(notas[0])
    print(f"El promedio de la materia {materia + 1} es: {promedio:.2f}")


# 9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
# • Inicializarlo con guiones "-" representando casillas vacías.
# • Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
# • Mostrar el tablero después de cada jugada.

tablero = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

jugador = "X"
for turno in range(9):
    for fila in tablero:
        print(" ".join(fila))
    print()
    print(f"Turno del jugador {jugador}")
    fila = int(input("Ingrese la fila (0, 1 o 2): "))
    columna = int(input("Ingrese la columna (0, 1 o 2): "))
    if tablero[fila][columna] == "-":
        tablero[fila][columna] = jugador
        if jugador == "X":
            jugador = "O"
        else:
            jugador = "X"
    else:
        print("Esa casilla ya esta ocupada. Intente de nuevo.")
        turno -= 1

for fila in tablero:
    print(" ".join(fila))
print("Fin del juego!")


# 10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
# • Mostrar el total vendido por cada producto.
# • Mostrar el día con mayores ventas totales.
# • Indicar cuál fue el producto más vendido en la semana.

ventas = [
    [10, 12, 8, 15, 9, 11, 13],
    [7, 9, 12, 10, 8, 14, 11],
    [14, 11, 10, 13, 12, 9, 8],
    [9, 10, 11, 12, 13, 14, 15]
]

for producto in range(len(ventas)):
    total = sum(ventas[producto])
    print(f"Total vendido del producto {producto + 1}: {total}")

mayor_ventas = 0
dia_mayor = 0
for dia in range(7):
    suma_dia = 0
    for prod in range(4):
        suma_dia += ventas[prod][dia]
    if suma_dia > mayor_ventas:
        mayor_ventas = suma_dia
        dia_mayor = dia
print(f"El dia con mayores ventas totales fue el día {dia_mayor + 1} con {mayor_ventas} ventas.")

mayor_producto = 0
indice_producto = 0
for producto in range(len(ventas)):
    total = sum(ventas[producto])
    if total > mayor_producto:
        mayor_producto = total
        indice_producto = producto
print(f"El producto mas vendido en la semana fue el producto {indice_producto + 1} con {mayor_producto} ventas.")


