#Write a program which contains one function named as ChkNum().Which accept one parameter as number. If number is even then it should display "Even Number" Otherwise display "Odd Number" on console
#input : 11 #Output : Odd Number 
#input : 8 #Output : Even Number
def ChkNum(No):
    if No % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")
def main():
    #Value = int(input("Enter a number: "))
    ChkNum(11)
    ChkNum(8)
if __name__ =="__main__":
    main()
#Output
#C:\Users\shreya borate\OneDrive\Desktop\Python>python Assignment16.2.py
#Odd Number
#Even Number