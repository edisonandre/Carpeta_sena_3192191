#Taller: Registro simple de producto y cálculo de costos

nombre = input("Ingrese el nombre del producto: ")
precio_unitario = float(input("Ingrese el precio unitario: "))
cantidad = int(input("Ingrese la cantidad comprada: "))

producto_info = (nombre, precio_unitario)
producto_lista = [producto_info, cantidad]
producto_dict = {
    "producto": producto_lista
}

costo_total = producto_info[1] * cantidad
print("\n--- Detalles de la compra ---")
print("Nombre del producto:", producto_info[0])
print("Precio unitario:", producto_info[1])
print("Cantidad comprada:", cantidad)
print("Costo total: $", costo_total)

#Taller #2: Factura de múltiples productos (versión fija sin bucles)

nombre1 = input("Ingrese el nombre del primer producto: ")
precio1 = float(input("Ingrese el precio unitario del primer producto: "))
cantidad1 = int(input("Ingrese la cantidad comprada del primer producto: "))
producto1 = [(nombre1, precio1), cantidad1]

nombre2 = input("\nIngrese el nombre del segundo producto: ")
precio2 = float(input("Ingrese el precio unitario del segundo producto: "))
cantidad2 = int(input("Ingrese la cantidad comprada del segundo producto: "))
producto2 = [(nombre2, precio2), cantidad2]

nombre3 = input("\nIngrese el nombre del tercer producto: ")
precio3 = float(input("Ingrese el precio unitario del tercer producto: "))
cantidad3 = int(input("Ingrese la cantidad comprada del tercer producto: "))
producto3 = [(nombre3, precio3), cantidad3]

factura = {
    "producto1": producto1,
    "producto2": producto2,
    "producto3": producto3
}

total1 = precio1 * cantidad1
total2 = precio2 * cantidad2
total3 = precio3 * cantidad3

total_general = total1 + total2 + total3
print("\n--- FACTURA DE COMPRA ---")
print(f"1. {nombre1} - ${precio1} x {cantidad1} = ${total1}")
print(f"2. {nombre2} - ${precio2} x {cantidad2} = ${total2}")
print(f"3. {nombre3} - ${precio3} x {cantidad3} = ${total3}")
print("----------------------------")
print(f"TOTAL A PAGAR: ${total_general}")

#Taller #3: Registro de notas de un estudiante
print()
nombre_estudiante = input("Ingrese el nombre del estudiante: ")  #nombre del estudiante

# Asignatura 1
materia1 = input("Ingrese el nombre de la primera asignatura: ")
nota1_1 = float(input(f"Ingrese la primera nota de {materia1}: "))
nota1_2 = float(input(f"Ingrese la segunda nota de {materia1}: "))
prom1 = (nota1_1 + nota1_2) / 2
datos1 = [(materia1, prom1), nota1_1, nota1_2]

# Asignatura 2
materia2 = input("Ingrese el nombre de la segunda asignatura: ")
nota2_1 = float(input(f"Ingrese la primera nota de {materia2}: "))
nota2_2 = float(input(f"Ingrese la segunda nota de {materia2}: "))
prom2 = (nota2_1 + nota2_2) / 2
datos2 = [(materia2, prom2), nota2_1, nota2_2]

# Asignatura 3
materia3 = input("Ingrese el nombre de la tercera asignatura: ")
nota3_1 = float(input(f"Ingrese la primera nota de {materia3}: "))
nota3_2 = float(input(f"Ingrese la segunda nota de {materia3}: "))
prom3 = (nota3_1 + nota3_2) / 2
datos3 = [(materia3, prom3), nota3_1, nota3_2] #lista 

materias = [datos1, datos2, datos3]

#espacio de almacenamiento de diccionario y guarda informacion
boletin = {
    "nombre": nombre_estudiante,
    "materias": materias
}

promedio_final = (prom1 + prom2 + prom3) / 3

print("======= BOLETÍN DE CALIFICACIONES =======")
print(f"Estudiante: {boletin['nombre']}")
print("-----------------------------------------")

#boletin 1 y coordenadas
m1 = boletin["materias"][0]
print(f"Asignatura: {m1[0][0]}")
print(f"  Nota 1: {m1[1]}")
print(f"  Nota 2: {m1[2]}")
print(f"  Promedio: {m1[0][1]}")
print("-----------------------------------------")

m2 = boletin["materias"][1]
print(f"Asignatura: {m2[0][0]}")
print(f"  Nota 1: {m2[1]}")
print(f"  Nota 2: {m2[2]}")
print(f"  Promedio: {m2[0][1]}")
print("-----------------------------------------")

m3 = boletin["materias"][2]
print(f"Asignatura: {m3[0][0]}")
print(f"  Nota 1: {m3[1]}")
print(f"  Nota 2: {m3[2]}")
print(f"  Promedio: {m3[0][1]}")
print("-----------------------------------------")

print(f"Promedio Final del Estudiante: {promedio_final}")
print("=========================================")

