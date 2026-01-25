#Design a Python application that creates two threads
#Thread1 should compute sum of elements from a list
#Thread2 should compute product of elements from the same list
#Return the result to the main thread display them
import threading

SumResult = 0
ProductResult = 1

def SumList(Data):
    global SumResult
    total = 0
    for i in Data:
        total = total + i
    SumResult = total

def ProductList(Data):
    global ProductResult
    prod = 1
    for i in Data:
        prod = prod * i
    ProductResult = prod

def main():
    print("Enter number of elements : ")
    Size = int(input())
    Data = list()

    print("Enter elements :")
    for i in range(Size):
        Data.append(int(input()))

    t1 = threading.Thread(target=SumList, args=(Data,))
    t2 = threading.Thread(target=ProductList, args=(Data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Sum of elements is : ", SumResult)
    print("Product of elements is : ", ProductResult)

if __name__ == "__main__":
    main()

#Output :
#PS C:\Users\shreya borate\OneDrive\Desktop\Python> python Assignment21.4.py
#Enter number of elements :
#5
#Enter elements :
#2
#4
#6
#7
#8
#Sum of elements is :  27
#Product of elements is :  2688