# Lucky Unicorn Decomposition Step 4
# Set up payment mechanics

# To do
# Adjust total correctly for a given token
#   - if it's a unicorn add $5
#   - if it's a zebra / horse, subtract 0.5
#   - if it's a donkey,subtract 1
# Give user feedback based on winnings
# State new total

# Assume starting amount is $10
total = 10

# Assume manual token input for testing purposes
token = input("Enter a token: ")

# Adjust correctly for a given token
if token == "unicorn":
    total += 5
    feedback = "Congratulations, you got a lucky unicorn and have won $5.00!"
elif token == "donkey":
    total -= 1
    feedback = "Sorry, you did not win anything this round"
else:
    total -= 0.5
    feedback = "Congratulations, you won 50¢!"

print()

print(feedback)
print("You have ${:.2f} to play with".format(total))
