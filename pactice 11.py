class Book:
    def __init__ (self, title, author, price, quantity):
        self.title = title
        self.author = author
        self.price = price
        self.quantity = quantity

    def apply_discount(self, discount_percentage):
        return self.price * discount_percentage/100

    def sell(self, amount):
        if self.quantity > 0:
            return self.quantity - amount
        elif self.quantity == 0:
            print('Не вистачає кількості заданої книги')

    def __str__(self):
        return f'Title: {self.title},Author: {self.author},Price {self.price},Quantity:{self.quantity}'

class BookStore:
    def __init__ (self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def search(self, query):
        filtered_books=[]
        for book in self.books:
            if query in (book.title, book.author):
                filtered_books.append(book)
        return filtered_books

    def calculate_total_value(self):
        total_value = 0
        for book in self.books:
            total_value += book.price * book.quantity

        return total_value


