#Write a lambda function using filter() which accepts a list of numbers and returns a list of Odd numbers
CheckEven = lambda No : No % 2 != 0
def main():
    Data = [1,2,3,4,5,6,7,8,9]
    print("Actual Data is : ",Data)

    FData = list(filter(CheckEven,Data))
    #FData = list(filter(lambda No : No % 2 == 0,Data))
    print("Data After Filter is : ",FData)

if __name__ == "__main__":
    main()
#Output
#Actual Data is :  [1, 2, 3, 4, 5, 6, 7, 8, 9]
#Data After Filter is :  [1, 3, 5, 7, 9]
