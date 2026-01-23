#Write a lambda function which accept one number and returns True if number is odd otherwise false
Check = lambda No : (No % 5 == 0)

def main():
   Value = 0 
   
   print("Enter Number : ") 
   Value = int(input()) 

   Ret = Check(Value) 

   print(Ret)
if __name__ == "__main__":
    main()
#Output
#Enter Number :
#20
#True