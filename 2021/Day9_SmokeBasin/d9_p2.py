with open("input.txt", "r") as file:
    data = [list(x) for x in file.read().split('\n')]
risk = 0

def basin(trys):
    count = 0
    while len(trys) > 0:
        if int(data[trys[0][0]][trys[0][1]]) != -1 and int(data[trys[0][0]][trys[0][1]]) != 9:
            data[trys[0][0]][trys[0][1]] = '-1' # Set the value to -1 to indicate that it has been visited
            count += 1
            if trys[0][0] < len(data)-1:
                trys.extend([[trys[0][0]+1, trys[0][1]]])
            if trys[0][0] > 0:
                trys.extend([[trys[0][0]-1, trys[0][1]]])
            if trys[0][1] < len(data[0])-1:
                trys.extend([[trys[0][0], trys[0][1]+1]])
            if trys[0][1] > 0:
                trys.extend([[trys[0][0], trys[0][1]-1]])
        trys.pop(0)
    return data,count

bsize = []
for i,i_d in enumerate(data):
    for j,j_d in enumerate(i_d):
        if int(j_d) == -1 or int(j_d) == 9:
            continue
        if not i == 0 and not i == len(data)-1: # Not on top or bottom side
            if not j == 0 and not j == len(i_d)-1: # Not on left or right side
                if int(j_d) < int(data[i-1][j]) and int(j_d) < int(data[i+1][j]) and int(j_d) < int(data[i][j-1]) and int(j_d) < int(data[i][j+1]):
                    risk += int(j_d)+1
                    data,count = basin([[i,j], [i-1,j], [i+1,j], [i,j-1], [i,j+1]])
                    bsize.append(count)
            elif j == 0: # On the left side
                if int(j_d) < int(data[i-1][j]) and int(j_d) < int(data[i+1][j]) and int(j_d) < int(data[i][j+1]):
                    risk += int(j_d)+1
                    data,count = basin([[i,j], [i-1,j], [i+1,j], [i,j+1]])
                    bsize.append(count)
            else: # On right side
                if int(j_d) < int(data[i-1][j]) and int(j_d) < int(data[i+1][j]) and int(j_d) < int(data[i][j-1]):
                    risk += int(j_d)+1
                    data,count = basin([[i,j], [i-1,j], [i+1,j], [i,j-1]])
                    bsize.append(count)
        elif i == 0: # On the top side
            if not j == 0 and not j == len(i_d)-1: # Not on left or right side
                if int(j_d) < int(data[i+1][j]) and int(j_d) < int(data[i][j-1]) and int(j_d) < int(data[i][j+1]):
                    risk += int(j_d)+1
                    data,count = basin([[i,j], [i+1,j], [i,j-1], [i,j+1]])
                    bsize.append(count)
            elif j == 0: # On the left side
                if int(j_d) < int(data[i+1][j]) and int(j_d) < int(data[i][j+1]):
                    risk += int(j_d)+1
                    data,count = basin([[i,j], [i+1,j], [i,j+1]])
                    bsize.append(count)
            else: # On right side
                if int(j_d) < int(data[i+1][j]) and int(j_d) < int(data[i][j-1]):
                    risk += int(j_d)+1
                    data,count = basin([[i,j], [i+1,j], [i,j-1]])
                    bsize.append(count)
        else: # On the bottom side
            if not j == 0 and not j == len(i_d)-1: # Not on left or right side
                if int(j_d) < int(data[i-1][j]) and int(j_d) < int(data[i][j-1]) and int(j_d) < int(data[i][j+1]):
                    risk += int(j_d)+1
                    data,count = basin([[i,j], [i-1,j], [i,j-1], [i,j+1]])
                    bsize.append(count)
            elif j == 0: # On the left side
                if int(j_d) < int(data[i-1][j]) and int(j_d) < int(data[i][j+1]):
                    risk += int(j_d)+1
                    data,count = basin([[i,j], [i-1,j], [i,j+1]])
                    bsize.append(count)
            else: # On right side
                if int(j_d) < int(data[i-1][j]) and int(j_d) < int(data[i][j-1]):
                    risk += int(j_d)+1
                    data,count = basin([[i,j], [i-1,j], [i,j-1]])
                    bsize.append(count)

print('\nRisk:', risk)
bsize = sorted(bsize, reverse = True)
print(bsize[0] * bsize[1] * bsize[2])