#listas
"""lista1=[3,5,7,9,11,66,55] #numeros
lista2=["w","a","m","o"] #letras
#metodo Sort()-->menor a mayor, solamente ordena o numeros o letras, pero no una lista combinada.
print(lista1)
print(lista2)
lista1.sort()
lista2.sort()
print(lista1)
print(lista2)
lista1.sort(reverse=True)
lista2.sort(reverse=True)
print(lista1)
print(lista2)"""
#lista con numeros aleatorios
import random
lista=[]
for w in range(10):
    x=random.randint(1,100)
    lista.append(x)
for q in lista:
    print(q,end=" ")
#ver SUM, MIN, MAX
#lista.sum() suma los datos
#lista.min() busca el valor menor
#lista.max() busca el valor máximo
#len(lista) --> lenght busca el largo de la lista
#UPPER--> convierte un string en mayusculas
#LOWER-->convierte un string en minusculas
#upper()
w="chao"
print(w.upper())
    


