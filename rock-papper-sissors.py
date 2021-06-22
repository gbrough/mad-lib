import random

r = None
p = None
s = None

user = input('choose "r" for rock, "p" for paper, "s", for sissors \n').lower()

options = ['r', 'p', 's']
machine = random.choice(options)

if machine == "r" and user == "s" or machine == "p" and user == "r" or machine == "s" and user == "p":
  print("The machine won")
elif user == "r" and machine == "s" or user == "p" and machine == "r" or user == "s" and machine == "p":
  print("Yay! You win!")
elif machine == user:
  print("It's a tie")

