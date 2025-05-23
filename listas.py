#aceder a elementos de la lista
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#indexacion negativa
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

#rangos de indices
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

#cambiar el valor de un articulo
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#insertar elementos
#Para insertar un nuevo elemento de la lista, sin reemplazar ninguno de los valores existentes, podemos usar el insert()método.
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

#añadir elementos al final de la lista
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#ampliar la lista
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#eliminar elementos de la lista
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#La delpalabra clave también elimina el índice especificado:
thislist = ["apple", "banana", "cherry"]
thislist[0]
print(thislist)

#La del palabra clave también puede eliminar la lista por completo.
thislist = ["apple", "banana", "cherry"]


#limpiar la lista
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#Ordenar lista alfanuméricamente}
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

#ordenas desendente
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

#Orden inverso
#El reverse()método invierte el orden de clasificación actual de los elementos
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

#unir dos listas
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)