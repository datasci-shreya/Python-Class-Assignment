#Write a program which contains lambda function which accept one parameter and return power of two
#Input : 4  #Output : 16
#Input : 6  #Output : 64
Power = lambda No : 2 ** No

def main():
    Result = 0
    Value = int(input("Enter Number : "))
    Result = Power(Value)
    print("Power of Number : ",Result)
if __name__ == "__main__":
    main()

#Output : 
#PS C:\Users\shreya borate\OneDrive\Desktop\Python> python Assignment19.1.py
#Enter Number : 4
#Power of Number :  16
#PS C:\Users\shreya borate\OneDrive\Desktop\Python> python Assignment19.1.py
#Enter Number : 6
#Power of Number :  64
#PS C:\Users\shreya borate\OneDrive\Desktop\Python>
