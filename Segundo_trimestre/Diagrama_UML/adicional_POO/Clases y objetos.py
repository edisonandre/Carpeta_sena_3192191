class celular():
    marca = "samsung" #objetos
    modelo = "s24"
    camara = "28MP"

celular1 = celular()  #objeto de la instacia de celular
celular2 = celular()
celular3 = celular()
celular4 = celular()

print(celular2.modelo)

#variables que pertenece a una clase

class celular():
    marca = "samsung" #objetos
    modelo = "s24"
    camara = "28MP"
    
celular1 = celular()  #objeto de la instacia de celular
celular.marca = "Apple" #no es optimo
print(celular1.marca)

class celular:          #valor a pasar
    def __init__(self, marca, modelo, camara): #(self) hace referencia asi mismo
        #motodo constructor
        self.mar = marca #marca es propiedad de self
        self.modelo = modelo #modelo es propiedad de self
        self.camara = camara #camara es propiedad de self
        
    def llamar(self):
        print(f"estas haciendo un llamado desde un: {self.modelo}")
        
    def cortar(self):
        print(f"cortaste la llamada desde tu: {self.modelo}")

celular1 = celular("samsung", "s24", "48MP")#guarda estos dato a clase
celular2 = celular("Honor", "x7a", "56MP")

celular1.cortar() #se ejecuta sin un print


#ejercico edad clase y grado
class Estudiante:
    def __init__(self, nombre, Edad, Grado):
        self.nombre = nombre
        self.edades = Edad
        self.grado = Grado
        
    def estudiar(self):
        print("estudiando...")
        
nombre = input("Digame su nombre ")
edad = input("ingrese su edad ")
grado = input("ingrese su grado ")

estudiante = Estudiante(nombre, edad, grado)

print(f"""
    DATOS DEL ESTUDIANTE: \n\n
    Nombre: {estudiante.nombre} \n
    Edad: {estudiante.edades} \n
    Grado: {estudiante.grado}  \n
    """)

while True:
    estudiar = input()
    if (estudiar.lower() == "estudiar"):
        estudiante.estudiar()


