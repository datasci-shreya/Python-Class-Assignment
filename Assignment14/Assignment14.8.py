##Write a lambda function which accept two number and returns addition
Add = lambda No1,No2 : No1 + No2
def main():
    print("Enter a Number")
    Value1 = int(input())
    print("Enter a Number")
    Value2 = int(input())

    Ret = Add(Value1, Value2)
    print("Addition is : ",Ret)

if __name__ == "__main__":
    main()
#Output 
#Enter a Number
#2
#Enter a Number
#1
#Addition is :  3