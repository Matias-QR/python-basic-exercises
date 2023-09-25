#Listas-->variable-->conjunto de datos
#estructura de datos-->dinamica-->multidato ("contenedor basura" se pueden mezclar todos los tipos en una misma lista)
#lista2=lista1
lista1=[] #lista vacía
lista2=["juan",23,1.75,True] #lista con datos.
#          0    1   2    3 -->izq a derecha
#          -4   -3  -2   -1 -->der a izq
#la ultima posicion de la lista es -1
"""print(lista2) #vista developer
print("el nombre es:",lista2[0])   #vista de usuario
print("el nombre es:",lista2[-4])  #vista de usuario
for z in lista2:
    print(z,end=" ")"""

#Metodos para las listas
#metodo AGREGAR-->append (agrega al final de una lista)
lista1.append("Matias")
lista1.append("Radovcic")
print(lista1)
#metodo Extend()-->una lista a otra
lista1.extend(["Sebastian","Quezada"])  #si son datos se pasan con corchetes
print(lista1)
lista1.extend(lista2)
print(lista1)
#metodo INSERT-->lista.insert(i,d)--> i=indice d=dato
lista1.insert(-1,"Saitam")
print(lista1)
#metodos eliminar
#Remove y Pop
#Remove--> elimina elemento segun el dato
lista1.remove("Matias")
print(lista1)
#pop()--> elimina siempre el ultimo elemento de la lista
#pop(2)-->elimina segun el indice
lista1.pop()
print(lista1)
