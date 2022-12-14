# Starting items state worry level

# Count the # of times each monkey inspects items over 10000 rounds
# Multiply top two monkeys' items to get monkey business value

class Monkey():
    def __init__(self, items: list, op: list, test: int, if_true: int, if_false: int):
        self.items = items
        self.op = op
        self.test = test
        self.if_true = if_true
        self.if_false = if_false
        self.inspected = 0

monkeys = []
input_file = open('input.txt', 'r').readlines()
for i, line in enumerate(input_file):
    line = line.strip('\n').split(' ')
    if line[0] == 'Monkey':
        items = input_file[i+1].strip('\n').replace(',', '').split(' ')[4:]
        op = input_file[i+2].strip('\n').replace('old', 'x').split(' ')[5:]
        test = int(input_file[i+3].strip('\n').split(' ')[5])
        if_true = int(input_file[i+4].strip('\n').split(' ')[9])
        if_false = int(input_file[i+5].strip('\n').split(' ')[9])
        monkeys.append(Monkey(items, op, test, if_true, if_false))
        
for i in range(10000):
    for j, monkey in enumerate(monkeys):
        monkey_op = monkey.op
        
        while len(monkey.items) > 0:
            monkey.inspected += 1
            item = monkey.items[0]
            item_op = monkey_op.copy()
            for k, op in enumerate(monkey_op):
                if op == 'x':
                    item_op[k] = str(item)
            item_new = eval(''.join(item_op))
            item_new = item_new % 9699690
            if item_new % monkey.test == 0:
                monkeys[monkey.if_true].items.append(str(item_new))
            else:
                monkeys[monkey.if_false].items.append(str(item_new)) 
            del monkey.items[0]
            
    for j, monkey in enumerate(monkeys):
        items = ', '.join(monkey.items)
    
score = []
for i, monkey in enumerate(monkeys):
    score.append(monkey.inspected)
    print(f'Monkey {i} inspected items {monkey.inspected} times.')

score.sort(reverse=True)
monkey_biz = score[0] * score[1]
print(f'Monkey Business: {monkey_biz}')