def joke():
    
    answer2 = int(input("Choose a number between 1-5 "))
    

    if answer2 == 1:
        print("Did you hear about the mathematician who's afraid of negative numbers?")
        print("He'll stop at nothing to avoid them")
        print()
    if answer2 == 2:
        print("Why did the chicken go to the seance?")
        print("To get to the other side")
        print()
    if answer2 == 3:
        print("A man tells his doctor, 'Doc, help me. I'm addicted to Twitter!")
        print("The doctor replies, 'Sorry, I don't follow you'")
        print()
    if answer2 == 4:
        print("What do you call a magic dog?")
        print("Labracadabrador")
        print()
    if answer2 == 5:
        print("What did the pirate say when he turned 80?")
        print("Aye matey")
        print()

answer1 = input("Hello would you like to hear a joke? ")
if answer1 == "yes":
    joke()
else:
    print("Okay then, goodbye")

answer3 = input("Would you like to hear another? ")
if answer3 == "yes":
    print("Choose a different number")
    joke()   
else:
    print("Okay then, goodbye")
