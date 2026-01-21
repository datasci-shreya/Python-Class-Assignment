#Write a program which accept one number and prints sum of first N natural numbers
#Input - 5
#Output - 15
print("Enter a number : ")
No = int(input())

Sum = 0
for i in range(1,No +1):
    Sum = Sum + i
print("Sum is : ",Sum)