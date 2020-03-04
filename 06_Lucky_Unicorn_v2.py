# Lucky Unicorn Fully Working Program
# Program should work - needs to be tested for usability
# v2 Made statements easier to view and made an intro / rules
import random

# Integer checking function below
def intcheck(question, low, high):
    valid = False
    error = "Whoops! Please enter an integer between {} and {}".format(low, high)
    while not valid:
        try:
            response = int(input(question))
            if low <= response <= high:
                return response
            else:
                print(error)
                print()

        except ValueError:
            print(error)

# Function to print out token statements and apply stars lines or arrows to statement
def token_statement(statement, char):
    print()
    print(char*len())
    print(statement)
    print()

# Main routine

# Introductions / Rules

print("***** Welcome to the Lucky Unicorn Game *****")
print()
print("To play, enter the amount of money between $1 and $10 (dollars only, no cents)")
print()
print("The cost is $1 per round")
print()
print("* Payouts *")
print("Unicorn: $5")
print("Donkey: $0")
print("Zebra and Horses: 50¢")
print()

# Ask user how much they want to play with (minimum $1, maximum $10)
balance = intcheck("How much money would you like to play with? ", 1, 10)

print("||||| Game In Progress |||||")

keep_going = ""
while keep_going == "":

    # Tokens list includes 10 items to prevent too many unicorns being chosen
    tokens = ["unicorn", "donkey", "donkey", "donkey",
              "horse", "horse", "horse",
              "zebra", "zebra", "zebra"]

    # Randomly choose a token from our list above
    token = random.choice(tokens)
    print()
    print("You got a {}".format(token))

    # Adjust balance based on the chosen token and generate feedback
    if token == "unicorn":
        # prints unicorn statement
        balance += 5    # wins $5
        feedback = "***** Congratulations, you got a lucky unicorn and have won $5.00! *****"
    elif token == "donkey":
        # prints donkey statement
        balance -= 1    # does not win anything (ie: loses $1)
        feedback = "|| Sorry, you did not win anything this round ||"
    else:
        # prints zebra / horse statement
        balance -= 0.5    # 'wins' 50c, paid $1 so loses 50c
        feedback = "<< Congratulations, you won 50¢ >>!"

    print()
    print(feedback)
    if balance < 1:
        print()
    else:
        print("You have ${:.2f} to play with".format(balance))
        print()

    # If user has enough money to play, ask if they want to play again
    if balance < 1:
            print("Sorry, you don't have enough money to continue. Game Over")
            keep_going = "end"
    else:
            keep_going = input("Press <enter> to play again or any key to quit")
# Farewell user at end of game
print("Thank you for playing")
