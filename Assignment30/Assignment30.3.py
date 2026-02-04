#Display File Line by Line
#Problem Statement :
#Write a program which accepts a file name from the user and displays the contents of the file line by line on the screen
#Input:
#Demo.txt
#Expected Output :
#Display each line of Demo.txt one by one
import os

def DisplayFile(FileName):

    try:
        fobj = open(FileName,"r")

        print("\nContents of file are :\n")
        for line in fobj:
            print(line, end="")

        fobj.close()

    except FileNotFoundError:
        print("Unable to open file as there is no such file")

    finally:
        print("\nEnd of Application")


def main():
    Name = input("Enter File Name : ")
    DisplayFile(Name)

if __name__ == "__main__":
    main()

#Output : 
#