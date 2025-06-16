
for i in range(5): 
    print(f"El valor del bucle es: {i}.")

print()

for i in range(3,-12,-3):
    print(f"El valor del bucle es: {i}.")
    
print("Fin del bucle")
    
colores = ["Rojo", "Azul", "Verde", "Amarillo"]

print("---LISTADO DE COLORES----")

for color in colores:
    print(f"-{color}.")
    
for color in colores:
    if color == "Azul" or color == "Verde": #esto lo que hace es que omite los valores selecionado
        #Luego aparecera el valor que no fue selecionadi
        print("Se ha saltado este valor.") # el mensaje aparece como los valores no puesto
        continue # saltar la ejecucion
    print(f"-color {color}.")
    
print()

for color in colores:
    if color == "Azul":
        print("Se ha roto la ejecucion del bucle.")
        break #rompre la ejecucion
    print(f"-color {color}.")