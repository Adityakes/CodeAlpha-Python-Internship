import random

# List of predefined words
WORDS = ["python", "computer", "developer", "mobile", "school"]

# Select a random word
word = random.choice(WORDS)

guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

print("=" * 40)
print("🎮 WELCOME TO HANGMAN GAME")
print("=" * 40)
print("Guess the hidden word one letter at a time.")
print(f"You have {max_wrong_guesses} wrong attempts.\n")

while wrong_guesses < max_wrong_guesses:

    # Display current progress
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print(f"Wrong Attempts Left: {max_wrong_guesses - wrong_guesses}")

    # Win condition
    if "_" not in display_word:
        print("\n🎉 Congratulations!")
        print(f"You guessed the word: {word}")
        break

    guess = input("\nEnter a letter: ").lower()

    # Input validation
    if len(guess) != 1 or not guess.isalpha():
        print("⚠ Please enter only one alphabet letter.")
        continue

    if guess in guessed_letters:
        print("⚠ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Correct Guess!")
    else:
        wrong_guesses += 1
        print("❌ Wrong Guess!")

# Lose condition
if wrong_guesses == max_wrong_guesses:
    print("\n💀 Game Over!")
    print(f"The correct word was: {word}")

print("\nThanks for playing! 👋")