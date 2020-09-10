from random import choices
ntrials = 15000
player1wins = 0
ndice1 = 3
ndice2 = 2
for i in range(ntrials):
    dice2 = choices(range(1,7), k = ndice2)
    if dice2[0] == dice2[1]:
        continue
    dice1 = choices(range(1,7), k = ndice1)
    if dice1.count(2) > 1 :
        continue
    dice1.sort(reverse = True)
    dice2.sort(reverse = True)
    sum1 = dice1[0] + dice1[1]
    sum2 = dice2[0] + dice2[1]
    if sum1 > sum2:
        player1wins += 1
print("Player 1's win percentage =" , player1wins/ntrials)

# This improves fairness becauses the win percentages are closer to 50/50 than before