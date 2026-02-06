#Design automation script which accept two directory names and one file extension. Copy all files with the specified extension from first directory into second directory. Second directory should be created at run time.
#Usage: Directory CopyExt.py "Demo" "Temp" ".exe"
#Demo is name of directory which is existing and contains files in it. We have to create new Directory as Temp and copy all files with extension.exe from Demo to Temp.
import os 
import sys 
def DirectoryCopyExtension(FirstDirectory,SecondDirectory,Extension): 
    try:
        Ret = os.path.exists(FirstDirectory)
        if Ret == False:
            print("There is no such directory")
            return
        
        Ret = os.path.isdir(FirstDirectory)
        if Ret == False:
            print("It is not a directory")
            return
        
        if not os.path.exists(SecondDirectory):
            os.mkdir(SecondDirectory)

        print("Files to be copied with extension", Extension)

        for File in os.listdir(FirstDirectory):
            
            if File.endswith(Extension):

                FirstDirectory_path = os.path.join(FirstDirectory,File)
                SecondDirectory_path = os.path.join(SecondDirectory,File)

                if os.path.isfile(FirstDirectory_path):
                     fobj = open(FirstDirectory_path,"rb")
                     fobj1 = open(SecondDirectory_path,"wb")
                        
                     Data = fobj.read()
                     fobj1.write(Data)

                     fobj.close()
                     fobj1.close()

                     print("Copied : ",File)
                       
    except FileNotFoundError:
        print("Unable to open file as there is no such file")

    finally:
        print("End of Application")

def main():

    if len(sys.argv) != 4:
        print("Invalid Number of Arguments")
        return

    DirectoryCopyExtension(sys.argv[1], sys.argv[2],sys.argv[3])

if __name__ == "__main__":
    main()

#Output :
#PS C:\Users\shreya borate\OneDrive\Desktop\Python\Automation> python Assignment31.4.py Demo temp .exe
#Files to be copied with extension .exe
#Copied :  Hello.exe
#Copied :  Python.exe
#End of Application
    
        