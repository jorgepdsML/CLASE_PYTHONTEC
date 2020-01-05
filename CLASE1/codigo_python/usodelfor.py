"""
uso del bucle for , if y el break
"""
#objeto.metodo
#importar modulo llamado time en nuestor archivo de python
import time
#lista1 , iterable
l1=[10,20,50,100,200]
#uso del bucle for
for var in l1:
    #si la condición es verdadero, colocar un break
    if var >20:
        break
    #imprimir valor 
    print(var)
    #temporizar 2 segundos
    time.sleep(2)
    
#se acabo el bucle for
print("FIN DE CODIGO")
