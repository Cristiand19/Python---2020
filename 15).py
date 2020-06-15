import numpy as np

N = int(input("Dimension"))
A = np.empty(N,dtype=int)

#Carga del vector
for i in range(0,N):
    A[i] = int(input("Ingrese un numero:"))

#Buscar numero
c = 0
x = int(input("Ingrese el numero que desea buscar en el vector:"))
for i in range(0,N):
    if A[i] == x:
        print("El numero",x,"se encuentra en la posicion",i+1,"del vector")
        c = c + 1
    i = i + 1
if c != 0:
    print("La cantidad de veces que aparece el numero",x,"en el vector es:",c)
else:
    print("El numero",x,"no se encuentra en el vector")