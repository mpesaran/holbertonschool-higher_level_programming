#!/usr/bin/python3
"""
prints all City objects from the city class and join it with
State class to print city name with linked state names
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_city import City
from model_state import State, Base


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]
    ))
    Base.metadata.create_all(engine)
    session = Session(engine)

    result = session.query(City, State).join(State).order_by(City.id).all()

    for city, state in result:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
