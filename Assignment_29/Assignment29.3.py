#Copy File Contents into a New File (Command Line)
#Problem Statement:
#Write a program which accepts an existing file name through command line arguments, creates a new file named Demo.txt, and copies all contents from the given file into Demo.txt
#Input (Command Line):
#ABC.txt
#Expected Output:
#Create Demo.txt and copy contents of ABC.txt into Demo.txt

import sys
def CopyContent(FileName,CopyFile = "Demo.txt"):
    

    try:

        fobj = open(FileName,"r")
        print("File gets sucessfully opened")

        Data = fobj.read()

        cobj = open(CopyFile,"w")
        print("Files gets Sucessfully Created")

        cobj.write(Data)

        fobj.close()
        cobj.close()

        print("Content Copied Sucessfully into Demo.txt")

    except FileNotFoundError:
        print("Unable to open file as there is no such file")

    finally:
        print("End of Application")
        

def main():
    CopyContent(sys.argv[1])
   

if __name__ == "__main__":
    main()

# Output:
#PS C:\Users\shreya borate\OneDrive\Desktop\Python\Automation> python Assignment29.3.py ABC.txt
#File gets sucessfully opened
#Files gets Sucessfully Created
#Content Copied Sucessfully into Demo.txt
#End of Application