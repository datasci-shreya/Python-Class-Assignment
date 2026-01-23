#Write a program which accept number from user and print that number of "*" on Screen 
#Input : 5 #Ouput : * * * * *   
def main():
   No = int(input("Enter a Number : "))
   for i in range (No +1):
      print("*",end=" ")
if __name__ == "__main__":
   main()  
#output:
#PS C:\Users\shreya borate\OneDrive\Desktop\Python> python Assignment16.8.py
#Enter a Number : 5
#* * * * * *