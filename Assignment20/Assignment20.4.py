#Design a Python application that creates three threads named Small, Capital, and Digits
#All threads accept a string as input
#The Small thread thread should count and display the number of lowercase characters
#The capital thread should count and display the number of uppercase characters
#The Digits thread should count and display the number of numeric digit
#Each thread must also display:
#Thread ID
#Thread Name
import threading 
def Small(s):
    count = 0
    for Ch in s:
        if Ch >= "a" and Ch <= "z":
            count = count + 1
    print("Small Thread")
    print("Thread Name is : ",threading.current_thread().name)
    print("Thread Id is : ",threading.get_ident())
    print("Lowercase count : ",count)

def Capital(s):
    count = 0
    for Ch in s:
        if Ch >= "A" and Ch <= "Z":
            count = count + 1
    print("Capital Thread")
    print("Thread Name is : ",threading.current_thread().name)
    print("Thread Id is : ",threading.get_ident())
    print("Uppercase count : ",count)

def Digits(s):
    Count = 0
    for Ch in s:
      if Ch >= '0' and Ch <= '9':
          Count = Count + 1
    print("Digits Thread")
    print("Thread Name is : ", threading.current_thread().name)
    print("Thread ID is : ", threading.get_ident())
    print("Digits Count is : ", Count)

def main():
    s = input("Enter String is : ")
    t1 = threading.Thread(target=Small,args=(s,),name="Small")
    t2 = threading.Thread(target=Capital,args=(s,),name="Capital")
    t3 = threading.Thread(target=Digits,args=(s,),name="Digit")

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

if __name__ == "__main__":
    main()

#Output:
#PS C:\Users\shreya borate\OneDrive\Desktop\Python> python Assignment20.4.py
#Enter String is : j
#Small Thread
#Thread Name is :  Small
#Thread Id is :  19048
#Lowercase count :  1
#Capital Thread
#Thread Name is :  Capital
#Thread Id is :  13132
#Uppercase count :  0
#Digits Thread
#Thread Name is :  Digit
#Thread ID is :  19776
#Digits Count is :  0