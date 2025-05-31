nombre = input("ingrese su nombre ")
#el usuario ingresa la nota
nota1 = float(input("ingrese la nota 1: "))
nota2 = float(input("ingrese la nota 2: "))
nota3 = float(input("ingrese la nota 3: "))

#calculo de la nota final
nota_final = (nota1 * 0.20) + (nota2 * 0.30) + (nota3 * 0.50)

print("La nota final de", nombre, "fue" ,nota_final)

#condicionales si pasa o no
if nota_final >= 3.0:
    print("aprobo en año")
else:
    print("no aprobo el año")