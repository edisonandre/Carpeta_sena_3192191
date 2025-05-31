frase = "El conocimiento es poder"
metodo = frase.find("conocimiento")
metodo1 = frase.find("poder")

# caracter y busca el primera letra del frase
print(metodo)
print(metodo1)


print("______\n")
text = "La practica hace al maestro"
print(text.find("practica"))
print(text.find("maestro"))

#en una sola linea el print y variable busca el caracter
print("_______\n")
frase = input("por favor ingrese una frase ")
text = input("¿que palabra quiere buscar de la frase anterios? ")
print(frase.find(text))

#ejemplo 2
print("________\n")
test = "Doña Uzeada de Ribera Maldonado de Bracamonte y Anaya era baja, rechoncha, abigotada. Ya no existia razon para llamar talle al suyo. Sus colores vivos, sanos, podian mas que el albayalde y el soliman del afeite, con que se blanqueaba por simular melancolias. Gastaba dos parches oscuros, adheridos a las sienes y que fingian medicamentos. Tenia los ojitos ratoniles, maliciosos. Sabia dilatarlos duramente o desmayarlos con recato o levantarlos con disimulo. Caminaba contoneando las imposibles caderas y era dificil, al verla, no asociar su estampa achaparrada con la de ciertos palmipedos domesticos. Sortijas celestes y azules le ahorcaban las falanges"
print(test)
print(test.find("Sabia"))
print(test.find("Caminaba"))
print(test.find("falanges"))

#entre corchete y la coordenada para la extracion
print(test[459:655])