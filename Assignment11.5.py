#write a program which accepts one number and checks whether it is palindrome or not  
#input -121  
#output - palindrome
print("Enter a number : ")
No = int(input())

Ans = No
result = 0

while No > 0:
    digit = No % 10
    result = result * 10 + digit
    No = No // 10

if Ans == result:
    print("Palindrome")
else:
    print("Not Palindrome")
