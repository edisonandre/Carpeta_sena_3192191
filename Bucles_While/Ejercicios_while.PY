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
