mi_tuplas = (1,2,3,4,5)
otra_tuplas = ("hola", "como", "esta")
print(mi_tuplas, otra_tuplas)

#se convierte a lista y tuplas con list y tuple
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
x = x+2
print(x)