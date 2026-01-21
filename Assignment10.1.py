#Write a program which accept one number and prints multiplication table of that number
#Input - 4
#Output - 4 8 12 16 20 24 28 32 36 40
print("Enter a number : ")
No = int(input())

for i in range(1, 11):
    Result = No * i
    print(Result , end=" ")
