# Each three sacks corresponds to a group
# a-z priority 1-26
# A-Z priority 27-52

input_file = open('input.txt', 'r').readlines()
score = 0
pos = 0

while pos in range(len(input_file[:-2])):
    line1 = list(set(input_file[pos].strip('\n')))
    line2 = list(set(input_file[pos+1].strip('\n')))
    line3 = list(set(input_file[pos+2].strip('\n')))
    
    char_list = []
    for char in line1:
        if char in line2 and char in line3:
            char_list.append(char)
            pos += 3
            break
    
    if char.islower():
        score += ord(char)-96 
    else:
        score += ord(char)-38
        
print(score)
    