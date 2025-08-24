class perro:
    def __init__(self, nombre, raza, edad):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        
    # metodo para hacer que el perro ladre
    def ladrar(self):
        return f"{self.nombre} dice: Guau guau"
    
    #metodo para obtener la informacion del perro
    def mostrar_informacion(self):
        return f"nombre: {self.nombre}, raza: {self.raza}, edad: {self.edad} años"
    
    #programa principal
mi_perro = perro("Firulais", "Labrador", 3)
print(mi_perro.ladrar())