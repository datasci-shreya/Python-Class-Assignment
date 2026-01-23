#Write a program which contains filte(),map() and reduce() in it.python application which contins one list of numbers.List contains the number which are accepted from.Filter should filter out all such numbers which greater than or equal to 70 and less than or equal to 90.Map function will increase each number by 10.Reduce will return will return product of all that numbers.
#Input : [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
#Output : 
#List after filter =[76,89,86,90,70]
#List after map =[86,99,96,100,80]
#Output of Reduce = 6538752000
from functools import reduce

def main():
    Data = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
    print("Actual Data is : ",Data)

    FData = list(filter(lambda No: No >= 70 and No <= 90, Data))
    print("List After filter:", FData)

    MData = list(map(lambda No: No + 10, FData))
    print("List After map:", MData)

    RData = reduce(lambda a, b: a * b, MData)
    print("Output of reduce:", RData)

if __name__ == "__main__":
    main()

#Output : 
#PS C:\Users\shreya borate\OneDrive\Desktop\Python> python Assignment19.3.py
#Actual Data is :  [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
#List After filter: [76, 89, 86, 90, 70]
#List After map: [86, 99, 96, 100, 80]
#Output of reduce: 6538752000

