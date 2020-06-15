import numpy as np

N = int(input("Cantidad de alumnos de Algebra I:"))
x = np.empty(N,dtype='U1')

#Carga del Vector
for i in range(0,N):
    inicial = input("Ingrese la inicial del nombre del alumno:").upper()
    x[i] = inicial

#Nombres que comienzan con vocal
vocales = 0
for i in range(0,N):
    if x[i] in 'AEIOU':
        vocales = vocales + 1
print("Cantidad de nombres cuya inicial comienza con vocal:",vocales)