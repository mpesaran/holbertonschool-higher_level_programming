#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa.
The script:
- Connects to a MySQL server running on localhost at port 3306.
- Retrieves all cities from the `cities` table, sorted in
ascending order by `cities.id`.
- Uses MySQLdb to interact with the database.
- Executes only one SQL query using `execute()`.
"""

import sys
import MySQLdb


def list_cities_by_states():
    """Lists all cities from the database with linked states"""
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        password=password,
        db=database,
        charset="utf8"
    )
    cursor = db.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name\
                   FROM cities\
                   JOIN states ON cities.state_id = states.id\
                   ORDER BY cities.id")
    results = cursor.fetchall()
    for result in results:
        print(result)
    cursor.close()
    db.close()


if __name__ == "__main__":
    list_cities_by_states()
