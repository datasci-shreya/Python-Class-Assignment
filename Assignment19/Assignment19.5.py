#Write a program which contains filte(),map() and reduce() in it.python application which contins one list of numbers.List contains the number which are accepted from.Filter should filter out all such numbers which greater than or equal to 70 and less than or equal to 90.Map function will increase each number by 10.Reduce will return will return product of all that numbers.
#Input : [2, 70, 11, 10, 17, 23, 31, 77]
#Output : 
#List After filter: [2, 11, 17, 23, 31]
#List After map: [4, 22, 34, 46, 62]
#Output of reduce: 62
from functools import reduce
def CheckPrime(No):
    if No <= 1:
        return False
    for i in range(2,No):
        if No % i == 0:
            return False
    return True

def main():
    Data = [2, 70, 11, 10, 17, 23, 31, 77]
    print("Actual Data is : ",Data)

    FData = list(filter(CheckPrime, Data))
    print("List After filter:", FData)

    MData = list(map(lambda No: No * 2 , FData))
    print("List After map:", MData)

    RData = reduce(lambda a, b: a if a > b else b, MData)
    print("Output of reduce:", RData)

if __name__ == "__main__":
    main()

#Output : 
#PS C:\Users\shreya borate\OneDrive\Desktop\Python> python Assignment19.5.py
#Actual Data is :  [2, 70, 11, 10, 17, 23, 31, 77]
#List After filter: [2, 11, 17, 23, 31]
#List After map: [4, 22, 34, 46, 62]
#Output of reduce: 62

