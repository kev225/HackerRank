'''
Task
Given a Book class and a Solution class, write a MyBook class that does the following:

Inherits from Book
Has a parameterized constructor taking these 3 parameters:
1.string  title
2.string  author
3.int     price
Implements the Book class' abstract display() method so it prints these  lines:
,Title: a space, and then the current instance's title.
,Author: a space, and then the current instance's author.
,Price: a space, and then the current instance's price.
'''

from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass
        
    

#Write MyBook class
class MyBook(Book):
    def __init__(self,title,author,price):
        self.title = title
        self.author= author
    def display(self):
        print("Title:", title)
        print("Author:",author)
        print("Price:", price)
            
    
title=input('Title:')
author=input('Author:')
price=int(input('Price:$'))
new_novel=MyBook(title,author,price)
new_novel.display()
