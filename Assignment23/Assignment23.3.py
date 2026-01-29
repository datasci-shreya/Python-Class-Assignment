#Write a Python program to implement a class named Numbers with the following specifications:
#The class should contain one instance variable:
#Value
#Define a constructor (init) that accepts a number from the user and initializes Value.
#Implement the following instance methods:
#ChkPrime()-returns True if the number is prime, otherwise returns False
#ChkPerfect()-retturns True if the number is perfect, otherwise returns False
#Factors()-displays all factors of the number
#SumFactors()-returns the sum of all factors (You may use this method as a helper in ChkPerfect() if required)
#Create multiple objects and call all methods.
class Numbers:
    def __init__(self, Value):
        self.Value = Value

    def ChkPrime(self):
        if self.Value <= 1:
            return False

        for i in range(2, self.Value):
            if self.Value % i == 0:
                return False

        return True

    def Factors(self):
        print("Factors are :")
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                print(i)
                
    def SumFactors(self):
        Sum = 0
        for i in range(1, self.Value):
            if self.Value % i == 0:
                Sum = Sum + i
        return Sum

    def ChkPerfect(self):
        if self.SumFactors() == self.Value:
            return True
        else:
            return False

num1 = Numbers(7)

print("Number =", num1.Value)

if num1.ChkPrime():
    print("It is a Prime number")
else:
    print("It is NOT a Prime number")

num1.Factors()

if num1.ChkPerfect():
    print("It is a Perfect number")
else:
    print("It is NOT a Perfect number")

print("-"*20)

num2 = Numbers(28)

print("Number =", num2.Value)

if num2.ChkPrime():
    print("It is a Prime number")
else:
    print("It is NOT a Prime number")

num2.Factors()

if num2.ChkPerfect():
    print("It is a Perfect number")
else:
    print("It is NOT a Perfect number")

#Output :
#PS C:\Users\shreya borate\OneDrive\Desktop\Python> python Assignment23.3.py
#Number = 7
#It is a Prime number
#Factors are :
#1
#7
#It is NOT a Perfect number
#--------------------
#Number = 28
#It is NOT a Prime number
#Factors are :
#1
#2
#4
#7
#14
#28
#It is a Perfect number