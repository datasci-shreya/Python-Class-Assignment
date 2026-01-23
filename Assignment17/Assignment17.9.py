#Write a program which accept one number from user and returm number of digits in that number
#Input : 5187934
#Output : 7
def CountDigits(No):
    Count = 0

    while No > 0:
        Count = Count + 1
        No = No // 10      

    return Count

def main():
    Value = int(input("Enter Number : "))

    Ret = CountDigits(Value)

    print("Number of digits is : ", Ret)

if __name__ == "__main__":
    main()
#Output 
#PS C:\Users\shreya borate\OneDrive\Desktop\Python> python Assignment17.9.py
#Enter Number : 5187934
#Number of digits is :  7

