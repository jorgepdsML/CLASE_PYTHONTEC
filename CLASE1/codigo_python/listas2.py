"""
USO DE LA LISTA Y SUS METODOS
"""
#lista1
lista1=[10,20,30]
N=len(lista1)
print("ANTES DEL METODO POP ",lista1)
#lista2
lista2=[5,2,3,100]
#concatenar listas
print(lista1+lista2)
#sacar un elemento de la ultima posición de la lista lista1
val=lista1.pop()
print("ELEMENTO QUE SE EXTRAIDO ES: ",val)
print("DESPUES DEL METODO POP" , lista1)
