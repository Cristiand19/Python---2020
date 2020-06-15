import numpy as np

A = np.empty(12,dtype=int)
aux = np.empty(12,dtype=int)#Vector auxiliar

#Carga de alumnos en el vector A
for i in range(0,12):
    A[i] = int(input("Alumnos:"))

may = -999
sum = 0
i = 0
for i in range(0,12):
    print("En la clase",i+1,"hay:",A[i],"alumnos")#Pongo i+1 para adaptarlo al numero de clases
    sum = sum + A[i]
    if A[i] > may:
        may = A[i]
prom = sum/12
print("Cantidad promedio de alumnos presentes:",prom)


#Hago una busqueda para saber si hay mas de una clase con mayor cantidad de asistencias
j = 0#Indice para mi vector auxiliar
x = may
i  = 0
while i < 12:
    if x == A[i]:
        aux[j] = i+1 #si encuentro una clase la guardo en el vector auxiliar
        j = j + 1
    i = i + 1

for i in range(0,j):
    print("La/las clase/s con mayor cantidad de asistencias es/son:",aux[i])

