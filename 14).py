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

#Determinar Categoria
D = 0
A = 0
P = 0
for i in range(0,N):
    if vector[i] == 'D':
        D = D + 1
    elif vector[i] == 'A':
        A = A + 1
    else:
        P = P + 1

#Cantidad de alumnos segun la categoria
if D != 0:
    print("La cantidad de alumnos en la categoria D es de:",D)
else:
    print("No existe ningun alumno en la categoria D")
if A != 0:
    print("La cantidad de alumnos en la categoria A es de:",A)
else:
    print("No existe ningun alumno en la categoria A")
if P != 0:
    print("La cantidad de alumnos en la categoria P es de:",P)
else:
    print("No existe ningun alumno en la categoria P")


#Categoria con mas alumnos
if D > A:
    if D > P:
        print("La categoria con mas alumnos es la categoria D,con:",D,"alumnos")
    else:
        print("La categoria con mas alumnos es la categoria P,con:",P,"alumnos")
else:
    if A > P:
        print("La categoria con mas alumnos es la categoria A,con:",A,"alumnos")
    else:
        print("La categoria con mas alumnos es la categoria P,con:",P,"alumnos")