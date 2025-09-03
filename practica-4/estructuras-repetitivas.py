# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
for i in range(100+1):
    print(i)


# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.
valor = int(input("Ingrese un número entero: "))
cantidadDeDigitos = len(str(valor))
print(f"El numero {valor} tiene {cantidadDeDigitos} digitos.")


# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.
valor1 = int(input("Ingrese el primer valor: "))
valor2 = int(input("Ingrese el segundo valor: "))
suma = 0
for i in range(valor1, valor2 + 1):
    suma += i
print(f"La suma de los numeros entre {valor1} y {valor2} es: {suma}")


# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.
sumaEnSecuencia = 0
while True:
    valor = int(input("Ingrese un numero entero (0 para finalizar): "))
    if valor == 0:
        break
    sumaEnSecuencia += valor
print(f"La suma total es: {sumaEnSecuencia}")


# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
valor = int(input("Adivine el numero (entre 0 y 9): "))
contadorIntentos = 1
numeroReal = 6

while valor != numeroReal:
    valor = int(input("Intente nuevamente: "))
    contadorIntentos += 1

if contadorIntentos == 1:
    print(f"Felicidades, adivinaste el numero en {contadorIntentos} intento!")
else:
    print(f"Felicidades, adivinaste el numero en {contadorIntentos} intentos!")


# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.
for i in range(100, -1, -1):
    if i % 2 == 0:
        print(i)


# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.
valor = int(input("Ingrese un numero entero positivo: "))
suma = 0
for i in range(1, valor + 1):
    suma += i
print(f"La suma de los numeros entre 0 y {valor} es: {suma}")

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio).
cantidadDeIngresos = 100
numerosPares = 0
numerosImpares = 0
numerosNegativos = 0
numerosPositivos = 0

for _ in range(cantidadDeIngresos):
    numeroIngresado = int(input("Ingrese un numero entero: "))
    if numeroIngresado % 2 == 0:
        numerosPares += 1
    else:
        numerosImpares += 1
    if numeroIngresado > 0:
        numerosPositivos += 1
    elif numeroIngresado < 0:
        numerosNegativos += 1

print(f"De los {cantidadDeIngresos} numeros ingresados son:")
print(f"Pares: {numerosPares}")
print(f"Impares: {numerosImpares}")
print(f"Positivos: {numerosPositivos}")
print(f"Negativos: {numerosNegativos}")


# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor).
cantidadDeIngresos = 100
suma = 0

for _ in range(cantidadDeIngresos):
    numeroIngresado = int(input("Ingrese un numero entero: "))
    suma += numeroIngresado

media = suma / cantidadDeIngresos
print(f"La media de los {cantidadDeIngresos} numeros ingresados es: {media}")


# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
numero = int(input("Ingrese un numero entero: "))
numeroAString = str(numero)
numeroInvertidoAStr = numeroAString[::-1]
numeroInvertido = int(numeroInvertidoAStr)
print(f"El numero invertido es: {numeroInvertido}")