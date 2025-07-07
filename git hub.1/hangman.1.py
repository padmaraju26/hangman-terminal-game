import random

def hangman():
    words = ['python', 'hangman', 'programming', 'challenge', 'developer', 'computer']
    word = random.choice(words)
    guessed_word = ['_'] * len(word)
    attempts = 6
    guessed_letters = []

    print("🎮 Welcome to Hangman!")
    print("Guess the word, one letter at a time.")
    print(f"You have {attempts} incorrect guesses allowed.\n")

    while attempts > 0 and '_' in guessed_word:
        print('Word:', ' '.join(guessed_word))
        print('Guessed letters:', ' '.join(guessed_letters))
        guess = input("Enter a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("⚠ Please enter a single valid letter.\n")
            continue

        if guess in guessed_letters:
            print("⛔ You've already guessed that letter.\n")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("✅ Good guess!\n")
            for i in range(len(word)):
                if word[i] == guess:
                    guessed_word[i] = guess
        else:
            print("❌ Incorrect guess!\n")
            attempts -= 1

    if '_' not in guessed_word:
        print('🎉 Congratulations! You guessed the word:', word)
    else:
        print('💀 Game Over! The word was:', word)
