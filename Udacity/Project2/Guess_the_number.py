# Guess the number

# This notebook simulates a classic game where you have to guess a random number from within a certain range.
# Typically, you might have to guess a number from 1 to 10, and have three guesses to get the right answer.
#
# In this case, you'll need to guess a random number between 1 and 100, and you will have 7 tries.
#
# Try running it and playing a round or two. Notice that the game always tells you whether your
# guess was too high or too low. This information allows you to rule out some of
# the numbers (so that you don't waste time guessing those numbers).
#
# With this fact in mind, try to make your guesses in the most efficient way you can. Specifically,
# try to make guesses that rule out the largest number of possibilities each time.


import random

total_tries = 0
start_range = 1
end_range = 100


def guess_the_number(total_tries, start_range, end_range):
    random_number = random.randrange(start_range, end_range)
    print("Random number between", start_range, "and", end_range, ":", random_number)

    success_message = "Awesome! You guessed correctly"
    failure_message = "Sorry! No more retries left"
    miss_message = "Oops! That's incorrect"

    total_tries = 1
    i = 0
    middle_value = int(end_range / 2)

    print("Random Number: ", random_number)
    print("Start Range: ", start_range)
    print("End Range: ", end_range)

    while random_number in range(start_range, end_range+1):

        if random_number == middle_value and total_tries <= 7:
            print(success_message, ", Target value: ", middle_value)
            return total_tries

        elif random_number > middle_value and total_tries <= 7:
            print(miss_message)
            start_range = middle_value + 1
            middle_value = int((start_range + end_range) / 2)
            total_tries += 1

        elif random_number < middle_value and total_tries <= 7:
            print(miss_message)
            end_range = middle_value - 1
            middle_value = int((start_range + end_range) / 2)
            total_tries += 1

        else:
            print(failure_message)
            print("Total tries: ", total_tries)



tries = guess_the_number(total_tries, start_range, end_range)

print("Total tries:", tries)
