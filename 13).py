import numpy as np

N = int(input("Dimension:"))
K = np.empty(N,dtype=int)

#Carga del Vector
for i in range(0,N):
    K[i] = int(input("Inngrese un numero: "))

#Mostrar Vector
print("Vector K")
for i in range(0,N):
    print(K[i],end="|")
print("\n")

#Desarrollo
b = 0
for i in range(0,N):
    aux = int(K[i]/2)*2#Utlizo una variable auxiliar para saber si el numero que esta en el vector es par
    if K[i] == aux:
        b = 1#Esta banndera se activa cuando se encuentra al menos un numero par
        print("Numero par:",K[i])
    i = i + 1
if b == 0:#Si la bandera nunca se activa ,significa que el vector no contiene numeros pares
    print("Vector sin numeros pares")
