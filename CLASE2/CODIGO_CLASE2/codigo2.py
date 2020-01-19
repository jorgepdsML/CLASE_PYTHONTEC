lista1=[30,40,50,100,200,30]
#acceder a un elemento de la posición
var1=int(input("INGRESAR UN DATO"))
#objeto.metodo(argumento)
lista1.append(var1)
print("LISTA ACTUALIZADA: ",lista1)
#pedir un indice desde la shell de python
indice=int(input("COLOCAR INDICE "))
#utilizar el metodo pop
valor=lista1.pop()
print("VALOR ES: ",valor)
print("LISTA 1 ACTUALIZA: ",lista1)