import re

with open("input.txt", "r") as file:
    data = [re.split(" \| | ", x) for x in file.read().split('\n')]

         # 0,1,2,3,4,5,6,7,8,9
matches = [0,0,0,0,0,0,0,0,0,0]
total = 0

for i,i_d in enumerate(data):
    
    pattern = ['', '', '', '', '', '', '', '', '', '']
    for j,j_d in enumerate(i_d[0:10]):
        pattern[j] = "".join(sorted(j_d))
        if len(j_d) == 2:
            right = sorted(j_d) # Pattern for one (aka the right side)
        elif len(j_d) == 4:
            four = sorted(j_d) # Pattern for four
    
    screen_in = ['', '', '', '']
    for j2,j2_d in enumerate(i_d[10:14]):
        screen_in[j2] = "".join(sorted(j2_d))
    
    screen_out = ['','','','']
    for k,k_d in enumerate(screen_in): # i_d[10:14]):
        if len(k_d) == 2:
            matches[1] += 1 # One
            screen_out[k] = '1'
        elif len(k_d) == 4:
            matches[4] += 1 # Four
            screen_out[k] = '4'
        elif len(k_d) == 3:
            matches[7] += 1 # Seven
            screen_out[k] = '7'
        elif len(k_d) == 7:
            matches[8] += 1 # Eight
            screen_out[k] = '8'
        elif re.search(right[0], k_d) and re.search(right[1], k_d) and len(k_d) == 5:
            matches[3] += 1 # Three
            screen_out[k] = '3'
        elif len(k_d) == 5:
            l = 0
            if re.search(four[0], k_d):
                l += 1
            if re.search(four[1], k_d):
                l += 1
            if re.search(four[2], k_d):
                l += 1
            if re.search(four[3], k_d):
                l += 1
            
            if l == 2:
                matches[2] += 1 # Two
                screen_out[k] = '2'
            elif l == 3:
                matches[5] += 1 # Five
                screen_out[k] = '5'
        elif len(k_d) == 6:
            l = 0
            if re.search(four[0], k_d):
                l += 1
            if re.search(four[1], k_d):
                l += 1
            if re.search(four[2], k_d):
                l += 1
            if re.search(four[3], k_d):
                l += 1
            
            if l == 4:
                matches[9] += 1 # Nine
                screen_out[k] = '9'
            elif re.search(right[0], k_d) and re.search(right[1], k_d):
                matches[0] += 1 # Zero
                screen_out[k] = '0'
            else:
                matches[6] += 1 # Six
                screen_out[k] = '6'
    #print("".join(screen_out))
    total += int("".join(screen_out))

# print('[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]')
# print(matches)
print(total)