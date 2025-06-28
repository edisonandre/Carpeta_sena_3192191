print("CAJERO AUTOMATICO\n")

clave = input("Escribe la contraseña ")
while clave != "1234":   # estructura para contraseña
    print("contraseña incorrecta \n")
    clave = input("intenta de nuevo ")
print("Acceso concedido")

saldo = 0
#depositar
while True:
    producto = input("Necesitas depositar (si/no) ")
    if producto == "si":
        producto = int(input("ingrese numero que vas a depositar "))
        saldo += producto
        print(f"El saldo total acomulado es: {saldo}")
        
        retirar = input("Si deseas retirar ingrese (si/no) ")
    
        producto = int(input("ingrese la cantidad que deseas retirar "))
        saldo -= producto
        print(f"El saldo total acomulado es: {saldo}")
    else:
        print(f"el saldo total {saldo}")
        break
        