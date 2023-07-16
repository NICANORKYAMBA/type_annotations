#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun July 09 11:30:00 2023

@Author: Nicanor Kyamba
"""
from database import EmployeeDatabase


"""Create a database connection"""
DB_URL = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
    "nicanorkyamba", "NICmakya98", "employees_db")

"""Create an instance of EmployeeDatabase"""
db = EmployeeDatabase(DB_URL)

"""Create employees"""
employee1 = db.create_employee(
    name='John Doe', age=25, salary=4500.67)
employee2 = db.create_employee(
    name='Nicanor Kyamba', age=21, salary=6500.99)
employee3 = db.create_employee(
    name='Jane Lucky', age=19, salary=3299.59)

"""Create departments"""
department1 = db.create_department(
    name='ICT', manager_id=employee1.employee_id)
department2 = db.create_department(
    name='Engineering and Construction', manager_id=employee2.employee_id)
department3 = db.create_department(
    name='Food and Science', manager_id=employee3.employee_id)

"""Add employees to departments"""
db.add_employee_to_department(employee1.employee_id, department1.department_id)
db.add_employee_to_department(employee2.employee_id, department2.department_id)
db.add_employee_to_department(employee3.employee_id, department3.department_id)

"""Create projects"""
project1 = db.create_project(name='Software Development: Planning Stage')
project2 = db.create_project(
    name='Taking levels and mass hauling on the ground')

"""Add employees to projects"""
db.add_employee_to_project(employee1.employee_id, project1.project_id)
db.add_employee_to_project(employee2.employee_id, project1.project_id)
db.add_employee_to_project(employee3.employee_id, project2.project_id)
