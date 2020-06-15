import numpy as np

dimF_A = 20
dimF_B = 15
A = np.empty(dimF_A,dtype=int)
B = np.empty(dimF_B,dtype=int)


#Carga del vector A
#La carga de este vector debe ser ordenada pero de forma descendente
dimL_A = int(input("Dimension de A:"))
for i in range(0,dimL_A):
    A[i] = int(input("Ingrese un numero:"))

#Mostrar vector
#Muestro el vector A
print("Vector A")
for i in range(0,dimL_A):
    print(A[i],end="|")

#Carga del vector B
#Para la carga de este vector no importa el orden
dimL_B = int(input("\nDimension de B:"))
for i in range(0,dimL_B):
    B[i] = int(input("Ingrese un numero:"))

#Mostrar vector
#Muestro el vector A
print("Vector A")
for i in range(0,dimL_A):
    print(A[i],end="|")

#Mostrar vector
#Muestro el vector B
print("\nVector B")
for i in range(0,dimL_B):
    print(B[i],end="|")

#Intercalo los elementos del vector B en el vector A
i = 0
while i < dimL_B:
    b1 = 0
    j = 0
    while j < dimL_A and b1 == 0:
        if B[i] > A[j]:
            k = dimL_A - 1
            while k >= j:
                A[k+1] = A[k]
                k = k - 1
            dimL_A = dimL_A + 1
            b1 = 1
            A[j] = B[i]
        j = j + 1
    if b1 == 0:
        A[j] = B[i]
        dimL_A = dimL_A + 1
    i = i + 1

print("\nVector Intercalado")
for i in range(0,dimL_A):
    print(A[i],end="|")
