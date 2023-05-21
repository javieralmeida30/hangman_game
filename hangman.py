
import random
from hangmanwords import word_list
from hangmanart import stages, logo

print(logo)

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6
letters = []
wrong_letters = []
# print(f'the solution is {chosen_word}.') see the solution.

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    letter_found = False

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            letter_found = True
            display[position] = letter

    if letter_found:
        letters.append(guess)
    else:
        wrong_letters.append(guess)

    print(f"used correct letters: {letters}")
    print(f"used wrong letters: {wrong_letters}")

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])
