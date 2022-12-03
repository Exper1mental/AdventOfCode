# Points
# 1 for Rock (A), 2 for Paper (B), 3 for Scissors (C)
# X ~ You lose, Y ~ Draw, Z ~ Win
# 0 for loss, 3 for draw, 6 for win
# Rock (A,X) < Paper (B,Y) < Scissors (C,Z) < Rock (A,X)
opponent_hands = {'A': [1, 'rock'], 'B': [2, 'paper'], 'C': [3, 'scissors']}
# player_hands = {'X': [1, 'rock'], 'Y': [2, 'paper'], 'Z': [3, 'scissors']}

plays = {'ax': [6, 0, 3], 'ay': [3, 3, 1], 'az': [0, 6, 2],
         'bx': [6, 0, 1], 'by': [3, 3, 2], 'bz': [0, 6, 3],
         'cx': [6, 0, 2], 'cy': [3, 3, 3], 'cz': [0, 6, 1],}

input_file = open('input.txt', 'r').readlines()
opponent_score = 0
player_score = 0

for line in input_file:
    opponent, player = line.strip('\n').split(' ')
    query = f'{opponent}{player}'.lower()
    # print(f'{opponent}, {user}')
    opponent_score += opponent_hands[opponent][0] + plays[query][0]
    player_score += plays[query][2] + plays[query][1]
    # print(player_score)
    
print(f'Opponent: {opponent_score}, Player: {player_score}')

    
    