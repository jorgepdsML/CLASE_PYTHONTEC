#importar el modulo sys
import sys
ruta=sys.path
ruta.append("C:\\Users\\pdsjo\\Desktop\\holaatodos")
tupla1=(10,20,30,"hola")#tuple
lista1=[10,20,30,"hola"]#list
print(sys.getsizeof(tupla1),sys.getsizeof(lista1))
print(sys.platform)