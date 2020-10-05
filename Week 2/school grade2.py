target = int(input("Hello. What is your target mark out of 100 for this exam? "))
ans = input("Would you like to know your actual result as a grade? ").lower()
if ans == "yes":
    mark = int(input("What mark did you get out of 100? "))
    if mark >= 90:
        grade = "A"
    elif mark >= 80:
        grade = "B"
    elif mark >= 70:
        grade = "C"
    elif mark >= 60:
        grade = "D"
    elif mark >= 50:
        grade = "E"
    else:
        grade = "Fail"
    print("Your grade for this test is ", grade)
    if target > mark:
        print("You will need to do some more homework for the next exam!")
    elif target == mark:
        print("You achieved the mark you aimed for. Well done. Can you achieve higher next time?")
    elif target < mark:
        print("Congratulations, did did better than you expected. Keep up the good work.")    

else:
  print("Okay, goodbye.")







