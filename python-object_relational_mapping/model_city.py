#!/usr/bin/python3
"""
City class that maps to the 'cities' table in MySQL.
The table should have an auto-generated id as primary key
and a name field for the cities name.
"""
from sqlalchemy import Integer, Column, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base, State


class City(Base):
    """
    City class that maps to the 'cities' table in MySQL.
    The table should have an auto-generated id as primary key
    and a name field for the cities name.
    """

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)

    state = relationship("State")
