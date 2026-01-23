#Write a lambda function using filter() which accepts a list of numbers and returns the list of numbers divisible by both 3 and 5
CheckEven = lambda No : No % 3 == 0 and No % 5 == 0
def main():
    Data = [4,5,7,9,10,15,20,30,45]
    print("Actual Data is : ",Data)

    FData = list(filter(CheckEven,Data))
    #FData = list(filter(lambda No : No % 3 == 0 and No % 5 == 0,Data))
    print("Data After Filter is : ",FData)

if __name__ == "__main__":
    main()
#Ouput
#Actual Data is :  [4, 5, 7, 9, 10, 15, 20, 30, 45]
#Data After Filter is :  [15, 30, 45]
