#Design a Python application that creates two threads
#Thread1 should find maximum element from a list
#Thread2 should find minimum element from the same list
#List should be accepted from user
import threading

def MaxList(Data):
  Max = Data[0]
  for i in Data:
        if i > Max:
           Max = i
  print("Maximum Number is :", Max)

def MinList(Data):
    Min = Data[0]
    for i in Data:
        if i < Min:
            Min = i
    print("Minimum Number is :", Min)

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

    t1 = threading.Thread(target=MaxList, args=(Data,))
    t2 = threading.Thread(target=MinList, args=(Data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()

#Output :
#PS C:\Users\shreya borate\OneDrive\Desktop\Python> python Assignment21.2.py
#Enter the number of elements :
#5
#Enter the elements :
#3
#4
#5
#5
#6
#Maximum Number is : 6
#Minimum Number is : 3