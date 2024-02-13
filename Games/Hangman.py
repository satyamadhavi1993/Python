import random

words_list = ["Apple", "Strawberry", "Guava", "Cherry", "Pear", "Banana", "Pineapple", "CustardApple",
              "Blueberry", "Watermelon", "Apricot", "Kiwi", "Papaya", "Mango", "Orange"]
numOfLives = 6
chosen_word = [i for i in str(random.choice(words_list)).lower()]
guessed_word = ['_' for i in range(len(chosen_word))]
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


while numOfLives > 0:
    letter = input("Enter your letter :: ").lower()
    for i in range(len(chosen_word)):
        if chosen_word[i] == letter:
            guessed_word[i] = letter
    print(" ".join(guessed_word))
    if letter not in chosen_word:
        numOfLives -= 1
        print(f'Number of lives :: {numOfLives}')
        print(stages[numOfLives])
    if guessed_word == chosen_word:
        print("You won !!")
        break

if numOfLives == 0 and not guessed_word == chosen_word:
    print("Hanged :(")
    print(stages[numOfLives])
