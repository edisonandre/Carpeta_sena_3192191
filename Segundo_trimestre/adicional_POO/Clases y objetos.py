# class celular():
#     marca = "samsung" #objetos
#     modelo = "s24"
#     camara = "28MP"

# celular1 = celular()  #objeto de la instacia de celular
# celular2 = celular()
# celular3 = celular()
# celular4 = celular()

# print(celular3.modelo)

#variables que pertenece a una clase

# class celular():
#     marca = "samsung" #objetos
#     modelo = "s24"
#     camara = "28MP"
    
# celular1 = celular()  #objeto de la instacia de celular
# celular.marca = "Apple" #no es optimo
# print(celular1.marca)

class celular:          #valor a pasar
    def __init__(self, marca, modelo, camara): #(self) hace referencia asi mismo
        #motodo constructor
        self.mar = marca #marca es propiedad de self
        self.modelo = modelo #modelo es propiedad de self
        self.camara = camara #camara es propiedad de self

celular1 = celular("samsung", "s24", "48MP")#guarda estos dato a clase
celular2 = celular("Honor", "x7a", "56MP")
print(celular1.mar)
print(celular2.modelo)

