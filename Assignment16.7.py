#Write a program which contains one funtion that accept one number from user and returns true if number is divisible by 5 otherwise return false
#input : 8 #ouput : False
#input : 25 #ouput : True
def ChkNum(No):
    if No % 5 == 0:
        return True
    else:
        return False
    
def main():
    Value = 0 
    print("Enter Number : ") 
    Value = int(input()) 

    Ret = ChkNum(Value) 

    print(Ret)
if __name__ == "__main__":
    main()
#Output
#PS C:\Users\shreya borate\OneDrive\Desktop\Python> python Assignment16.7.py
#Enter Number :
#8
#False
#PS C:\Users\shreya borate\OneDrive\Desktop\Python> python Assignment16.7.py
#Enter Number :
#25
#True