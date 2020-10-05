# Ask student for percentage mark to convert to grade
# e.g 91-100 = A 81-90 = BaseException
target_grade = str(
    input("What grade do you hope to achieve? (A/B/C/D/E)")).upper()
mark_grade = int(input("What is your mark out of 100? "))
if mark_grade >= 90:
    mark_grade = "A"
elif mark_grade >= 80:
    mark_grade = "B"
elif mark_grade >= 70:
    mark_grade = "C"
elif mark_grade >= 60:
    mark_grade = "D"
elif mark_grade >= 50:
    mark_grade = "E"
else:
    mark_grade = "Fail"
    print("You will need to resit the exam.")
print("You achieved grade " + mark_grade)

if target_grade == mark_grade:
    print("Well done! You have achieved your target grade")
elif target_grade == "A" and mark_grade == "B" or "C" or "D" or "E" or "Fail":
    print("Sorry, you will have to try harder next time!")
elif target_grade == "A" or "B" and mark_grade == "C" or "D" or "E" or "Fail":
    print("Sorry, you will have to try harder next time!")
elif target_grade == "A" or "B" or "C" and mark_grade == "D" or "E" or "Fail":
    print("Sorry, you will have to try harder next time!")
elif target_grade == "A" or "B" or "C" or "D" and mark_grade == "E" or "Fail":
    print("Sorry, you will have to try harder next time!")
elif target_grade == "A" or "B" or "C" or "D" or "E" and mark_grade == "Fail":
    print("Sorry, you will have to try harder next time!")
else:
    print("Well done, you did better than you expected!")

    # NOT WORKING if you type in a higher target grade than mark grade you still get sorry try harder. There must be a simpler way to achieve this.
