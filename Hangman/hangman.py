import random

print("HANGMAN")
words = ["python", "java", "javascript", "php"]
word = random.choice(words)
word_set = set(word)
letter = []
wrong_letter = []


def de_sh():
    for letter1 in word:
        if letter1 in letter:
            print(letter1, end='')
        else:
            print('_', end='')


def playing():
    life = 8
    while life > 0:
        print('')
        letter1 = input("Input a letter: ")
        for qwe1 in word:
            if letter1 == qwe1:
                letter.append(letter1)
        if letter1 not in word:
            print("That letter doesn't appear in the word")
        print('')
        life -= 1
        if life > 0:
            de_sh()


print("HANGMAN")
print('')
print(len(word) * '_', end='')
playing()
print("""Thanks for playing!
We'll see how well you did in the next stage""")
