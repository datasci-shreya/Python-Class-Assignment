#Write a lambda function which accept two number and returns maximum number
def Maximum(No1, No2):
    if No1 > No2:
        return No1
    else:
        return No2

def main():
    print("Enter First Number : ")
    Value1 = int(input())

    print("Enter Second Number : ")
    Value2 = int(input())

    Ret = Maximum(Value1, Value2)

    print("Maximum Number is :", Ret)

if __name__ == "__main__":
    main()
#Output
#Enter First Number :
#6
#Enter Second Number :
#4
#Maximum Number is : 6
