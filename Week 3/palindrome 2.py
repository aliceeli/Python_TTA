palindrome = input("""Please enter a word
I will tell you if it is a palindrome: """)

palindrome2 = palindrome[::-1]

if palindrome == palindrome2:
    print("That's a palindrome!")
else:
    print("No, sorry. Try again.")


