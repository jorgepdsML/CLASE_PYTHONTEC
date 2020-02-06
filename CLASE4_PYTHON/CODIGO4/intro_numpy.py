try:
    import numpy as np
except ModuleNotFoundError:
    print("HUBO ERROR AL MOMENTO DE IMPORTAR UN MODULO")

#utilizar un objeto de la clase numpy.ndarray
a1=np.linspace(0,10,100)
#utilizar otra clase para definir un objeto
a2=np.array([1,2])
n2=a2.ndim
forma2=a2.shape
print("DIMENSIONES DEL VECTOR a2 es: ",n2)
print("FORMA DEL VECTOR a2 es: ",forma2)
a3=np.array([[1,0],[0,1]])
#determinar las dimensiones
n3=a3.ndim
forma3=a3.shape
print("DIMENSIONES DEL VECTOR a3 es: ",n3)
print("FORMA DEL VECTOR a3 es : ",forma3)
