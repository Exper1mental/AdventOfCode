# head can overlap with tail
# Use dict or list pairing them?

# head and tail must always be touching
#   diagonally adjacent or overlapping
#   if so, moving tail not required
#   otherwise, moving tail necessary

## For moving tail
# If head and tail are in same row or column
#   if head moves two steps away in that row
#   or column, the tail must also move a step
#   the same direction

# If head and tail not touching and not in same row/column
#   tail must move diagonally one step towards head
#   (one step towards head and one step towards heads row/column)

# ASSUME the head and tail start at the same position
# L -> left
# R -> right
# U -> up
# D -> down

## GOAL
# Count:
# Unique positions of the tail of the rope. (Append list with position and then run unique on it)
# set(list)

def iterator(i):
    if abs(i) == i:
        return 1
    else:
        return -1

def head_mover(line, head):
    if line[0] == 'U':
        head[0] -= 1
    elif line[0] == 'D':
        head[0] += 1
    elif line[0] == 'L':
        head[1] -= 1
    else:
        head[1] += 1
    return head
 
def tail_mover(head, tail):
    r = head[0] - tail[0]
    c = head[1] - tail[1]
    
    if (r == 0 or c == 0) and abs(r) + abs(c) > 1: # If same row/column
        if r == 0:
            tail[1] += iterator(c)
        elif c == 0:
            tail[0] += iterator(r)
            
    elif abs(r) + abs(c) > 2: # If diagonal
        tail[0] += iterator(r)
        tail[1] += iterator(c)
    return tail

input_file = open('input_test.txt', 'r').readlines()
head = [0,0] # r,c
tail = [0,0] # r,c
head_history = ['0 0']
tail_history = ['0 0']

for i, line in enumerate(input_file):
    line = line.strip('\n').split(' ')
    
    for j in range(int(line[1])):
        head = head_mover(line, head)
        head_history.append(f'{head[0]} {head[1]}')
        tail = tail_mover(head, tail)
        tail_history.append(f'{tail[0]} {tail[1]}')

print(len(set(tail_history)))
