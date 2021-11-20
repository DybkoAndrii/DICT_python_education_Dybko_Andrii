import random

dmn = [[x, y] for x in range(7) for y in range(x, 7)]
players = []
while len(players) != 14:
    qwe = random.choice(dmn)
    players.append(qwe)
    dmn.remove(qwe)
player, computer = players[:7], players[7:]
lst = [i for i in players if i[0] == i[1]]
max_num = -1
snake = []
for i in lst:
    if i[0] > max_num:
        max_num = i[0]
        snake = i
if snake in player:
    player.remove(snake)
    status = "player"
else:
    computer.remove(snake)
    status = "computer"
print("Stock pieces: {}".format(dmn))
print("Computer pieces: {}\nPlayer pieces: {}".format(computer, player))
print("Domino snake: {}\nStatus: {}".format(snake, status))
