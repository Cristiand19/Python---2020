import numpy as np

B = np.array([1500,1700,1300,3000,3500,2700,2500,1350,3050,5000,3650,4800,#2018
              6000,5500,3200,6700,4900,6850,7000,7500,8000,8500,9000,7700])#2019


#La mayor ganancia de los trimestres pares
i = 3
while i < 24:
    may = -999
    c = i
    ct = 1
    while ct <= 3:
        print(B[c])
        if B[c] > may:
            may = B[c]
        c = c + 1
        ct = ct + 1
    print("La mayor ganancia del trimestre es de:",may)
    i = i + 6
