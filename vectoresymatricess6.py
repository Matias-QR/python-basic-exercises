#numpy --> vectores y matrices
import numpy as np # np es un seudonimo para usar la libreria, podría ser otro nombre
import random
#A=np.array([0]*10) #metodo rustico pa crear un vector de largo 10
A=np.arange(10)#metodo optimo o moderno para definir un arreglo de largo 10
B=np.arange(10)
for w in range(len(A)):             #llena el vector con numeros aleatorios.
    A[w]=random.randint(0,500)
    #w=w+1 el ciclo for tiene un contador interno
print("arreglo A: ",A)
print("arreglo A indices pares: ",A[::2])
print("El valor mayor del vector es: ",max(A))
print("El valor menos del arreglo es: ",min(A))

#listas, vectores y matrices por naturaleza son --> variable
B=A #copiar los vectores [:]   -copy
print("arreglo B:",B)
for w in range(len(B)):
    B[w]=B[w]*3
print("arreglo B*3:",B)
print("La suma de los elementos es: ",sum(B))
print("el promedio del arreglo B es: ",(sum(B)/len(B)))

#si lo hicieramos con un While o While not
#tendriamos que colocar un contador ej w=w+1 y luego
#quebrar el ciclo con un break
#el ciclo While no tiene un contasdor interno.
