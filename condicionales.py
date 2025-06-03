"""los operadores relacionales en python son

operador     nombre               ejemplo            significado
   <       menor que               5<4         5 es menor que 4
   >       mayor que               7>4         7 es mayor que 4
   ==      igual a                 4==4        4 es igual a 4
   !=      no igual a (diferente)  4!=5        4 no es igual a 5
   <=      menor o igual           6<=6        6 es menor o igual a 6
   >=      mayor o igual           9>=5        9 es mayor o igual a 5

operadores logicos

operador logico               simbolo
conjucion                       and
"""



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

gen = int(input("ingrese el año de nacimiento para saber la generacion "))
if gen > 1920 and gen < 1940:
    print("Generacion Silenciosa")
elif gen > 1941 and gen < 1964:
    print("Boby Boomer")
elif gen > 1965 and gen < 1979:
    print("Generacion x")
elif gen > 1980 and gen < 2000:
    print("Generacion Y")
elif gen > 2001 and gen < 2010:
    print("generacion Z")
elif gen > 2011 and gen < 2024:
    print("Generacion alfa")
elif gen > 2025:
    print("Generacion Beta")
else:
    print("es muy joven o ya no existe")