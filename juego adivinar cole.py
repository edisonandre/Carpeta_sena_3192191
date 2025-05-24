print("esto es un juego de adivinanza para saber un resultado final")
print("sigan las instruciones y con el paso vas mirando si el resuldado da igual")

# Solicitar un número al usuario
num1 = int(input("Ingrese un número: "))

# Verificar la primera condición
if num1 > 999:
    # Verificar la segunda condición
    if num1 <= 9999:
        igual = num1 + 19998
        print(f"el juego predice  que el resultado será ", igual, " ahora ingrese el segundo numero de 4 cifras")
    else:
        print("El número ingresado no cumple la condición.")
else:
    print("El número ingresado es menor o igual a 999.")

num2 = int(input("ingrese el segundo numero "))
# verificar la primera condicion
if num2 > 999:
    #verificar la segunda condicion
    if num2 <= 9999:
        num3 = 9999 - num2
        print("el juego elige el numero ", num3)
    else:
        print("El numero ingresado no cumple la condicion.")
else:
    print("El número ingresado es menor o igual a 999.")

num4 = int(input("ingrese el otro numero "))
#verificar la primera condicion
if num4 > 999:
    #verificar la segunda condicion
    if num4 <= 9999:
        num5 = 9999 - num4
        print("el juego elige el numero ", num3)
    else:
        print("El numero ingresado no cumple la condicion.")
else:
    print("El número ingresado es menor o igual a 999.")

final = num1 + num2 + num3 + num4 + num5
print(f"el numero adivinado fue ", igual, " y el resultado final es ",final)











