import random
WORDS = ['shubham', 'akash', 'dev', 'vivek', 'aanurag','aahyush']
MAX_WRONG = 6

def choose_word():
    return random.choice(WORDS)

def show_progress(word, guessed):
    return ' '.join(letter if letter in guessed else '_' for letter in word)

def hangman():
    word = choose_word()
    guessed = set()
    wrong = 0

    print("Welcome to Hangman!")

    while wrong < MAX_WRONG:
        print("\nWord:", show_progress(word, guessed))
        print(f"Wrong guesses left: {MAX_WRONG - wrong}")
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter one valid letter.")
            continue

        if guess in guessed:
            print("You already guessed that letter.")
            continue

        guessed.add(guess)

        if guess in word:
            print("Good guess!")
            if all(letter in guessed for letter in word):
                print(f"\nCongratulations! You guessed the word: {word}")
                break
        else:
            print("Wrong guess.")
            wrong += 1

    if wrong == MAX_WRONG:
        print(f"\nGame over! The word was: {word}")

if __name__ == "__main__":
    hangman()