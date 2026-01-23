#Write a lambda function which accept one number and returns True if number is even otherwise false
CheckEven = lambda No : (No % 2 == 0)

def main():
   Value = 0 
  

   print("Enter Number : ") 
   Value = int(input()) 

   Ret = CheckEven(Value) 

   print(Ret)
if __name__ == "__main__":
    main()
#Output
#Enter Number :
#6
#True
#Enter Number :
#7
#False
