##Write a lambda function which accept two number and returns Multiplication
Multiplication = lambda No1,No2 : No1 *  No2
def main():
    print("Enter a Number")
    Value1 = int(input())
    print("Enter a Number")
    Value2 = int(input())

    Ret = Multiplication(Value1, Value2)
    print("Multiplication is : ",Ret)
    
if __name__ == "__main__":
    main()
#Output
#Enter a Number
#5
#Enter a Number
#2
#Multiplication is :  10