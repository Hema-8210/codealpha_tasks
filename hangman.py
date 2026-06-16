import random
word_list = ["python", "apple", "table", "river", "house"]
secret_word = random.choice(word_list)
guessed_letters = []
chances = 6
print("Welcome to Hangman Game")
while chances > 0:
    current_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            current_word += letter
        else:
            current_word += "_"
    print("\nWord :", current_word)
    if current_word == secret_word:
        print("You Won!")
        break
    user_letter = input("Enter a letter : ").lower()
    if user_letter in secret_word:
        if user_letter not in guessed_letters:
            guessed_letters.append(user_letter)
            print("Correct Guess")
        else:
            print("Already Entered")
    else:
        chances -= 1
        print("Wrong Guess")
        print("Remaining Chances :", chances)
if chances == 0:
    print("Game Over")
    print("Correct Word was :", secret_word)
