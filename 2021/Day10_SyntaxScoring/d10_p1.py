with open("input.txt", "r") as file:
    data = [x for x in file.read().split('\n')]

i_char = ['(', '[', '{', '<']
o_char = [')', ']', '}', '>']
p_char = [3,57,1197,25137]

err = []
points = 0

for i,i_d in enumerate(data):
    close = []
    for j,j_d in enumerate(list(i_d)):
        if j_d in i_char:
            in_loc = i_char.index(j_d)
            close.append(o_char[in_loc])
        elif j_d in o_char:
            if j_d == close[-1]:
                close.pop()
            else:
                err.extend([[i,j,j_d]])
                break

for k,k_d in enumerate(err):
    k_loc = o_char.index(k_d[2])
    points += p_char[k_loc]

print(points)