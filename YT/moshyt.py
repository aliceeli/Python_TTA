


weight = int(input("Weight: "))
lbs_or_kgs = input("(L)bs or (K)gs: ").lower()
if lbs_or_kgs == "l":
    weight *= 0.45
    print(f"That is {weight}kgs")
elif lbs_or_kgs == "k":
    weight *= 2.2
    print(f"That is {weight}lbs")

else:
    print("Please try and again and enter L or K.")




name = input("Please enter your name: ")
if len(name) < 3:
    print("Name must be at least 3 characters long.")
elif len(name) > 50:
    print("Name can be a maximum of 50 characters.")
else:
    print("Thank you.")
