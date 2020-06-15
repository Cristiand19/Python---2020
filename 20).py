import numpy as np

N = int(input("Ingrese la Dimension:"))
A = np.empty(N,dtype=int)
B = np.empty(N,dtype=int)

#Cargar vector A
for i in range(0,N):
    A[i] = int(input("Ingrese un numero:"))

print("vector A")
#Muestro el arreglo A
for i in range(0,N):
    print(A[i],end="|")

#Hago la diferencia de los elementos sucesivos del arreglo A y guardo los resultados en el arreglo B
j = 0
i = 0
while i < N - 1:
    B[j] = A[i] - A[i+1]
    j = j + 1
    i = i + 1
d = j

#Muestro el arreglo B
print("\nvector B")
for i in range(0,d):
    print(B[i],end="|")