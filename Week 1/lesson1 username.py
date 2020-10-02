def user_name():
    # Function that asks the user to enter a name
    # and then displays a greeting
    # Username is stored in variable user
    user = input("Please enter your name ")
    print("Hello " + user + ". It's a pleasure to meet you")
    
user_name()


def numbers():
    # Ask for 4 separate numbers in 4 variables
    # It should then display the total of the 4 numbers

    # Ask for the 4 variables and numbers as whole numbers
    num_1 = int(input("Enter your first number: "))
    num_2 = int(input("Enter your second number: "))
    num_3 = int(input("Enter your third number: "))
    num_4 = int(input("Enter your fourth number: "))

    # Add them up
    sum_num = num_1 + num_2 + num_3 + num_4

    # Display the sum
    print("The sum of these numbers is " + str(sum_num))

numbers()
    
