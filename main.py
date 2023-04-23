import random
from hangman_art import logo, stages
from hangman_words import word_list

print(f"Welcome to {logo}")

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

game_over = False
lives = 6
display = ["_"] * word_length

while not game_over:
    guess = input("\nGuess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("\nYou lose.")
            print(f"\nThe word was {chosen_word}")

    print(f"{' '.join(display)}")

    if "_" not in display:
        game_over = True
        print("\nYou win.")

    print(stages[lives])
