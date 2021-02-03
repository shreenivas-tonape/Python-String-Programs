print("Write a Python program for sub string presence in string ? ")
print("===========================================================")

str = input("Enter the string text : ")
sub_str = input("Enter sub string text : ")

if str.find(sub_str) == -1:
    print("Not Found")
else:
    print("Found")