# HANGMAN GAME - Khushi Joshi

#Importing required modules
from hangman_words import word_list
import hangman_art
import random

#Initializing the variables
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(hangman_art.logo)

#Creating blanks
display = []
for _ in range(word_length):
    display += "_"
print(f"{' '.join(display)}")

while not end_of_game:
    guess = input("\nGuess a letter: ").lower()

    #Checking if the user has entered a letter they've already guessed, 
    #printing the letter and letting them know.
    if guess in display:
        print(f"You've already guessed '{guess}'.")
    
    #Checking the guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Checking if user has made a wrong guess.
    if guess not in chosen_word:
        print(f"'{guess}' is not in the word.")
        lives -= 1
        print(hangman_art.stages[lives])

    #Joining all the elements in the list and turning it into a String. 
    #Also displaying number of chnaces left.
    print(f"\n{' '.join(display)}")
    print(f"Chances left: {lives}")

    #Checking if chances are over
    if lives == 0:
        end_of_game = True
        print(f"\nWord was: {chosen_word}")
        print("You lose :(")
        
    #Checking if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print(f"\nWord was: {chosen_word}")
        print("You win !!!")

