#write a program which accepts one number and checks whether it is perfect number or not
#input - 6
#output - perfect number
print("Enter a Number : ")
No = int(input())
Result = 0
for i in range(1, No):
    if No % i == 0:
        Result = Result + i
if Result == No:
    print("Perfect Number : ",No)
else:
    print("Not Perfect Number : ",No)




