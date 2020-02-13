"""
crear arreglo de 3 dimensiones
"""
import numpy as np
#ARREGLO DE 2 DIMENSIONES
a2d=np.array([ [3,4,4,6],
               [5,6,4,7] ])
s2=a2d.shape
#Número de filas
nf=s2[0]
#Número de columnas
nc=s2[1]
#acceder ala posición 1,1
a11=a2d[1][1]
#acceder a toda la primera fila
af1=a2d[0][:]
print(af1)
#ARREGLO DE 3 DIMENSIONES
a3d=np.array([ [[5,6],[7,8]], [[1,2],[4,5]]  ] )
print(a3d)
print("NÚMERO DE DIMENSIONES ES :" ,a3d.ndim)
#acceder a la primera capa del arreglo a3d
capa1=a3d[0][:][:]
capa2=a3d[1][:][:]
print(capa1+capa2)