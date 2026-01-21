#Write a program which accept one number and prints factorial of that number
#Input - 5
#Output - 120
print("Enter a number : ")
No = int(input())

Factorial = 1
for i in range(1,No + 1):
    Factorial = Factorial * i
print("Factorial is : ",Factorial)