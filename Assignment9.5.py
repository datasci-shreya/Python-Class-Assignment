#Write a program which accept one number and checks whether it is divisible by 3 and 5
#Input - 15
#Output - Divisible by 3 & 5
def CheckDivisible(No): 
    if No % 3 == 0 and No % 5 == 0: 
        print("Divisible by 3 and 5")
    else:
        print("Not Divisible by 3 and 5")

CheckDivisible(17) 

