#!/usr/bin/python3
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """
    State class that maps to the 'states' table in MySQL.
    The table should have an auto-generated id as primary key
    and a name field for the state name.
    """
    __tablename__ = 'states'
    # Defining class attributes as columns
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
