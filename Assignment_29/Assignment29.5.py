#Frequency of a String in File
#Problem Statement:
#Write a program which accepts a file name and one string from the user and returns the frequency (count of occurrences) of that string in the file.
#Input:
#Demo.txt Marvellous
#Expected Output:
#Count how many times "Marvellous" appears in Demo.txt
import sys

def StringFrequency(FileName, SearchString):
    try:
        fobj = open(FileName, "r")
        print("File opened successfully")
        Data = fobj.read()
        Count = Data.count(SearchString)

        print("Frequency of string is:", Count)
        fobj.close()

    except FileNotFoundError:
        print("Unable to open file as there is no such file")

    finally:
        print("End of Application")
def main():
    StringFrequency(sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    main()

#Output :
#PS C:\Users\shreya borate\OneDrive\Desktop\Python\Automation> python Assignment29.5.py Demo.txt Marvellous
#File opened successfully
#Frequency of string is: 1
#End of Application