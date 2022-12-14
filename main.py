
import random
# replit needs to be installed.
from replit import clear
from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

# Import the logo from hangman_art.py and print it at the start of the game.xxx
from hangman_art import logo
print(logo)

# Testing code
# print(f'Chosen word: {chosen_word}.')

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("| Guess a letter: |").lower()

    clear()
# If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"{guess}, Has already been guessed.")
    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    
    if guess not in chosen_word:
        print(guess + " is not in the word. ")
        print(f"{lives} trys left.")

        # If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # Import the stages from hangman_art.py and make this error go away.
    from hangman_art import stages
    print(stages[lives])

