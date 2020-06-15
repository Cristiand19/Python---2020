import numpy as np

F = int(input("Filas:"))
C = int(input("Columnas:"))
M = np.empty((12,37),dtype=int)

#Carga de la matriz
for i in range(0,F):
    for j in range(0,C):
        M[i,j] = int(input("Ingrese un numero:"))

print("Matriz M")
#Mostrar Matriz
for i in range(0,F):
    for j in range(0,C):
        print(M[i,j],end="|")
    print("")

