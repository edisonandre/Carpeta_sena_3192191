edad = 30
if edad >= 18:
    print("es adulto")
else:
    print("es menor de edad")
    
a = 25
b = 50
if a > b and b > a: 
    print("Ambas condiciones son verdaderas")
    
numero = 24
if numero > 36:
    print("el numero es grande")
else:
    print("el numero de chico")

#ejemplos de condicionales aninadas
x = 25
if x > 10:
    print("por encima de diez")
    if x >20:
        print('y tambien por encima de 20')
    else:
        print("pero no por encima de 20")

a = 2 + 3
if a == 4:
    print("es igual a 4")
elif a == 5:
    print("es igual  a 5")
elif a == 6:
    print("es igual a 6")
else:
    print("ERROR el numero suma no aparece")
    
num1, num2 = int(input("ingrese un numero ")), int(input("ingrese un numero "))
print("el resultado debe ser 4 :D")
resul = num1 * num2
print("el resultado final es 4" if resul == 4 else "el resultado es diferente")