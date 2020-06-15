import numpy as np

#N = int(input("Cantidad de empleados:"))
#v = np.empty(N,dtype=int)
v = np.empty(20,dtype=int)

#Carga del vector
for i in range(0,20):
    v[i] = int(input("Ingrese la edad del empleado: "))

#Categorias
catA = 0
catB = 0
catC = 0
for i in range(0,20):
    if v[i] > 45:
        catA = catA + 1
    elif v[i] >= 30 and v[i] <= 40:
        catB = catB + 1
    elif v[i] == 18:
        catC = catC + 1
print("Empleados mayores a 45 años:", catA)
print("Empleados entre 30 y 40 años inclusive:", catB)
print("Empleados de 18 años:", catC)

#Mostrar vector
for i in range(0,20):
    print(v[i],end=",")
print("")

