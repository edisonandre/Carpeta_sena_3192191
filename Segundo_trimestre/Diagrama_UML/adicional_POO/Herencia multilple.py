class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        
    def hablar(self):
        print("Hola, estoy hablando un poco")
    
class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad
        
    def mostrar_habilidad(self):
        return f"Mi habilidad es: {self.habilidad}"
    
class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, empresa, salario):
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self,habilidad)
        self.salario = salario
        self.empresa = empresa
        
    def mostrar_habilidad(self):
        return f"Mi habilidad es: {self.habilidad}"
        
    def presentarse(self):
        # return f"{super().mostrar_habilidad()}"
        print(f"Hola, soy: {self.nombre}, {self.mostrar_habilidad()} y trabajo en {self.empresa}")
    
    
    

roberto = EmpleadoArtista("roberto", 44, "argentino", "cantar", "Google", 10000)

herencia = issubclass(EmpleadoArtista, Artista)
instancia = isinstance(roberto, EmpleadoArtista) 
print(instancia)

# roberto.presentarse()
# print(roberto.nacionalidad)
