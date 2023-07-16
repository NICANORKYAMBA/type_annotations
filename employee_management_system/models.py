#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun July 09 11:30:00 2023

@Author: Nicanor Kyamba
"""
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy.dialects.mysql import CHAR
from uuid import uuid4
import bcrypt

Base = declarative_base()

employee_project_association = Table(
    'employee_project_association', Base.metadata,
    Column('employee_id', CHAR(36), ForeignKey('employees.employee_id')),
    Column('project_id', CHAR(36), ForeignKey('projects.project_id'))
)


class Employee(Base):
    """
    Employee class
    """
    __tablename__ = 'employees'

    employee_id = Column(
        CHAR(36),
        default=lambda: str(uuid4()),
        primary_key=True,
        unique=True,
        nullable=False
    )
    name = Column(String(250), nullable=False, unique=True)
    age = Column(Integer, nullable=False)
    salary = Column(Float, nullable=False)
    department_id = Column(
        CHAR(36),
        ForeignKey('departments.department_id'),
        nullable=True,
        unique=True
    )
    department = relationship(
        'Department',
        back_populates='employees',
        foreign_keys=[department_id],
        uselist=False,
        viewonly=True
    )
    projects = relationship(
        'Project',
        secondary=employee_project_association,
        back_populates='employees'
    )
    works_in_department = relationship(
        'Department',
        back_populates='employees',
        foreign_keys=[department_id],
        viewonly=True
    )


class Department(Base):
    """
    Department class
    """
    __tablename__ = 'departments'

    department_id = Column(
        CHAR(36),
        default=lambda: str(uuid4()),
        primary_key=True,
        unique=True,
        nullable=False
    )
    name = Column(String(250), nullable=False, unique=True)
    manager_id = Column(
        CHAR(36),
        ForeignKey('employees.employee_id'),
        nullable=False,
        unique=True
    )
    employees = relationship(
        'Employee',
        back_populates='works_in_department',
        foreign_keys=[Employee.department_id],
        uselist=True,
        viewonly=True
    )

    def add_employee(self, employee):
        """Adds an employee to the department."""
        self.employees.append(employee)
        employee.department_id = self.department_id


class Project(Base):
    """
    Project class
    """
    __tablename__ = 'projects'

    project_id = Column(
        CHAR(36),
        default=lambda: str(uuid4()),
        primary_key=True,
        unique=True,
        nullable=False
    )
    name = Column(String(250), nullable=False)
    employees = relationship(
        'Employee',
        secondary=employee_project_association,
        back_populates='projects'
    )


class User(Base):
    """
    User class
    """
    __tablename__ = 'users'

    user_id = Column(
        CHAR(36),
        default=lambda: str(uuid4()),
        primary_key=True,
        unique=True,
        nullable=False
    )
    username = Column(String(250), nullable=False, unique=True)
    password_hash = Column(String(250), nullable=False)

    def set_password(self, password: str) -> None:
        """Sets the password for the user."""
        password_bytes = password.encode('utf-8')
        salt = bcrypt.gensalt()
        self.password_hash = bcrypt.hashpw(
            password_bytes, salt).decode('utf-8')

    def check_password(self, password: str) -> bool:
        """Checks the password for the user."""
        password_bytes = password.encode('utf-8')
        stored_password_bytes = self.password_hash.encode('utf-8')
        return bcrypt.checkpw(password_bytes, stored_password_bytes)
