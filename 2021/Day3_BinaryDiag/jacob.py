with open('input.txt', 'r') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

num_digits = len(lines[0])
num_zeros = [0 for _ in range(num_digits)]
num_ones = [0 for _ in range(num_digits)]

for line in lines:
    for idx, l in enumerate(line):
        if l == '0':
            num_zeros[idx] += 1
        if l == '1':
            num_ones[idx] += 1

idx = 0

while 1 < len(lines):
    
    new_lines = []
    
    for line in lines:
        
        if num_ones[idx] < num_zeros[idx]:
            most_common_num = '0'
        if num_zeros[idx] <= num_ones[idx]:
            most_common_num = '1'
            
        if line[idx] == most_common_num:
            new_lines.append(line)
            
    lines = new_lines
    idx += 1
    
    num_zeros = [0 for _ in range(num_digits)]
    num_ones = [0 for _ in range(num_digits)]
    
    for line in lines:
        for j, l in enumerate(line):
            if l == '0':
                num_zeros[j] += 1
            if l == '1':
                num_ones[j] += 1

ox_rating = int(lines[0], 2)

with open('input.txt', 'r') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

num_digits = len(lines[0])
num_zeros = [0 for _ in range(num_digits)]
num_ones = [0 for _ in range(num_digits)]

for line in lines:
    for idx, l in enumerate(line):
        if l == '0':
            num_zeros[idx] += 1
        if l == '1':
            num_ones[idx] += 1

idx = 0

while 1 < len(lines):
    
    new_lines = []
    
    for line in lines:
        
        if num_ones[idx] < num_zeros[idx]:
            most_common_num = '0'
        if num_zeros[idx] <= num_ones[idx]:
            most_common_num = '1'
        
        if line[idx] != most_common_num:
            new_lines.append(line)
            
    lines = new_lines
    idx += 1
    
    num_zeros = [0 for _ in range(num_digits)]
    num_ones = [0 for _ in range(num_digits)]
    
    for line in lines:
        for j, l in enumerate(line):
            if l == '0':
                num_zeros[j] += 1
            if l == '1':
                num_ones[j] += 1
    
co2_rating = int(lines[0], 2)

print(ox_rating, co2_rating)
print(ox_rating * co2_rating)