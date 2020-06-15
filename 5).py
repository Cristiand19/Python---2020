import numpy as np

N = 20
vector = np.empty(N,dtype='U1')

#Carga del vector
for i in range(0,N):
    print("Alumno",i+1)
    Nota_de_parcial_1 =  int(input("Ingrese la primera nota:"))
    Nota_de_parcial_2 = int(input("Ingrese la segunda nota: "))
    Nota_de_parcial_3 = int(input("Ingrese la tercera nota: "))
    sum = Nota_de_parcial_1 + Nota_de_parcial_2 + Nota_de_parcial_3
    Nota_Promedio = int(sum/3)
    print(Nota_Promedio)
    if Nota_Promedio >= 0 and Nota_Promedio <= 5:
        vector[i] = 'D'
    elif Nota_Promedio >= 6 and Nota_Promedio <= 8:
        vector[i] = 'A'
    else:
        vector[i] = 'P'

#Mostrar Categorias
for i in range(0,N):
    print("Alumno",i+1,"Categoria",vector[i])

