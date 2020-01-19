def umbralizar(M1,umbral):
    #conseguir filas
    Nf=len(M1)
    #conseguir columnas
    Nc=len(M1[0])
    Mv=[]
    for filas in range(Nf):
        Mv.append([])
    for x in range(Nf):
        for y in range(Nc):
            if M1[x][y]>=umbral:
                Mv[x].append(1)
            else:
                Mv[x].append(0)
    return Mv
def saludar():
    print("FUNCIÓN SALUDAR")
LISTA=["umbralizar","saludar"]


