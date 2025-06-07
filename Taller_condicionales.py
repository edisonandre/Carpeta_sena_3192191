#1. Verifica si un número es positivo, negativo o cero.
n = int(input("ingrese un numero que necesite saber su valor "))
if n >= 1:
    print("es positivo")
elif n <= 0:
    print("es negativo")
elif n == 0:
    print("es cero")
else:
    print("error")

#2. Calcula el mayor de dos números ingresados.
n2 = int(input("ingrese un numero "))
n3 = int(input("ingrese el segundo numero "))

if n2 > n3:
    print("es mayor ", n2)
elif n2 < n3:
    print("es menor ", n3)
else:
    print("ERROR")

# 3 Determina si un número es par o impar.
print("sistema para saber si es par o impar ")
n4 = int(input("ingrese un numero "))

if n4 % 2 == 0:
    print("es par")
elif n4 % 2 != 0:
    print("es impar")
else:
    print("EEROE")
    
# Dado un número, verifica si está entre 10 y 20.
print("sistema para saber si el numero esta entre 10 y 20 ")
n5 = int(input("Ingrese un número para verificar si está entre 10 y 20: "))

if 10 <= n5 <= 20:
    print("El número está entre 10 y 20.")
else:
    print("El número NO está entre 10 y 20.")
    
# Dados tres números, encuentra el mayor usando condicionales.
# Pedimos al usuario que ingrese tres números
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
num3 = int(input("Ingresa el tercer número: "))

# Usamos condicionales para encontrar el mayor
if num1 >= num2 and num1 >= num3:
    mayor = num1
elif num2 >= num1 and num2 >= num3:
    mayor = num2
else:
    mayor = num3

print("El número mayor es:", mayor)

#6 Calcula el precio final con un 10% de descuento si el total es mayor a $100.
print("Se quiere saber que la suma del precio del producto es mayor de $100 para hacer el descuento")
precio = int(input("ingrese el valor del producto "))
if precio >= 100:
    resul = (precio * 10) / 100  #calculo para sacar el porcentaje
    print("el precio final si se puede hacer el cuento del 10% ", resul)
else:
    print("no se puede hacer el descuento es menor de $100")

#7 erifica si una persona puede votar (mayor o igual a 18 años).
print("Se quiere saber si es mayor de edad para votar")
persona = int(input("ingrese la edad "))
if persona >= 18:
    print("puede votar!")
else:
    print("no puede votar")
    
#8 Dado el precio y tipo de cliente (VIP o normal), aplica un descuento del 20% solo a VIP
precio1 = int(input("ingrese el precio "))  # el precio que tiene que pagar normal
tipo_cliente = input("Que tipo de cliente eres VIP o normal ").upper   # el tipo para saber si es vip

if tipo_cliente == "VIP":
    result = (precio1 * 20) / 100  #calculo para hacar el porcentaje
    print("Eres 'VIP' tienes descuente del 20% ", result, "tienes que pagar")
else:
    print("tienes que pagar el precio normal cliente ", precio, "tienes que pagar")

#9. Determina si un número es múltiplo de 5 y de 3 al mismo tiempo.
# Pedimos al usuario que ingrese un número
numero = int(input("Ingresa un número: "))

# Verificamos si es múltiplo de 5 y de 3
if numero % 5 == 0 and numero % 3 == 0:  # sentencia para saber si el numero es multiplo 5 o 3
    print("El número es múltiplo de 5 y de 3 al mismo tiempo.")
else:
    print("El número NO es múltiplo de 5 y de 3 al mismo tiempo.")

# 10 Dado un número, verifica si es divisible entre dos números dados.
# Ingresamos los tres números
numero = int(input("Ingresa el número que deseas verificar: "))
divisor1 = int(input("Ingresa el primer divisor: "))
divisor2 = int(input("Ingresa el segundo divisor: "))

# Verificamos si es divisible entre ambos
if numero % divisor1 == 0 and numero % divisor2 == 0:
    print(f"{numero} es divisible entre {divisor1} y {divisor2}.")
else:
    print(f"{numero} NO es divisible entre {divisor1} y {divisor2}.")


""" EJERCICIOS CON LISTA (CON CONDICIONALES)"""
#11.Crea una lista con 5 números. Si el tercer número es mayor que 10, muestra “Mayor a 10”, si no, muestra “Menor o igual a 10”.
listt = [4,6,12,9,7]
if listt[2] > 10:
    print("Mayor a 10")
else:
    print("Menor o igual a 10")
    
#12 Verifica si el número 7 está en la lista [3, 5, 7, 9]. Si está, muestra “Está en la lista”, si no, muestra “No está en la lista”.
listt2 = [3, 5, 7, 9]
if 7 in listt2:
    print("Está en la lista")
else:
    print("No está en la lista")
    
#13 Suma los dos primeros elementos de la lista [4, 6, 2, 8]. Si la suma es mayor que 10, muestra “Suma alta”, de lo contrario, muestra “Suma baja”.
list1 = [4,6,2,8]
if list1[0] + list1[1] >= 10:
    print("Suma alta")
else:
    print("Suma baja")

#14. Dada la lista ["Ana", "Luis", "Pedro", "Marta"], muestra el último nombre. Si ese nombre es “Marta”, muestra “Nombre correcto”, si no, “Nombre diferente”.
list2 = ["Ana", "Luis", "Pedro", "Marta"]
if list2[3] == "Marta":
    print("Nombre correcto")
else:
    print("Nombre diferente")
    
#15.Crea una lista con tres colores. Cambia el segundo color solo si es igual a "azul", y muestra la lista actualizada.
llist = ["Naranja", "Rojo", "Azul"]
if "Azul" in llist:
    llist[2] = "Morado"
    print("La lista actualizada")
else:
    print("Sigues con el mismo color !COLOR NO ESTA EN LA LISTA¡ ", llist)
    

""" Ejercicios con Tuplas (con condicionales) """
#16.Crea una tupla con los valores (5, 8, 12, 20). Si el primer valor es menor que el último, muestra “Orden ascendente”, si no, “Orden descendente”.
tupla = (5,8,12,20)
if tupla[0] < tupla[3]:
    print("Orden ascendente")
else:
    print("Orden descendente")
    
#17.Dada la tupla (25, 32, 28), verifica si el segundo valor es mayor a 30. Si lo es, muestra “Edad mayor a 30”, si no, “Edad menor o igual a 30”.
tuplas = (25, 32, 28)
if tuplas[1] > 30:
    print("Edad mayor a 30")
else:
    print("Edad menor o igual a 30")

#18. Convierte la tupla (1, 2, 3) a lista, cambia el segundo valor a 10 solo si es igual a 2, luego vuelve a convertirla en tupla y muéstrala.
x = (1, 2 , 3)

if x[1] == 2:
    y = list(x)
    y[1] = 10
    print(y)
else:
    print("No es igual a 2")
    
#19. Dada la tupla (4, 9), accede al segundo valor. Si es mayor que 5, muestra “Coordenada alta”, si no, “Coordenada baja”.
tuplas1 = (4, 9)
if tuplas1 [1] > 5:
    print("Coordenadas alta")
else:
    print("Coordenadas baja")

#20. Compara si las tuplas (3, 4) y (3, 5) son iguales. Si lo son, muestra “Tuplas iguales”, si no, “Tuplas diferentes”.
tuplas3, tuplas4 = (3, 4), (3,5)
if tuplas3 == tuplas4:
    print("Tuplas iguales")
else:
    print("Tuplas diferentes")


""" Ejercicios con Diccionarios (con condicionales) """
#21. Crea un diccionario con {"nombre": "Juan", "edad": 17}. Si la edad es mayor o igual a 18, muestra “Adulto”, si no, muestra “Menor de edad”.
persona = {"nombre": "Juan", "edad": 17}
if persona["edad"] >= 18:
    print("Adulto")
else:
    print("Menor de edad")

#22. Crea un diccionario {"nombre": "Lucía", "edad": 20}. Si la edad es mayor a 18, cambia el valor de “edad” a 21. Luego muestra el diccionario.
dicionari = {"nombre": "Lucía", "edad": 20}
if dicionari["edad"] >= 18:
    x = dicionari["edad"] = 21
    print(dicionari)
else:
    print("Es menor")

#23.Crea un diccionario con {"nombre": "Carlos"}. Si la clave “ciudad” no existe, agrégala con el valor “Bogotá” y muestra el diccionario.
dicionary = {"nombre": "Carlos"}
if dicionary == ["ciudad"]:
    print(dicionary)
else:
    dicionary.update({"color": "red"})
    print(dicionary)
    
#24. Dado el diccionario {"producto": "pan", "precio": 1200}, verifica si la clave “precio” existe. Si existe, muestra su valor, si no, muestra “No hay precio”.
