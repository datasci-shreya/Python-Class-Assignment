#write a program which accepts one number and prints binary equivalent
print("Enter a Number : ")
No = int(input())
Binary = " "

while No > 0:
    rem = No % 2
    Binary = str(rem) + Binary
    No = No // 2

print("Binary equivalent is :", Binary)



