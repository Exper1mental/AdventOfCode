import numpy as np
filename = 'input.txt'
data = np.loadtxt(filename, delimiter=',', skiprows=0, usecols=0, dtype=str)

#print(np.size(data,0)) # number of rows
#print(len(data[0])) # length of first string
#print(data[0]) # first string

gamma = ""
epsilon = ""

for i in range(len(data[0])):
    ones = 0
    zeroes = 0
    for j in range(np.size(data,0)):
        #print(data[j][i])
        num = data[j][i]
        if num == '1':
            ones += 1
        elif num == '0':
            zeroes += 1
    if ones > zeroes:
        gamma = gamma + '1'
        epsilon = epsilon + '0'
    else:
        gamma = gamma + '0'
        epsilon = epsilon + '1'

print(gamma)
print(epsilon)
print(int(gamma, 2))
print(int(epsilon, 2))

print(int(gamma, 2) * int(epsilon, 2))

