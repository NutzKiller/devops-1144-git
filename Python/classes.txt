# Exercise: Understanding a Python Library System
#1
# What is the purpose of the `Book` class? What attributes does it have?
# What is the purpose of the `Library` class? What does its `books` attribute store?

#the purpose of the "Book" class is to create new books and store their attributes which is "title", "author", "copies"
#the purpose of the "Library" class is to hold and store books and their attributes and the "books" attribute store the books in the library and their attributes are "title", "author", "copies"

#2
# What does the `add_book` method do?
# What happens when the `list_books` method is called?

#the "add_book" method adds a new book and appends it to the list of books list
#the "list_books" method lists all the books in the library

#3
# What is the output of the `list_books` method after the books are added?
# What happens if you call `add_book` with a new book object?

#the output of the "list_books" method is: "Python 101", "John Doe", 3 and "Data Science Handbook", "Jane Smith", 5

#if you call "add_book" with a new book object, it will be added to the list of books

#4
# If you wanted to add a method to find a book by title in the library, how would you do it?

#you can add a method find_a_book by title in the library by adding a new method to the "Library" class and then calling it in the "list_books" method and then calling it in the "find_a_book" method