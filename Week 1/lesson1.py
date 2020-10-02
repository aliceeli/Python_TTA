import random

myName = input("Hello! What is your name? ")

number = random.randint(1,10)

print("Well, " + myName + " I am thinking of a number between 1 and 10")

guess = int(input("Take a guess: "))

if guess == number:
    print("Good job, " + myName + "! You guessed my number")
else:
    print("Sorry, that's not right " + myName)
              
print("I was thinking of ", number)
