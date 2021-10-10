import random

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
        if len(letter1) == 0 or len(letter1) > 1:
            print('You should input a single letter')
            print('')
            de_sh()
            continue
        if letter1.capitalize() == letter1:
            print('Please enter a lowercase English letter')
            print('')
            de_sh()
            continue
        if letter1 in letter:
            print("You've already guessed this letter.")
        if letter1 in wrong_letter:
            print("You've already guessed this letter.")
        for qwe1 in word:
            if letter1 == qwe1:
                letter.append(letter1)
        if letter1 not in word:
            if letter1 not in wrong_letter:
                wrong_letter.append(letter1)
                print("That letter doesn't appear in the word")
                life -= 1
        print('')
        if life > 0:
            de_sh()
        else:
            print("You lost!")
        if word_set == set(letter):
            print('')
            print("You guessed the word!")
            print("You survived!")
            print('')
            break


print("HANGMAN")
print('')
print(len(word) * '_', end='')
playing()
print("""Thanks for playing!
We'll see how well you did in the next stage""")
