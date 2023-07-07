#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 10:05:55 2019

@Author: Firstname Lastname
"""
from typing import List
from models import Order, Customer, Book
from database import BookDatabase
from utils import display_orders


class OrderManager:
    def __init__(self, database: BookDatabase) -> None:
        """Class Constructor."""
        self._database = database

    def place_order(self, customer: Customer, books: List[Book]) -> None:
        """Placing an order."""
        order = Order(customer, books)
        self._database.place_orders_to_database(order)

    def get_orders(self) -> List[Order]:
        """Get all orders."""
        return self._database.get_orders_from_database()

    def display_all_orders(self) -> None:
        """Diplay all orders"""
        orders = self.get_orders()
        display_orders(orders)
