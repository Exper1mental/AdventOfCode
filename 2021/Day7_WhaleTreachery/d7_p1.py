with open("input.txt", "r") as file:
    crab_pos = [int(x) for x in file.read().split(',')]

fuel_cost=crab_pos.copy()
max_pos = max(crab_pos)
min_pos = min(crab_pos)
array = [0,0]

for i in range(min_pos, max_pos+1):
    for j,k in enumerate(crab_pos):
        fuel_cost[j] = abs(k-i)
    cost = sum(fuel_cost)
    if cost < array[0] or i == 0:
        array = [cost, i]

print(array)