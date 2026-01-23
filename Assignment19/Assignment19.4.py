#Write a program which contains filte(),map() and reduce() in it.python application which contins one list of numbers.List contains the number which are accepted from.Filter should filter out all such numbers which greater than or equal to 70 and less than or equal to 90.Map function will increase each number by 10.Reduce will return will return product of all that numbers.
#Input : [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
#Output : 
#List after filter =[2,4,4,2,8,10]
#List after map =[4,16,164,64,100]
#Output of Reduce = 204
from functools import reduce

def main():
    Data = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
    print("Actual Data is : ",Data)

    FData = list(filter(lambda No: No % 2 == 0, Data))
    print("List After filter:", FData)

    MData = list(map(lambda No: No ** 2 , FData))
    print("List After map:", MData)

    RData = reduce(lambda a, b: a + b, MData)
    print("Output of reduce:", RData)

if __name__ == "__main__":
    main()

#Output : 
#PS C:\Users\shreya borate\OneDrive\Desktop\Python> python Assignment19.4.py
#Actual Data is :  [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
#List After filter: [2, 4, 4, 2, 8, 10]
#List After map: [4, 16, 16, 4, 64, 100]
#Output of reduce: 204

