#Write a program which accept one number and prints all odd numbers till that number
print("Enter a number : ")
No = int(input())

for i in range(1,No + 1):
    if i % 2  != 0:
         
     print(i , end=" ")
