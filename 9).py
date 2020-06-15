import numpy as np

x = int(input("CAntidad de elementos del vector:"))
E = np.empty(x,dtype=int)

#Carga del vector
for i in range(0,x):
    E[i] = int(input("Ingrese un numero:"))

#Permutacion
i = 0
j = x - 1
while i < x and j > i:
    aux = E[i]
    E[i] = E[j]
    E[j] = aux
    j = j - 1
    i = i + 1


#Mostrar Vector
for i in range(0,x):
    print(E[i],end="|")
print("")
