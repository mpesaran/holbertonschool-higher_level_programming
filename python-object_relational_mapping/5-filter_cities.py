#!/usr/bin/python3
"""
Connects to a MySQL server running on localhost at port 3306.
Retrieves all cities for the given state, sorted by `cities.id`.
Uses parameterized queries to prevent SQL injection.
"""

import sys
import MySQLdb


def list_cities_of_a_state():
    """ Lists all cities of a given state from the database """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        password=password,
        db=database,
        charset="utf8"
    )
    cursor = db.cursor()
    cursor.execute("SELECT cities.name\
                   FROM cities\
                   JOIN states ON cities.state_id = states.id\
                   WHERE BINARY states.name = %s\
                   ORDER BY cities.id", (state_name,))
    result = cursor.fetchall()

    city_list = ", ".join(city[0] for city in result)
    print(city_list)

    cursor.close()
    db.close()


if __name__ == "__main__":
    list_cities_of_a_state()
