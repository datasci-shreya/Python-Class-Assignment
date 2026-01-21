#write a program which accepts one number and prints sum of digits 
#Input - 123
#Output - 6
print("Enter a number : ")
No = int(input())
Sum = 0
while No > 0:
    Digit = No % 10
    Sum = Sum + Digit
    No = No // 10

print("Sum of Digits  is : ", Sum)
