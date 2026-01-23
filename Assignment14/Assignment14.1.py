#Write a lambda function which accept one number and returns square of that number


Square = lambda No : No * No
No= int(input("Enter a number : "))
Result = Square(No)
print("Square is : ",Result)




print("_"*15)
Square = lambda No : No * No
def main():
    Value = 0
    print("Enter a Number : ")
    Value = int(input())
    Ret = Square(Value)
    print("Square is : ",Ret)
      
if __name__ == "__main__":
      main()
#Ouput
#Enter a number : 5
#Square is :  25
#_______________
#Enter a Number :
#5
#Square is :  25