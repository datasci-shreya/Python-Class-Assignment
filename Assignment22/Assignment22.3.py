#Write a Python program to implement a class named Arithmetic with the following characteristics:
#The class should contain two instance variables: Valuel and Value2
#Define a constructor (init) that initializes all instance variables to 0
#Implement the following instance methods:
#Accept()-accepts values for Valuel and Value2 from the user
#Addition()- returns the addition of Valuel and Value2
#Subtraction () - returns the subtraction of Valuel and Value2
#Multiplication() returns the multiplication of Valuel and Value2
#Division()- returns the division of Valuel and Value2 (handle division by zero properly)
#Create multiple objects of the Arithmetic class and invoke all the instance methods
class Arithmetic:

    def __init__(self):
        self.No1 = 0
        self.No2 = 0

    def Accept(self):
        self.No1 = int(input("Enter First Number :"))
        self.No1 = int(input("Enter Second Number :"))
    
    def Addition(self):
        return self.No1 + self.No2
        
    
    def Subtraction(self):
        return self.No1 - self.No2
        
    
    def Multiplication(self):
        return self.No1 * self.No2
    
    def Division(self):
        if self.No2 == 0:
            print("Error: Division by zero is not allowed")
            return None
        else:
            return self.No1 / self.No2
        
obj1 = Arithmetic()
obj1.Accept()
print("Addition is:", obj1.Addition())
print("Subtraction is:", obj1.Subtraction())
print("Multiplication is:", obj1.Multiplication())
print("Division is:", obj1.Division())

obj2 = Arithmetic()
obj2.Accept()
print("Addition is:", obj2.Addition())
print("Subtraction is:", obj2.Subtraction())
print("Multiplication is:", obj2.Multiplication())
print("Division is:", obj2.Division())

#Output:
#PS C:\Users\shreya borate\OneDrive\Desktop\Python> python Assignment22.3.py
#Enter First Number :8
#Enter Second Number :2
#Addition is: 2
#Subtraction is: 2
#Multiplication is: 0
#Error: Division by zero is not allowed
#Division is: None
#Enter First Number :17
#Enter Second Number :3
#Addition is: 3
#Subtraction is: 3
#Multiplication is: 0
#Error: Division by zero is not allowed
#Division is: None