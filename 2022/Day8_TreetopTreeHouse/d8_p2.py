input_file = open('input.txt', 'r').readlines()
rows = len(input_file)
cols = len(input_file[0].strip('\n'))
max_score = 0


def looper(i, j, h, row_step, col_step):
    count = 0
    k = i
    l = j
    while True:
        if k in [-1, rows] or l in [-1, cols]:
            break
        if k != i or l != j:
            if h > int(input_file[k].strip('\n')[l]):
                count += 1
            else:
                count += 1
                break
        k += row_step
        l += col_step        
    return count

def tree_score(i, j, h):    
    top = looper(i, j, h, -1, 0)
    bottom = looper(i, j, h, 1, 0)
    left = looper(i, j, h, 0, -1)
    right = looper(i, j, h, 0, 1)
    score = left*right*top*bottom
    return score

for i, line in enumerate(input_file):
    line = line.strip('\n')
    for j, tree_h in enumerate(line):
        score = tree_score(i, j, int(tree_h))
        if score > max_score:
            max_score = score
print(max_score)