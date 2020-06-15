import numpy as np

N = 13 #Cambiar valor de N si desea trabajar con mas o con menos elementos
E = np.empty(N,dtype=int)

#Carga del vector
for i in range(0,N):
    E[i] = int(input("Ingrese un numero:"))

#Mostrar Vector
print("Vector E")
for i in range(0,N):
    print(E[i],end="|")

#Permutar
i = 0
while i < N - 1:
    aux = E[i]
    E[i] = E[i+1]
    E[i+1] = aux
    i = i + 2

#Mostrar Vector
#Muestro el vector permutado
print("\nVector E permutado")
for i in range(0,N):
    print(E[i],end="|")
