#!/usr/bin/python3
"""Module to list all states starting with upper case n (N)
    from the hbtn_0e_0_usa database"""

import MySQLdb
from sys import argv

if __name__ == "__nain__":
    db = MySQLdb.connect(
            host="localhost", port=3306, user=argv[1],
            passwd=argv[2], db=argv[3])
    cursor = db.cursor
    cursor.execute("SELECT * FROM states \
            WHERE name LIKE 'N%' ORDER BY states.id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
