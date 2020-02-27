# Lucky Unicorn Decomposition Step 2
# Generate a random token

import random

tokens = ["unicorn", "donkey", "donkey", "donkey",
          "horse", "horse", "horse",
          "zebra", "zebra", "zebra"]

for item in range(1,15):

    chosen = random.choice(tokens)
    print(chosen)
