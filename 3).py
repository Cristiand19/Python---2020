import numpy as np
import random

vector = np.empty(15,dtype=int)

#Cargar Vector
for i in range(0,15):
    vector[i] = random.randint(1,100)

#Mostrar Vector
for i in range(0,15):
    print(vector[i],end=",")
print("")