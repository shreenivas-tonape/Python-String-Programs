print("Write a Python program to reverse internal content of each words ?")
print("==================================================================")

str = input("Enter the string text : ")
str1 = str.split()
l = []

for word in str1:
    l.append(word[::-1])
output = " ".join(l)
print("Reverse internal content of each words in the given string : ",output)