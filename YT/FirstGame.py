print("Welcome to my first game!")
name = input("What is your name? ")
age = int(input("What is your age? "))
print("Hello", name, "you are", age, "years old.")

if age >= 18:
    print("You are old enough to play.")

    wants_to_play = input("Do you want to play a game? ").lower()
    if wants_to_play == "yes":
        health = 10
        print("You are starting with ", health, "health.")
        print("Let's play!")

        left_or_right = input("First choice... Left or Right (left/right)? ")
        if left_or_right == "left":
            print("Nice, you follow the path and reach a lake...")

            across_or_around = input("Do you swim across or go around (across/around)? ")
            if across_or_around == "around":
                print("You went around and reached the other side of the lake")
            elif across_or_around == "across":
                print("You managed to get across, but were bit by a fish and lost 5 health.")
                health -= 5
            else:
                print("You lose.")

            house_or_river = input("You notice a house and a river. Which do you go to? (house/river) ")
            if house_or_river == "house":
                print("You go to the house and are greeted by the owner... He doesn't like you and you lose 5 health.")
                health -= 5
            else:
                print("You fell in the river and lost...")

            if health <= 0:
                print("You now have 0 health and you lost the game...")
            else:
                print("You have survived...You win!")

        else:
            print("You fell down a hole and lost.")

    else:
        print("See you later...")          

else:
    print("Sorry, you are not old enough to play.")    
        

        



