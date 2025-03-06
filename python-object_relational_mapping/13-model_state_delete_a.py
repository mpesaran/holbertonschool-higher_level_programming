#!/usr/bin/python3
"""
Deletes records containing 'a' from table
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]
    ))
    Base.metadata.create_all(engine)
    session = Session(engine)

    state_to_delete = session.query(State).filter(
        State.name.ilike('%a%')
        ).all()

    for state in state_to_delete:
        session.delete(state)
    session.commit()
    session.close()
