cells = list("_" * 9)
cells_x = cells.count("X")
cells_o = cells.count("O")
cells__ = cells.count("_")
winners = 0


def board():
    print("---------")
    print("| ", end="")
    for i in cells[:3]:
        print(i, end=" ")
    print("|")
    print("| ", end="")
    for i in cells[3:6]:
        print(i, end=" ")
    print("|")
    print("| ", end="")
    for i in cells[6:9]:
        print(i, end=" ")
    print("|")
    print("---------")


def rs_lt():
    global winners
    if cells[0] == cells[1] == cells[2] != "_":
        print(cells[0] + " wins")
        winners += 1
    elif cells[3] == cells[4] == cells[5] != "_":
        print(cells[3] + " wins")
        winners += 1
    elif cells[6] == cells[7] == cells[8] != "_":
        print(cells[6] + " wins")
        winners += 1
    elif cells[2] == cells[4] == cells[6] != "_":
        print(cells[2] + " wins")
        winners += 1
    elif cells[0] == cells[4] == cells[8] != "_":
        print(cells[0] + " wins")
        winners += 1
    elif cells[0] == cells[3] == cells[6] != "_":
        print(cells[3] + " wins")
        winners += 1
    elif cells[1] == cells[4] == cells[7] != "_":
        print(cells[4] + " wins")
        winners += 1
    elif cells[2] == cells[5] == cells[8] != "_":
        print(cells[5] + " wins")
        winners += 1
    elif cells__ < 1:
        winners += 1
        print("Draw")


board()
turn = "X"
while True:
    take = input("Enter the coordinates: ")
    coord = list(take)
    x, y = str(coord[2]), str(coord[0])
    if x.isalpha() or y.isalpha() or x == " " or y == " ":
        print("You should enter numbers!")
        continue
    elif y == "1":
        if x == "1":
            if cells[0] != "X" and cells[0] != "O":
                cells[0] = turn
            else:
                print("This cell is occupied! Choose another one!")
                continue
        elif x == "2":
            if cells[1] != "X" and cells[1] != "O":
                cells[1] = turn
            else:
                print("This cell is occupied! Choose another one!")
                continue
        elif x == "3":
            if cells[2] != "X" and cells[2] != "O":
                cells[2] = turn
            else:
                print("This cell is occupied! Choose another one!")
                continue
        else:
            print("Coordinates should be from 1 to 3!")
            continue
    elif y == "2":
        if x == "1":
            if cells[3] != "X" and cells[3] != "O":
                cells[3] = turn
            else:
                print("This cell is occupied! Choose another one!")
                continue
        elif x == "2":
            if cells[4] != "X" and cells[4] != "O":
                cells[4] = turn
            else:
                print("This cell is occupied! Choose another one!")
                continue
        elif x == "3":
            if cells[5] != "X" and cells[5] != "O":
                cells[5] = turn
            else:
                print("This cell is occupied! Choose another one!")
                continue
        else:
            print("Coordinates should be from 1 to 3!")
            continue
    elif y == "3":
        if x == "1":
            if cells[6] != "X" and cells[6] != "O":
                cells[6] = turn
            else:
                print("This cell is occupied! Choose another one!")
                continue
        elif x == "2":
            if cells[7] != "X" and cells[7] != "O":
                cells[7] = turn
            else:
                print("This cell is occupied! Choose another one!")
                continue
        elif x == "3":
            if cells[8] != "X" and cells[8] != "O":
                cells[8] = turn
            else:
                print("This cell is occupied! Choose another one!")
                continue
        else:
            print("Coordinates should be from 1 to 3!")
            continue
    else:
        print("Coordinates should be from 1 to 3!")
        continue
    board()
    rs_lt()
    if winners > 0:
        break
    if turn == "X":
        turn = "O"
    else:
        turn = "X"
