#Write a lambda function using filter() which accepts a list of numbers and returns the count of even numbers
CheckEven = lambda No : No % 2 == 0 
def main():
    Data = [4,5,7,9,10,15,20,30,45]
    print("Actual Data is : ",Data)

    FData = list(filter(CheckEven,Data))
    #FData = list(filter(lambda No : No % 2 == 0 ,Data))
    Count = len(FData)
    print("Data After Filter is : ",FData)
    print("Count of Even Numbers is : ",Count)

if __name__ == "__main__":
    main()
#Ouput
#Actual Data is :  [4, 5, 7, 9, 10, 15, 20, 30, 45]
#Data After Filter is :  [4, 10, 20, 30]
#Count of Even Numbers is :  4