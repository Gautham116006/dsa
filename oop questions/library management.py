"""
Sure! Here's a challenging problem related to object-oriented programming (OOP):

Problem: Implement a library management system that allows users to check out and return books. The system should handle
multiple users and multiple books. Each book has a unique identifier, title, and author.
Each user has a unique identifier and a name.

Requirements:
1. The system should allow users to search for books by title or author.
2. Users should be able to check out books if they are available. Once a book is checked out, it should be marked as
unavailable.
3. Users should be able to return books they have checked out. Once a book is returned, it should be marked as available
4. The system should keep track of the due date for each checked-out book.
5. Users should not be able to check out more than a certain number of books at a time (e.g., a maximum of 3 books per
user).
6. The system should provide a way to display the list of books checked out by a particular user.
7. The system should be able to generate a report of all books currently checked out, including the user who has checked
 out each book.

Your task is to design and implement the classes and methods required to fulfill the above requirements. Think about the
relationships between the classes and how the data should be stored and managed within the system. You may also consider
 additional features or functionalities to enhance the system.

Note: You can choose any programming language to solve this problem.
"""


class Library:
    """
    The main library class
    """
    all_books = []
    readers = []

    class Book:
        def __init__(self, uid, title, author):
            """
            :param uid: The unique identifier
            :param title: The title name
            :param author: The author name
            """
            self.uid = uid
            self.title = title
            self.author = author

    # end class Book

    class Reader:
        """
        The reader class
        """

        def __init__(self, uid, name):
            """
            :param uid: The unique identifier for a reader
            :param name: The name of the reader
            """
            self.uid = uid
            self.name = name
            self.book_borrowed = 0

        # end def __init__

        def search_by_book_name(self, book_name):
            """
            :param book_name: The book name
            :return: If the book was found or not, and if it is found whether it is currently available to borrow
            """
            for book in Library.all_books:
                if book.title == book_name:
                    print("Book Found")
                    return
                    # end if
            #  end for
            print("Book not found")

        # end def search_by_book_name

        def search_by_author(self, author_name):
            """
            :param author_name: The author name
            :return: The list of books written by that author
            """
            books_by_the_same_author = []
            for book in Library.all_books:
                if book.author == author_name:
                    books_by_the_same_author.append(book)
                # end if
            # end for
            return books_by_the_same_author
        # end def search_by_author

        def borrow_book(self, book_name):
            pass
        # end def borrow_book

        def return_book(self, book_name):
            pass
        # end def return_book
    # end class Reader
# end class Library
