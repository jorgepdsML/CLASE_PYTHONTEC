"""
USO DEL ITERABLE range
"""
import time

#range(valor_inicial,limite_superior o limite_inferor,paso)

r1=range(10,-2,-1)# 10 9 8 7 6 5 4 3 2 1 0 -1
r2=range(15,20,2)#15 17 19
r3=range(1,90,30)#1 31 61 

#uso del bucle for
for val in r1:
    print("VALOR ES :",val)
    time.sleep(1.5)
print("FIN DE CODIGO")
