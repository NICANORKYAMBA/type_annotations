#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri July 7 11:00 2023

@Author: Nicanor Kyamba
"""
from typing import List
from models import Book, Customer, Order


def display_books(books: List[Book]) -> None:
    if books:
        for book in books:
            print("Title: {}".format(book._title))
            print("Author: {}".format(book._author))
            print("Price: ${}".format(book._price))
            print("Publication Year: {}".format(book._publication_year))
            print()
    else:
        print("No books found")


def display_customers(customers: List[Customer]) -> None:
    if customers:
        for customer in customers:
            print("Name: {}".format(customer._name))
            print("Email: {}".format(customer._email))
            print()
    else:
        print("No customers found")


def display_orders(orders: List[Order]) -> None:
    if orders:
        for order in orders:
            print("Customer: {}".format(order._customer._name))
            print("Books Ordered:")
            for book in order._books:
                print("Title: {}".format(book._title))
                print("Author: {}".format(book._author))
                print("Price: ${}".format(book._price))
                print("Publication Year: {}".format(book._publication_year))
                print()
            print()
    else:
        print("No orders found")
