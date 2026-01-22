#write a program which accepts marks and display grade
#condition example
#>=75-Distinction
#>=60-first class
#>=50-second class
#< 50-fail
print("Enter Marks : ")
Marks = int(input())
if Marks>= 75:
    print("Grade:Distinction")
elif Marks >= 60:
    print("Grade:First Class")
elif Marks >= 50:
    print("Grade:Second Class")
else:
    print("Grade:Fail")




