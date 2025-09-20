class gato():
    def sonido(self):
        return "Miau"
    
class perro():
    def sonido(self):
        return "Guau"
    
def hacer_sonido(animal):
    print(animal.sonido())
    
Gato = gato()
Perro = perro() #uno le estoy pasando la misma funcion pero cambia el argumento pero de esta forma estoy ejecutanfo el mismo medotdo pero xambiar el onjeto deonde se esta implemetando

hacer_sonido(Perro)