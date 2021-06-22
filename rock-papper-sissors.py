import random

r = None
p = None
s = None

user = input('choose "r" for rock, "p" for paper, "s", for sissors \n').lower()

options = ['r', 'p', 's']
machine = random.choice(options)

if machine == user:
  print("It's a tie")
elif user == "r" and machine == "s" or user == "p" and machine == "r" or user == "s" and machine == "p":
  print("Yay! You win!")
else:
  print("Sorry, the machine won")

