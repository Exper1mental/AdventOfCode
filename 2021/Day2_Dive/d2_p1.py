import numpy as np
filename = 'input.txt'
data = np.loadtxt(filename, delimiter=' ', skiprows=0, usecols=1, dtype=int)
data_str = np.loadtxt(filename, delimiter=' ', skiprows=0, usecols=0, dtype=str)
j = 0
position = 0
depth = 0
aim = 0
for i in range(0, len(data)):
    if data_str[i] == "up":
        aim = aim - data[i]
    elif data_str[i] == "down":
        aim = aim + data[i]
    elif data_str[i] == "forward":
        position = position + data[i]
        depth = depth + aim * data[i]
print(position)
print(depth)
print(aim)
print(position*depth)