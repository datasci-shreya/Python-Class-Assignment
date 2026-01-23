#Write a program which accept one number and display below pattern
# input : 5
# Output :
# * * * * *
#* * * *
#* * *
#* *
#*

def main ():
    No = int(input("Enter a Number : "))

    for i in range(No,0,-1):
        for j in range(i):
            print("*",end=" ")
        print()
if __name__=="__main__":
    main()
#Output
#PS C:\Users\shreya borate\OneDrive\Desktop\Python> python Assignment17.6.py
#Enter a Number : 5
#* * * * *
#* * * *
#* * *
#* *
#*
