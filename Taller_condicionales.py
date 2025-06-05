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
print("sistema para saber cual de los 3 numeros es el mayor")
nu = int(input("ingrese un numero "))
nu1 = int(input("ingrese el segundo numero "))
nu2 = int(input("ingrese el tercer numero "))

if nu > nu1:
    print("el primer numero es mayor ",nu)
elif nu1 > nu2:
    print("el segundo numero es mayor ", nu1)
elif nu2 > nu:
    print("el tercer numero es mayor ", nu2)
else:
    print("ERROR")