print("You awaken in a dark cell. The stone floor is damp and cold beneath you.")
print("To your left is an open door through which a light is flickering.")
print("To your right you see a desk with a large, open book.")

door_or_book = input("Do you go left or right? (left/right) ").lower()
print()
if door_or_book == "left":
    print("You slowly bring yourself to your feet and walk towards the door")
    print("Once outside the cell you see at the end of the corridor a staircase.")
    
    up_or_down = input("Do you go up or down? (up/down) ").lower()
    print()
    if up_or_down == "up":
        print("You have chosen to acend the staircase.")
        print("As you climb the darkness expands until you can't even see your hand before your face.")
        print("You lose your sense of reality as you climb and climb through total darkness.")
        print("As your legs ache and you feel you can climb no more, you hear the sound of music coming from above.")
        up_or_down1 = input("Do you continue up, or turn back? (up/back) ")
        print()
        if up_or_down1 == "up":
            print("You continue upwards towards the music. As you reach the top of the staircase you see a door which is slightly ajar.")
        elif up_or_down1 == "back":
            print("You have chosen to decend the staircase.")
    elif up_or_down == "down":
        print("You have chosen to decend the staircase.")
        

elif door_or_book == "right":
    print("You approach the large, leather bound book on the desk")
    print("The book is mostly written in some unidentified script, but you see numerals which you recognise")
    yes_or_no = input("Do you attempt to figure out what the numerals mean? (yes/no) ").lower()
    print()
    if yes_or_no == "yes":
        print("As you inspect the numerals more closely, you realise they are all odd numbers.")
    elif yes_or_no == "no":
        print("You turn away from the book and exit the cell into the corridor.")
