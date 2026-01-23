#Write a lambda function using filter() which accepts a list of strings and returns the list of strings having length greater than 5
String = lambda a : len(a) > 5
def main():
    Data = ["Shreya","Shrutika","Siya","Sanika","Samu"]
    print("Actual Data is : ",Data)
    FData =list(filter(String,Data))
    #FData=list(filter( lambda a : len(a) > 5,Data))
    print("Data After Filter is : ",FData)

if __name__ == "__main__":
    main()
#Output
#Actual Data is :  ['Shreya', 'Shrutika', 'Siya', 'Sanika', 'Samu']
#Data After Filter is :  ['Shreya', 'Shrutika', 'Sanika']