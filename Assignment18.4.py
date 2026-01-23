#Write a program which accept N numbers from user and store it into list.Accept one another number from user and return frequency of that number from list
#Input : Number of elements : 11
#Input Elements :13 5 45 7 4 56 5 34 2 5 65 
#Element to Search : 5
#Outtput : 3
def Frequency(Data, No):
    Count = 0

    for i in range(len(Data)):
        if Data[i] == No:
            Count = Count + 1

    return Count
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

    print("Enter element to Search : ")
    Search = int(input())

    Result = Frequency(Data, Search)

    print("Frequency is:", Result)


if __name__ == "__main__":
    main()
#Output
#PS C:\Users\shreya borate\OneDrive\Desktop\Pyhton Marvellous> python Assignment18.4.py
#Enter the number of elements :
#11
#Enter the elements :
#13
#5
#7
#4
#56
#5
#34
#2
#5
#65
#Enter element to Search :
#5
#Frequency is: 3