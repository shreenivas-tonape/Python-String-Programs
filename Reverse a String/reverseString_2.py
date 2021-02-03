print("Write a Python program to reverse a string ? using reversed")
print("===========================================================")

str = input("Enter the string text : ")
rstr = reversed(str)
output = "".join(rstr)
print("Reverse a given string text : ",output)