# Solicitar datos al usuario
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

#ejercicio 2
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

#actividad 3

