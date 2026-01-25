#Design a Python application that creates two threads named EvenList and OddList
#Both threads should accept a list of integers as input
#The EvenList thread should :
#Extract all even elements from the list
#calculate and display their sum
#The OddList thread should :
#Extract all odd elements from the list
#calculate and display their sum
#Threads should run concurrently
import threading

def EvenList(Data):
    Sum = 0
    for i in Data:
        if i % 2 == 0:
            Sum = Sum + i
    print("Sum of Even elements : ", Sum)

def OddList(Data):
    Sum = 0
    for i in Data:
        if i % 2 != 0:
            Sum = Sum + i
    print("Sum of Odd elements : ", Sum)

def main():
    Size = 0
    Value = 0
    
    print(("Enter number of elements : "))
    Size = int(input())
    Data = list()

    print("Enter the elements :")
    for i in range(Size):
        Value = int(input())
        Data.append(Value) 

    t1 = threading.Thread(target=EvenList, args=(Data,))
    t2 = threading.Thread(target=OddList, args=(Data,))

    t1.start()
    t2.start()
    t1.join()
    t2.join()

if __name__ == "__main__":
    main()
#Output :
#PS C:\Users\shreya borate\OneDrive\Desktop\Python> python Assignment20.3.py
#Enter number of elements :
#5
#Enter the elements :
#9
#8
#6
#7
#5
#Sum of Even elements :  14
#Sum of Odd elements :  21