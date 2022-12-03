import re

with open("input.txt", "r") as file:
    data = [re.split(" \| | ", x) for x in file.read().split('\n')]
# print(data[0][0:10])
# print(data[0][10:14])

         # 1,2,3,4,5,6,7,8,9,0
matches = [0,0,0,0,0,0,0,0,0,0]

for i,i_d in enumerate(data):
    
    pattern = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for j,j_d in enumerate(i_d[0:10]):
        pattern[j] = "".join(sorted(j_d))
    # print(pattern)
    
    screen = ['0', '1', '2', '3']
    for j2,j2_d in enumerate(i_d[10:14]):
        screen[j2] = "".join(sorted(j2_d))
    # print(screen)
    
    for k,k_d in enumerate(screen): # i_d[10:14]):
        if len(k_d) == 2:
            matches[1] += 1
        elif len(k_d) == 4:
            matches[4] += 1
        elif len(k_d) == 3:
            matches[7] += 1
        elif len(k_d) == 7:
            matches[8] += 1
        # else:
        #      chars = list(k_d)
        
        # if i == 0 and j == 0:
        #     print("".join(list(k_d)))
        #     print("".join(sorted(k_d)))

print(sum(matches))

