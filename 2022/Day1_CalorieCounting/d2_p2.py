input_file = open('input.txt', 'r').readlines()
calories = 0
calories_list = []

for line in input_file:
    stripped_line = line.strip('\n')
    if stripped_line == '':
        calories_list.append(calories)
        calories = 0
    else:
        calories += int(stripped_line)
calories_list.append(calories)

calories_list = sorted(calories_list)
top_three = calories_list[-3:]
print(sum(top_three))