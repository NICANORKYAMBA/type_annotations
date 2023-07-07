#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 12:56:03 2020

@Author: Firstname Lastname
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
import MySQLdb


class EmployeeDatabase:
    """Employee Database"""
    def __init__(self, db_url: str) -> None:
        """Init"""
        self._engine = create_engine(db_url, module=MySQLdb, echo=True)
        self._Session = sessionmaker(bind=self._engine)
        self.create_tables()

    def create_tables(self) -> None:
        """Create tables"""
        Base.metadata.create_all(self._engine)

    def get_session(self):
        """Get session"""
        return self._Session()
