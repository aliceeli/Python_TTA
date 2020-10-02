

def calculator():
    int1 = float(input("Choose your first number: "))

    int2 = float(input("Choose your second number: "))

    multiplyer = str(input("Input one of the following + - / * "))

    if multiplyer == "+":
        print(int1 + int2)
    elif multiplyer == "-":
        print(int1 - int2)
    elif multiplyer == "/":
        print(int1 / int2)
    elif multiplyer == "*":
        print(int1 * int2)
    else:
        print("Try Again")
        calculator()


print("Welcome to my calculator")
calculator()
