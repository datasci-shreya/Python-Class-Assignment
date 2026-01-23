#Write a program which accept N numbers from user and store it into list.return Mximum number from that list
#Input Elements :13 5 45 7 4 56 
#Outtput : 56
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

    Min = Data[0]

    for i in range(1,Size) :
        if Data[i] < Min:
         Min = Data[i]

    print("Minimum Number is : ", Min)
    
if __name__ == "__main__":
    main()

#Output
#PS C:\Users\shreya borate\OneDrive\Desktop\Python> python Assignment18.3.py
#Enter the number of elements :
#4
#Enter the elements :
#13
#5
#45
#7
#Minimum Number is :  5