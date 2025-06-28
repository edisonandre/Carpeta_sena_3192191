i = 1

while i <= 100:
    print("contador: ", i)
    i -= 1

contador = int(input("ingrese"))
while contador > 0:
    print(f"contador:, {contador}")
    contador -= 1
    break
print("termino el contador") 

while True:
    texto = input("Escribe algo (o escribe salir para terminar): ")
    if texto == "salir":
        break
    print("Escribiste: ", texto)


contador = 1
while contador <= 100:
    print(f"contador {contador} \n")
    contador += 1
    
print()
contador1 = int(input("ingrese un numero "))
while contador1 > 0:
    print(f"contador: {contador1}")
    contador1 -= 1
    print("Termino el contador")  
while True:
    texto = input("escribe algo (o escribe 'salir' para terminar)")
    if texto == "salir":
        print("salio de programa")
        break  
num = 4
while num > 0:
    print(f"{num}")
    num -= 1
    print("Termino el conteo")  
numero = int(input("ingresa la tabla de multiplicar "))
contador = 1

while contador <= 10:
    resultado = numero * contador
    print(f"{numero} * {contador} = {resultado}")
    contador += 1

clave = input("Escribe la contraseña ")
while clave != "python123":
    print("contraseña incorrecta \n")
    clave = input("intenta de nuevo ")
print("Acceso concedido")


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
    
numero = 1
while numero <= 10:
    if numero % 2 == 0:
        print(f"{numero} es par")
    else:
        print(f"{numero} es impar")
    numero += 1