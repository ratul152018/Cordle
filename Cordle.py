import random
import os


def make_raw(str):
    str = str.replace("\n",'')
    str = str.upper()
    return str


with open("words.txt", 'r') as f:
    word_list = f.readlines()
    
random = random.randint(0,len(word_list))
word = make_raw(word_list[random])


exam = ['-', '-', '-', '-', '-']

os.system("color 02")
os.system("cls")

print("""
+ ================================ +
|   CORDLE - WORDLE in god mode    |
+ ================================ +

Guess the CORDLE in 6 tries.

    Examples:
        Draft
        DR^--

    The letter D and R is in the word and in the correct spot.
    The letter A is in the word but in the wrong spot.
    The letter U is not in the word in any spot.

    '?' - to reveal the word (or surrender)

    Type and hit the enter button to submit.
    Let's start..
    
""")

for try_count in range(1,7):
    guess = make_raw(input())

    if guess == "?":
        break

    while len(guess) != 5:
        print("invalid input, Input 5 letters word only")
        guess = make_raw(input())
    
    for z in range(5):
        if guess[z] == word[z]: #green
            exam[z] = guess[z]

        elif guess[z] in word: #yellow
            exam[z] = '^'

        else: #gray
            exam[z] = '-'

    print(''.join(exam))

    if guess == word:
        print("Won in", try_count, "try!!")
        break

print(f"Game Over '{word}' was secret the word")
key = input("Press enter to exit!")
