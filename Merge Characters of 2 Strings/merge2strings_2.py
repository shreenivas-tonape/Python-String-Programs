print("Write a Python program to merge characters of 2 strings in to a single string by taking characters alternatively ?")
print("==================================================================================================================")

str1 = input("Enter the string text : ")
str2 = input("Enter the string text : ")

i,j = 0,0
output = " "

while i<len(str1) or j<len(str2):
    if i<len(str1):
        output = output+str1[i]
        i=i+1
    if j<len(str2):
        output = output+str2[j]
        j=j+1
print(output)