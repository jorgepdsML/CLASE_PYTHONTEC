"""
definición de funciones
"""
def funcion_externa():
    global var1, var2
    var1=200
    var2=300
    print(var1+var2)
    print("FUNCIÓN EXTERNA")
    def funcion_interna():
        print("FUNCIÓN ANIDADA DE LA FUNCIÓN EXTERNA")
    funcion_interna()
    print("SALIENDO DE LA FUNCIÓN EXTERNA")
def saludos(ingresa):
    print("FUNCIÓN SALUDOS")
    return 2*ingresa
#definición de la función polinomio
#----ao*x^2+a1*x+a2
def polinomio(a0,a1,a2):
    def interna(x):
        v=a0*(x**2)+a1*x+a2
        return v
    return interna
def linspace(to,tf,N):
    l=[]
    razon=(tf-to)/N
    for val in range(N):
        l.append(to+razon*val)
    return l
def ones(A,N):
    l=[]
    for i in range(N):
       l.append(A*1)
    return l
#lista de entrada
x=linspace(-3,3,100)
#utilizar la función polinomio
a0,a1,a2=1,1,1
#función polinomio
p=polinomio(a0,a1,a2)#retorna la función interna (copia)
y=[]
for val in x:
    y.append(p(val))
#crear grafica para el eje Y

from matplotlib import pyplot as plt
plt.plot(x,y)
plt.show()

