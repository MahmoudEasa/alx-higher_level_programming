#!/usr/bin/python3

"""Script that lists all states with a name starting with N
    (upper N) from the database hbtn_0e_0_usa
"""

if __name__ == '__main__':
    import MySQLdb
    import sys

    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         password=sys.argv[2], database=sys.argv[3])

    c = db.cursor()
    c.execute(f"SELECT * FROM states WHERE name LIKE 'N%'\
              ORDER BY states.id ASC")
    all_data = c.fetchall()

    for data in all_data:
        print(data)

    c.close()
    db.close()
