#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2023/7/7 10:30
# @Author  : Nicanor Kyamba
# @File    : database.py

from typing import Optional, List
from models import Book, Customer, Order


class BookDatabase:
    """Book database object."""
    def __init__(self) -> None:
        """Initialize the book database."""
        self._books: List[Book] = []
        self._customers: List[Customer] = []
        self._orders: List[Order] = []

    def add_book_to_database(self, book: Book) -> None:
        """Add a book to the database."""
        self._books.append(book)

    def add_customer_to_database(self, customer: Customer) -> None:
        """Add a customer to the database."""
        self._customers.append(customer)

    def place_orders_to_database(self, order: Order) -> None:
        """Add an order to the database."""
        self._orders.append(order)

    def get_books_from_database(self) -> Optional[list[Book]]:
        """Get all books from the database."""
        return self._books

    def get_customers_from_database(self) -> Optional[list[Customer]]:
        """Get all customers from the database."""
        return self._customers

    def get_orders_from_database(self) -> Optional[list[Order]]:
        """Get all orders from the database."""
        return self._orders
