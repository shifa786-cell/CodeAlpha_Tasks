import random

words = ["apple", "banana", "python", "coding", "computer"]

word = random.choice(words)

guessed_letters = []
display = ["_"] * len(word)
wrong_guesses = 0
max_guesses = 6

print("🎮 Welcome to Hangman Game!")
print("You have 6 incorrect guesses.")
print("Word:", " ".join(display))

while wrong_guesses < max_guesses and "_" in display:
    guess = input("\nGuess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Enter a single valid letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!")
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
    else:
        wrong_guesses += 1
        print("Wrong guess!")
        print("Remaining guesses:", max_guesses - wrong_guesses)

    print("Word:", " ".join(display))

if "_" not in display:
    print("\n🎉 You won! The word is:", word)
else:
    print("\n❌ Game Over! The word was:", word)