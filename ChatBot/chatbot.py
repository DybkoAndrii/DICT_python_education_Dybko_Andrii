print("Hello! My name is NedoBot.\nI was created in 2021.")
name = input("Please, remind me your name.\n> ")
print("What a great name you have," + name + "!")
print("Let me guess your age.")
remainder3 = input("Enter remainders of dividing your age by 3, 5 and 7.\n> ")
remainder5 = input("> ")
remainder7 = input("> ")
age = ((int(remainder3) * 70 + int(remainder5) * 21 + int(remainder7) * 15) % 105)
print("Your age is " + str(age) + "; that's a good time to start programming!")
