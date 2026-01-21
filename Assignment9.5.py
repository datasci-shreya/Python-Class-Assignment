#Write a program which accept one number and checks whether it is divisible by 3 and 5
#Input - 15
#Output - Divisible by 3 & 5
def CheckDivisible(No): #CheckDivisible is function  with passing one parameter value
    if No % 3 == 0 and No % 5 == 0: # % checks remainder If remainder is 0 for both 3 and 5 the number is divisible else not divisible 
        print("Divisible by 3 and 5")
    else:
        print("Not Divisible by 3 and 5")

CheckDivisible(17) #function with passing argument 

