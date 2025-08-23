# print("-------------------ejercicio 1------------------")
# #Escribe un programa que pida dos números al usuario y muestre la suma de ambos.
# num1, num2 = int(input("Ingrese el primer número: ")), int(input("Ingrese el segundo número: "))
# print("La suma de los dos números es:", num1 + num2)

# print("-------------------ejercicio 2------------------")
# #Escribe un programa que pida dos números y muestre la resta del primero menos el segundo.
# num1, num2 = int(input("Ingrese el primer número: ")), int(input("Ingrese el segundo número: "))
# print("La suma de los dos números es:", num1 - num2)

# print("-------------------ejercicio 3------------------")
# #3. Escribe un programa que multiplique dos números ingresados por el usuario.
# num1, num2 = int(input("Ingrese el primer número: ")), int(input("Ingrese el segundo número: "))
# print("La suma de los dos números es:", num1 * num2)

# print("-------------------ejercicio 4------------------")
# #4. Escribe un programa que divida dos números ingresados por el usuario y muestre el resultado.
# num1, num2 = int(input("Ingrese el primer número: ")), int(input("Ingrese el segundo número: "))
# print("La suma de los dos números es:", num1 / num2)

# print("-------------------ejercicio 5------------------")
# #5. Pide al usuario su nombre y apellido por separado, y muestra un saludo con el nombre completo.
# nombre, apellido = input("Ingrese su nombre "), input("Ingrese su apellido ")
# print("buenos dias señor", nombre + " " + apellido)

# print("-------------------ejercicio 6------------------")
# #Escribe un programa que pida al usuario su nombre y muestre solo la primera letra.
# print("La primera letra de su nombre es:", input("Ingrese su nombre: ")[0])

# print("-------------------ejercicio 7------------------")
# #7. Escribe un programa que pida una palabra y muestre su última letra.
# print("la ultima letra de su nombre es:", input("Ingrese su nombre: ")[-1])

# print("-------------------ejercicio 8------------------")
# #Escribe un programa que calcule el área de un rectángulo pidiendo la base y la altura al usuario.
# base, altura = float(input("ingrese la base del rectangulo: ")), float(input("ingrese la altura del rectangulo "))
# print("el area del rectangulo es:", base * altura)

# print("-------------------ejercicio 9------------------")
# #Pide al usuario su año de nacimiento y calcula su edad (usa 2025 como año actual).
# print("su edad a base de su año de naciento es: ",(2025 - int(input("ingrese su año de nacimiento: "))))

# print("-------------------ejercicio 10------------------")
# #10. Pide al usuario un nombre de usuario y un dominio, y genera una dirección de correo (ej: usuario@dominio).
# print("crear una direccion", input("ingrese su nombre de usuario ") + "@" +  input("crea un dominio para su direccion "))

# print("-------------------ejercicio 11------------------")
# #Pide al usuario su nombre y muestra cuántas letras tiene.
# nombre = input("ingrese su nombre: ")
# print("su nombre tiene", len(nombre), "letras")

# print("-------------------ejercicio 12------------------")
# #Pide dos palabras al usuario y muestra la combinación de ambas en una sola línea.
# palabra1, palabra2 = input("ingrese una palabra "), input("ingrese otra palabra ")
# print("la combinacion de la palabra fue:", palabra1 + " " + palabra2)

# print("-------------------ejercicio 13------------------")
# #Pide una palabra y muestra la segunda letra.
# print("la segunda letra de su nombre es:", input("ingrese una palabra: ")[1])

# print("-------------------ejercicio 14------------------")
# #Pide una palabra y muestra las tres primeras letras.
# print("las tres primeras letras de su nombre son:", input("ingrese una palabra: ")[0:3])

# print("-------------------ejercicio 15------------------")
# #Pide una palabra y muestra las letras en orden inverso.
# print("las tres primeras letras de su nombre son:", input("ingrese una palabra: ")[::-1])

# print("-------------------ejercicio 16------------------")
# #Pide dos números y muestra la suma, la resta, la multiplicación y la división en diferentes líneas.
# num1, num2 = int(input("Ingrese el primer número: ")), int(input("Ingrese el segundo número: "))
# print("la respuesta de las operacion son: ",num1 + num2)
# print("la respuesta de las operacion son: ",num1 - num2)
# print("la respuesta de las operacion son: ",num1 * num2)
# print("la respuesta de las operacion son: ",num1 / num2)

# print("--------------------ejercicio 17------------------")
# #Pide un número al usuario y muestra el doble de ese número.
# print("el doble de su numero es:", int(input("ingrese un numero: ")) * 2)

# print("--------------------ejercicio 18------------------")
# #Pide un número al usuario y muestra la mitad (división por 2).
# print("la mitad de su numero es:", int(input("ingrese un numero: ")) / 2)

# print("--------------------ejercicio 19------------------")
# #Pide una frase y muestra cuántos caracteres tiene.
# print("su frase tiene", len(input("ingrese una frase: ")), "caracteres")

# print("--------------------ejercicio 20------------------")
# #Pide al usuario una palabra y repítela 3 veces usando concatenación
# print("su palabra repetida 3 veces es:", input("ingrese una palabra: ") * 3)

# print("--------------------ejercicio 21------------------")
# #21.Pide al usuario su nombre y muestra las dos primeras y las dos últimas letras.
# letr = input("Ingrese su nombre: ")
# print("Las dos primeras y las dos últimas letras son:", letr[:2], letr[-2:])

# print("--------------------ejercicio 22------------------")
# #Pide una palabra y muestra la letra del medio (solo si tiene número impar de letras).
# print("palabra y muestra la letra del medio")
# palabra = input("escriba una palabra:")
# posicion_medio = len(palabra) 
# print("la letra de medio es:", palabra[posicion_medio // 2])

# print("--------------------ejercicio 23------------------")
# #pide una frase y muestra solo los primeros 10 caracteres.
# print("los diez primeros caracteres son:", input("ingrese una frase: ")[:11])

# print("--------------------ejercicio 24------------------")
# #Pide un número y muestra el resultado de elevarlo al cuadrado (sin usar potencias, solo multiplicación).
# num = int(input("ingrese un numero que quiera elevarlo al cuadrado "))
# print("el resultado del evelado al cuadrado es: ",num * num * num)

# print("--------------------ejercicio 25------------------")
# #Pide al usuario dos números y muestra cuál es el mayor (sin usar if, solo operaciones
# num1, num2 = int(input("Ingrese el primer número: ")), int(input("Ingrese el segundo número: "))
# mayor = ((num1 + num2) + (num1 - num2) * ((num1 - num2) >= 0)) // 2
# print("El número mayor es:", mayor)

# print("--------------------ejercicio 26------------------")
# #Pide al usuario su edad y muestra cuántos días ha vivido (aproximando 365 días por año).
# print("los dias que a vivido son: ", int(input("ingrese su edad ")) * 365)

# print("--------------------ejercicio 27------------------")
# #Pide al usuario una palabra y muestra cada letra por separado (una por línea
# palabra = input("Dime una palabra: ")
# for i in range(len(palabra)):
#     print(palabra[i])
    
# print("--------------------ejercicio 28------------------")
# #Pide una palabra y muestra si tiene más de 5 letras (usando solo operaciones de longitud y texto).
# print("si tiene mas de 5 letras", len(input("ingrese una palabra ")) > 5)

# print("--------------------ejercicio 29------------------")
# #pide un número y muestra su valor multiplicado por 10.
# print("El resultado es: ", int(input("Ingrese un numero: ")) * 10)

# print("--------------------ejercicio 30------------------")
# #Pide una palabra y muestra la palabra escrita dos veces, una en mayúsculas y otra en minúsculas (solo si el estudiante sabe usar métodos de string).
# palabra = input("ingrese una palabra")
# print("la palabra es minuscula ",palabra.lower())
# print("la palabra es mayuscula ", palabra.upper())
