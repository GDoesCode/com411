def play_guess_the_number():
    import random
    answered = False

    value_min = int(input("Please enter the minimum value:\n"))
    value_max = int(input("Please enter the maximum value:\n"))
    num = random.randint(value_min, value_max)
    guess = int(input(f"I am thinking of a number between {value_min} and {value_max}. Can you guess what it is?\n"))

    while not answered:
        if guess < num:
            print("Your guess is too low.")
            guess = int(input("Try again:\n"))
        elif guess > num:
            print("Your guess is too high.")
            guess = int(input("Try again:\n"))
        else:
            print("Congratulations! You guessed my number!")
            answered = True


play_guess_the_number()