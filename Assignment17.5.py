#Write a program which accept one number from user and check whether number is prime or not
#Input : 5
#Output : It is Prime Number
def ChkNum(No):
   if No <= 1:
    print("Not Prime")
   else:
    for i in range(2, No ):
        if No % i == 0:
            return False
    return True
       
def main():
    Value = int(input("Enter Number :"))
    Ret = ChkNum(Value)
    if Ret == True:
      print("It is Prime Number ")
    else:
       print("It is Not Prime Number ")
     
if __name__ == "__main__":
    main()
#Output
#PS C:\Users\shreya borate\OneDrive\Desktop\Python> python Assignment17.5.py
#Enter Number :5
#It is Prime Number