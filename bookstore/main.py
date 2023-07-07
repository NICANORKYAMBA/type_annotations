#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri July  7 12:39:26 2023

@Author: Nicanor Kyamba
"""
from database import BookDatabase
from customer import CustomerManager
from order import OrderManager
from utils import display_books, display_customers, display_orders
from models import Book, Customer


def main() -> None:
    database = BookDatabase()
    customer_manager = CustomerManager(database)
    order_manager = OrderManager(database)

    """Add books to the database"""
    book1 = Book("The Hobbit", "J.R.R. Tolkien", 10.99, 2022)
    book2 = Book("The Lord of the Rings", "J.R.R. Tolkien", 14.99, 2021)
    book3 = Book("The Cuacasian Chalk Circle", "Bertolt Bretch", 12.99, 2023)
    book4 = Book("The Seven Kings of Dorne", "Bertolt Bretch", 15.99, 2022)
    book5 = Book("The River and the Source", "Margret Ogola", 20.99, 2010)
    database.add_book_to_database(book1)
    database.add_book_to_database(book2)
    database.add_book_to_database(book3)
    database.add_book_to_database(book4)
    database.add_book_to_database(book5)

    """Add customers to the database"""
    customer1 = Customer("Nicanor Kyamba", "kyamba@me.com")
    customer2 = Customer("John Smith", "john@me.com")
    customer3 = Customer("Jane Doe", "jane@me.com")
    customer4 = Customer("Kalvins Dolphin", "kalvins@me.com")
    database.add_customer_to_database(customer1)
    database.add_customer_to_database(customer2)
    database.add_customer_to_database(customer3)
    database.add_customer_to_database(customer4)

    """Place orders"""
    order_manager.place_order(customer1, [book1, book2])
    order_manager.place_order(customer2, [book4, book3, book5, book1])
    order_manager.place_order(customer3, [book1, book5, book3])
    order_manager.place_order(customer4, [book5, book1, book2])

    """Retrieve books from the database"""
    books = database.get_books_from_database()
    customers = customer_manager.get_customers()
    orders = order_manager.get_orders()

    """Display books"""
    print("Books available in our bookstore:")
    display_books(books)

    """Display customers"""
    print("Customers using our bookstore:")
    display_customers(customers)

    """Display orders"""
    print("Orders placed:")
    display_orders(orders)


if __name__ == "__main__":
    """Run the main function"""
    main()
