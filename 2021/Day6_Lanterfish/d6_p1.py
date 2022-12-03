import numpy as np

with open("input.txt", "r") as file:
    fish = np.array([int(x) for x in file.read().split(',')])

print(fish)

fishes=fish.copy()
days = 80

for k in range(0,days,1):
    for i,j in enumerate(fishes):
        if j > 0:
            fish[i] -= 1
        else:
            fish[i] = 6
            fish = np.append(fish, [8])
    fishes=fish.copy()

print(np.size(fish))