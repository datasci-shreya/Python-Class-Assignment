#Write a program which accepts one number and prints that many numbers in reverse order 
#input -5
#output - 5 4 3 2 1
print("Enter a number : ")
No = int(input())
while No >= 1:
    print(No, end=" ")
    No = No - 1
