#Write a program which accept one number from user and returm addition of its factors
#Input : 12
#Output : 16 (1 + 2 + 3 + 4 + 6)
def FactorSum(No):
    Sum = 0
    
    for i in range(1,No):
        if No % i == 0:
            Sum = Sum + i
    return Sum
        
def main():
    Value = int(input("Enter Number :"))

    Ret = FactorSum(Value)

    print("Sum of Factors is : ",Ret)

if __name__ == "__main__":
    main()
#Output
#PS C:\Users\shreya borate\OneDrive\Desktop\Python> python Assignment17.4.py
#Enter Number :12
#Sum of Factors is :  16