import random
easy_level_turns = 10
hard_level_turns = 5
end_game = False


def check_answer(guess, answer, turns):
    # Function to check user's guess against actual answer.
    """checks answer against guess. Returns the number of turns remaining."""
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")


def set_difficulty():
    # Make function to set difficulty.
    difficulty_level = input("Choose the difficulty levels, easy or hard? : ")
    if difficulty_level == "easy":
        return easy_level_turns
    elif difficulty_level == "hard":
        return hard_level_turns
    print(f"You have {difficulty_level} turns to try.")


def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1, 100)
    print(answer)

    turns = set_difficulty()
    # Repeat the guessing functionality if they get it wrong.
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        # Track the number of turns and reduce by 1 if they get it wrong.
        turns = check_answer(guess, answer, turns)
        """checks answer against guess. Returns the number of turns remaining."""
        if turns == 0:
            print(f"You run out of turns, The correct answer is {answer}")
            #stop the game when turns ==0
            return
        elif guess != answer:
            print("Guess again.")


game()


