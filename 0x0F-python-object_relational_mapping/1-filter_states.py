#!/usr/bin/python3

import MySQLdb
from sys import argv

"""This is a script that lists all states with a name starting with
    Uppercase N in the database hbtn_0e_0_usa"""
if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost", port=3306, name=argv[1],
            passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states \
            WHERE name LIKE 'N%' ORDER BY states.id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
