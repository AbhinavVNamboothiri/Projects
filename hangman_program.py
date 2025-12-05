# Hangman Game

import random

words = ["python", "java", "javascript", "c", "c++", "ruby", "swift", "go", "kotlin", "scala"]

# Dictionary of hangman stages
hangman_art = { 0: (" ",
                    " ",
                    " "),
                1: (" 0 ",
                    " ",
                    " "),
                2: (" 0 ",
                    "|",
                    " "),
                3: (" 0 ",
                    "/|",
                    " "),
                4: (" 0 ",
                    "/|\\",
                    " "),
                5: (" 0 ",
                    "/|\\",
                    "/ "),
                6: (" 0 ",
                    "/|\\",
                    "/ \\")}

def display_hangman(tries):
    print("*****************")
    for row in hangman_art[tries]:
        print(row)
    print("*****************")
def display_hint(hint):
    print(" ".join(hint))
def display_answer(answer):
    print(" ".join(answer))
def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_gusses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_hangman(wrong_gusses)
        display_hint(hint)
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print(f"You already guessed the letter {guess}.")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_gusses += 1
        if "_" not in hint:
            display_hangman(wrong_gusses)
            display_answer(answer)
            print("Congratulations! You guessed the word.")
            is_running = False
        elif wrong_gusses >= len(hangman_art) - 1:
            display_hangman(wrong_gusses)
            display_answer(answer)
            print("Game Over! You lost.")
            is_running = False

        


    
    

if __name__ == "__main__":
    main()

    
    

