#Count Words in a File
#Problem Statement :
#Write a program which accepts a file name from the user and counts the total number of words in that file
#Input :
#Demo.txt
#Expected Output :
#Total number of words in Demo.txt
import os
def CountWords(FileName):

    try:
        fobj = open(FileName,"r")
        Data = fobj.read()
        fobj.close()

        Words = Data.split()

        print("Total Number Of Words in" ,FileName,"is :",len(Words))

    except FileNotFoundError:
        print("Unable to open file as there is no such file")

    finally:
        print("End of Application")

def main():
    Name = input("Enter File Name : ")
    CountWords(Name)

if __name__ == "__main__":
    main()

# Output :
#PS C:\Users\shreya borate\OneDrive\Desktop\Python\Automation> python Assignment30.2.py Demo.txt
#Enter File Name : Demo.txt
#Total Number Of Words in Demo.txt is : 3
#End of Application
