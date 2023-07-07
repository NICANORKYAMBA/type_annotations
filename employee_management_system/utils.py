#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Friday July  7 21:56:26 2023

@Author: Nicanor Kyamba
"""
from typing import List
from models import Employee, Department


def display_employee(employee: Employee) -> None:
    """
    Displays employee information
    """
    print("ID: {}".format(employee.id))
    print("Name: {}".format(employee.name))
    print("Age: {}".format(employee.age))
    print("Salary: {}".format(employee.salary))


def display_department(department: Department) -> None:
    """
    Displays department information
    """
    print("ID: {}".format(department.id))
    print("Name: {}".format(department.name))
    if department.manager:
        print("Manager: {}".format(department.manager.name))


def display_employees(employees: List[Employee]) -> None:
    """
    Displays employee information
    """
    for employee in employees:
        display_employee(employee)
        print()


def display_departments(departments: List[Department]) -> None:
    """
    Displays department information
    """
    for department in departments:
        display_department(department)
        print()
