import numpy as np

#N = int(input("Dim: "))
S= np.empty(5,dtype=int)

for i in range(0,5):
    S[i] = int(input("Ingrese un salario:"))


print("Salario Actual:")
for i in range(0,5):
    print("[",S[i],"]",end="")
print("")