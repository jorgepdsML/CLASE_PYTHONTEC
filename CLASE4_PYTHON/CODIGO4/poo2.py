"""
INTRODUCCIÓN A LA PROGRAMACIÓN ORIENTADA A OBJETOS (POO)
"""
#definir una clase rectangulo()
class rectangulo():
    #definir el método especial __init__
    def __init__(self,ancho,largo):
        #definir un atributo nombre
        self.width=ancho
        self.height=largo
    #definir un método area
    def area(self):
        w=self.width
        h=self.height
        print("AREA  ES: ",w*h,"m2")
    #definir un método perimetro
    def perimetro(self):
        return 2*(self.height+self.width)
    #definir un método mi_nombre
    def mi_nombre(self):
        print("MI NOMBRE ES: ",self.nombre)
#INSTANCIAR OBJETOS , SE EJECUTARA AUTOMATICAMENTE EL __init__(self)
rect1=rectangulo(100,20)
#UTILIZAR EL MÉTODO area
rect1.area()
#calcular el perimetro de rectangulo
per=rect1.perimetro()
print("PERIMETR ES: ",per)