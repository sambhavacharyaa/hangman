import random

import hangman_words as hw
import hangman_art as ha
print(ha.logo)
word_list = ["champions", "flowchart", "computer"]
chosen_word = random.choice(hw.word_list)

lives = 6
word_length = len(chosen_word)

display = ['_' for _ in range(word_length)]

end_of_game = False

while not end_of_game:
    guess = input("Guess the letter: ").lower()
    
    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        
        if letter == guess:
            display[position] = letter

    print(display)

    if guess not in chosen_word:
        lives -= 1
        print("You have chose a wrong letter. You've lost a live")
        if lives == 0:
            end_of_game = True
            print("You lose")
            print(f"The word was {chosen_word}")

    if "_" not in display:
        end_of_game = True
        print("You Win")
    print(ha.stages[lives])