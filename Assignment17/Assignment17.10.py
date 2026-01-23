#Write a program which accept one number from user and returm addition of digits in that number
#Input : 5187934
#Output : 37
def SumOfDigits(No):
    Sum = 0

    while No > 0:
        digit = No % 10        
        Sum = Sum + digit     
        No = No // 10         
    return Sum

def main():
    Value = int(input("Enter Number : "))

    Ret = SumOfDigits(Value)

    print("Sum of digits is : ", Ret)

if __name__ == "__main__":
    main()

#Output
#PS C:\Users\shreya borate\OneDrive\Desktop\Python> python Assignment17.10.py
#Enter Number : 5187934
#Sum of digits is :  37