import random
import time

# Script variables
#name = "Kevin"
name = input("Enter Name: ")
#question = "Is the earth flat?"
question = input("Type Question: ")
answer = ""

# Generate random number
random_number = random.randint(1,12)
# print(random_number)

# check random number and set answer
if random_number == 1:
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now"
elif random_number == 7:
  answer = "My sources say no"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful"
elif random_number == 10:
  answer = "Affirmative"
elif random_number == 11:
  answer = "Surely you can't be serious..."
elif random_number == 12:
  answer = "What do you mean?"
else:
  answer = "Error"

# Check if question was provided
if question == "":
  print("Magic 8-Ball just closed the gate, need a valid question to participate.")
# Check if name was provided
elif name == "":
  print(f"asks: {question}")
  time.sleep(1)
  print(f"Magic 8-Ball's answer: {answer}")
else:
  print(f"{name} asks: {question}")
  time.sleep(1)
  print(f"Magic 8-Ball's answer: {answer}")
