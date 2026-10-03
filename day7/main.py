import random
from hangman_words import word_list

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
=========
''', '''
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


chosen_word = random.choice(word_list)

lives = 6

placeholder = ""

for letter in chosen_word:
    placeholder += "_"

print(placeholder)

game_over = False

correct_letters = []

while not game_over:
    print(f"you have {lives} left ")
    guess = input("guess a letter: ").lower()
    if guess in correct_letters:
        print(f"you have already guesses {guess}")

    display = ""

    for letter in chosen_word:
        if guess == letter:
            display += letter
            correct_letters.append(letter)

        elif letter in correct_letters:
            display += letter

        else:
            display += "_"

    print(display)

    if guess not in chosen_word:
        lives -= 1
        print(f"your guessed {guess} is wrong")
        if lives == 0:
            game_over = True
            print("You Lose!")
            print(f"the correct word was {chosen_word}")

    if "_" not in display:
        game_over = True
        print("you win!")

    print(stages[lives])
