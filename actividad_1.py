
print("Actividad de la lista")
# Pedimos 10 números al usuario
num1 = int(input("Ingrese un número entero: "))
num2 = int(input("Ingrese un número entero: "))
num3 = int(input("Ingrese un número entero: "))
num4 = int(input("Ingrese un número entero: "))
num5 = int(input("Ingrese un número entero: "))
num6 = int(input("Ingrese un número entero: "))
num7 = int(input("Ingrese un número entero: "))
num8 = int(input("Ingrese un número entero: "))
num9 = int(input("Ingrese un número entero: "))
num10 = int(input("Ingrese un número entero: "))
# Lista con los números
lista_1 = [num1, num2, num3, num4, num5, num6, num7, num8, num9, num10]
# Creamos tuplas con el número y su cuadrado
tupla1 = (num1, num1**2)
tupla2 = (num2, num2**2)
tupla3 = (num3, num3**2)
tupla4 = (num4, num4**2)
tupla5 = (num5, num5**2)
tupla6 = (num6, num6**2)
tupla7 = (num7, num7**2)
tupla8 = (num8, num8**2)
tupla9 = (num9, num9**2)
tupla10 = (num10, num10**2
# Lista de tuplas
lista_2 = [tupla1, tupla2, tupla3, tupla4, tupla5, tupla6, tupla7, tupla8, tupla9, tupla10]
# Imprimir la lista de tuplas
print("Lista de tuplas (número, cuadrado):")
print(lista_2
# Sumamos solo los primeros valores (los números originales)
suma = sum(lista_1)
promedio = suma // 10
doble = suma * 
print("Suma:", suma)
print("Promedio:", promedio)
print("Doble de la suma:", doble
print("---------- acceder a los elementos de un diccionario ----------")

dictionary = {"a": 1, 
            "e": 2
            }

print(f"clave a: {dictionary['a']}")
print(f"clave e: {dictionary['e']}")

dictionary = {"numbers": [18, 20, 28],
            "groups": {"a": 1, "b": 2}
            }

print(dictionary)
print(f"clave numbers: {dictionary['numbers']}")
print(f"clave groups: {dictionary['groups']}")

print(f"clave numbers: {dictionary['numbers'][1]}")
print(f"clave groups b: {dictionary['groups']['b']}")

print(dictionary,["z"])
