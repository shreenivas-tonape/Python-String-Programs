print("Write a Python program to reverse order of words present in the given string ?")
print("==============================================================================")

str = input("Enter the string text : ")
str1 = str.split()
str2 = str1[::-1]
output = " ".join(str2)
print("Reverse order of words present in the given string : ",output)