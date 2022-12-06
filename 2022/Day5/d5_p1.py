input_file = open('input.txt', 'r').readlines()
row_list = []
for i, line in enumerate(input_file):
    # Identify column header line
    if len(line) > 1:
        if line[1] == '1':
            col_header_row = col_height = i
            break
    # Create 2-level list of row contents
    line = line.strip('\n')
    char_list = []
    for i in range(0,len(line),4):
        char = line[i+1]
        char_list.append(char)
    row_list.append(char_list)

# Convert row list to column list w/o blank entries
col_list = []
for i in range(len(row_list[0])):
    char_list = ''
    for j in row_list:
        if j[i] != ' ':
            char_list = char_list + j[i]
    col_list.append(char_list)

# Identify and Perform Move Commands
for i, line in enumerate(input_file[col_header_row+2:]):
    entry_list = line.strip('\n').split(' ')
    for j in range(int(entry_list[1])):
        col_list[int(entry_list[5])-1] = col_list[int(entry_list[3])-1][0] + col_list[int(entry_list[5])-1]
        col_list[int(entry_list[3])-1] = col_list[int(entry_list[3])-1][1:]

top_crates = ''
for i, col in enumerate(col_list):
    top_crates = top_crates + col[0]
print(top_crates)