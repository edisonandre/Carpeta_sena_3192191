"""Ejercicios con while, condicionales y estructura"""

# 1 suma hasta cero
total = 0
contador = int(input("Ingrese un numero para sumar asta que ingrese un cero "))
while contador != 0:
    total += contador
    contador = int(input("ingrese otro numero \n"))
    print("Sumatoria de numeros ingresados ", total)
    
# 2 contraseña secreta
clave = input("Escribe la contraseña ")
while clave != "python123":   # estructura para contraseña
    print("contraseña incorrecta \n")
    clave = input("intenta de nuevo ")
print("Acceso concedido")

#3 lista de compras

lista = []
print("Escribir fin para dejar de ingresar productos")
producto = input("ingrese un producto: ")
while producto != "fin":
    lista.append(producto)
    producto = input("ingrese otro producto: ").lower()
    print(lista)

#4 contador de pares e impares
contador = 0
pares = 0
impares = 0
while contador <= 9:
    num = int(input(f"ingrese el numero {contador + 1}: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    contador += 1
print("cantidad de pares:", pares)
print("cantidad de impares", impares)

# 5 promedio de calificaciones
notas = []
while True:
    entrada = input("Ingrese una nota entre 0 y 5 (o escriba 'salir' para terminar): ")
    if entrada.lower() == "salir":
        break  # asta aqui se termino si se escribe salir
    nota = float(entrada)
    if nota >= 0 and nota <= 5:
        notas.append(nota)
    else:
        print("La nota debe estar entre 0 y 5.")

if notas: #esta  es cuando ya tiene nota y aparece el promedio
    promedio = sum(notas) / len(notas)
    print("El promedio de las notas es:", promedio)
else:
    print("No se ingresaron")
    
#6 tabla de multiplicar interativa
contar = "si"
while contar.lower()== "si":
    numero = int(input("Ingrese la tabla de multiplicar: "))
    contar = 1
    print (f"\ntabla del {numero}: \n")
    
    while contar <= 10:
        resultado = numero * contar
        print(f"{numero} * {contar} = {resultado}")
        contar += 1
    contar = input("\nDESEAS VER OTRA TABLA DE MULTIPLICAR (SI/NO)\n")
    
#7 Adivina el número secreto
numero_secreto = 17
intento = int(input("Adivina el número secreto: "))
while intento != numero_secreto:
    if intento < numero_secreto:
        print("El número es mayor.")
    else:
        print("El número es menor.")
    intento = int(input("Intenta de nuevo: "))
print("¡Felicidades! Adivinaste")

# 8 Tupla de frutas
frutas = ("manzana", "pera", "banano", "uva")
print("Adivina una fruta que esté en la tupla.")
adivinada = False

while not adivinada:
    intento = input("Escribe el nombre de una fruta: ").lower()
    if intento in frutas:
        print("¡Correcto! Esa fruta está en la tupla.")
        adivinada = True
    else:
        print("No está en la tupla, intenta de nuevo.")
        
#9 Diccionario de traducción
diccionario = {
    "gato": "cat",
    "perro": "dog",
    "casa": "house",
    "libro": "book",
    "manzana": "apple"
}

print("Escribe 'salir' para terminar.")
while True:
    palabra = input("Ingresa una palabra en español: ").lower()
    if palabra == "salir":
        break
    if palabra in diccionario:
        print(f"La traducción de '{palabra}' es: {diccionario[palabra]}")
    else:
        print("La palabra no está en el diccinario")
        
#10 Calculadora básica
while True:
    print("\nCalculadora básica")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    opcion = input("Elige una opción (1-5): ")

    if opcion == "5":
        print("¡Hasta luego!")
        break

    if opcion in ("1", "2", "3", "4"):
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))

        if opcion == "1":
            print("Resultado:", num1 + num2)
        elif opcion == "2":
            print("Resultado:", num1 - num2)
        elif opcion == "3":
            print("Resultado:", num1 * num2)
        elif opcion == "4":
            if num2 != 0:
                print("Resultado:", num1 / num2)
            else:
                print("No se puede dividir por cero.")
    else:
        print("Opción no válida. Intenta de nuevo.")
        
#11 Registro de edades
personas = {}

while True:
    nombre = input("Ingrese el nombre de la persona (o escriba 'salir' para terminar): ")
    if nombre.lower() == "salir":
        break
    edad = input("Ingrese la edad de la persona: ")
    personas[nombre] = edad

print("Diccionario de personas y edades:")
print(personas)

#12 Buscar en lista
colores = ["rojo", "azul", "verde", "amarillo", "negro"]
print("Adivina un color que esté en la lista.")

encontrado = False
while not encontrado:
    intento = input("Escribe un color: ").lower()
    if intento in colores:
        print("¡Correcto! Ese color está en la lista.")
        encontrado = True
    else:
        print("No está en la lista, intenta de nuevo.")
        
#13 Potencias de un número
numero = int(input("Ingresa un número para ver sus potencias del 1 al 5: "))
exponente = 1
while exponente <= 5:
    print(f"{numero}^{exponente} = {numero ** exponente}")
    exponente += 1
    
# 14 Lista de cuadrados
cuadrados = []
contador = 1
while contador <= 5:
    num = int(input(f"Ingrese el número {contador}: "))
    cuadrados.append(num ** 2)
    contador += 1

print("Lista de cuadrados:", cuadrados)

#15 Diccionario de estudiantes
estudiantes = {}

while True:
    nombre = input("Ingrese el nombre del estudiante (o escriba 'fin' para terminar): ")
    if nombre.lower() == "fin":
        break
    nota = float(input("Ingrese la nota final de ese estudiante: "))
    estudiantes[nombre] = nota

print("Diccionario de estudiantes y sus notas:")
print(estudiantes)