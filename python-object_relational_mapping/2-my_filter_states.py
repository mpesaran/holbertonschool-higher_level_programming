#!/usr/bin/python3
"""
This script uses the MySQLdb module to connect to a MySQL database
and lists values equal to argument given by user from 'states' table in
 the specified database, if start with N. The results are sorted in
 ascending order by the state ID and displayed as tuples.
"""

import sys
import MySQLdb


def filter_states():
    """
    This function will list values in states table matches
    argument passed by user
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

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
                   WHERE BINARY name= '{}'\
                   ORDER BY id".format(state_name)
                   )
    results = cursor.fetchall()
    for state in results:
        print(state)
    cursor.close()
    db.close()


if __name__ == "__main__":
    filter_states()
