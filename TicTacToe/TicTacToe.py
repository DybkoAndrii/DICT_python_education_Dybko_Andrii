cells = list(input("Enter cells: "))
cells_x = cells.count("X")
cells_o = cells.count("O")
cells__ = cells.count("_")
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
winners = 0


def imp():
    global winners
    if cells[0] == cells[1] == cells[2] != "_":
        winners += 1
    if cells[3] == cells[4] == cells[5] != "_":
        winners += 1
    if cells[6] == cells[7] == cells[8] != "_":
        winners += 1
    if cells[2] == cells[4] == cells[6] != "_":
        winners += 1
    if cells[0] == cells[4] == cells[8] != "_":
        winners += 1
    if cells[0] == cells[3] == cells[6] != "_":
        winners += 1
    if cells[1] == cells[4] == cells[7] != "_":
        winners += 1
    if cells[2] == cells[5] == cells[8] != "_":
        winners += 1


imp()
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
