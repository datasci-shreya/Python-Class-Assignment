#Write a program which accept N numbers from user and store it into list.return addition of all prime numbers from the list.Main python file accepts N numbers from user and pass each number to ChkPrime function which is part of our user defined module named as MarvellousNum.Name of the function from main python file should be ListPrime()
#Input : Number of elements : 11
#Input Elements : 13 5 45 7 4 56 10 34 2 5 8
#Output : 32 (13 + 5 + 7 + 2 + 5)
def ChkPrime(No):
    for i in range(2, No):
        if No % i == 0:
            return False
    return True

def ListPrime(Data):
    Sum = 0

    for i in range(len(Data)):
        if ChkPrime(Data[i]) == True:
            Sum = Sum + Data[i]

    return Sum

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
    Result = ListPrime(Data)

    print("Addition of prime Number is : ", Result)
    
if __name__ == "__main__":
    main()

#Output
#PS C:\Users\shreya borate\OneDrive\Desktop\Python> python Assignment18.5.py
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