# X=1 to start
# addx V adds V to X after 2 cycles
# Signal strength = X * cycle number
# noop completes a cycle

# Goal:
# Find signal strength in 20th, 60th, 100th, 140th, 180th, and 220th cycles

input_file = open('input_test_large.txt', 'r').readlines()
cycle = 1
cycles = [20, 60, 100, 140, 180, 220]
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
sig_strength = []
for i in cycles:
    for j in range(i, 0, -1):
        x = adder.get(j)
        if x is not None:
            x_vals[i] = x[0]
            sig_strength.append(i*x[0])
            break
print(adder)
# print()
# print(x_vals)
# print(sig_strength)
print(sum(sig_strength))
