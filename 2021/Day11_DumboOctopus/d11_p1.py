with open("input_small_p1-s1.txt", "r") as file:
    data = [list(x) for x in file.read().split('\n')]

flashes = 0
i = 0
j = 0
k = 0

def looper(data,i,j,flashes):
    flash = 0
    
    for i,i_d in enumerate(data):
        for j,j_d in enumerate(i_d):
            if int(data[i][j]) > 9:
                data[i][j] = str(int(data[i][j]) - 9)
                flashes += 1
                flash = 1
                
                if i > 0:
                    data[i-1][j] = str(int(data[i-1][j]) + 1)
                if i < len(data)-1:
                    data[i+1][j] = str(int(data[i+1][j]) + 1)
                if j > 0:
                    data[i][j-1] = str(int(data[i][j-1]) + 1)
                if j < len(data[i])-1:
                    data[i][j+1] = str(int(data[i][j+1]) + 1)
                if i > 0 and j > 0:
                    data[i-1][j-1] = str(int(data[i-1][j-1]) + 1)
                if i > 0 and j < len(data[i])-1:
                    data[i-1][j+1] = str(int(data[i-1][j+1]) + 1)
                if i < len(data)-1 and j > 0:
                    data[i+1][j-1] = str(int(data[i+1][j-1]) + 1)
                if i < len(data)-1 and j < len(data[i])-1:
                    data[i+1][j+1] = str(int(data[i+1][j+1]) + 1)
                break
        if flash == 1:
            break
    
    return data,flash,flashes

for k in range(1):
    for i,i_d in enumerate(data):
        for j,j_d in enumerate(i_d):
            data[i][j] = str(int(data[i][j]) + 1)
            if int(data[i][j]) > 9:
                data[i][j] = str(int(data[i][j]) - 9)
                flashes += 1
                flash = 1
                
                if i > 0:
                    data[i-1][j] = str(int(data[i-1][j]) + 1)
                if i < len(data)-1:
                    data[i+1][j] = str(int(data[i+1][j]) + 1)
                if j > 0:
                    data[i][j-1] = str(int(data[i][j-1]) + 1)
                if j < len(data[i])-1:
                    data[i][j+1] = str(int(data[i][j+1]) + 1)
                if i > 0 and j > 0:
                    data[i-1][j-1] = str(int(data[i-1][j-1]) + 1)
                if i > 0 and j < len(data[i])-1:
                    data[i-1][j+1] = str(int(data[i-1][j+1]) + 1)
                if i < len(data)-1 and j > 0:
                    data[i+1][j-1] = str(int(data[i+1][j-1]) + 1)
                if i < len(data)-1 and j < len(data[i])-1:
                    data[i+1][j+1] = str(int(data[i+1][j+1]) + 1)
                
                while flash == 1:
                    data,flash,flashes = looper(data,i,j,flashes)
print(flashes)
print(f'{data[0]}\n{data[1]}\n{data[2]}\n{data[3]}\n{data[4]}')
