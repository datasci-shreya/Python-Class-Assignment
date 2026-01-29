#Write a Python program to implement a class named BookStore with the following specifications:
#The class should contain two instance variables:
#Name (Book Name)
#Author (Book Author)
#The class should contain one class variable:
#Noof Books (initialize it to 0)
#Define a constructor (init) that accepts Name and Author and initializes instance variables.
#Inside the constructor, increment the class variable NoOf Books by 1 whenever a new object is created.
#Implement ati instance method:
#Display() should display book details in the format: <BookName> by <Author>. No of books: <NoOfBooks>
#Example usage:
#obj1 BookStore ("Linux System Programming", "Robert Love")
#Objl. Display() #Linux System Programming by Robert Love. No of books: 1
#Obj2 BookStore("C Programming", "Dennis Ritchie") Obj2.Display() #C Programming by Dennis Ritchie. No of books: 2
class BookStore:
    NoOfBooks = 0

    def __init__(self, Name, Author):
        self.Name = Name
        self.Author = Author
        BookStore.NoOfBooks = BookStore.NoOfBooks + 1

    def Display(self):
        print(f"{self.Name} by {self.Author}. No of books : {BookStore.NoOfBooks}")

obj1 = BookStore("Linux System Programming", "Robert Love")
obj1.Display()

obj2 = BookStore("C Programming", "Dennis Ritchie")
obj2.Display()

#Output :
#PS C:\Users\shreya borate\OneDrive\Desktop\Python> python Assignment23.1.py
#Linux System Programming by Robert Love. No of books : 1
#C Programming by Dennis Ritchie. No of books : 2