#Write a python program to implement a class named demo with the following specification
#The class should contains two instance variables: No1 and No2
#The class should contain one class variable named Value
#Define a constructor (__init__) that accept two parameters and initializes the instance variables
#Implements two intance methods:
#Fun() - display the values of instance variables no1 and no2
#Gun() - display the values of instance variables no1 and no2
#Create two objects of the demo class as follows:
#obj1 = demo(11,21)
#obj2 = demo(51,101)
#call the instance methoods in the given sequence:
#obj1.Fun()
#obj2.Fun()
#obj1.Gun()
#obj2.Gun()
class Demo:
    Value = 10

    def __init__(self,A,B):
        self.No1 = A
        self.No2 = B

    def fun (self):
        print("Inside instance Method fun : ",self.No1,self.No2)

    def gun (self):
        print("Inside instance Method gun : ",self.No1,self.No2)

obj1 = Demo(11,21)
obj2 = Demo(51,101)
    
obj1.fun()
obj2.fun()
obj1.gun()
obj2.gun()
        
#Output :
#PS C:\Users\shreya borate\OneDrive\Desktop\Python> python Assignment22.1.py
#Inside instance Method fun :  11 21
#Inside instance Method fun :  51 101
#Inside instance Method gun :  11 21
#Inside instance Method gun :  51 101