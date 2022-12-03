import numpy as np

with open("input.txt", "r") as file:
    lines = file.read().splitlines()

    x_max = 0
    y_max = 0
    
    for i in enumerate(lines):
        row = lines[i[0]].split(' ')
        
        start = row[0].split(',')
        if int(start[0]) > x_max:
            x_max = int(start[0])
        if int(start[1]) > y_max:
            y_max = int(start[1])
        
        finish = row[2].split(',')
        if int(finish[0]) > x_max:
            x_max = int(finish[0])
        if int(finish[1]) > y_max:
            y_max = int(finish[1])
    
    line_count = np.zeros((y_max+1, x_max+1))
    
    for i in enumerate(lines):
        row = lines[i[0]].split(' ')
        start = row[0].split(',')
        finish = row[2].split(',')
        x_low = min(int(start[0]), int(finish[0]))
        x_high = max(int(start[0]), int(finish[0]))
        y_low = min(int(start[1]), int(finish[1]))
        y_high = max(int(start[1]), int(finish[1]))
        if x_low != x_high and y_low != y_high:
            continue
        for j in range(x_low, x_high+1):
            for k in range(y_low, y_high+1):
                line_count[k,j] += 1

    k = 0
    for i in range(y_max+1):
        for j in range(x_max+1):
            if line_count[i,j] > 1:
                k += 1

    # print(line_count)
    print(k)