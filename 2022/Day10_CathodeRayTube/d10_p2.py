# X=1 to start
# addx V adds V to X after 2 cycles
# Signal strength = X * cycle number
# noop completes a cycle

# Goal:


input_file = open('input_test_large.txt', 'r').readlines()
cycle = 1
adder = {}
delay = 0
first = True
x = 1

for i, line in enumerate(input_file):
    line = line.strip('\n').split(' ')
    if line[0] == 'addx':
        cycle += 2
        if first:
            adder[cycle] = [x + int(line[1]), int(line[1])]
            first = False
            prev_key = cycle
        else:
            adder[cycle] = [adder.get(prev_key)[0] + int(line[1]), int(line[1])]
            prev_key = cycle
    else:
        cycle += 1

x_vals = {}
cycles = [40, 80, 120, 160, 200, 240]

print(adder.keys())

i_old = 0
pixels = ''
count = 0
for i in adder.keys():
    if i // 40 != count:
        print(pixels)
        pixels = ''
        count += 1
    
    x = adder.get(i)[0]
    if i-x <=2 and i-x >= 0:
        for j in range(i_old, i):
            pixels = pixels + '#'
    else:
        for j in range(i_old, i):
            pixels = pixels + '.'
            
    i_old = i
        
print(adder)
# print()
# print(x_vals)