#write a program which accepts one number and prints count of digit in that number 
#Input - 7521
#Output - 4
print("Enter a number : ")
No = int(input())
count = 0

for i in No:
    if No.isdigit():
        count = count + 1

print(count)