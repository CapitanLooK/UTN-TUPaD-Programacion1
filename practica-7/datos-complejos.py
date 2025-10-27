#1) Dado el diccionario precios_frutas
#precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
#Añadir las siguientes frutas con sus respectivos precios:
#● Naranja = 1200
#● Manzana = 1500
#● Pera = 2300
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300
print(precios_frutas)


#2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
#● Banana = 1330
#● Manzana = 1700
#● Melón = 2800
precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800
print(precios_frutas)


#3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los precios.
frutas = list(precios_frutas.keys())
print(frutas)


#4) Escribí un programa que permita almacenar y consultar números telefónicos.
#• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
#• Luego, pedí un nombre y mostrale el número asociado, si existe.
contactos = {}
for _ in range(5):
    nombre = input("Ingrese el nombre del contacto: ")
    numero = input("Ingrese el número telefonico: ")
    contactos[nombre] = numero
nombre_consulta = input("Ingrese el nombre del contacto a consultar: ")
if nombre_consulta in contactos:
    print(f"El numero de {nombre_consulta} es: {contactos[nombre_consulta]}")
else:
    print(f"No se encontro el contacto: {nombre_consulta}")


#5) Solicita al usuario una frase e imprime:
#• Las palabras únicas (usando un set).
#• Un diccionario con la cantidad de veces que aparece cada palabra.
frase = input("Ingrese una frase: ")
palabras = frase.split()
palabras_unicas = set(palabras)
print("Palabras unicas:", palabras_unicas)
contador_palabras = {palabra: palabras.count(palabra) for palabra in palabras_unicas}
print("Cantidad de veces que aparece cada palabra:", contador_palabras)

#6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. Luego, mostrá el promedio de cada alumno.
alumnos = {}
for _ in range(3):
    nombre = input("Ingrese el nombre del alumno: ")
    notas = tuple(float(input(f"Ingrese la nota {i+1} de {nombre}: ")) for i in range(3))
    alumnos[nombre] = notas

for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"El promedio de {nombre} es: {promedio}")


#7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:
#• Mostrá los que aprobaron ambos parciales.
#• Mostrá los que aprobaron solo uno de los dos.
#• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir)

aprobados_parcial_1 = {"Juan", "Ana", "Pedro"}
aprobados_parcial_2 = {"Ana", "Luis", "Carlos"}
print("Aprobados ambos parciales:", aprobados_parcial_1.intersection(aprobados_parcial_2))
print("Aprobados solo uno de los dos:", aprobados_parcial_1.symmetric_difference(aprobados_parcial_2))
print("Aprobados al menos un parcial:", aprobados_parcial_1.union(aprobados_parcial_2))


#8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. Permití al usuario:
#• Consultar el stock de un producto ingresado.
#• Agregar unidades al stock si el producto ya existe.
#• Agregar un nuevo producto si no existe.'
stock = {}
while True:
    accion = input("Ingrese 'consultar', 'agregar' o 'nuevo' para gestionar el stock (o 'salir' para terminar): ").lower()
    if accion == 'salir':
        break
    elif accion == 'consultar':
        producto = input("Ingrese el nombre del producto a consultar: ")
        print(f"El stock de {producto} es: {stock.get(producto, 0)}")
    elif accion == 'agregar':
        producto = input("Ingrese el nombre del producto a agregar stock: ")
        cantidad = int(input("Ingrese la cantidad a agregar: "))
        if producto in stock:
            stock[producto] += cantidad
        else:
            print(f"El producto {producto} no existe en el stock.")
    elif accion == 'nuevo':
        producto = input("Ingrese el nombre del nuevo producto: ")
        cantidad = int(input("Ingrese la cantidad inicial de stock: "))
        stock[producto] = cantidad
    else:
        print("Accion no reconocida. Intente nuevamente.")
print("Stock final:", stock)


# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos. Permití consultar qué actividad hay en cierto día y hora.
agenda = {}
while True:
    accion = input("Ingrese 'agregar' para añadir un evento o 'consultar' para buscar uno (o 'salir' para terminar): ").lower()
    if accion == 'salir':
        break
    elif accion == 'agregar':
        dia = input("Ingrese el dia del evento (formato: DD/MM): ")
        hora = input("Ingrese la hora del evento (formato: HH:MM): ")
        evento = input("Ingrese la descripción del evento: ")
        agenda[(dia, hora)] = evento
    elif accion == 'consultar':
        dia = input("Ingrese el dia a consultar (formato: DD/MM): ")
        hora = input("Ingrese la hora a consultar (formato: HH:MM): ")
        evento = agenda.get((dia, hora), "No hay eventos programados.")
        print(f"Evento para {dia} a las {hora}: {evento}")
    else:
        print("Accion no reconocida. Intente nuevamente.")


#10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde:
#• Las capitales sean las claves.
#• Los países sean los valores.
paises_y_capitales = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Chile": "Santiago"
}
capitales_y_paises = {capital: pais for pais, capital in paises_y_capitales.items()}
print("Diccionario de capitales y paises:", capitales_y_paises)