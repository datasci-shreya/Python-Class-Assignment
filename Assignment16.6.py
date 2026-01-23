#Write a program which accept number from user and check whether that number is positive or negative or zero.
#input : 11 #output : Positive Number
#input : -8 #output : Negative Number
#input : 0 #output : Zero Number 

def ChkNum(No):
    if No > 0:
        print("Positive Number  ")
    elif No < 0:
        print("Negative Number  ")
    else:
        print("Zero Number  ")
def main():
    Value = int(input("Enter a Number : "))
    ChkNum(Value)
    
if __name__ == "__main__":
    main()

#Output
#PS C:\Users\shreya borate\OneDrive\Desktop\Python> python Assignment16.6.py
#Enter a Number : 11
#Positive Number
#PS C:\Users\shreya borate\OneDrive\Desktop\Python> python Assignment16.6.py
#Enter a Number : -8
#Negative Number
#PS C:\Users\shreya borate\OneDrive\Desktop\Python> python Assignment16.6.py
#Enter a Number : 0
#Zero Number

