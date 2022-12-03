with open("input.txt", "r") as file:
    data = [x for x in file.read().split('\n')]

i_char = ['(', '[', '{', '<']
o_char = [')', ']', '}', '>']
p_char = [3,57,1197,25137]
s_char = [1,2,3,4]

err = []
points = 0
score = []
l = -1

for i,i_d in enumerate(data):
    row_score = 0
    close = []
    for j,j_d in enumerate(list(i_d)):
        l_err = 0
        if j_d in i_char:
            in_loc = i_char.index(j_d)
            close.append(o_char[in_loc])
        elif j_d in o_char:
            if j_d == close[-1]:
                close.pop()
            else:
                l_err = 1
                l += 1
                err.extend([[i,j,j_d]])
                break
    if l_err == 1:
        l_loc = o_char.index(err[l][2])
        points += p_char[l_loc]
    else:
        for k,k_d in enumerate(reversed(close)):
            out_loc = o_char.index(k_d)
            row_score *= 5
            row_score += s_char[out_loc]
        score.append(row_score)

print(points)
print(sorted(score)[int((len(score)-1)/2)])