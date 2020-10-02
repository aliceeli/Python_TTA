motorbike = 2000

year_1 = (motorbike - motorbike/10)
year_2 = (year_1 - year_1/10)
year_3 = (year_2 - year_2/10)
year_4 = (year_3 - year_3/10)
year_5 = (year_4 - year_4/10)
year_6 = (year_5 - year_5/10)
year_7 = (year_6 - year_6/10)

print(motorbike)
print(year_1)
print(year_2)
print(year_3)
print(year_4)
print(year_5)
print(year_6)
print(year_7)


""" Motorbike initial cost = year 1
motorbike minus 10 percent = year 2
reduce by 10 until value = >1000

"""
print("Part2")
motorbike = 2000
print(motorbike)
value = float(motorbike*0.9)
print(value)
if value >= 1000:
    print(value*0.9)
    value = (value*0.9)
if value >= 1000:
    print(value*0.9)
    value = (value*0.9)
if value >= 1000:
    print(value*0.9)
    value = (value*0.9)
if value >= 1000:
    print(value*0.9)
    value = (value*0.9)
if value >= 1000:
    print(value*0.9)
    value = (value*0.9)
if value >= 1000:
    print(value*0.9)
    value = (value*0.9)
if value >= 1000:
    print(value*0.9)
    value = (value*0.9)
if value >= 1000:
    print(value*0.9)
    value = (value*0.9)
if value <= 1000:
    print("Final value: £",value)
    
        


