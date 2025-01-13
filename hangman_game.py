import random
import string
from hangman_pictures import stage_1, stage_2, stage_3, stage_4, stage_5, stage_6, stage_7


vocabulary = ["holiday", "dog", "hummer", "patrol", "christmas"]
lives_left = 6
print(f"You have {lives_left} lives left.")
chosen_word = random.choice(vocabulary)
masked_word = ["_"] * len(chosen_word)
guesses = []
while lives_left > 0 and "_" in masked_word:
    print("Word to guess:", masked_word)
    guess_letter = input("Enter the guessed letter: ").lower()

    if len(guess_letter) != 1:
        print("Enter only 1 letter!")
        continue
    if guess_letter not in string.ascii_lowercase:
        print("Enter a LETTER, not a number or special character!")
        continue
    if guess_letter in guesses:
        print("You already guessed that letter!")
        continue
    guesses.append(guess_letter)
    print("Guesses so far:", guesses)
    if guess_letter in chosen_word:
        for idx, value in enumerate(chosen_word):
            if guess_letter == value:
                masked_word[idx] = guess_letter
        print("Correct guess!")
    else:
        lives_left -= 1
        print("Incorrect guess. Lives left:", lives_left)
    if lives_left == 6:
        stage_1()
    elif lives_left == 5:
        stage_2()
    elif lives_left == 4:
        stage_3()
    elif lives_left == 3:
        stage_4()
    elif lives_left == 2:
        stage_5()
    elif lives_left == 1:
        stage_6()
    elif lives_left == 0:
        stage_7()
if "_" not in masked_word:
    print(f"Congratulations! You guessed the word: {chosen_word}")
else:
    print(f"Game over! The correct word was: {chosen_word}")

