lista=[100,20,21,23,24]
#dato nulo
nulo=None
#lista_impar 21 23
#lista_par 10 20 24
lista_par=[]
lista_impar=[]
for val in lista:
    if val%2==0:
        lista_par.append(val)
    else:
        lista_impar.append(val)
print(lista_par)
print(lista_impar)

