print("suma de dos numeros")
num = int(input("ingresar el primer numero "))
num1 = int(input("ingresar el segundo numero "))
resul = num + num1
print("el resultado de la suma es:", resul)
print("")
#resta
print("resta de dos numeros")
res1 = int(input("ingrese el primer numero: "))
res2 = int(input("ingrese el segundo numero: "))
res = res1 - res2
print("el resultado de la resta es: ", res)
print("")
#multiplicacion
print("multiplacion de dos numeros")
mul1 = int(input("ingrese el primer numero: "))
mul2 = int(input("ingrese el segundo numero: "))
mult = mul1 * mul2
print("resultado de la multiplicacion es: ", mult)
print("")
#division
div = int(input("ingrese el primer numero que quiera dividir: "))
div2 = int(input("ingrese el segundo numero que quiera dividir: "))
resul_div = div / div2
print("el resultado de la division fue: ", resul_div)
print("")
print("nombre y apellido y saludo")
nombre = input("Escriba su nombre ")
apellido = input("Escriba su apellido ")
print(f"buenos dias señor", nombre, apellido)
print("")
#primera letra del nombr
print("va aparecer la primera letra del nombre")
nom = input("ingrese su primer nombre: ")
print(nom[0])
#7 ultima letra
print("va aparecer la ultima letra del nombre")
nombr = input("ingrese su nombre")
print(nombr[-1])
#8 area
print("calcular area del rectangulo")
base = float("ingrese la base del rectangulo ")
altura = float("ingrese la altura del rectangulo ")
area = base * altura
print("la area del rectangulo fue de: ", area)
#9 año de nacimiento
año = int(input("ingrese su año de nacimiento "))
print("su edad a base de su año de naciento es: ",(2025 - año))
#10 direcion
print("crear una direccion")
nombre_usuario = input("ingrese su nombre de usuario ")
dominio = input("crea un dominio para su direccion ")
print(nombre_usuario + "@" +dominio)
#11 contador de letras
print("contador de letras de un nombre")
longitud = len(input("ingrese su nombre ")) #len se utiliza para contar los caracteres
print("tiene", longitud, "caracteres")
#2 combinacion
print("combinacion de dos palabras")
pal = input("ingrese una palabra ")
pal2 = input("ingrese otra palabra ")
print("la combinacion de la palabra fue:", pal, pal2)
#13 muestra la segunda letra
print("muetra la segunda letra de una palabra")
palabra = input("ingrese una palabra")
print(palabra[1])
#14 las tres letras
print("muestra las tres primeras letras")
letr = input("ungrese una palabra ")
print(letr[0:3])
#5 orden inverso
print("mostrara la palabra en orden inverso")
inv = input("ingrese una palabra")
palabra_inversa = inv[::-1]
print("la palabra inversa que ingreso es:", palabra_inversa)
#6 suma, resta, multiplicacion y division
num1 = int(input("ingrese un numero "))
num2 = int(input("ingrese el segundo numero "))
print("la respuesta de las operacion son: ",num1 + num2)
print("la respuesta de las operacion son: ",num1 - num2)
print("la respuesta de las operacion son: ",num1 * num2)
print("la respuesta de las operacion son: ",num1 / num2)
#7 doble de un numero
print("muestra el doble de un numero")
exp = int(input("ingrese un numero "))
print("el doble de ",exp ** 2) #se multiplica 2 veces a la ve
#18 divide la midad 2 de un numero
print("muestra la mitad de un numero")
mit = int(input("ingrese un numero "))
print("el doble de ",mit // 2) #se multiplica 2 veces a la ve
#19 contador de letras en frase
print("contador de letras de un nombre")
longitud = len(input("ingrese una frase")) #len se utiliza para contar los caracteres
print("tiene", longitud, "caracteres")
#20 concatenacion
print("palabra se va a repetir 3 veces")
texto1 = input("ingrese una palabra ")
texto1 = texto1 * 3
print(texto1)
#21 
print("muestra las 2 primeras letras y las 3 ultimas")
letr = input("ingrese su nombre:")
print(letr[0:2], letr[3:])
#22
print("palabra y muestra la letra del medio")
palabra = input("escriba una palabra:")
posicion_medio = len(palabra) 
print("la letra de medio es:", palabra[posicion_medio // 2])
#23
print("muestra las 10 primeras letras")
letr = input("ungrese una palabra ")
print(letr[0:11])
4 
num = int(input("ingrese un numero que quiera elevarlo al cuadrado"))
print("el resultado del evelado al cuadrado es: ",num ** 3)
5
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
print(f"El número mayor es: {(num1 + num2 + (num1 - num2)) // 2}")
#6 años vividos
print(f"Has vivido aproximadamente {int(input("Ingrese su edad: ")) * 365} días.")
#7
palabra = input("Dime una palabra: ")
i = len(palabra)
print(palabra[i])
#8
palabra = input("Ingrese una palabra: ")
print("Tiene más de 5 letras:", len(palabra) > 5)
#29
num = int(input("Ingrese un número: "))
print("El resultado es:", num * 10)
#30
string = input ("introduce un string:")
print(f"\n¿Todas las letras estan en minusculas? {string.islower()}")
string = string.lower()
print(f"string en minusculas: {string}")
print ("\n¿Todas las letras estan en mayusculas?:")
print (f"string en mayusculas: {string.upper()}")
print (f"string original: {string}")