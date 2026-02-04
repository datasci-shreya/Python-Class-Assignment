# Check File Exists in Current Directory 
#Problem Statement:
#Write a program which  accept a file name from the user and checks whether that file exits in the current directory or not
#Input :
#Demo.txt
#Expected Output:
#Dsplay whether Demo.txt exits or not+

import os

def CheckExists(FileName):

    if os.path.exists(FileName):
        print("File Exists in Current Directory")
    else:
        print("There is no such Directory ")

def main():
    FileName = input("Enter File Name : ")

    CheckExists(FileName)

if __name__ == "__main__":
    main()

#Output :
#PS C:\Users\shreya borate\OneDrive\Desktop\Python\Automation> python Assignment29.1.py
#Enter File Name : Demo.txt
#File Exists in Current Directory