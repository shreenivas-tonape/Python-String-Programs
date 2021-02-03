print("Write a Python program to merge characters of 2 strings in to a single string by taking characters alternatively ?")
print("==================================================================================================================")

str1 = input("Enter the string text : ")
str2 = input("Enter the string text : ")

i,j = 0,0
output = " "

while i<len(str1) or j<len(str2):
    output = output+str1[i]+str2[j]
    i = i+1
    j = j+1
print(output)