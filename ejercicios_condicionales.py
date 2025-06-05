"""  Ejercicio 1

    programa de condicon 
    para saber si es apto para creditos
    
    si se cumple las condiciones segun edades
    """

# print("SISTEMA CREDITICIA A/D\n")
# n = input("ingrese su nombre")
# m = int(input("ingrese su edad"))

# if m >= 18:
#     print("Eres apto para hacer el credito")
#     c = int(input("Cual es la cantidad del credito"))
#     print("El senor ", n, " va hacer el credito con la cantidada de ",c)
# else:
#     print("No es apto para una vida crediticia")


# print("SISTEMA DE PAGOS SEGUN LA EDAD")
# años = int(input("ingrese la edad"))
# if años == 0 and años <= 4:
#     print("entra gratis")
# elif años >= 5 and años <= 18:
#     print("paga 5 euros")
# elif años >= 19:
#     print("paga 18 euros")
# else:
#     print("fin programa")

print("CALCULADORA")
print("""
    SUMA ---- S
    RESTA ---- R
    MULTIPLICACION ---- M
    DIVICION --- D \n
    """)
num = int(input("ingrese el primer numero"))
num2 = int(input("ingrese el segundo numero"))

operacion = input("ingrese la opcion que necesites").upper()
if operacion == "S":
    resul = num + num2
    print("El resultado de la suma que elegiste fue de ", resul)
elif operacion == "R":
    resul = num - num2
    print("El resultado de la resta que elegiste fue de ", resul)
elif operacion == "M":
    resul = num * num2
    print("El resultado de la multiplicacion que elegiste fue de ", resul)
elif operacion == "D":
    resul = num / num2
    print("El resultado de la divicion que elegiste fue de ", resul)
else:
    print("no esta en el rango de operaciones")
