import numpy as np

N = int(input("Ingrese la Dimension:"))
A = np.empty(N,dtype=int)
B = np.empty(N,dtype=int)

#Cargo el arreglo A
for i in range(0,N):
    A[i] = int(input("Ingrese un numero:"))

#Muestro el arreglo A
print("vector A")
for i in range(0,N):
    print(A[i],end="|")

#Hago la suma de los elementos opuestos del arreglo A y guardo los resultados en el arreglo B
k = 0
j = N - 1
i = 0
while i < N and j >= i:
    if j == i:
        B[k] = A[i]
    else:
        B[k] = A[i] + A[j]
    j = j - 1
    k = k + 1
    i = i + 1
d = k
#Muestro el arreglo B
print("\nvector B")
for i in range(0,d):
    print(B[i],end="|")