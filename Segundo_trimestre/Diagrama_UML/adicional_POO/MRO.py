class a:
    def hablar(self):
        print("Hola desde a")
        
class f(a):
    def hablar(self):
        print("Hola desde f")

class b(a):
    def hablar(self):
        print("Hola desde b")

class c(f):
    def hablar(self):
        print("Hola desde c")
        
class d(b,c):
    pass

D = d()
print(d.mro())