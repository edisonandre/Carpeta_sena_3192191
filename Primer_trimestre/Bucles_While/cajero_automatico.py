print("=== CAJERO AUTOMÁTICO ===")

# Paso 1: Verificar contraseña
clave_correcta = "1234"
clave = input("Ingrese su contraseña: ")

while clave != clave_correcta:
    print("Contraseña incorrecta. Intente de nuevo.")
    clave = input("Ingrese su contraseña: ")

print("Acceso concedido.")

# Paso 2: Menú de operaciones
saldo = 0  # Saldo inicial

while True:
    print("\n--- MENÚ ---")
    print("1. Ingresar saldo")
    print("2. Retirar saldo")
    print("3. Ver saldo")
    print("4. Salir")

    opcion = input("Elija una opción (1-4): ")

    if opcion == "1":
        ingreso = float(input("¿Cuánto desea ingresar?: "))
        if ingreso > 0:
            saldo += ingreso
            print(f"Se ingresaron ${ingreso}. Nuevo saldo: ${saldo}")
        else:
            print("El valor debe ser mayor que cero.")

    elif opcion == "2":
        retiro = float(input("¿Cuánto desea retirar?: "))
        if retiro > saldo:
            print("Fondos insuficientes.")
        elif retiro <= 0:
            print("El valor debe ser mayor que cero.")
        else:
            saldo -= retiro
            print(f"Se retiraron ${retiro}. Saldo restante: ${saldo}")

    elif opcion == "3":
        print(f"Su saldo actual es: ${saldo}")

    elif opcion == "4":
        print("Gracias por usar el cajero. ¡Hasta pronto!")
        break

    else:
        print("Opción inválida. Intente nuevamente.")
