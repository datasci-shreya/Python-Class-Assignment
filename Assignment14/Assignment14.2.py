#Write a lambda function which accept one number and returns cube of that number
#First method
Cube = lambda No : No * No *No
No= int(input("Enter a number : "))
Result = Cube(No)
print("Cube is : ",Result)

print("_"*15)
#Second method 
Cube = lambda No : No * No * No
def main():
    Value = 0
    print("Enter a Number : ")
    Value = int(input())
    Ret = Cube(Value)
    print("Cube is : ",Ret)
      
if __name__ == "__main__":
      main()
#Enter a number : 6
#Cube is :  216
#_______________
#Enter a Number :
#6
#Cube is :  216