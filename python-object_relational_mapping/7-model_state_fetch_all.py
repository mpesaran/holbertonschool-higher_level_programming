#!/usr/bin/python3
"""
A script that lists all State objects from the database hbtn_0e_6_usa.

This script connects to a MySQL database using SQLAlchemy, retrieves all the
State objects from the `states` table, and prints them in ascending order by
the state's ID.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]
        ), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))

    session.close()
