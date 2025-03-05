#!/usr/bin/python3
"""
Adds a new object to the database and prints it's id
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import State, Base


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]
    ))
    Base.metadata.create_all(engine)
    session = Session(engine)

    new_state = State(name="Louisiana")

    session.add(new_state)
    session.commit()

    print(new_state.id)
