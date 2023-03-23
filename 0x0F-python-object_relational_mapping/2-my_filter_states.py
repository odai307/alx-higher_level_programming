#!/usr/bin/python3
"""display all values in states table where name matches the argument"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(
            host="localhost", user=argv[1], port=3306,
            passwd=argv[2], db=argv[3], argv[4])
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM states
            WHERE name LIKE {argv[4]} \
            ORDER BY states.id")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
    
