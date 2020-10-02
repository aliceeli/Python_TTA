""" Set variable to be rand int 1-10
ask user input guess
print output if guess is correct

loop 6 times
let them know if guess too high
let them know if guess too low
"""

import random

guesses = 0
number = random.randint(1,10)

guess = int(input("Hello. I have chosen a random number 1-10 can you guess what it is? "))

print("You have chosen ", guess)

if guess == number:
    print("Well done. You guessed correctly!")
else:
    print("Sorry, that's not right. You have 5 more chances to guess correctly")
    guesses +=1

while guesses <= 5 and guess != number:
    guess = int(input("Guess again "))
    if guess == number:
        print ("Well done you guessed correctly!")
    elif guess <= number:
        print("Try a higher number")
    elif guess >= number:
        print("Try a lower number")
    else:
        guesses +=1
        print("Sorry, that's not right")
        if guesses == 5:
            print("Sorry you have no more chances to guess correctly")
            print("The number was ", number)  
            break
