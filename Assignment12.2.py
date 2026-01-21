#Write a program which accepts one number and prints its factor
#input - 12
#output - 1 2 3 4 6 12
print("Enter a number : ")
No = int(input())
for i in range(1, No + 1):
    if No % i == 0:
        print(i, end=" ")
