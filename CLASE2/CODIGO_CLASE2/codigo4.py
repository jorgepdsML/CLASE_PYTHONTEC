#2x2
#MATRIZ 2D
import time
l1=[[10,50,3],
    [20,15,4]]
l2=[[12,50,5],
    [0,1,1]]
#determinar numero de filas
Nf=len(l1)
#determinar numero de columnas
Nc=len(l1[0])
M3=[]
#añadir la misma cantidad de filas a la matriz M3
for fila in range(Nf):
    M3.append([])
#para cada fila
for x in range(Nf):
    #para cada columna
    for y in range(Nc):
        #multiplicar elemento a elemento l1 y l2
        multi=l1[x][y]*l2[x][y]
        #agregar en la matriz m3 el valor encontrado
        M3[x].append(multi)
        print(multi,end=" ")
        time.sleep(1.5)
    print("")
print(M3)

