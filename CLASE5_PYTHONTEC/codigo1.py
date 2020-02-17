#importar los modulos necesarios
#--HERRAMIENTA NUMPY Y OPENCV
import numpy as np
import cv2
#arreglo de numpy
a1=np.array([1,2,0])
print(a1)
print("DIMENSIONES DE a1 es:",a1.ndim)
print("FORMA DE a1 es:",a1.shape)
a2=np.array([[10,20,], [1,0]])
print(a2)
print("DIMENSIONES DE a2 es:",a2.ndim)
print("FORMA DE a2 es:",a2.shape)
#accediendo a todos los elementos de la segunda fila
c1=a2[:,0]
print("PRIMERA COLUMNA ES: ",c1)
#crear arreglo de 3 dimensiones
a3=np.array()