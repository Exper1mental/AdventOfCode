input_file = open('input_test.txt', 'r').readlines()
rows = len(input_file)
cols = len(input_file[0])
tree_list = []
max_score = 0

def is_shortest_tree(i, j, h):
    left = 0
    right = 0
    top = 0
    bottom = 0
    
    if i > 0:
        top += 1
    if i < len(input_file)-2:
        bottom += 1
    if j > 0:
        left += 1
    if j < len(input_file[i].strip('\n'))-1:
        right += 1
    
    k = j - 1
    while True: # Check row
        if k < j:
            if h > int(input_file[i].strip('\n')[k]):
                left += 1
                if k > 0:
                    k -= 1
                else:
                    k = j + 1
            else:
                k = j + 1
        elif k > j:
            if h > int(input_file[i].strip('\n')[k]):
                right += 1
                if k < len(input_file[i].strip('\n'))-2:
                    k += 1
                else:
                    break
            else:
                break
            
    k = i - 1
    while True: # Check column
        if k < i:
            if h > int(input_file[k].strip('\n')[j]):
                top += 1
                k -= 1
            else:
                k = i + 1
        elif k > i:
            if h > int(input_file[k].strip('\n')[j]):
                bottom += 1
                k += 1
            else:
                break
    
    score = left*right*top*bottom
    print(left, right, top, bottom, score)
    return score

for i, line in enumerate(input_file):
    line = line.strip('\n')
    for j, tree_h in enumerate(line):
        score = is_shortest_tree(i, j, int(tree_h))
        if score > max_score:
            max_score = score
                

print(max_score)
        
        
    
# Tree visible if top, bottom, left, and right tree are shorter (same height means hidden)
# All trees on edges are visible