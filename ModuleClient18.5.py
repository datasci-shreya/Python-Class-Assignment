import MarvellousNum

def main():
    Size = 0
    Value = 0

    print("Enter the number of elements : ")
    Size = int(input())

    Data = list()

    print("Enter the elements :")

    for i in range(Size):
        Value = int(input())
        Data.append(Value) 
    Result = MarvellousNum.ListPrime(Data)

    print("Addition of prime Number is : ", Result)
    
if __name__ == "__main__":
    main()

#Output
#PS C:\Users\shreya borate\OneDrive\Desktop\Python> python ModuleClient18.5.py
#Enter the number of elements :
#11
#Enter the elements :
#13
#5
#45
#7
#4
#56
#10
#34
#2
#5
#8
#Addition of prime Number is :  32