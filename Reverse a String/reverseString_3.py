print("Write a Python program to reverse a string ? using while loop")
print("==============================================================")

str = input("Enter the string text : ")
output = " "
x = len(str)-1

while x>=0:
    output = output+str[x]
    x = x-1
print("Reverse a given string text : ",output)
