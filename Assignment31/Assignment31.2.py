#Design automation script which accept directory name and two file extensions from user.
#Rename all files with first extension with the second file extension
#Usage : DirectoryRename.py "Demo" ".txt" ".doc"
#Demo is name of directory and .txt is the extension that we want to search and rename with .doc
#After execution that script each .txt file gets renamed as .doc
#Design automation script which accept directory name and two file extensions from user.
#Rename all files with first extension with the second file extension
#Usage : DirectoryRename.py "Demo" ".txt" ".doc"

import os
import sys

def DirectoryRename(DirName, OldExt, NewExt):

    try:
        Ret = os.path.exists(DirName)
        if Ret == False:
            print("There is no such directory")
            return

        Ret = os.path.isdir(DirName)
        if Ret == False:
            print("It is not a directory")
            return

        print("\nRenaming files from", OldExt, "to", NewExt, "\n")

        for File in os.listdir(DirName):

            if File.endswith(OldExt):

                OldFileName = os.path.join(DirName, File)

                NewFileName = File.replace(OldExt, NewExt)
                NewFileName = os.path.join(DirName, NewFileName)

                os.rename(OldFileName, NewFileName)

                print("Renamed :", OldFileName, "--", NewFileName)

    except FileNotFoundError:
        print("Unable to open file as there is no such file")

    finally:
        print("End of Application")

def main():
    if len(sys.argv) != 4:
        print("Invalid Number of Arguments")
        return

    DirectoryRename(sys.argv[1], sys.argv[2], sys.argv[3])

if __name__ == "__main__":
    main()

#Output :
#PS C:\Users\shreya borate\OneDrive\Desktop\Python\Automation> python Assignment31.2.py Demo .txt .doc\
#Renaming files from .txt to .doc\
#Renamed : Demo\Hello.txt -- Demo\Hello.doc\
#Renamed : Demo\Python.txt -- Demo\Python.doc\
#End of Application