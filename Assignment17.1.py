#Create on module named as Arithmetic which contains 4 functions as Add() for addition,Sub() for subtraction,Mul() for multiplication and Div() for division.All functions accept two parameters as number and perform the operation.write on python program which call all the functions from arithmetic module by accepting the parameters from user.
def Add(No1,No2):
    Ans = None
    Ans = No1 + No2
    return Ans
def Sub(No1,No2):
    Ans = None
    Ans = No1 - No2
    return Ans
def Mul(No1,No2):
    Ans = None
    Ans = No1 * No2
    return Ans 
def Div(No1,No2):
    Ans = None
    Ans = No1 / No2
    return Ans 
def main():
    No1 = int(input("Enter First Number : "))
    No2 = int(input("Enter Second Number : "))

    Addition=Add(No1,No2)
    Subtraction = Sub(No1,No2)
    Multiplication= Mul(No1,No2)
    Division = Div(No1,No2)

    print("Addition is : ", Addition)
    print("Subtraction is : ", Subtraction)
    print("Multiplication is : ", Multiplication)
    print("Division is : ", Division)

if __name__ =="__main__":
    main()

print("_"*15)_______________________________________

def Add(No1, No2):
    return No1 + No2

def Sub(No1, No2):
    return No1 - No2

def Mul(No1, No2):
    return No1 * No2

def Div(No1, No2):
    return No1 / No2

def main():
    No1 = int(input("Enter First Number : "))
    No2 = int(input("Enter Second Number : "))

    print("Addition is : ", Add(No1, No2))
    print("Subtraction is : ", Sub(No1, No2))
    print("Multiplication is : ", Mul(No1, No2))
    print("Division is : ", Div(No1, No2))

if __name__ == "__main__":
    main()



