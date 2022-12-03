# Points
# 1 for Rock (A,X), 2 for Paper (B,Y), 3 for Scissors (C,Z)
# 0 for loss, 3 for draw, 6 for win
# Rock (A,X) < Paper (B,Y) < Scissors (C,Z) < Rock (A,X)


opponent_hands = {'A': [1, 'rock'], 'B': [2, 'paper'], 'C': [3, 'scissors']}
player_hands = {'X': [1, 'rock'], 'Y': [2, 'paper'], 'Z': [3, 'scissors']}

plays = {'ax': [3, 3], 'ay': [0, 6], 'az': [6, 0],
         'bx': [6, 0], 'by': [3, 3], 'bz': [0, 6],
         'cx': [0, 6], 'cy': [6, 0], 'cz': [3, 3],}

input_file = open('input.txt', 'r').readlines()
opponent_score = 0
player_score = 0

for line in input_file:
    opponent, player = line.strip('\n').split(' ')
    query = f'{opponent}{player}'.lower()
    # print(f'{opponent}, {user}')
    opponent_score += opponent_hands[opponent][0] + plays[query][0]
    player_score += player_hands[player][0] + plays[query][1]
    
print(f'Opponent: {opponent_score}, Player: {player_score}')

    
    