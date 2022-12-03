import numpy as np
filename = 'input.txt'
data = np.loadtxt(filename, delimiter=',', skiprows=0, dtype=int)
j = 0
for i in range(3, len(data)):
    x = data[i-3]+data[i-2]+data[i-1]
    y = data[i-2]+data[i-1]+data[i]
    if x < y:
        j += 1
print(j)
print(x)
print(y)