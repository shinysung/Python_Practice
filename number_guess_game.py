# Number guessing game


import random


answer = random.randint(1, 21)
i = 0
tries = 0
NUM_TRIES = 4
guess = 0


while guess != answer and tries < NUM_TRIES:
    guess = int(input("You have {} chances left. Try to guess a number between 1 and 20: ".format(NUM_TRIES - tries)))
    tries += 1

    if guess > answer:
        print("Down")
    elif guess < answer:
        print("Up")


if guess == answer:
    print("Congratulations. You guessed the number in {} attempts.".format(i))
else:
    print("Unfortunately, the correct answer is {}.".format(answer))