#Write a program which contains one function ChkGreater() that accepts two numbers and prints the greater number.
#Input - 10 20 
#Output - 20 is greater
def ChkGreater(No1, No2): #ChkGreater() is function with passing two parameter
    if No1 > No2: #if else is used to compare them
        print(No1, "is greater")
    else:
        print(No2, "is greater")

ChkGreater(10, 20) #funtion with passing arguments
