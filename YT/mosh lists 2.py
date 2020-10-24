mylist = [4, 4, 4, 6, 7, 3, 8, 10, 3]
myList2 = []
print(mylist)
for x in mylist:
    if x not in myList2:
        myList2.append(x)

   
print(myList2)
