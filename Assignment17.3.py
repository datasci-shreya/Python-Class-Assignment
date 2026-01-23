#Write a program which accept one number from user and returm its factorial
#Input : 5
#Output : 120
def Factorial(No):
    Fact = 1
    
    for i in range(1,No + 1):
        Fact = Fact * i

    return Fact
def main():
    Value = int(input("Enter Number :"))

    Ret = Factorial(Value)

    print("Factorial is : ",Ret)

if __name__ == "__main__":
    main()
#Output
#PS C:\Users\shreya borate\OneDrive\Desktop\Python> python Assignment17.3.py
#Enter Number :5
#Factorial is :  120