cells = list(input("Enter cells: "))
print("---------")
print("| ", end="")
for u in cells[:3]:
    print(u, end=" ")
print("|")
print("| ", end="")
for o in cells[3:6]:
    print(o, end=" ")
print("|")
print("| ", end="")
for i in cells[6:]:
    print(i, end=" ")
print("|")
print("---------")
