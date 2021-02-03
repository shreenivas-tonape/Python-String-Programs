print("Write a Python program to calculate the length of a string ? Using def function")
print("=================================================================================")

def lengthString(str):
    count = 0
    for i in str:
        count = count+1
    return count

print(lengthString("shreenivas"))