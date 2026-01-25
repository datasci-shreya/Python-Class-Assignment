#Design a Python application where multiple threads update a shared variable
#Use a Lock to avoid race condition
#Each thread should increment shared counter multiple times
#Display final value of counter after all threads complete
import threading

counter = 0
lock = threading.Lock()

def Increment():
    global counter
    for i in range(100):        
        with lock:
         counter = counter + 1

def main():
    global counter
    t1 = threading.Thread(target=Increment)
    t2 = threading.Thread(target=Increment)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Final Counter Value is :", counter)

if __name__ == "__main__":
    main()

#Output :
#PS C:\Users\shreya borate\OneDrive\Desktop\Python> python Assignment21.3.py
#Final Counter Value is : 200