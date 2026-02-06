#Design automation script which accept directory name and delete all duplicate files from that directory. Write names of duplicate files from that directory into log file named as Log.txt. Log.txt file should be created into current directory
#Usage: Directory Dusplicate Removal.py "Demo"
#Demo is name of directory
import hashlib
import os
import sys

def CalculateChecksum(FileName):       
    fobj = open(FileName, "rb")

    hobj = hashlib.md5()

    Buffer = fobj.read(1000)
    
    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1000)

    fobj.close()

    return hobj.hexdigest()

def FindDuplicate(DirectoryName = "Marvellous"):
    Ret = False

    Ret = os.path.exists(DirectoryName)

    if(Ret == False):
        print("There is no such directory")
        return
    
    Ret = os.path.isdir(DirectoryName)

    if(Ret == False):
        print("It is not a directory")
        return
    
    Duplicate = {}

    for FolderName, SubFolderName, Filename in os.walk(DirectoryName):
        for fname in Filename:
            fname = os.path.join(FolderName,fname)
            Checksum = CalculateChecksum(fname)

            if Checksum in Duplicate:
                Duplicate[Checksum].append(fname)
            else:
                Duplicate[Checksum] = [fname]

    return Duplicate

def DisplayResult(MyDict):
    fobj = open("Log.txt","w")
    Result = list(filter(lambda x : len(x) > 1, MyDict.values()))

    for files in Result:
        for fname in files:
            fobj.write(fname + "\n")

        
    fobj.close()

    print("Duplicates file names written in Log.txt")

def DeleteDuplicate(Path):

    MyDict = FindDuplicate(Path)

    Result = list(filter(lambda x : len(x) > 1, MyDict.values()))

    Count = 0
    Cnt = 0

    for value in Result:
        for subvalue in value:
            Count = Count + 1
            if(Count > 1):
                print("Deleted file : ",subvalue)
                os.remove(subvalue)
                Cnt = Cnt + 1
        Count = 0

    print("Total deleted files : ",Cnt)

def main():
    if len(sys.argv) != 2:
        print("Invalid Number of Arguments")
        return

    Duplicate = FindDuplicate(sys.argv[1])
    DisplayResult(Duplicate)

    DeleteDuplicate(sys.argv[1])

if __name__ == "__main__":
    main()

#Output :
#PS C:\Users\shreya borate\OneDrive\Desktop\Python\Automation> python Assignment32.3.py Demo
#Duplicates file names written in Log.txt
#Deleted file :  Demo\Hello.txt
#Deleted file :  Demo\python.txt
#Total deleted files :  2