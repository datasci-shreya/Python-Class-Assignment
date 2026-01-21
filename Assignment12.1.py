#Write a program which accepts one character and checks whether it is vowel or consonant
#input - a
#output - Vowel
print("Enter a number : ")
char = int(input())

if char in "aeiouAEIOU":
    print("Vowel")
else:
    print("Consonant")