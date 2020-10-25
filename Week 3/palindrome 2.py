palindrome = input("""Please enter a word
I will tell you if it is a palindrome: """)

if palindrome == palindrome[::-1]:
    print("That's a palindrome!")
else:
    print("No, sorry. Try again.")


