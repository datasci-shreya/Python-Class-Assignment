#Design automation script which accept directory name and file extension from user.Display all files with that extension
#Usage : DirectoryFileSearch.py "Demo" ".txt"
#Demo is name of directory and .txt is the extension that we want to search
import os
import sys

def DirectoryFileSearch(DirName , Extension):

    try:
        Ret = os.path.exists(DirName)
        if Ret == False:
            print("There is no such directory")
            return

        Ret = os.path.isdir(DirName)
        if Ret == False:
            print("It is not a directory")
            return

        print("Files with .txt Extentions are :")

        for File in os.listdir(DirName):
            if File.endswith(Extension):
                print(DirName + "/" + File)

    except FileNotFoundError:
        print("Unable to open file as there is no such file")

    finally:
        print("End of Application")

def main():

    if len(sys.argv) != 3:
        print("Invalid Number of Arguments")
        return

    DirectoryFileSearch(sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    main()

#Output :
#PS C:\Users\shreya borate\OneDrive\Desktop\Python\Automation> python Assignment31.1.py Demo .txt
#Files with .txt Extentions are :
#Demo/Hello.txt
#Demo/Python.txt
#End of Application