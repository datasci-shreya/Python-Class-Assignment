#Write a lambda function using map() which accepts a list of numbers and returns a list of square of each number
Square = lambda No : No * No
def main():
    Data = [1,2,3,4,5,6,7,8,9]
    print("Actual Data is : ",Data)

    MData = list(map(Square,Data))
    #MData = list(map(lambda No : No * No,Data))
    print("Square is : ",MData)

if __name__ == "__main__":
    main()
#Output
#Actual Data is :  [1, 2, 3, 4, 5, 6, 7, 8, 9]
#Square is :  [1, 4, 9, 16, 25, 36, 49, 64, 81]
