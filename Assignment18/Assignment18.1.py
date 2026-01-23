#Write a program which accept N numbers from user and store it into list.return addition of all elements from that list 
#Input : Number of elements : 6
#Input Elements :13 5 45 7 4 56 
#Outtput : 130
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

    Sum = 0

    for i in range(Size):
        Sum = Sum + Data[i]

    print("Summation is : ", Sum)
    
if __name__ == "__main__":
    main()

#Output
#PS C:\Users\shreya borate\OneDrive\Desktop\Python> python Assignment18.1.py
#Enter the number of elements :
#6
#Enter the elements :
#13
#5
#45
#7
#4
#56
#Summation is :  130