#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  5 15:51:26 2020

@Author: Firstname Lastname
"""
from typing import List
from models import Customer
from database import BookDatabase
from utils import display_customers


class CustomerManager:
    """Class for managing customers"""
    def __init__(self, database: BookDatabase) -> None:
        """Initialize the customer manager"""
        self._database = database

    def add_customer(self, name: str, email: str) -> None:
        """Add a customer to the database"""
        customer = Customer(name, email)
        self._database.add_customer_to_database(customer)

    def get_customers(self) -> List[Customer]:
        """Get all customers from the database"""
        return self._database.get_customers_from_database()

    def display_all_customers(self) -> None:
        """Display all customers"""
        customers = self.get_customers()
        display_customers(customers)
