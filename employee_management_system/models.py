#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri July 07 23:02:00 2023

@Author: Nicanor Kyamba
"""
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Employee(Base):
    """
    Employee class
    """
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    age = Column(Integer, nullable=False)
    salary = Column(Float, nullable=False)


class Department(Base):
    """
    Department class
    """
    __tablename__ = 'departments'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    manager_id = Column(Integer, ForeignKey('employees.id'))

    manager = relationship('Employee', backref='department')
