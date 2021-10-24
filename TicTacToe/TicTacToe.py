cells = list(input("Enter cells: "))
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
    if winners == 0 or winners == 1:
        if cells_x == cells_o + 1 or cells_x == cells_o - 1 or cells_x == cells_o:
            if cells[0] == cells[1] == cells[2] != "_":
                print(cells[0] + " wins")
            elif cells[3] == cells[4] == cells[5] != "_":
                print(cells[3] + " wins")
            elif cells[6] == cells[7] == cells[8] != "_":
                print(cells[6] + " wins")
            elif cells[2] == cells[4] == cells[6] != "_":
                print(cells[2] + " wins")
            elif cells[0] == cells[4] == cells[8] != "_":
                print(cells[0] + " wins")
            elif cells[0] == cells[3] == cells[6] != "_":
                print(cells[3] + " wins")
            elif cells[1] == cells[4] == cells[7] != "_":
                print(cells[4] + " wins")
            elif cells[2] == cells[5] == cells[8] != "_":
                print(cells[5] + " wins")
            elif cells__ > 0:
                print("Game not finished")
            else:
                print("Draw")
        else:
            print("Impossible")
    else:
        print("Impossible")


board()
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
                cells[0] = "X"
            else:
                print("This cell is occupied! Choose another one!")
                continue
        elif x == "2":
            if cells[1] != "X" and cells[1] != "O":
                cells[1] = "X"
            else:
                print("This cell is occupied! Choose another one!")
                continue
        elif x == "3":
            if cells[2] != "X" and cells[2] != "O":
                cells[2] = "X"
            else:
                print("This cell is occupied! Choose another one!")
                continue
        else:
            print("Coordinates should be from 1 to 3!")
            continue
    elif y == "2":
        if x == "1":
            if cells[0] != "X" and cells[0] != "O":
                cells[0] = "X"
            else:
                print("This cell is occupied! Choose another one!")
                continue
        elif x == "2":
            if cells[1] != "X" and cells[1] != "O":
                cells[1] = "X"
            else:
                print("This cell is occupied! Choose another one!")
                continue
        elif x == "3":
            if cells[2] != "X" and cells[2] != "O":
                cells[2] = "X"
            else:
                print("This cell is occupied! Choose another one!")
                continue
        else:
            print("Coordinates should be from 1 to 3!")
            continue
    elif y == "3":
        if x == "1":
            if cells[0] != "X" and cells[0] != "O":
                cells[0] = "X"
            else:
                print("This cell is occupied! Choose another one!")
                continue
        elif x == "2":
            if cells[1] != "X" and cells[1] != "O":
                cells[1] = "X"
            else:
                print("This cell is occupied! Choose another one!")
                continue
        elif x == "3":
            if cells[2] != "X" and cells[2] != "O":
                cells[2] = "X"
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
    break
