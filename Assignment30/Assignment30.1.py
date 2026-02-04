#Count Lines in a File
#Problem Statement:
#Write a program which accepts a file name from the user and counts how many lines are present in the file
#Input:
#Demo.txt
#Expected Output:
#Total number of lines in Demo.txt
import os
def CountLines(FileName):

    try:
        fobj = open(FileName,"r")
        Lines = fobj.readlines()
        fobj.close()

        print("Total Number Of Lines in" ,FileName,"is :",len(Lines))

    except FileNotFoundError:
        print("Unable to open file as there is no such file")

    finally:
        print("End of Application")

def main():
    Name = input("Enter File Name : ")
    CountLines(Name)

if __name__ == "__main__":
    main()

#Output :
#PS C:\Users\shreya borate\OneDrive\Desktop\Python\Automation> python Assignment30.1.py Demo.txt
#Enter File Name : Demo.txt
#Total Number Of Lines in Demo.txt is : 1
#End of Application