def my_function(j,fun_bingo,row):
    for k in enumerate(row):
        if j[1] == k[1]:
            row[k[0]] = '-1'
        if fun_bingo != 1:
            sum_h = sum(int(x) for x in row)
            sum_v = sum(int(x) for x in (row1[k[0]],row2[k[0]],row3[k[0]],row4[k[0]],row5[k[0]]))
            if sum_h == -5 or sum_v == -5:
                fun_bingo = 1
                print(f'bingo in chart {i} after {j[0]} draws having drawn {j[1]}')
    return fun_bingo,row

def my_new_function(row):
    for k in enumerate(row):
        if k[1] == '-1':
            row[k[0]] = '0'
    sum_h = sum(int(x) for x in row)
    # print(row)
    return sum_h


with open("input.txt", "r") as file:
    lines = file.read().splitlines()
    draws = lines[0].split(',')
    bingo_draws = []

for i in range(int((len(lines)-1)/6)):
    bingo = 0
    row1 = lines[6*i+2].split()
    row2 = lines[6*i+3].split()
    row3 = lines[6*i+4].split()
    row4 = lines[6*i+5].split()
    row5 = lines[6*i+6].split()
    #if i == 0:
        # print(f'{row1}\n{row2}\n{row3}\n{row4}\n{row5}')
    for j in enumerate(draws):
        bingo,row1 = my_function(j,bingo,row1)
        bingo,row2 = my_function(j,bingo,row2)
        bingo,row3 = my_function(j,bingo,row3)
        bingo,row4 = my_function(j,bingo,row4)
        bingo,row5 = my_function(j,bingo,row5)
        # print(f'\n{row1}\n{row2}\n{row3}\n{row4}\n{row5}')
        if bingo == 1:
            bingo_draws.append(j[0])
            break

temp = max(bingo_draws)
res = [l for l, m in enumerate(bingo_draws) if m == temp]
print(f'Chart requiring maximum draws: {res[0]} with {bingo_draws[res[0]]} draws and {int(draws[bingo_draws[res[0]]])} having been drawn')

bingo = 0
row1 = lines[6*res[0]+2].split()
row2 = lines[6*res[0]+3].split()
row3 = lines[6*res[0]+4].split()
row4 = lines[6*res[0]+5].split()
row5 = lines[6*res[0]+6].split()

for j in enumerate(draws):
    bingo,row1 = my_function(j,bingo,row1)
    bingo,row2 = my_function(j,bingo,row2)
    bingo,row3 = my_function(j,bingo,row3)
    bingo,row4 = my_function(j,bingo,row4)
    bingo,row5 = my_function(j,bingo,row5)
    if bingo == 1:
        # print(f'{row1}\n{row2}\n{row3}\n{row4}\n{row5}\n')
        bingo_draws.append(j[0])
        break

sum1 = my_new_function(row1)
sum2 = my_new_function(row2)
sum3 = my_new_function(row3)
sum4 = my_new_function(row4)
sum5 = my_new_function(row5)

total_sum = sum(int(x) for x in (sum1,sum2,sum3,sum4,sum5))
num_drawn = int(draws[bingo_draws[res[0]]])
output = total_sum * num_drawn
print(total_sum,num_drawn,output)
# print(int((len(lines)-1)/6), (len(lines)-1)/6)