print("Write a Python program to string is Palindrome or Not ?")
print("=======================================================")

str = input("Enter the string text : ")
str1 = str[::-1]

if str == str1 :
    print("String is a palindrome")
else:
    print("String is a not palindrome")
