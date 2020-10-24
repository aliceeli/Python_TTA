# Write program input 4 numbers and stores then

# create txt file called numbers

# input the numbers
# write numbers to numbers.txt
#close file

num_1 = input("Please enter your first number: ")
num_2 = input("Please enter your second number: ")
num_3 = input("Please enter your third number: ")
num_4 = input("Please enter your fourth number: ")

myFile = open("numbers.txt", "w")
myFile.write(f"{num_1}, {num_2}, {num_3}, {num_4}")


myFile.close()
