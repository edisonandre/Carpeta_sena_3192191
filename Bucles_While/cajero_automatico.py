print("CAJERO AUTOMATICO\n")

clave = input("Escribe la contraseña ")
while clave != "1234":   # estructura para contraseña
    print("contraseña incorrecta \n")
    clave = input("intenta de nuevo ")
print("Acceso concedido")

saldo = 0
#depositar
while clave != 1234:
    pregunta = input("¿Deseas depositar slado? (si/no): ").lower()
    if pregunta == "si":
        cantidad = int(input("Cuantos quiere depositar"))
        saldo += cantidad
        print(f"tienes saldo total de {saldo}")
    elif pregunta == "no":
        pregunta = input("Deseas retirar dinero? (si/no): ").lower()
        cantidad = int(input("¿Cuanto deseas retirar?: "))

        cantidad <= saldo
        saldo -= cantidad
        print(f"saldo actual: {saldo}")
    else:
        print("Saldo insuficiente")
        
