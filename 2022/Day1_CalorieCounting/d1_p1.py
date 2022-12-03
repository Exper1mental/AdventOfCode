input_file = open('input.txt', 'r')
calories = max_calories = 0

for line in input_file:
    stripped_line = line.strip('\n')
    if stripped_line == '':
        if calories > max_calories:
            max_calories = calories
        calories = 0
    else:
        calories += int(stripped_line)
print(max_calories)