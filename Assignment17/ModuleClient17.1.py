#Create on module named as Arithmetic which contains 4 functions as Add() for addition,Sub() for subtraction,Mul() for multiplication and Div() for division.All functions accept two parameters as number and perform the operation.write on python program which call all the functions from arithmetic module by accepting the parameters from user.

import Arithmetic17

def main():
    No1 = int(input("Enter First Number : "))
    No2 = int(input("Enter Second Number : "))

    print("Addition is : ", Arithmetic17.Add(No1, No2))
    print("Subtraction is : ", Arithmetic17.Sub(No1, No2))
    print("Multiplication is : ", Arithmetic17.Mul(No1, No2))
    print("Division is : ", Arithmetic17.Div(No1, No2))

if __name__ == "__main__":
    main()
#Output
#PS C:\Users\shreya borate\OneDrive\Desktop\Python> python ModuleClient17.1.py
#Enter First Number : 10
#Enter Second Number : 5
#Addition is :  15
#Subtraction is :  5
#Multiplication is :  50
#Division is :  2.0