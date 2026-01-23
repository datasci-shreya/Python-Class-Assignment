#Write a program which accept one number and display below pattern
# input : 5
# Output : 
#1
#1 2
#1 2 3
#1 2 3 4
#1 2 3 4 5

def main ():
    No = int(input("Enter a Number : "))

    for i in range(1,No + 1):
        for j in range(1 ,i + 1):
            print(j,end=" ")
        print()
if __name__=="__main__":
    main()
#Output
#PS C:\Users\shreya borate\OneDrive\Desktop\Python> python Assignment17.8.py
#Enter a Number : 5
#1
#1 2
#1 2 3
#1 2 3 4
#1 2 3 4 5