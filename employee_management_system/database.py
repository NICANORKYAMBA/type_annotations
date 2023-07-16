#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun July  09 11:00:00 2023

@Author: Nicanor Kyamba
"""
from sqlalchemy import create_engine, Column
from sqlalchemy.orm import sessionmaker
from models import Base, Employee, Department, Project, User
from uuid import UUID
import MySQLdb


class EmployeeDatabase:
    """Employee Database"""

    def __init__(self, db_url: str) -> None:
        """Initializing the class"""
        self._engine = create_engine(db_url, module=MySQLdb, echo=False)
        Base.metadata.create_all(self._engine)
        Session = sessionmaker(bind=self._engine)
        self._Session = Session()

    def create_employee(self,
                        name: str,
                        age: int,
                        salary: float,
                        department_id: UUID = None) -> Employee:
        """Create employee"""
        if not name:
            raise ValueError('Name is required')
        if age <= 18:
            raise ValueError(
                'An employee cannot be less than 18 years of age!')
        if salary < 1000:
            raise ValueError('Salary should be above 1000 USD')
        employee = Employee(
            name=name,
            age=age,
            salary=salary,
            department_id=department_id if department_id else None
        )
        self._Session.add(employee)
        self._Session.commit()
        return employee

    def get_employee(self, employee_id: UUID) -> Employee:
        """Get employee"""
        return self._Session.query(Employee).get(employee_id)

    def update_employee(self,
                        employee_id: UUID,
                        name: str = None,
                        age: int = None,
                        salary: float = None) -> Employee:
        """Update employee"""
        employee = self.get_employee(employee_id)
        if name is not None:
            employee.name = name
        if age is not None:
            employee.age = age
        if salary is not None:
            employee.salary = salary
        self._Session.commit()
        return employee

    def delete_employee(self,
                        employee_id: UUID) -> Employee:
        """Delete employee"""
        employee = self.get_employee(employee_id)
        self._Session.delete(employee)
        self._Session.commit()
        return employee

    def create_department(self,
                          name: str,
                          manager_id: UUID = None) -> Department:
        """Creates department"""
        department = Department(name=name, manager_id=manager_id)
        self._Session.add(department)
        self._Session.commit()
        return department

    def get_department(self, department_id: UUID) -> Department:
        """Get department"""
        return self._Session.query(Department).get(department_id)

    def update_department(self,
                          department_id: UUID,
                          name: str = None,
                          manager_id: UUID = None) -> Department:
        """Update department"""
        department = self.get_department(department_id)
        if name:
            department.name = name
        if manager_id:
            department.manager_id = manager_id
        self._Session.commit()
        return department

    def delete_department(self, department_id: UUID = None) -> None:
        """Delete a department"""
        department = self.get_department(department_id)
        self._Session.delete(department)
        self._Session.commit()

    def add_employee_to_department(self, employee_id: UUID, department_id: UUID) -> None:
        """Add employee to a department"""
        employee = self.get_employee(employee_id)
        department = self.get_department(department_id)

        if employee is None:
            raise ValueError(
                'Employee with ID: {} does not exist'.format(employee_id))

        if department is None:
            raise ValueError(
                'Department with ID: {} does not exist'.format(department_id))

        employee.department_id = department_id
        self._Session.commit()

    def create_project(self, name: str) -> Project:
        """Create a new project"""
        project = Project(name=name)
        self._Session.add(project)
        self._Session.commit()
        return project

    def get_project(self, project_id: UUID = None) -> Project:
        """Get project from database"""
        return self._Session.query(Project).get(project_id)

    def update_project(self,
                       project_id: UUID,
                       name: str = None) -> Project:
        """Update a given project"""
        project = self.get_project(project_id)
        if name:
            project.name = name
        self._Session.commit()
        return project

    def delete_project(self, project_id: UUID) -> None:
        """Delete a project"""
        project = self.get_project(project_id)
        self._Session.delete(project)
        self._Session.commit()

    def add_employee_to_project(self,
                                employee_id: UUID,
                                project_id: UUID) -> None:
        """Add employee to a given project"""
        employee = self.get_employee(employee_id)
        project = self.get_project(project_id)
        employee.projects.append(project)
        self._Session.commit()

    def remove_employee_from_project(self,
                                     employee_id: UUID,
                                     project_id: UUID) -> None:
        """Remove an employee from a project"""
        employee = self.get_employee(employee_id)
        project = self.get_project(project_id)
        employee.projects.remove(project)
        self._Session.commit()

    def create_user(self, username: str, password: str) -> User:
        """Create a new user"""
        if not username:
            raise ValueError('Valid username required')
        if not password:
            raise ValueError('Valid password required')
        user = User(username=username)
        user.set_password(password)
        self._Session.add(user)
        self._Session.commit()
        return user

    def get_user(self, user_id: UUID) -> User:
        """Get user from database by their id"""
        return self._Session.query(User).get(user_id)

    def login(self, user_id: UUID, password: str) -> User:
        """Authenticate user using their user_id and password"""
        user = self.get_user(user_id)
        if not user:
            raise ValueError('Invalid username!')
        if not user.check_password(password):
            raise ValueError('Invalid password!')
        return user
