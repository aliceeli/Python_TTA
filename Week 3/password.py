#asks user to input password
#re enter password
#compare the two
#if same, tell user if its weak, medium strong
#weak=just lowercase/uppercase
#strong=contains lower+uppercase and numbers


print("Hello, let's create a password.")
password = input("Please enter the word you would like to use here: ")
if len(password) > 5:
    password2 = input("Please re-enter your password: ")
    if password == password2:
        print("Thank you, the two passwords match.")
    
        if password.islower() or password.isupper():
            for letter in password:
                if letter.isdigit():
                    print("That is a medium password")
                    break
            else:
                print("That is a weak password.")
                    
        elif not password.islower() and not password.isupper():
            for letter in password:
                if letter.isdigit():
                    print("That is a strong password")
                    break

    else:
        print("Sorry those passwords do not match.")
else:
    print("You need to choose a longer password.")

