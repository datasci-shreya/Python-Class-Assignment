#Design a Python application that creates two threads named EvenFactor and OddFactor
#Both threads accept one integer number as a parameter
#The EvenFactor thread should :
#Identify all even factors of the given number
#Calculate and display the sum of even factors
#The OddFactor thread should :
#Identify all odd factors of the given number
#Calculate and display the sum of odd factors
#After both threads complete execution , main thread should display the message "Exit from main"
import threading 

def EvenFctor(No):
    Sum = 0
    for i in range(1,No + 1):
        if No % i == 0 and i % 2 == 0:
            print("Even Factor : ",i)
            Sum = Sum + i 
    print("Sum of Even Numbers : ",Sum)
    
def OddFactor(No):
    Sum = 0
    for i in range(1,No + 1):
        if No % i == 0 and i % 2 != 0:
            print("Odd Factor : ",i)
            Sum = Sum + i 
    print("Sum of Odd Numbers : ",Sum)

def main():

    Value = int(input("Enter the Number : "))
  
    t1 = threading.Thread(target=EvenFctor,args=(Value,))
    t2 = threading.Thread(target=OddFactor,args=(Value,))

    t1.start()
    t1.join()
    t2.start()
    t2.join()

if __name__ == "__main__":
    main()

#Output : 
#PS C:\Users\shreya borate\OneDrive\Desktop\Python> python Assignment20.2.py
#Enter the Number : 6
#Even Factor :  2
#Even Factor :  6
#Sum of Even Numbers :  8
#Odd Factor :  1
#Odd Factor :  3
#Sum of Odd Numbers :  4