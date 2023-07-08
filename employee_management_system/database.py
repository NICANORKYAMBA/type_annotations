#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri July  07 23:56:03 2023

@Author: Nicanor Kyamba
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
import MySQLdb


class EmployeeDatabase:
    """Employee Database"""
    def __init__(self, db_url: str) -> None:
        """Init"""
        self._engine = create_engine(db_url, module=MySQLdb, echo=False)
        self._Session = sessionmaker(bind=self._engine)
        self.create_tables()

    def create_tables(self) -> None:
        """Create tables"""
        Base.metadata.create_all(self._engine)

    def get_session(self):
        """Get session"""
        return self._Session()
