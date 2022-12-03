import numpy as np
filename = 'input.txt'
data = np.loadtxt(filename, delimiter=',', skiprows=0, dtype=int)
j = 0
for i in range(1, len(data)):
    if data[i-1] < data[i]:
        j += 1
print(j)