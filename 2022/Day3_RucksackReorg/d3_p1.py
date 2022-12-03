# All sack items split evenly between two compartments
# a-z priority 1-26
# A-Z priority 27-52

input_file = open('input.txt', 'r').readlines()
score = 0

for line in input_file:
    line = line.strip('\n')
    line_len = len(line)
    pack1 = set(line[:int(line_len/2)])
    pack2 = set(line[int(line_len/2):])
    pack2_list = list(pack2)
    
    char_list = []
    for char in pack1:
        if char in pack2_list:
            char_list.append(char)
    
    for char in char_list:
        if char.islower():
            score += ord(char)-96 
        else:
            score += ord(char)-38
        
print(score)
    