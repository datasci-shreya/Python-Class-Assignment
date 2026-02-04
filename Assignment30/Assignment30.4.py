#Copy File Contents into Another File
#Problem Statement :
#Write a program which accepts two file names from the user
#First file is an existing file
#Second file is a new file
#Copy all contents from the first file into the second file
#Input :
#ABC.txt Demo.txt
#Expected Output :
#Contents of ABC.txt copied into Demo.txt

import os

def DisplayFile(FileName):
    try:
        fobj = open(FileName, "r")

        print("Contents of file are:\n")
        for Line in fobj:
            print(Line, end="")
        fobj.close()

    except FileNotFoundError:
        print("Unable to open file as there is no such file")

    finally:
        print("\nEnd of Application")

def main():
    Name = input("Enter file name: ")

    DisplayFile(Name)

if __name__ == "__main__":
    main()

# Output :
#PS C:\Users\shreya borate\OneDrive\Desktop\Python\Automation> python Assignment30.4.py Demo.txt
#Enter file name: Demo.txt
#Contents of file are:
#Jay Ganesh Marvellous...
#End of Application