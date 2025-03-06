#!/usr/bin/python3
"""
Updates a record's name in database
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

    state_to_update = session.query(State).filter_by(id=2).first()
    # session.query(State).filter_by(id=2).update({
    #       "name": "New Mexico"
    #        }) alternative way

    if state_to_update:
        state_to_update.name = "New Mexico"
    session.commit()
