# print("Sistema de calificacion")
# print("------------------------")
# print("""
#     Nivel de Calificacion
#     Superior = 5.0
#     alto = 4.0
#     basico = 3.0
#     bajo 1.0
#     """)
# nombre = input("ingrese su nombre ")

# print("a continuacion ingrese sus notas de ingles")
# nota1 = float(input("ingrese su primera nota "))
# nota2 = float(input("ingrese su segunda nota "))
# nota3 = float(input("ingrese su tercera nota "))

# result = (nota1 + nota2 + nota3) / 3

# print (f"la nota final de {nombre} fue {result}")

# print("ingrese las calificaciones de religion")
# nota4 = float(input("ingrese su primera nota "))
# nota5 = float(input("ingrese su segunda nota "))
# nota6 = float(input("ingrese su tercera nota "))

# result1 = (nota4 + nota5 + nota6) / 3

# print (f"la nota final de {nombre} fue {result1}")

# print("ingrese las calificaciones de filosofia")
# nota7 = float(input("ingrese su primera nota "))
# nota8 = float(input("ingrese su segunda nota "))
# nota9 = float(input("ingrese su tercera nota "))

# result6 = (nota7 + nota8 + nota9) / 3

# print (f"la nota final de {nombre} fue {result1}")

# print("ingrese las calificaciones de pensamiento logica")
# nota7 = float(input("ingrese su primera nota "))
# nota8 = float(input("ingrese su segunda nota "))
# nota9 = float(input("ingrese su tercera nota "))

# result2 = (nota7 + nota8 + nota9) / 3

# print (f"la nota final de {nombre} fue {result2}")

# print("ingrese las calificaciones de quimica")
# notav = float(input("ingrese su primera nota "))
# notab = float(input("ingrese su segunda nota "))
# notan = float(input("ingrese su tercera nota "))

# result3 = (notav + notab + notan) / 3

# print (f"la nota final de {nombre} fue {result3}")
# final = (result + result1 + result6 + result2 + result3) / 5
# print("la nota final fue", final,(final > 3.5))

# print("edades estudiantes 1 a 3")
# edad = ["6 años", "7 años", "8 años"]
# print("las edades de son: ", edad)

# edad.append(input("agregar otra edad"))
# print("los nuevos edades de los estudiantes de 1 a 3 son: ", edad)


# clientes = ['ana', 'CARLOS', 'beatriz', 'ANA', 'diana', 'carlos', 'ELENA']

# clientes.append('JULIANA')

# total_elementos = len(clientes)
# print(f"Total de elementos: {total_elementos}")

# nombre_menor = min(clientes)
# nombre_mayor = max(clientes)
# print(f"Nombre alfabéticamente menor: {nombre_menor}")
# print(f"Nombre alfabéticamente mayor: {nombre_mayor}")

# # Crear una lista ordenada para encontrar el nombre del medio
# lista_ordenada = (clientes)
# indice_medio = len(clientes) // 2
# nombre_medio = lista_ordenada[indice_medio]

# # Eliminar la primera aparición del nombre del medio
# clientes.remove(nombre_medio)
# print(f"Nombre eliminado (alfabéticamente en el medio): {nombre_medio}")

# nombres = ["ana", "carlos", "beatriz", "luis"]
# nombres_max = max(nombres)
# print(nombres_max)

# print("---------------------------")
# #index.() para encontrar la posicion de la primera aparicion
# nombres_indice = nombres.index("ana")
# print(nombres_indice)
numeros = [1, 2, 3, 2]
numeros.reverse()
numeros.remove(2)
numeros.reverse()

print(numeros)
