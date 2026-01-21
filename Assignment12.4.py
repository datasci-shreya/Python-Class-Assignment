#Write a program which accepts one number and prints that many numbers starting from 1
# Input - 5
# output - 1 2 3 4 5 
print("Enter a number : ")
No = int(input())
for i in range(1, No + 1):
    print(i, end=" ")
