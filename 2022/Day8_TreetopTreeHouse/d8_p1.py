input_file = open('input.txt', 'r').readlines()
rows = len(input_file)
cols = len(input_file[0])
visible_trees = 0
hidden_trees = 0

def is_shortest_tree(i, j, h):
    left = False
    right = False
    top = False
    bottom = False
    
    for k in range(len(input_file[i].strip('\n'))): # Check row
        if k < j:
            if h <= int(input_file[i][k]):
                left = True
        elif k > j:
            if h <= int(input_file[i][k]):
                right = True
    for k in range(len(input_file)): # Check column
        if k < i:
            if h <= int(input_file[k][j]):
                top = True
        elif k > i:
            if h <= int(input_file[k][j]):
                bottom = True
    
    if left and right and top and bottom:
        return True
    
    return False

for i, line in enumerate(input_file):
    line = line.strip('\n')
    for j, tree_h in enumerate(line):
        if i == 0 or i == rows-1 or j == 0 or j == cols-2:
            visible_trees += 1
        else:
            if is_shortest_tree(i, j, int(tree_h)):
                hidden_trees += 1
            else:
                visible_trees += 1
                
print(visible_trees, hidden_trees)