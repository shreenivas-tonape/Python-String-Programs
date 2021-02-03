print("Write a Python program to sort characters of the string, first alphabet symbols followed by digits ? ")
print("=====================================================================================================")

str = "B4A1D3"
alpha = []
digit = []

for ch in str:
    if ch.isalpha():
        alpha.append(ch)
    else:
        digit.append(ch)
output = "".join(sorted(alpha)+sorted(digit))
print(output)