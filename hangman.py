import random

class HangmanGame:
    def __init__(self, filename="words.txt"):
        self.filename = filename
        self.word = self.choose_word()
        self.guessed_letters = []
        self.attempts = 6

    def choose_word(self):
        try:
            with open(self.filename, "r") as file:
                words = file.read().splitlines()
                return random.choice(words)
        except FileNotFoundError:
            print(f"Error: File '{self.filename}' not found.")
            return None

    def display_word(self):
        displayed_word = ""
        for letter in self.word:
            if letter in self.guessed_letters:
                displayed_word += letter
            else:
                displayed_word += "_"
        return displayed_word

    def display_hangman(self):
        stages = [
            """
            --------
            |      |
            |      O
            |     \\|/
            |      |
            |     / \\
            -
            """,
            """
            --------
            |      |
            |      O
            |     \\|/
            |      |
            |     /
            -
            """,
            """
            --------
            |      |
            |      O
            |     \\|/
            |      |
            |
            -
            """,
            """
            --------
            |      |
            |      O
            |     \\|
            |      |
            |
            -
            """,
            """
            --------
            |      |
            |      O
            |      |
            |      |
            |
            -
            """,
            """
            --------
            |      |
            |      O
            |
            |
            |
            -
            """,
            """
            --------
            |      |
            |
            |
            |
            |
            -
            """
        ]
        return stages[self.attempts]

    def play(self):
        while True:
            if not self.word:
                print("Exiting Hangman.")
                return

            print("Welcome to Hangman!")
            print("The word has", len(self.word), "letters.")

            while self.attempts > 0:
                print(self.display_hangman())
                print("Guessed letters:", ", ".join(self.guessed_letters))
                displayed = self.display_word()
                print("Word:", displayed)

                guess = input("Guess a letter: ").lower()

                if guess == "quit":
                    print("Thanks for playing!")
                    return

                if len(guess) != 1 or not guess.isalpha():
                    print("Please enter a single alphabetical character.")
                    continue

                if guess in self.guessed_letters:
                    print("You've already guessed that letter.")
                    continue

                self.guessed_letters.append(guess)

                if guess not in self.word:
                    print("Incorrect!")
                    self.attempts -= 1
                else:
                    print("Correct!")

                if "_" not in self.display_word():
                    print("\nCongratulations! You guessed the word:", self.word)
                    break

            if "_" in self.display_word():
                print(self.display_hangman())
                print("\nSorry, you ran out of attempts. The word was:", self.word)

            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again != "yes":
                print("Thanks for playing!")
                break

if __name__ == "__main__":
    game = HangmanGame()
    game.play()
