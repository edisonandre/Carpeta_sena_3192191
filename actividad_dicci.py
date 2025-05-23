auto = {"marca": "toyota", "modelo": "corolla"}
valor = auto.pop("marca")
print(valor)
print(auto)

auto1 = {"marca": "toyota", "modelo": "corolla"}
del auto1["modelo"]
print(auto1)

color = auto.pop("color", "no especificado")
print(color)

print(auto["modelo"])
auto["modelo"] = "camry"

#creacion de un diccionario
nombre_diccionario = {
    "clave": "valor1",
    "clave2": "valor2",
}