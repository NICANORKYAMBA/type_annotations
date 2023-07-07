#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri July  07 22:19:07 2023

@Author: Nicanor Kyamba
"""
from sqlalchemy.orm import Session
from models import Employee, Department
from database import EmployeeDatabase
from utils import display_employees, display_departments


def main() -> None:
    """Main"""
    db_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format("nicanorkyamba", "NICmakya98", "employees_db")
    database = EmployeeDatabase(db_url)

    """Create session"""
    session: Session = database.get_session()

    """Create tables"""
    database.create_tables()

    """Add employees to database"""
    employee1 = Employee(name="John Doe", age=30, salary=4500.0)
    employee2 = Employee(name="Jane Doe", age=20, salary=2000.0)
    employee3 = Employee(name="Jack Doe", age=40, salary=5000.0)
    session.add_all([employee1, employee2, employee3])
    session.commit()

    """Add departments to database"""
    department1 = Department(name="IT", manager=employee1)
    department2 = Department(name="Engineering")
    session.add_all([department1, department2])
    session.commit()

    """Retrieve and display employees and departments"""
    employees = session.query(Employee).all()
    departments = session.query(Department).all()

    print("Employees:")
    display_employees(employees)

    print("Departments:")
    display_departments(departments)


if __name__ == "__main__":
    """Run main"""
    main()
