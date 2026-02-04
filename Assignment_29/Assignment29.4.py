#Compare Two Files (Command Line)
#Problem Statement:
#Write a program which accepts two file names through command line arguments and compares the contents of both files
#If both files contain the same contents, display Success
#Otherwise display Failure
#Input (Command Line):
#Demo.txt Hello.txt
#Expected Output:
#Success OR Failure

import sys

def CompareFiles(File1, File2):

    try:
        fobj1 = open(File1, "r")
        print("First file opened successfully")

        fobj2 = open(File2, "r")
        print("Second file opened successfully")

        Data1 = fobj1.read()
        Data2 = fobj2.read()

        if Data1 == Data2:
            print("Success")
        else:
            print("Failure")

        fobj1.close()
        fobj2.close()

    except FileNotFoundError:
        print("Unable to open file as there is no such file")

    finally:
        print("End of Application")
def main():

    CompareFiles(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()

#Output :
#PS C:\Users\shreya borate\OneDrive\Desktop\Python\Automation> python Assignment29.4.py Demo.txt Hello.txt
#First file opened successfully
#Second file opened successfully
#Success
#End of Application