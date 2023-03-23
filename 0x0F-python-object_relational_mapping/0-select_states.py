#!/usr/bin/python3
"""script which prints all states from the database htbn_oe_0_usa"""

import MySQLdb
from sys import argv

mysql_user = argv[1]
mysql_password = argv[2]
database_name = argv[3]

db = MySQLdb.connect(host = "localhost", port = 3306, name = mysql_user, password = mysql_password, db = database_name)
cursor = db.cursor()
cursor.execute("SELECT * FROM states ORDER BY id ASC")
rows = cursor.fetchall()
for row in rows:
    print(row)
cursor.close()
db.close()
