#Question 1 — Factorial
#Task: Take number from user. Print factorial.
number= int(input('enter number: '))
import math
print(math.factorial(number))

#Question 2 — File Save
#Task: Take user name and goal. Save both into file.
name=input('enter name: ')
goal=input('entetr goal: ')
with open("output.txt", "w") as file:
    file.write("Name: " + name + "\n")
    file.write("Goal: " + goal)

#Question 3 — Random Guessing Game
#Task: Generate random number from 1–10. Ask user to guess.

number=int(input('enter number: '))
import random
guess=random.randint(1,10)
if number==guess:
    print('correct guess...!')
else:
    print('try again....!')

#Question 4 — Dictionary + Loop
#Task: Create dictionary of 3 players and scores.
players={
    "virat" : 97,
    "rohit" : 88,
    "dhoni" : 79
}
for key, value in players.items():
    print(key, ":", value)