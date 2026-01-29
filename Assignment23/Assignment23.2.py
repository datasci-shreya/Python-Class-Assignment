#Write a Python program to implement a class named BankAccount with the following requirements:
#The class should contain two instance variables:
#Name (Account holder name)
#Amount (Account balance)
#The class should contain one class variable:
#ROI (Rate of Interest), initialized to 10.5
#Define a constructor (init) that accepts Name and initial Amount
#Implement the following instance methods:
#Display()-displays account holder name and current balance 
#Deposit()-accepts an amount from the user and adds it to balance
#Withdraw()- accepts an amount from the user and subtracts it from balance (Ensure withdrawal is allowed only if sufficient balance exists)
#CalculateInterest()-calculates and returns interest using formula: Interest (Amount ROI) / 100
#Create multiple objects and demonstrate all methods.
class BankAccount:
    ROI = 10.5

    def __init__(self, Name, Amount):
        self.Name = Name
        self.Amount = Amount


    def Display(self):
        print("----- Account Details -----")
        print("Account Holder Name :", self.Name)
        print("Current Balance     :", self.Amount)


    def Deposit(self):
        value = float(input("Enter amount to deposit: "))
        self.Amount =self.Amount + value
        print("Deposit Successful!")

  
    def Withdraw(self):
        value = float(input("Enter amount to withdraw: "))

        if value <= self.Amount:
            self.Amount -= value
            print("Withdrawal Successful")
        else:
            print("Insufficient Balance")

    def CalculateInterest(self):
        interest = (self.Amount * BankAccount.ROI) / 100
        return interest

obj1 = BankAccount("Shreya", 5000)

obj1.Display()

obj1.Deposit()
obj1.Display()

obj1.Withdraw()
obj1.Display()

interest = obj1.CalculateInterest()
print("Interest on balance =", interest)

#Output :
#PS C:\Users\shreya borate\OneDrive\Desktop\Python> python Assignment23.2.py
#----- Account Details -----
#Account Holder Name : Shreya
#Current Balance     : 5000
#Enter amount to deposit: 500
#Deposit Successful!
#----- Account Details -----
#Account Holder Name : Shreya
#Current Balance     : 5500.0
#Enter amount to withdraw: 3000
#Withdrawal Successful
#----- Account Details -----
#Account Holder Name : Shreya
#Current Balance     : 2500.0
#Interest on balance = 262.5