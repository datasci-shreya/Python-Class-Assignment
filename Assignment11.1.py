#write a program which accepts one number and checks whether it is prime or not 
#Input - 11 
#Output - Prime number
print("Enter a number : ")
No = int(input())

if No <= 1:
    print("Not Prime")
else:
    for i in range(2, No ):
        if No % i == 0:
            print("Not Prime Number")
            break
    else:
        print("Prime Number")
