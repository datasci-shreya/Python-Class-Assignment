#Write a lambda function which accept two number and returns minimum number
def Minimum(No1, No2):
    if No1 < No2:
        return No1
    else:
        return No2

def main():
    print("Enter First Number : ")
    Value1 = int(input())

    print("Enter Second Number : ")
    Value2 = int(input())

    Ret = Minimum(Value1, Value2)

    print("Minimum Number is :", Ret)

if __name__ == "__main__":
    main()
#Output
#Enter First Number :
#6
#Enter Second Number :
#4
#Minimum Number is : 4
