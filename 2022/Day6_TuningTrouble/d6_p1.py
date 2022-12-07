input_str = open('input.txt', 'r').readlines()[0].strip('\n')

for i, char in enumerate(input_str[:-4]):
    temp_str = input_str[i:i+4]
    if len(temp_str) == len(set(temp_str)):
        print(f'first marker after {i+4} ({input_str[i:i+4]})')
        break