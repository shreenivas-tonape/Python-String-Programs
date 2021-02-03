print("Write a Python program to print the characters present at even index and odd index separately for  the given string?")
print("====================================================================================================================")

str = input("Enter the string text : ")

i = 1
while i<len(str):
    print(str[i],end="")
    i = i+2