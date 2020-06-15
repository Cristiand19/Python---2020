import numpy as np

dimF = 5
dimL = 0
vector = np.empty(dimF,dtype=int)

while dimL < dimF:
    num = int(input("Ingrese un numero: "))
    vector[dimL] = num
    dimL = dimL + 1
    for i in range(0,dimL):
        print(vector[i],end=" , ")
    print("DimLog =",dimL)


