# Этап 1.
print("Hello! My name is NedoBot.\nI was created in 2021.")
# Этап 2.
name = input("Please, remind me your name.\n> ")
print("What a great name you have," + name + "!")
# Этап 3.
print("Let me guess your age.")
remainder3 = input("Enter remainders of dividing your age by 3, 5 and 7.\n> ")
remainder5 = input("> ")
remainder7 = input("> ")
age = ((int(remainder3) * 70 + int(remainder5) * 21 + int(remainder7) * 15) % 105)
print("Your age is " + str(age) + "; that's a good time to start programming!")
# Этап 4.
qwe = int(input("Now I will prove to you that I can count to any number you want.\n> "))
qwe1 = list(range(qwe + 1))
for rty in qwe1:
    print(str(rty) + "!")
print("Completed, have a nice day!")
# Этап 5.
print("""Let's test your programming knowledge.
   Why do we use methods?
1. To repeat a statement multiple times.
2. To decompose a program into several small subroutines.
3. To determine the execution time of a program.
4. To interrupt the execution of a program.""")
x = 1
while x == 1:
    answer = int(input("> "))
    if answer == 2:
        print("Completed, have a nice day!")
        break
    else:
        print("Please, try again.")
        continue
print("Congratulations, have a nice day!")
