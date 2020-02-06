"""
INTRODUCCIÓN A LA PROGRAMACIÓN ORIENTADA A OBJETOS (POO)
"""
#definir una clase rectangulo()
class rectangulo():
    #definir el método especial __init__
    def __init__(self,n):
        #definir un atributo nombre
        self.nombre=n
    #definir un método area
    def area(self):
        print("MÉTODO AREA")
    #definir un método perimetro
    def perimetro(self):
        print("MÉTODO PERIMETRO")
    #definir un método mi_nombre
    def mi_nombre(self):
        print("MI NOMBRE ES: ",self.nombre)
#INSTANCIAR OBJETOS , SE EJECUTARA AUTOMATICAMENTE EL __init__(self)
r1=rectangulo("JORGE")
#EJECUTAR MÉTODO mi_nombre()
r1.mi_nombre()

