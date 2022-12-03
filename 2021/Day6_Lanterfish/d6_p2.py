with open("input.txt", "r") as file:
    fish = [int(x) for x in file.read().split(',')]

array = [0, fish.count(1), fish.count(2), fish.count(3), fish.count(4), fish.count(5), 0, 0, 0]
days = 256

for k in range(0,days,1):
    newfish = array[0]
    for i in range(1,len(array),1):
        array[i-1] = array[i]
    array[-1] = newfish
    array[-3] = array[-3] + newfish

print(sum(array))