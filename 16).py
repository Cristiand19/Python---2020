import numpy as np

A = np.array([23,40,36,15,7,10])#Quini
B = np.empty(6,dtype=int)

print("¿Quiere hacer trampa?")
print("Opciones:"
      "\n1 - Si"
      "\n2 - No")
opcion = int(input(">"))
if opcion == 1:
    print("Numeros ganadores")
    for i in range(0,6):
        print(A[i],end="|")

#Jugada
print("\nIngrese su jugada")
b1 = 0
i = 0
while i < 6 and b1 == 0:
    num = int(input("Ingrese un numero:"))
    if num > 0 and num < 45:
        B[i] = num
    else:
        b1 = 1
    i = i + 1

#Determinar validez de la jugada
if b1 == 0:
    print("Se ingreso su jugada")
    #Determinar si se gano el gano el Quini
    b2 = 0
    i = 0
    while i < 6 and b2 == 0:
        if A[i] != B[i]:
            b2 = 1
        i = i + 1
    if b2 == 0:
        print("Gano")
    else:
        print("No gano")
else:
    print("No se pudo realizar la jugada porque el numero que ingresó,no está dentro de los permitidos")