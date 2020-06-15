import numpy as np

N = int(input("Ingrese la dimension:"))
A = np.empty(N,dtype=int)

#Carga del vector
#Cargo el vector con los numeros de legajo
for i in range(0,N):
    A[i] = int(input("Ingrese un numero de legajo:"))

#Mostrar vector
#Muestro el vectro con los numeros de legajo cargados
print("vector A")
for i in range(0,N):
    print(A[i],end="|")

#Ordeno el vector de forma ascendente
i = 0
while i < N - 1:
    p = i
    j = i + 1
    while j < N:
        if A[j] < A[p]:
            p = j
        j = j + 1
    aux = A[p]
    A[p] = A[i]
    A[i] = aux
    i = i + 1

#Muestro el vector ordenado
print("\nVector A ordenado")
for i in range(0,N):
    print(A[i], end="|")

#Hago una busqueda binaria para buscar un determinado numero de legajo
NL = int(input("\nIngrese el numero de legajo que desea buscar:"))
j = 0
p = 0
u = N - 1
M = int((p+u)/2)
while p <= u and NL != A[M]:
    if NL < A[M]:
        u = M - 1
    else:
        p = M + 1
    M = int((p+u)/2)
if p <= u:
    j = M
    print("Numero de legajo existente")
else:
    print("Numero de legajo inexistente")