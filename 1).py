import numpy as np

vector = np.empty(10,dtype=int)

for i in range(0,10):
    a = int(input("Ingrese el 1er numero:"))
    b = int(input("ingrese el segundo numero: "))
    if a > b:
        vector[i] = a
    else:
        vector[i] = b


for i in range(0,10):
    print(vector[i])
