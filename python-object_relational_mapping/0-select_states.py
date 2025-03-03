#!/usr/bin/python3
"""
This script uses the MySQLdb module to connect to a MySQL database
and lists all states from the 'states' table in the specified database.
The results are sorted in ascending order by the state ID and displayed
as tuples.
"""

import sys
import MySQLdb


def list_states():
    """Fetches data from db to list states"""
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8"
        )
    # Creates a cursor to execute queries
    cur = db.cursor()
    # Execute the query to select all states, sorted by states.id
    cur.execute("SELECT id, name FROM states ORDER BY id ASC")
    results = cur.fetchall()   # Fetch all the results
    for state in results:
        print(state)
    # Close the cursor and the connection
    cur.close()
    db.close()


if __name__ == "__main__":
    list_states()
