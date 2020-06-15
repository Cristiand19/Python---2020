import numpy as np

#Carga del vector
N = np.empty(20,dtype=int)
for i in range(0,20):
    numero = int(input("Ingrese un numero: "))
    N[i] = numero

#Resolucion
cnuc = 0 #Cantidad de numeros de una cifra : contador
cantidad_de_primos = 0
for i in range(0,20):
    if N[i] >= 1 and N[i]<= 9:
        cnuc = cnuc + 1
    if N[i] >= 10 and N[i] <= 99:#Para los numeros primos solo se admiten los enteros positivos ya que no existen numeros primos negativos
        #Algoritmo de numero primo
        b = 0
        c = 2
        while c < N[i] and b == 0:
            aux = int(N[i]/c)*c#Para saber si hay algun numero divisible por el numero que yo ingreso
            if aux == N[i]:
                b = 1 #Si se activa la bandera entonces no es un numero primo
            c = c + 1
        if b == 0:
            cantidad_de_primos = cantidad_de_primos + 1
    if N[i] >= 100 and N[i] <= 999:
        unidad = N[i] - int(N[i]/10)*10
        x = int(unidad/3)*3
        if x == unidad:
            print("Multiplo de 3:",unidad)
porcentaje = (cnuc*20)/100
print("Porcentaje de numeros de una cifra:",porcentaje)
print("Cantidad de numeros primos de 2 cifras:",cantidad_de_primos)







