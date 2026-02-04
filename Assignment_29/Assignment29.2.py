#Display File Contents
#Problem Statement:
#Write a program which accepts a file name from the user, opens that file, and displays the entire contents on the console
#Input:
#Demo.txt
#Expected Output:
#Display contents of Demo.txt on console
def main():
    FileName = input ("Enter File Name : ")
    try:

        fobj = open(FileName,"r")
        print("File gets sucessfully opened")

        Data = fobj.read()

        print("Data from file is : ",Data)
        fobj.close()

    except FileNotFoundError:
        print("Unable to open file as there is no such file")

    finally:
        print("End of Application")
        

if __name__ == "__main__":
    main()

# Output :  
#PS C:\Users\shreya borate\OneDrive\Desktop\Python\Automation> python Assignment29.2.py
#Enter File Name : Demo.txt
#File gets sucessfully opened
#Data from file is :  Jay Ganesh Marvellous...
#End of Application