import numpy as np

#v = np.array(['V','a','m','o','s',' ','a',' ','r','e','a','l','i','z','a','r',' ','e','l',' ','d','i','a','g','r','a','m','a'])
N = 28
v = np.empty()
for i in range(0,28):
    if v[i] == 'a' or v[i] == 'e' or v[i] == 'o' or v[i] == 'u':
        v[i] = 'i'

for i in range(0,28):
    print(v[i],end="")
print("")

