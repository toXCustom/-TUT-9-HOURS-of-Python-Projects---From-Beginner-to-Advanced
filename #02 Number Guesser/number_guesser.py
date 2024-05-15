import random

# Asking the user with a number
top_of_range = input("Type a number: ")

# Making shure that the input is a number
if top_of_range.isdigit():
    # Making the input a int number
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number larger than 0 next time.")
        quit()
else:
    print("Please type a number next time.")
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")

    # Making shure that the input is a number
    if user_guess.isdigit():
    # Making the input a int number
        user_guess= int(user_guess)

    else:
        print("Please type a number next time.")
        continue

    if user_guess == random_number:
        print("You got it correctly!")
        break
    elif user_guess > random_number:
        print("You were above the number!")
    else:
        print("You were below the number!")

print("You got it in", guesses, "guesses")