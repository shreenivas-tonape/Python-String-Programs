print("Write a Python program to reverse order of words present in the given string ?")
print("==============================================================================")

def stringWords(str):
    for i in str.split("/n"):
        return (" ".join(i.split()[::-1]))

print(stringWords("durga software solution"))