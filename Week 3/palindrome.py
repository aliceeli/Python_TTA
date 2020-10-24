#write program to take in word and says if it is palindrome

#does 0=-1, 1=-2 2=-3
#if len of word = 3, (2)


word = input("""
Please enter a 3-10 letter word.
I will tell you if it is a palindrome: """).lower()

if len(word) == 3 or 4:
    if word[0] == word[-1] and word[1] == word[-2]:
        print("That is a palindrome")
    else:
        print("Nope, sorry.")

elif len(word) == 5 or 6:
    if word[0] == word[-1] and word[1] == word[-2] and word[2] == word[-3]:
        print("That is a palindrome")
    else:
        print("Nope, sorry.")

elif len(word) == 7 or 8:
    if word[0] == word[-1] and word[1] == word[-2] and word[2] == word[-3] and word[3] == word[-4]:
        print("That is a palindrome")
    else:
        print("Nope, sorry.")


elif len(word) == 9 or 10:
    if word[0] == word[-1] and word[1] == word[-2] and word[2] == word[-3] and word[3] == word[-4] and word[4] == word[-5]:
        print("That is a palindrome")
    else:
        print("Nope, sorry.")

else:
    print("Please restart and enter a 3-10 letter word.")
