#-----importar numpy como np
#sys.path tiene una lista de todas rutas
#donde se importa un modulo o paquete
import numpy as np
#crear arreglos
#escalar
a1=np.array(0.0)
#print("DIMENSION DE A1  ES :",a1.ndim)
#1D
a2=np.array( [1,2.0,20,30,100] ) # a2[3]
#DETERMINAR LA CANTIDAD ELEMENTOS POR DIMENSIÓN O POR EJE
s2=a2.shape
print(a2)
print("DIMENSIÓN DE A2 es: ",a2.ndim)
print("SHAPE DE A2 ES: ",s2)
print("SIZE DE A2 ES: ",a2.size)
#2D
a3=np.array([  [1,2,3],[0,4,5],[1,1,2],[0,1,1] ])# a3[0][2]
#atributo shape , almacena cantidad de elementos por dimensión
s3=a3.shape
print(a3)
print("DIMENSIÓN DE A3 ES: ",a3.ndim)
print("SHAPE DE A3 ES: ",s3)
print("SIZE DE A3 ES: ",a3.size)