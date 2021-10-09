import random

print("HANGMAN")
qwe1 = ["python", "java", "javascript", "php"]
qwe2 = random.choice(qwe1)
qwe3 = {'python':"pyt___", 'java':"jav_", 'javascript':"jav_______", 'php':"php"}
qwe0 = input("Guess the word " + qwe3[qwe2] + ":")
if qwe0 == qwe2:
    print("You survived!")
else:
    print("You lost!")
