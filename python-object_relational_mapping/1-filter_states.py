#!/usr/bin/python3
"""
This script uses the MySQLdb module to connect to a MySQL database
and lists all states from the 'states' table in the specified database,
if start with N. The results are sorted in ascending order by the state
ID and displayed as tuples.
"""

import sys
import MySQLdb


def filter_states():
    """This function will lists all states starting with N"""
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        password=password,
        db=database,
        charset="utf8"
    )
    cursor = db.cursor()
    cursor.execute("SELECT id, name\
                   FROM states\
                   WHERE name LIKE BINARY 'N%'\
                   ORDER BY id"
                   )
    results = cursor.fetchall()
    for state in results:
        print(state)
    cursor.close()
    db.close()


if __name__ == "__main__":
    filter_states()
