#Write a program which accept one number and prints all even numbers till that number
#Input
#Output - 2 4 6 8 10
print("Enter a number : ")
No = int(input())

for i in range(1, No+1):
    if i % 2 == 0:
        print(i, end=" ")
