print("Write a Python program to calculate the length of a string ? Using while loop")
print("===============================================================================")

str = input("Enter the string text : ")
count = 0
while str[count:]:
    count = count+1
print("Length of the given string text : ",count)