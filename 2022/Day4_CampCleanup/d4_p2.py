
input_file = open('input.txt', 'r').readlines()
count = 0

for line in input_file:
    elf1, elf2 = line.strip('\n').split(',')
    elf1, elf2 = [elf1.split('-'), elf2.split('-')]
    if int(elf1[0]) >= int(elf2[0]) and int(elf1[0]) <= int(elf2[1]):
        count += 1
    elif int(elf1[1]) >= int(elf2[0]) and int(elf1[1]) <= int(elf2[1]):
        count += 1
    elif int(elf1[0]) <= int(elf2[0]) and int(elf1[1]) >= int(elf2[1]):
        count += 1
print(count)