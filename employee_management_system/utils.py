#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun July 09 12:00:00 2023

@Author: Nicanor Kyamba
"""
from models import Employee, Department, Project, User


def print_employee(employee: Employee) -> None:
    """Print employee details"""
    print("Employee: ")
    print("Employee ID: {}".format(employee.employee.id))
    print("Name: {}".format(employee.name))
    print("Age: {}".format(employee.age))
    print("Salary: {}".format(employee.salary))
    print("Department ID: {}".format(employee.department_id))
    print()

def print_department(department: Department) -> None:
    """Print department details"""
    print("Department: ")
    print("Department ID: {}".format(department.department.id))
    print("Name: {}".format(department.name))
    print("Manager ID: {}".format(department.manager_id))

def print_project(project: Project) -> None:
    """Print project details"""
    print("Project: ")
    print("Project ID: {}".format(project.project_id))
    print("Name: {}".format(project.project_name))
    print()

def print_user(user: User) -> None:
    """Print user details"""
    print("User details: ")
    print("User ID {}".format(user.user_id))
    print("Username: {}".format(user.username))
    print("Password Hash: {}".format(user.password_hash))
    print()
