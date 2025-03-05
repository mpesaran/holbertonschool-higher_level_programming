#!/usr/bin/python3
"""
Fetch a State object by name from the database, SQL injection safe
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import State, Base


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]
    ), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    state = sys.argv[4]

    result = session.query(State).filter(State.name == state).one_or_none()

    if result:
        print(result.id)
    else:
        print("Not found")

    session.close()
