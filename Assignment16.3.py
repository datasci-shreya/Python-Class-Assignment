#Write a program which contains one function named as Add().Which accept two numbers.From user and return addition of that two numbers
#input : 11 5 
#Output : 16

def Add(No1 ,No2):
    Ans = None
    Ans = No1 + No2
    return Ans
    
def main():
    Result = 0
    Value1 = int(input("Enter a number: "))
    Value2 = int(input("Enter a number: "))

    Result = Add(Value1,Value2)

    print("Addition is:",Result)
        
if __name__ =="__main__":
    main()
#Output
#Enter a number: 11
#Enter a number: 5
#Addition is: 16