#write a program which accepts one number and print reverse of that number 
# input - 123
# output - 321
print("Enter a number : ")
No = int(input())
Reverse = 0
while No > 0:
    Digit = No % 10
    Reverse = Reverse * 10 + Digit
    No = No // 10

print("Reverse number is : ", Reverse)
