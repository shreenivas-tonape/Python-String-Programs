print("Write a Python program for the requirement, input – a4b3c2 and expected output – aaaabbbcc ? ")
print("=============================================================================================")

str = "a4b3c2"
output = " "

for ch in str:
    if ch.isalpha():
        x = ch
    else:
        d = int(ch)
        output = output+x*d
print(output)