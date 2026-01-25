#Design a Python application that creates two threads named Thread1 and Thread2.
#Thread1 should display numbers from 1 to 50
#Thread2 should display numbers from 50 to 1
#Ensure:
#Thread2 starts only after Thread1 completes
#Use proper thread synchronization
import threading

def Display1():
    print("Thread1 Numbers is :")
    for i in range(1, 51):
        print(i)


def Display2():
    print("Thread2 Numbers is :")
    for i in range(50, 0, -1):
        print(i)


def main():

    t1 = threading.Thread(target=Display1, name="Thread1")
    t2 = threading.Thread(target=Display2, name="Thread2")

    t1.start()
    t1.join()      

    t2.start()
    t2.join()

    print("Both Threads Execute")


if __name__ == "__main__":
    main()

#Ouput:
#Thread1 Numbers is :
#1
#2
#...
#50
#Thread2 Numbers is :
#50
#49
#...
#1
#Both Threads Execute