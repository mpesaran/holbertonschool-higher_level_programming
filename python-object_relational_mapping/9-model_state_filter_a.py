#!/usr/bin/python3
"""
Fetches the state objects that contain the letter
'a' from database usin sqlAlchemy
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
    result = session.query(State).filter(
        State.name.ilike('%a%')
        ).order_by(State.id)
    for state in result:
        print(f"{state.id}: {state.name}")

    session.close()
