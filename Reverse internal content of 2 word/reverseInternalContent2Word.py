print("Write a Python program to reverse internal content of every second word present in the given string ?")
print("=====================================================================================================")

str = input("Enter the string text : ")
str1 = str.split()
i=0
l=[]
while i<len(str1):
    if i%2 == 0:
        l.append(str1[i])
    else:
        l.append(str1[i][::-1])
    i = i+1
output = " ".join(l)
print("Reverse internal content of every 2 word in the given string :",output)