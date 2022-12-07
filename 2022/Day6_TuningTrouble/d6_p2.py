input_str = open('input.txt', 'r').readlines()[0].strip('\n')
chars = 14

for i, char in enumerate(input_str[:-char]):
    temp_str = input_str[i:i+char]
    if len(temp_str) == len(set(temp_str)):
        print(f'first marker after {i+char} ({input_str[i:i+char]})')
        break