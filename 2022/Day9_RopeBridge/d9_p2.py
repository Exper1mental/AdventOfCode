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

input_file = open('input.txt', 'r').readlines()
knots = [[0,0], [0,0], [0,0], [0,0], [0,0], \
         [0,0], [0,0], [0,0], [0,0], [0,0]] # r,c
tail_history = ['0 0']

for i, line in enumerate(input_file):
    line = line.strip('\n').split(' ')
    
    for j in range(int(line[1])):
        knots[0] = head_mover(line, knots[0])
        
        for k in range(9):
            knots[k+1] = tail_mover(knots[k], knots[k+1])
            if k == 8:
                tail_history.append(f'{knots[k+1][0]} {knots[k+1][1]}')

print(len(set(tail_history)))