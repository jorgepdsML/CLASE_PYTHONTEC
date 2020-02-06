"""
INTRODUCCIÓN A LA PROGRAMACIÓN ORIENTADA A OBJETOS
Codigo para la definición de clases en python
"""
def linspace(to,tf,N):
    l=[]
    razon=(tf-to)/N
    for val in range(N):
        l.append(to+razon*val)
    return l

def funcion2(x):
    try:
        #crear lista vacia
        l2=[]
        #acceder a cada valor de la lista de entrada <x>
        for val in x:
            if val>=0:
                valor=1/(1+2.71**(-val))
            elif -2<=val<0:
                a=0.1
                valor=a*val
            else:
                valor=0
            l2.append(valor)
        return l2
    except:
        print("MENSAJE DE ERROR DEL BLOQUE try")

x=linspace(-5,5,100)
y=funcion2(x)
from matplotlib import pyplot as plt
plt.scatter(x,y)
plt.show()