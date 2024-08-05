import random

import hangman




from hangman_wordlists import word_list   # good option this


chosen_word= random.choice(word_list)


end_of_game = False
lives = 6

from hangman import hangman_logo
print(hangman_logo)

display = []
for _ in range(len(chosen_word)):
    display += "_"


# TODO-2 : -Loop through each position in the chosen_word;
# If the letter at that position matches 'guess' then reveal that letter in the display at that position.
# e.g if the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].





while not end_of_game:
    guess = input("Guess a letter: ").lower()
    # Check the guessed letter

    if guess in display:
        print(f"You've already guessed {guess}")
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
       # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
           display[position] = letter


    print(f"{' '.join(display)}")

    if guess not in chosen_word:
        print(f"You guessed {guess}, thay is not in the word. You lose a life. ")
        lives -=1
        if lives == 0:
            print("You lose.")




    if "_" not in display:
        end_of_game = True
        print("You win.")

    from hangman import hangman_stages

    print(hangman_stages[lives])

