with open("input.txt", "r") as file:
    data = [list(x) for x in file.read().split('\n')]
risk = 0

for i,i_d in enumerate(data):
    for j,j_d in enumerate(i_d):
        if not i == 0 and not i == len(data)-1: # Not on top or bottom side
            if not j == 0 and not j == len(i_d)-1: # Not on left or right side
                if j_d < data[i-1][j] and j_d < data[i+1][j] and j_d < data[i][j-1] and j_d < data[i][j+1]:
                    print(j_d, end=' NN')
                    risk += int(j_d)+1
            elif j == 0: # On the left side
                if j_d < data[i-1][j] and j_d < data[i+1][j] and j_d < data[i][j+1]:
                    print(j_d, end=' NL')
                    risk += int(j_d)+1
            else: # On right side
                if j_d < data[i-1][j] and j_d < data[i+1][j] and j_d < data[i][j-1]:
                    print(j_d, end=' NR')
                    risk += int(j_d)+1
        elif i == 0: # On the top side
            if not j == 0 and not j == len(i_d)-1: # Not on left or right side
                if j_d < data[i+1][j] and j_d < data[i][j-1] and j_d < data[i][j+1]:
                    print(j_d, end=' TN')
                    risk += int(j_d)+1
            elif j == 0: # On the left side
                if j_d < data[i+1][j] and j_d < data[i][j+1]:
                    print(j_d, end=' TL')
                    risk += int(j_d)+1
            else: # On right side
                if j_d < data[i+1][j] and j_d < data[i][j-1]:
                    print(j_d, end=' TR')
                    risk += int(j_d)+1
        else: # On the bottom side
            if not j == 0 and not j == len(i_d)-1: # Not on left or right side
                if j_d < data[i-1][j] and j_d < data[i][j-1] and j_d < data[i][j+1]:
                    print(j_d, end=' BN')
                    risk += int(j_d)+1
            elif j == 0: # On the left side
                if j_d < data[i-1][j] and j_d < data[i][j+1]:
                    print(j_d, end=' BL')
                    risk += int(j_d)+1
            else: # On right side
                if j_d < data[i-1][j] and j_d < data[i][j-1]:
                    print(j_d, end=' BR')
                    risk += int(j_d)+1

print('\nRisk:', risk)