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
    status = "computer"
else:
    computer.remove(snake)
    status = "player"


def playing_field():
    print("=" * 70)
    print("Stock size: {}".format(len(dmn)))
    print("Computer pieces: {}".format(len(computer)))
    if len(table) > 6:
        print("\n{}{}{}\n".format(table[:3], "...", table[-3:]))
    else:
        print("\n{}\n".format(table))
    for i in range(len(player)):
        print("{}:{}".format(i + 1, player[i]))


def comp_turn():
    z = random.choice(range(-len(computer), len(computer)+1))
    if z > 0:
        table.append(computer[z-1])
        computer.remove(computer[z-1])
    elif z < 0:
        table.insert(0, computer[-z-1])
        computer.remove(computer[-z-1])
    else:
        table.append(dmn[0])
        dmn.pop(0)


def pl_turn(qwe1):
    if qwe1 > 0:
        table.append(player[qwe1-1])
        player.remove(player[qwe1-1])
    elif qwe1 < 0:
        table.insert(0, player[-qwe1-1])
        player.remove(player[-qwe1-1])
    else:
        table.append(dmn[0])
        dmn.pop(0)


table = [snake]
playing_field()
while True:
    if status == "computer":
        print(input("Status: Computer is about to make a move. Press Enter to continue...\n"))
        comp_turn()
        status = "player"
    else:
        pl_movie = input("Status: It's your turn to make a move. Enter your command.\n ")
        try:
            int(pl_movie)
        except ValueError:
            print("Invalid input. Please try again.")
            continue
        else:
            if int(pl_movie) in range(-len(player), len(player)+1):
                pl_turn(int(pl_movie))
                status = "computer"
            else:
                print("Invalid input. Please try again.")
                continue
    playing_field()
    if len(computer) == 0:
        print("Status: The game is over. The computer won!")
        break
    elif len(player) == 0:
        print("Status: The game is over. You won!")
        break
    elif table[0][0] == table[-1][-1]:
        score = 0
        for t in range(len(table)):
            for s in table[t]:
                if s == table[0][0]:
                    score += 1
        if score == 8:
            print("Status: The game is over. It's a draw!")
            break
