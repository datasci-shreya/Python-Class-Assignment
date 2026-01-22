#Write a lambda function using reduce() which accepts a list of numbers and returns a addition of all elements
from functools import reduce
Addition = lambda No1,No2: No1 + No2 
def main():
    Data = [1,2,3,4,5,6,7,8,9]
    print("Actual Data is : ",Data)
    RData = reduce(Addition,Data)
    #RData = reduce(lambda a,b : a + b,Data))
    print("Data After Reduce is : ",RData)

if __name__ == "__main__":
    main()
#Output
#Actual Data is :  [1, 2, 3, 4, 5, 6, 7, 8, 9]
#Data After Reduce is :  45