#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
B
Created on Fri July  7 11:00:25 2023

@Author: Nicanor Kyamba
"""
from typing import List


class Book:
    """A book object"""
    def __init__(
            self, title: str,
            author: str,
            price: float,
            publication_year: int) -> None:
        """Initialize the book"""
        self._title = title
        self._author = author
        self._price = price
        self._publication_year = publication_year


class Customer:
    """A customer object"""
    def __init__(self, name: str, email: str) -> None:
        """Initialize the customer"""
        self._name = name
        self._email = email


class Order:
    """A order object"""
    def __init__(
            self,
            customer: Customer,
            books: List[Book]) -> None:
        """Initialize the order"""
        self._customer = customer
        self._books = books
