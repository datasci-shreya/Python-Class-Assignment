#Write a lambda function which accept one number and returns True if number is odd otherwise false
CheckOdd = lambda No : (No % 2 != 0)

def main():
   Value = 0 
   
   print("Enter Number : ") 
   Value = int(input()) 

   Ret = CheckOdd(Value) 

   print(Ret)
if __name__ == "__main__":
    main()
#Output
#Enter Number :
#3
#True
#Enter Number :
#4
#False