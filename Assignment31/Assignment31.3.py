#Design automation script which accept two directory names. Copy all files from first directory into second directory. Second directory should be created at run time.
#Usage: Directory Copy.py "Demo" "Temp"
#Demo is name of directory which is existing and contains files in it. We have to create new Directory as Temp and copy all files from Demo to Temp.
import os 
import sys 
def DirectoryCopy(FirstDirectory,SecondDirectory): 
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

        for File in os.listdir(FirstDirectory):

            FirstDirectory_path = os.path.join(FirstDirectory,File)
            SecondDirectory_path = os.path.join(SecondDirectory,File)
            print("Files in source directory:", os.listdir(FirstDirectory))


            if os.path.isfile(FirstDirectory_path):
                fobj = open(FirstDirectory_path,"rb")
                fobj1 = open(SecondDirectory_path,"wb")
                
                Data = fobj.read()
                fobj1.write(Data)

                print("Copying from",FirstDirectory,"to",SecondDirectory)

                print("Copied : ",File)

    except FileNotFoundError:
        print("Unable to open file as there is no such file")

    finally:
        print("End of Application")

def main():

    if len(sys.argv) != 3:
        print("Invalid Number of Arguments")
        return

    DirectoryCopy(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()

#Output :
#PS C:\Users\shreya borate\OneDrive\Desktop\Python\Automation> python Assignment31.3.py Demo temp
#Files in source directory: ['Hello.doc', 'Python.doc']
#Copying from Demo to temp
#Copied :  Hello.doc
#Files in source directory: ['Hello.doc', 'Python.doc']
#Copying from Demo to temp
#Copied :  Python.doc
#End of Application



    
        