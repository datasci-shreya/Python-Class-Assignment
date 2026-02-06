#Design automation script which accept directory name and display checksum of all files
#Usage : DirectoryChecksum.py "Demo"
#Demo is name of directory
import hashlib
import os
import sys
def DirectoryChecksum(FileName):        
    fobj = open(FileName, "rb")

    hobj = hashlib.md5()

    Buffer = fobj.read(1000)
    
    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1000)

    fobj.close()

    return hobj.hexdigest()

def DirectoryWatcher(DirectoryName):
    Ret = False

    Ret = os.path.exists(DirectoryName)

    if(Ret == False):
        print("There is no such directory")
        return
    
    Ret = os.path.isdir(DirectoryName)

    if(Ret == False):
        print("It is not a directory")
        return
    
    for FolderName, SubFolderName, Filename in os.walk(DirectoryName):
        for fname in Filename:
            fname = os.path.join(FolderName,fname)
            Checksum = DirectoryChecksum(fname)

            print(f"File name : {fname} Checksum : {Checksum}")

def main():

    if len(sys.argv) != 2:
        print("Invalid number of arguments")
        return
    
    DirectoryWatcher(sys.argv[1])
    
if __name__ == "__main__":
    main() 

#Output :
#PS C:\Users\shreya borate\OneDrive\Desktop\Python\Automation> python Assignment32.1.py Demo
#File name : Demo\Hello.doc Checksum : 8a6ff01aed7cbaff69339b76a5bdc9fb
#File name : Demo\Hello.exe Checksum : d41d8cd98f00b204e9800998ecf8427e
#File name : Demo\Python.doc Checksum : d9a1bda2a347af1799bcf3d676faaad7
#File name : Demo\Python.exe Checksum : d41d8cd98f00b204e9800998ecf8427e