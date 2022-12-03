import numpy as np
filename = 'input.txt'
data_original = np.loadtxt(filename, delimiter=',', skiprows=0, usecols=0, dtype=str)
data_O2 = np.copy(data_original)
data_CO2 = np.copy(data_original)

def my_function(data,fun_i,type):
    if np.size(data,0) != 1: # if there is more than one string
        ones = 0
        zeroes = 0
        
        for j in range(np.size(data,0)): # loop over all strings
            #print(data[j][fun_i])
            index_num = data[j][fun_i]
            if index_num == '1':
                ones += 1
            elif index_num == '0':
                zeroes += 1
        
        if type == "O2":
            if ones >= zeroes:
                num = '1'
            else:
                num = '0'
        elif type == "CO2":
            if ones >= zeroes:
                num = '0'
            else:
                num = '1'
        
        data_new = np.array([])
        for l in range(np.size(data,0)): # loop over all strings
            index_num = data[l][fun_i]
            if num == index_num:
                data_new = np.append(data_new, data[l])
        data = np.copy(data_new)
    return data

#print(np.size(data,0)) # number of rows
#print(len(data[0])) # length of first string
#print(data[0]) # first string

for i in range(len(data_original[0])): # loop over all characters in first string
    data_O2 = my_function(data_O2, i, 'O2')
    data_CO2 = my_function(data_CO2, i, 'CO2')
    
# print(data_O2[0])
# print(data_CO2[0])
print(int(data_O2[0], 2))
print(int(data_CO2[0], 2))

print(int(data_O2[0], 2) * int(data_CO2[0], 2))

