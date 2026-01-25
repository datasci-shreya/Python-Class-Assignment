#Design a Python application that creates two separate threads named Even and Odd
#The Even thread should display first 10 even numbers
#The Odd thread should display first 10 odd numbers
#Both threads should execute independently using the threading module
#Ensure proper thread creation and execution

import threading 

def Even():
    print("Even Numbers : ")
    for i in range(1,21):
        if i % 2 == 0:
            print(i) 
    
def Odd():
    print("Odd Numbers : ")
    for i in range(1,21):
        if i % 2 != 0:
            print(i)
def main():
  
    t1 = threading.Thread(target=Even)
    t2 = threading.Thread(target=Odd)

    t1.start()
    t1.join()
    t2.start()
    t2.join()

if __name__ == "__main__":
    main()

#Output :
#PS C:\Users\shreya borate\OneDrive\Desktop\Python> python Assignment20.1.py
#Even Numbers :
#2
#4
#6
#8
#10
#12
#14
#16
#18
#20
#Odd Numbers :
#1
#3
#5
#7
#9
#11
#13
#15
#17
#19