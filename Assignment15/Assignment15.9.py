#Write a lambda function using reduce() which accepts a list of numbers and returns product of all elements
from functools import reduce
Product = lambda No1 ,No2 : No1 * No2
def main():
    Data = [1,2,3,4,5,6,7,8,9]
    print("Actual Data is : ",Data)
    
    RData = reduce(Product,Data)
    #RData = reduce(lambda No1 , No2 = No1 * No2,Data))
    print("Data After Reduce is : ",RData)

if __name__ == "__main__":
    main()
#Output
#Actual Data is :  [1, 2, 3, 4, 5, 6, 7, 8, 9]
#Data After Reduce is :  362880