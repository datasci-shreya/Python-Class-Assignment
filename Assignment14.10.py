##Write a lambda function which accept three number and returns largest number
def Maximum(No1, No2 ,No3):
    if No1 > No2 and No1 > No3:
        return No1
    elif No2 > No1 and No2 > No3:
        return No2
    else:
        return No3
    
def main():
    print("Enter First Number : ")
    Value1 = int(input())

    print("Enter Second Number : ")
    Value2 = int(input())

    print("Enter Second Number : ")
    Value3= int(input())


    Ret = Maximum(Value1, Value2,Value3)

    print("Largest Number is :", Ret)

if __name__ == "__main__":
    main()
#Output
#Enter First Number :
#2
#Enter Second Number :
#8
#Enter Second Number :
#5
#Largest Number is : 8
